from math import cos, sin, sqrt


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
