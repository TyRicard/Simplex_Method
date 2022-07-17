# Name: Ty Ricard
# Student no.: V00909036

from fractions import Fraction
import sys

class InputParser:

    # Simple conditionals checking for the file_name
    def get_pivot_rule(arguments):
        initialization_approach = None
        pivot_rule = None

        if len(arguments) > 3:
            print("Too many arguments were provided")
            exit(1)

        # Set the Flags if applicable
        for arg_index in range(1, len(arguments)):
            if (arguments[arg_index] == "-coeff") and (pivot_rule is None):
                pivot_rule = "Largest Coefficient"

            elif (arguments[arg_index] == "-inc") and (pivot_rule is None):
                pivot_rule = "Largest Increase"
            
            elif (arguments[arg_index] == "-aux") and (initialization_approach is None):
                initialization_approach = "Auxiliary"

            elif (arguments[arg_index] == "-dual") and (initialization_approach is None):
                initialization_approach = "Dual"

            else:
                print("The Flag Provided is not valid or is a duplicate")
                exit(1)

        # Assign defaults if necessary
        if pivot_rule is None:
            pivot_rule = "Largest Coefficient"

        if initialization_approach is None:
            initialization_approach = "Auxiliary"
            
        return (pivot_rule, initialization_approach)


    def split_by_whitespace(line):
        if "\t" in line:
            string_row = line.split("\t")
        else:
            string_row = line.split()
        return string_row


    # Parsing the file for the necessary data
    def get_lp():
        lp_string_lines = sys.stdin.readlines()

        is_first = True
        lp = []

        # For each row of the string, get the coefficients, and append to the LP
        # Note, for the objective function, append a zero for easy conversion to a dictionary
        # For fractions: https://docs.python.org/3/library/fractions.html
        for line in lp_string_lines:
            string_row = []
            lp_row = []

            string_row = InputParser.split_by_whitespace(line)
            for coeff in string_row:
                lp_row.append(Fraction(coeff))
            
            if is_first:
                lp_row.append(Fraction(0, 1))
                is_first = False

            lp.append(lp_row)
        
        return lp





