from math import *


class Physics:
    pass


class Motion_In_One_Dimension(Physics):

    def __init__(self, distance=0, time=0, velocity=0):
        self.distance = distance
        self.time = time
        self.velocity = velocity

    def solve_time(self):
        # Formula = t = d/t
        if self.time is None or self.time == 0:
            # distance is bigger than 0
            if self.distance is not None and self.distance > 0:
                if self.velocity > 0:
                    # time rounded to 3 places
                    time = round(float(self.distance / self.velocity), 3)
                    self.time = time
                    return time
                return False
            return False
        return False

    def solve_distance(self):
        # Formula:  D = s/t
        if self.distance is None or self.distance == 0:
            try:
                if self.velocity > 0 and self.time > 0:
                    self.distance = round(float(self.velocity*(self.time)), 3)
                    return self.distance
                else:
                    return False
            except:
                pass
        return False

    def solve_velocity(self):
        # Formula = v = d/t
        if self.velocity is None or self.velocity == 0:
            try:
                if self.time != 0 and self.distance != 0:
                    velocity = round(float(self.distance/self.time), 2)
                    self.velocity = velocity
                    return self.velocity
                else:
                    return False
            except:
                pass
        return False


class Motion_In_One_Dimension_Advanced(Motion_In_One_Dimension):

    def __init__(self, distance, time, velocity, initVel=0, accel=0, finVel=0):
        super().__init__(distance, time, velocity)
        self.initVel = init_vel
        self.accel = accel
        self.finVel = finVel
'''
    def solve_final_velocity(self):
        solution = None
        if self.finVel == 0 or self.finVel is None:
            if self.initVel != 0 or self.initVel is not None:
                if self.accel > 0 or self.accel != 0:
                    if self.time > 0 or self.time != 0:
                        # Formula:  Vf = Vi + a * t
                        solution = self.initVel + (self.accel * self.time)
                        self.finVel = solution
                        return self.finVel
                    return False
                return False
            return False
        elif self.finVel == 0 or self.finVel is None:
            if self.initVel != 0 or self.initVel is not None:
                if self.accel > 0 or self.accel != 0:
                    if self.time is None or self.time == 0:
                        if self.distance is not None or self.distance > 0:
                            # Formula: Vf**2 = Vi**2 + 2a*D
                            solution = self.initVel**2 + ((2*self.accel) * self.distance)
                            self.finVel = sqrt(solution)
                            return self.finVel
                        return False
                    return False
                return False
            return False
        else:
            return "Unable to find a solution!"

    def solve_displacement(self):
        solution = None
        if self.initVel is not None or self.initVel > 0:
            if self.time > 0 or self.time is not None:
                if self.accel is not None or self.accel > 0:
                    # Formula:  x = Vi*t + 1/2(a*(t**2))
                    solution = self.initVel * self.time + (self.accel * (self.time**2))/2
                    return solution
                return False
            return False
        elif self.initVel is not None or self.initVel > 0:
            if self.finVel is not None or self.finVel > 0:
                if self.time is not None or self.time > 0:
                    # Formula: x = ((Vi+Vf)/2)*t
                    solution = ((self.initVel + self.finVel)/2) * self.time
                    return solution
                return False
            return False
        else:
            return "Unable to find a solution"
'''

# Removed the tests because the variables have been reset to floats
# For more accuracy. Thanks to Amaras (*_*)!....

# The tests will be re-evaluated.
'''
def tests():
    from time import time
    now = time()

    test_time = Motion_In_One_Dimension(1000, 0, 12)
    test_distance = Motion_In_One_Dimension(0, 20, 30)
    test_velocity = Motion_In_One_Dimension(2000, 20, 0)

    assert(test_time.solve_time() == 83)
    print("Test for solving time problems passed\n")

    assert(test_distance.solve_distance() == 600)
    print("Test for solving distance problems passed\n")

    assert(test_velocity.solve_velocity() == 100)
    print("Test for solving velocity problems passed\n")

    then = time()
    time_took = then - now
    print("All Tests Took %10.3f seconds!" % time_took)

tests()
'''
