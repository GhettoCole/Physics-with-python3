from math import cos, sin, sqrt

# The code is still buggy, later to be fixed.

class NumberError(Exception):
    def __init__(self, reason):
        self.reason = reason

    def __str__(self):
        return repr(self.reason)


class CannotCompute(Exception):
    def __init__(self, reason):
        self.reason = reason

    def __str__(self):
        return repr(self.reason)


class Physics:
    pass


class MotionInOneDimension(Physics):

    def __init__(self, distance=0, time=0, velocity=0, accel=0):
        self.distance = distance
        self.time = time
        self.velocity = velocity
        self.accel = accel

    def solve_time(self):
        # Formula: t = d/v
        if self.time is None or self.time == 0:
            if self.velocity is not None and self.distance is not None:
                solution = round(self.distance / self.velocity, 3)
                self.time = solution
                print(self.time)
        else:
            raise CannotCompute("Sorry, I Could Not Compute A Solution")

    def solve_distance(self):
        # Formula: D = v*t
        if self.distance is None or self.distance == 0:
            if self.velocity is not None and self.time is not None:
                solution = round(self.velocity * self.time, 3)
                self.distance = solution
                print(self.distance)
        else:
            raise CannotCompute("Sorry, I Could Not Compute A Solution")

    def solve_velocity(self):
        # Formula: V = d/t
        if self.velocity is None or self.velocity == 0:
            if self.distance is not None and self.time is not None:
                solution = round(self.distance / self.time, 3)
                self.velocity = solution
                print(self.velocity)
        else:
            raise CannotCompute("Sorry, I Could Not Compute A Solution")

    def solve_acceleration(self):
        if self.accel is None or self.accel == 0:
            if self.velocity is not None and self.time is not None:
                solution = round(self.velocity / self.time, 3)
                self.accel = solution
                print(self.accel)

    def solve_kinetic_energy(self, mass):
        if self.velocity is not None:
            kinetic_energy = 0.5 * mass * self.velocity ** 2
            return kinetic_energy
        raise CannotCompute("Sorry, I Cannot Compute A Solution.")

    def solve_potential_energy(self, mass, height):
        potential_energy = mass * 9.8 * height
        return potential_energy

    def solve_momentum(self, mass):
        if self.velocity is not None:
            return mass * self.velocity


class MotionInTwoDimensions(MotionInOneDimension):

    def __init__(self, mass, aoi, fric_force, appl_force, coeff_fric, velocity):
        super().__init__(velocity)
        self.mass = mass
        self.aoi = aoi  # angle-of-inclination
        self.fric_force = fric_force
        self.appl_force = appl_force  # applied force
        self.coeff_fric = coeff_fric  # coefficient of friction
        self.normal = None  # Adding the 'normal' attribute

    def solve_momentum(self):
        if self.mass is not None and self.velocity is not None:
            return self.mass * self.velocity

    def solve_max_static_frictional_force(self):
        if self.coeff_fric is not None and self.normal is not None:
            fs_max = self.coeff_fric * self.normal
            return fs_max

    def solve_work_done(self, displacement):
        if self.force is not None and displacement is not None:
            return self.force * displacement * cos(self.aoi)

    def solve_kinetic_energy(self):
        if self.velocity is not None:
            kinetic_energy = 0.5 * self.mass * self.velocity ** 2
            return kinetic_energy

    def solve_potential_energy(self, height):
        potential_energy = self.mass * 9.8 * height
        return potential_energy

    def solve_net_force(self):
        fx = self.fx if self.fx is not None else 0
        fy = self.fy if self.fy is not None else 0
        net_force = sqrt(fx ** 2 + fy ** 2)
        return net_force

    def find_angle(self):
        if self.fx is not None and self.fy is not None:
            return round(tan(self.fy / self.fx), 3)
        raise CannotCompute("Sorry, I Cannot Compute A Solution.")


import tkinter as tk
from math import cos, tan
from tkinter import messagebox

class MotionSolverApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Physics Motion Solver")
        self.geometry("400x300")

        self.label = tk.Label(self, text="Enter values for solving motion problems:")
        self.label.pack()

        self.frame = tk.Frame(self)
        self.frame.pack()

        # Motion in One Dimension
        self.distance_label = tk.Label(self.frame, text="Distance:")
        self.distance_label.grid(row=0, column=0)
        self.distance_entry = tk.Entry(self.frame)
        self.distance_entry.grid(row=0, column=1)

        self.time_label = tk.Label(self.frame, text="Time:")
        self.time_label.grid(row=1, column=0)
        self.time_entry = tk.Entry(self.frame)
        self.time_entry.grid(row=1, column=1)

        self.velocity_label = tk.Label(self.frame, text="Velocity:")
        self.velocity_label.grid(row=2, column=0)
        self.velocity_entry = tk.Entry(self.frame)
        self.velocity_entry.grid(row=2, column=1)

        self.accel_label = tk.Label(self.frame, text="Acceleration:")
        self.accel_label.grid(row=3, column=0)
        self.accel_entry = tk.Entry(self.frame)
        self.accel_entry.grid(row=3, column=1)

        self.solve_button = tk.Button(self.frame, text="Solve", command=self.solve_motion)
        self.solve_button.grid(row=4, column=0, columnspan=2)

        # Motion in Two Dimensions
        self.mass_label = tk.Label(self.frame, text="Mass:")
        self.mass_label.grid(row=5, column=0)
        self.mass_entry = tk.Entry(self.frame)
        self.mass_entry.grid(row=5, column=1)

        self.angle_label = tk.Label(self.frame, text="Angle of Inclination:")
        self.angle_label.grid(row=6, column=0)
        self.angle_entry = tk.Entry(self.frame)
        self.angle_entry.grid(row=6, column=1)

        self.fric_force_label = tk.Label(self.frame, text="Frictional Force:")
        self.fric_force_label.grid(row=7, column=0)
        self.fric_force_entry = tk.Entry(self.frame)
        self.fric_force_entry.grid(row=7, column=1)

        self.appl_force_label = tk.Label(self.frame, text="Applied Force:")
        self.appl_force_label.grid(row=8, column=0)
        self.appl_force_entry = tk.Entry(self.frame)
        self.appl_force_entry.grid(row=8, column=1)

        self.coeff_fric_label = tk.Label(self.frame, text="Coefficient of Friction:")
        self.coeff_fric_label.grid(row=9, column=0)
        self.coeff_fric_entry = tk.Entry(self.frame)
        self.coeff_fric_entry.grid(row=9, column=1)

        self.fx_label = tk.Label(self.frame, text="Force in X-direction:")
        self.fx_label.grid(row=10, column=0)
        self.fx_entry = tk.Entry(self.frame)
        self.fx_entry.grid(row=10, column=1)

        self.fy_label = tk.Label(self.frame, text="Force in Y-direction:")
        self.fy_label.grid(row=11, column=0)
        self.fy_entry = tk.Entry(self.frame)
        self.fy_entry.grid(row=11, column=1)

        self.solve_button_2d = tk.Button(self.frame, text="Solve 2D", command=self.solve_motion_2d)
        self.solve_button_2d.grid(row=12, column=0, columnspan=2)

    def get_motion_one_dimension_values(self):
        try:
            distance = float(self.distance_entry.get())
        except ValueError:
            distance = None

        try:
            time = float(self.time_entry.get())
        except ValueError:
            time = None

        try:
            velocity = float(self.velocity_entry.get())
        except ValueError:
            velocity = None

        try:
            accel = float(self.accel_entry.get())
        except ValueError:
            accel = None

        return distance, time, velocity, accel

    def solve_motion(self):
        distance, time, velocity, accel = self.get_motion_one_dimension_values()

        try:
            motion = MotionInOneDimension(distance=distance, time=time, velocity=velocity, accel=accel)

            if distance is None:
                motion.solve_distance()
            if time is None:
                motion.solve_time()
            if velocity is None:
                motion.solve_velocity()
            if accel is None:
                motion.solve_acceleration()

            messagebox.showinfo("Solution", f"Distance: {motion.distance}\nTime: {motion.time}\nVelocity: {motion.velocity}\nAcceleration: {motion.accel}")

        except CannotCompute as e:
            messagebox.showerror("Error", str(e))

    def get_motion_two_dimensions_values(self):
        try:
            mass = float(self.mass_entry.get())
        except ValueError:
            mass = None

        try:
            aoi = float(self.angle_entry.get())
        except ValueError:
            aoi = None

        try:
            fric_force = float(self.fric_force_entry.get())
        except ValueError:
            fric_force = None

        try:
            appl_force = float(self.appl_force_entry.get())
        except ValueError:
            appl_force = None

        try:
            coeff_fric = float(self.coeff_fric_entry.get())
        except ValueError:
            coeff_fric = None

        try:
            velocity = float(self.velocity_entry.get())
        except ValueError:
            velocity = None

        try:
            fx = float(self.fx_entry.get())
        except ValueError:
            fx = None

        try:
            fy = float(self.fy_entry.get())
        except ValueError:
            fy = None

        return mass, aoi, fric_force, appl_force, coeff_fric, velocity, fx, fy

    def solve_motion_2d(self):
        mass, aoi, fric_force, appl_force, coeff_fric, velocity, fx, fy = self.get_motion_two_dimensions_values()

        try:
            motion = MotionInTwoDimensions(mass=mass, aoi=aoi, fric_force=fric_force,
                                           appl_force=appl_force, coeff_fric=coeff_fric, velocity=velocity)
            motion.fx = fx
            motion.fy = fy

            motion.solve_velocity()
            motion.solve_acceleration()
            motion.solve_max_static_frictional_force()
            motion.solve_work_done(10)  # Pass the displacement as an argument, here 10 is assumed.
            motion.solve_kinetic_energy()
            motion.solve_potential_energy(10)  # Pass the height as an argument, here 10 is assumed.
            motion.solve_net_force()
            motion.find_angle()

            messagebox.showinfo("Solution", f"Velocity: {motion.velocity}\nAcceleration: {motion.accel}\nMax Static Frictional Force: {motion.solve_max_static_frictional_force()}\nWork Done: {motion.solve_work_done(10)}\nKinetic Energy: {motion.solve_kinetic_energy()}\nPotential Energy: {motion.solve_potential_energy(10)}\nNet Force: {motion.solve_net_force()}\nAngle: {motion.find_angle()}")

        except CannotCompute as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    app = MotionSolverApp()
    app.mainloop()
