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
            # if type(self.distance) != int or type(self.distance) != float:
            #     raise NumberError("Distance Must Be A Number")
            # elif type(self.velocity) != int or type(self.velocity) != float:
            #     raise NumberError("Velocity Must Be A Number")
            # else:
            solution = None
            if self.velocity is not None:
                if self.distance is not None:
                    solution = round(self.distance / self.velocity, 3)
                    self.time = solution
                    print(self.time)
                return False
            return False
        else:
            raise CannotCompute("Sorry, I Could Not Compute A Solution")

    def solve_distance(self):
        # Formula: D = v*t
        solution = None
        if self.distance is None or self.distance == 0:
            # if type(self.velocity) != int or type(self.velocity) != float:
            #     raise NumberError("Velocity Must Be A Number")
            # elif type(self.time) != int or type(self.time) != float:
            #     raise NumberError("Time Must Be A Number")
            if self.velocity is not None and self.time is not None:
                solution = round(self.velocity * self.time, 3)
                self.distance = solution
                print(self.distance)
            return False
        else:
            raise CannotCompute("Sorry, I Could Not Compute A Solution")

    def solve_velocity(self):
        solution = None
        # Formula: V = d/t
        if self.velocity is None or self.velocity == 0:
            # if type(self.distance) != int or type(self.distance) != float:
            #     raise NumberError("Distance Must Be A Number")
            # elif type(self.time) != int or type(self.time) != float:
            #     raise NumberError("Time Must Be A Number")
            if self.distance is not None and self.time is not None:
                solution = round(self.distance/self.time, 3)
                self.velocity = solution
                print(self.velocity)
            return False
        else:
            raise CannotCompute("Sorry, I Could Not Compute A Solution")

    def solve_acceleration(self):
        solution = None
        # Formula: a =  v/t
        if self.accel is None or self.accel == 0:
            # if type(self.velocity) != int or type(self.velocity) != float:
            #     raise NumberError("Velocity Must Be A Number")
            # elif type(self.time) != int or type(self.time) != float:
            #     raise NumberError("Time Must Be A Number")
            if self.velocity is not None and self.time is not None:
                solution = round(self.velocity/self.time, 3)
                self.accel = solution
                print(self.accel)
            return False
        else:
            raise CannotCompute("Sorry, I Could Not Compute A Solution")


class Motion_In_One_Dimension_Advanced(Motion_In_One_Dimension):

    def __init__(self, distance, time, velocity, initVel=0, accel=0, finVel=0):
        super().__init__(distance, time, velocity, accel)
        self.initVel = initVel
        self.finVel = finVel

    def solve_final_velocity(self):
        # 1 - Formula: Vf = Vi + a * t
        # 2 - Formula: Vf**2 = Vi**2 + 2a*D
        solution = None
        if self.finVel == 0 or self.finVel is None:
            # if type(self.initVel) != int or type(self.initVel) != float:
            #     raise NumberError("Initial Velocity Must Be A Number")
            # elif type(self.accel) != int or type(self.accel) != float:
            #     raise NumberError("Acceleration Must Be A Number")
            # elif type(self.time) != int or type(self.time) != float:
            #     raise NumberError("Time Must Be A Nu!=mber")
            if self.initVel is not None and self.accel is not None and self.time is not None:
                solution = self.initVel + (self.accel * self.time)
                self.finVel = round(solution, 3)
                print(self.finVel)
            return False
        else:
            # if type(self.initVel) != float or type(self.initVel) != int:
            #     raise NumberError("Initial Velocity Must Be A Number")
            # elif type(self.accel) != float or type(self.accel) != int:
            #     raise NumberError("Acceleration Must Be A Number")
            # elif type(self.distance) != float or type(self.distance) != int:
            #     raise NumberError("Distance Must Be A Number")
            if self.initVel is not None and self.distance is not None and self.accel is not None:
                solution = self.initVel**2 + ((2*(self.accel)) * self.distance)
                self.finVel = round(sqrt(solution), 3)
                print(self.finVel)
            return False
        # else:
        #     raise CannotCompute("Sorry, I Could Not Compute A Solution")

    def solve_displacement(self):
        # 1 - Formula: x = Vi*t + 1/2(a)*t**2
        # 2 - Formula: x = ((Vi+Vf)/2)*t
        solution = None
        # if type(self.initVel) != float or type(self.initVel) != int:
        #     raise NumberError("Initial Velocity Must Be A Number")
        # elif type(self.time) != float or type(self.time) != int:
        #     raise NumberError("Time Must Be A Number")
        # elif type(self.accel) != float or type(self.accel) != int:
        #     raise NumberError("Acceleration Must Be A Number")
        if self.initVel is not None and self.accel is not None and self.time is not None:
            try:
                if self.initVel == 0:
                    # Change formula
                    # x = 1/2(a)*t**2
                    solution = 1/2*(self.accel)*self.time**2
                    print(round(solution, 3))
                elif self.initVel != 0:
                    # Use original formula
                    # x = Vi*t +  1/2(a)*t**2
                    solution = self.initVel*self.time + 1/2*(self.accel)*self.time**2
                    print(round(solution, 3))
                else:
                    # if type(self.finVel) != float or type(self.finVel) != int:
                    #     raise NumberError("Final Velocity Must Be A Number")
                    if self.initVel is not None:
                        solution = ((self.initVel + self.finVel)/2)*self.time
                        print(round(solution, 3))
            except Exception as e:
                print("Error:  ", e)

obj = Motion_In_One_Dimension_Advanced(200, 0, 0, 0, 5.1, None)
obj.solve_final_velocity()
# self, distance, time, velocity, initVel=0, accel=0, finVel=0