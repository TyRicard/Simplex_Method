from fractions import Fraction
from SimplexMethod import SimplexMethod
from Variable import Variable

# For basic printing: https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/
# For format printing: https://pythonguides.com/python-print-2-decimal-places/
class OutputHandler:

    def print_status(simplex):
        print(simplex.status)
    

    def print_optimal_value(simplex):
        float_optimal = float(simplex.optimal)
        print("{0:.7g}".format(float_optimal))


    def print_optimal(simplex):
        OutputHandler.print_status(simplex)
        OutputHandler.print_optimal_value(simplex)
        OutputHandler.print_points(simplex)


    def print_unbounded(simplex):
        OutputHandler.print_status(simplex)
        

    def print_infeasible(simplex):
        OutputHandler.print_status(simplex)


    def print_points(simplex):
        point_list = []
        for var in simplex.variables:
            if var.is_point():
                point_list.append("{0:.7g}".format(float(var.get_value())))
        print(*point_list)






