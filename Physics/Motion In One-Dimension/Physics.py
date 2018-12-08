from math import *
# from symbol import *
# from sympy import *
# from matplotlib import *
# from scipy import *
# from visual import *

# Programmer: Given Lepita
# Project: Physics Simulator & Assistant
# Date: 2018/01


class Physics:
    pass


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


class Motion_In_One_Dimension(Physics):

    def __init__(self, distance=0, time=0, velocity=0, accel=0):
        self.distance = distance
        self.time = time
        self.velocity = velocity
        self.accel = accel

    def solve_time(self):
        # Formula: t = d/v
        if self.time is None or self.time == 0:
            solution = None
            if self.velocity is not None and self.distance is not None:
                solution = round(self.distance / self.velocity, 3)
                self.time = solution
                print(self.time)
            return ""
        else:
            raise CannotCompute("Sorry, I Could Not Compute A Solution")

    def solve_distance(self):
        # Formula: D = v*t
        solution = None
        if self.distance is None or self.distance == 0:
            if self.distance is not None and self.time is not None:
                solution = round(self.velocity * self.time, 3)
                self.distance = solution
                print(self.distance)
            return ""
        else:
            raise CannotCompute("Sorry, I Could Not Compute A Solution")

    def solve_velocity(self):
        # Formula: V = d/t
        if self.velocity is None or self.velocity == 0:
            if self.distance is not None and self.time is not None:
                solution = round(self.distance / self.time, 3)
                self.velocity = solution
                print(self.velocity)
            return ""
        else:
            raise CannotCompute("Sorry, I Could Not Compute A Solution")

    def solve_acceleration(self):
        solution = None
        if self.accel is None or self.accel == 0:
            if self.velocity is not None and self.time is not None:
                solution = round(self.velocity / self.time, 3)
                self.accel = solution
                print(self.accel)
            return ""
        else:
            raise CannotCompute("Sorry, I Could Not Compute A Solution")


class Motion_In_One_Dimension_Advanced(Motion_In_One_Dimension):

    def __init__(self, distance, time, velocity, accel, initVel=0, finVel=0):
        super().__init__(distance, time, velocity, accel)
        self.initVel = initVel
        self.finVel = finVel

    def solve_force(self, mass):
        if self.accel == 0:
            return 0
        return (mass * self.accel)

    def solve_final_velocity(self):
        # 1 - Formula: Vf = Vi + a * t
        # 2 - Formula: Vf**2 = Vi**2 + 2a*D
        solution = None
        if self.finVel == 0 or self.finVel is None:
            if self.initVel is not None and self.accel is not None and self.time is not None:
                solution = self.initVel + (self.accel * self.time)
                self.finVel = round(solution, 3)
                print(self.finVel)
            return ""
        else:
            temp = 0
            if self.initVel is not None and self.accel is not None and self.distance is not None:
                x = self.initVel ** 2
                y = (2*self.accel) * self.distance
                temp = x + y
                self.finVel = round(sqrt(temp), 1)
                print(self.finVel)
            return ""

    def solve_displacement(self):
        # 1 - Formula: x = Vi*t + 1/2(a) * t**2
        # 2 - Formula: x = ((Vi + Vf)/2)*t
        solution = None
        if self.initVel is not None and self.accel is not None and self.time is not None:
            try:
                if self.initVel == 0:
                    # Formula: x = 1/2(a) * t**2
                    # Formula: x = 1/2Vf * t
                    solution = round((self.accel/2) * (self.time**2), 3)
                    print(solution)
                elif self.initVel != 0:
                    # Use original formula
                    solution = round(((self.initVel * self.time) + (self.accel/2) * (self.time**2)), 3)
                    print(solution)
                elif self.finVel != 0 and self.initVel != 0:
                    # Use original formula
                    solution = round(((self.initVel + self.finVel)/2 * self.time), 3)
                    print(solution)
                else:
                    solution = round(((self.finVel/2)*self.time), 3)
                    print(solution)
            except:
                raise CannotCompute("There seems to be an error in this code. But I am sure our engineers are still trying to bug it out. (~)-_-(~) ")

    def solve_massOraccel(self, force, mass=None):
        if force is not None:
            temp = 0
            if self.accel is None:
                # solve for accel
                temp = round((force / mass), 3)
                self.accel = temp
                print(self.accel)
            elif mass is None:
                # solve for mass
                temp = round((force / self.accel), 3)
                mass = temp
                print(mass)
            else:
                pass
        else:
            raise CannotCompute("There seems to be an error in this code. But I am sure our engineers are still trying to bug it out. (~)0_-(~)")


class Motion_In_Two_Dimensions(Physics):

    def __init__(self, fx, fy, fres):
        self.fx = fx
        self.fy = fy
        self.fres = fres

    def solve_x_component(self, angle):
        solution = None
        if self.fres != 0:
            if self.fx is None or self.fx == 0:
                solution = self.fres * cos(angle)
                self.fx = round(solution, 3)
            else:
                pass
        else:
            raise CannotCompute("X-component is already given. Fx = {}".format(self.fx))
        return self.fx

    def solve_y_component(self, angle):
        solution = None
        if self.fres != 0:
            if self.fy is None or self.fy == 0:
                solution = self.fres * sin(angle)
                self.fy = round(solution, 3)
            else:
                pass
        else:
            raise CannotCompute("Y-component is already given. Fy = {}".format(self.fy))
        return self.fy

    def solve_resultant_force(self):
        fx = self.fx
        fy = self.fy
        if fx and fy:
            fres = sqrt((fx**2 + fy**2))
        self.fres = round(fres, 3)
        return self.fres

    def find_angle(self):
        return round(tan(self.fy / self.fx), 3)


class Motion_In_Two_Dimensions(Motion_In_One_Dimension_Advanced):

    def __init__(self, mass, aoi, normal, fric_force, appl_force, coeff_fric, velocity):
        super().__init__(velocity)
        self.mass = mass
        self.aoi = aoi  # angle-of-inclination
        self.fric_force = fric_force
        self.appl_force = appl_force  # applied force
        self.coeff_fric = coeff_fric  # coefficient of friction

    def solve_momentum(self):
        if self.mass is not None:
            pass

    def solve_normal(self):
        solution = None
        if self.aoi is not None or self.aoi != 0:
            # N = Fg perpendicular
            solution = (self.mass * 9.8) * cos(self.aoi)
            self.normal = round(solution, 3)

            def solve_max_static_frictional_force():
                if self.coeff_fric is not None and solution != None or solution != 0:
                    fs_max = self.coeff_fric * solution
                    return round(fs_max, 3)
                else:
                    pass
            ask = input("Do you want to solve for the maximum static friction? ")
            yes = ["Yes", "Y", "yes", "y"]
            if ask in yes:
                solve_max_static_frictional_force()
            return self.normal
        else:
            CannotCompute("Sorry I cannot compute a solution.")

    def solve_parallel_component(self):
        solution = None
        if self.appl_force is not None or self.appl_force != 0:
            if self.aoi is not None or self.aoi != 0:
                solution = self.appl_force * sin(self.aoi)
            else:
                pass
        elif self.appl_force is None or self.appl_force == 0:
            if self.aoi is not None or self.aoi != 0:
                if self.mass is not None or self.mass != 0:
                    solution = (self.mass * 9.8) * sin(self.aoi)
                    return solution
                else:
                    pass
            else:
                pass
        else:
            CannotCompute("Sorry I cannot compute a solution.")

    def solve_perpendicular_component(self):
        solution = None
        if self.appl_force is not None or self.appl_force != 0:
            if self.aoi is not None or self.aoi != 0:
                solution = self.appl_force * cos(self.aoi)
            else:
                pass
        elif self.appl_force is None or self.appl_force == 0:
            if self.aoi is not None or self.aoi != 0:
                if self.mass is not None or self.mass != 0:
                    solution = (self.mass * 9.8) * cos(self.aoi)
                    return solution
                else:
                    pass
            else:
                pass
        else:
            CannotCompute("Sorry I cannot compute a solution.")
