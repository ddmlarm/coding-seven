"""
Dayna Mitty Larm
Southern Utah University
CSIS-1300-01-SP23: Programming with Python

Coding Seven 
GitHub: https://github.com/ddmlarm/coding-seven
Requirements: Numbers-1.txt located in folder with integer_analytics.py 
"""

import sys
import time


def main():
    """Main Driver for the integer_analytics.py program. 

    Reads a .txt file and prints the total numbers contained in the file, the 
    largest number, and the shortest number. Printes runtimes for two different 
    file scanning functions. """

    print("\nScanning File...")
    print("---------------------------")
    scan_file_runtime = scan_file(True)

    print("\n\nScanning File with List...")
    print("---------------------------")
    scan_file_with_list_runtime = scan_file_with_list(True)

    function_runtimes = "Function Runtimes"

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # VALUE SET TO FALSE: Average Runtimes are Inconsistent and Unreliable  #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    find_average_runtimes = False

    # Run program again to get average runtimes
    if find_average_runtimes:
        function_runtimes = "Average " + function_runtimes

        times_run = 1
        while times_run <= 1000:
            scan_file_runtime += scan_file(False)
            scan_file_with_list_runtime += scan_file_with_list(False)
            times_run += 1

        # Divide runtime sums by numver of times_run
        scan_file_runtime = scan_file_runtime/times_run
        scan_file_with_list_runtime = scan_file_with_list_runtime/times_run

    # # # # # # # # # # # # # # # # # # # # # # #  END FIND AVERAGE RUNTIME #

    # Convert runtimes to strings
    scan_file_runtime = str(scan_file_runtime)
    scan_file_with_list_runtime = str(scan_file_with_list_runtime)

    # Add spaces to shorter runtime for readable printing
    while len(scan_file_runtime) < len(scan_file_with_list_runtime):
        scan_file_runtime = " " + scan_file_runtime

    while len(scan_file_with_list_runtime) < len(scan_file_runtime):
        scan_file_with_list_runtime = " " + scan_file_with_list_runtime

    # Print Runtimes
    print(f"\n\n{function_runtimes}")
    print("---------------------------")
    print("Scan File Runtime:           ", scan_file_runtime, "(ns)")
    print("Scan File with List Runtime: ",
          scan_file_with_list_runtime, "(ns)\n")


def scan_file(print_results):
    """
    Returns the runtime taken to scan a file's contents for the total numbers, 
    largest number, and smallest number contained in the file. 

    Keyword arguments:
        print_results -- a boolean indicating whether the result wills be 
        printed to the terminal
    """
    # start_time = time.perf_counter_ns()  # start time

    try:
        start_time = time.perf_counter_ns()  # start time

        number_contents = open("Numbers-1.txt", mode="r", encoding="utf-8")

        total_numbers = 0
        largest_number = 0
        smallest_number = sys.maxsize

        has_next_line = True
        while has_next_line:
            # line will be read to string or None
            number = number_contents.readline()
            if number:
                # If number is not None, convert to int
                number = int(number)
                total_numbers += 1  # increment total numbers
                if number > largest_number:
                    largest_number = number  # replace largest number
                if number < smallest_number:
                    smallest_number = number  # replace smallest number
            else:
                has_next_line = False

        end_time = time.perf_counter_ns()  # end time

        if print_results:
            print("Total Numbers in File:   ", total_numbers)
            print("Largest Number in File:  ", largest_number)
            print("Smallest Number in File: ", smallest_number)

    except FileNotFoundError:
        print(FileNotFoundError)

    # end_time = time.perf_counter_ns()  # end time
    run_time = end_time-start_time  # run time
    return run_time


def scan_file_with_list(print_results):
    """
    Returns the runtime taken to scan a file's contents for the total numbers, 
    largest number, and smallest number contained in the file using .readlines() 
    to scan the file to a list[str]. 

    Keyword arguments:
        print_results -- a boolean indicating whether the result wills be 
        printed to the terminal
    """
    # start_time = time.perf_counter_ns()  # start time

    try:
        start_time = time.perf_counter_ns()  # start time

        # Read .txt file lines to list[str]
        number_contents = open("Numbers-1.txt", mode="r",
                               encoding="utf-8").readlines()

        total_numbers = 0
        largest_number = 0
        smallest_number = sys.maxsize

        for number in number_contents:
            # If number is not None, convert to int
            number = int(number)
            total_numbers += 1  # increment total numbers
            if number > largest_number:
                largest_number = number  # replace largest number
            if number < smallest_number:
                smallest_number = number  # replace smallest number

        end_time = time.perf_counter_ns()  # end time

        if print_results:
            print("Total Numbers in File:   ", total_numbers)
            print("Largest Number in File:  ", largest_number)
            print("Smallest Number in File: ", smallest_number)

    except FileNotFoundError:
        print(FileNotFoundError)

    # end_time = time.perf_counter_ns()  # end time
    run_time = end_time-start_time  # run time
    return run_time


# Main Driver
main()


# NOTES # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Program was initially designed to test the runtime comparison between
# scanning a file line by line with open().readline(), or to a list of strings
# with open().readlines(). Tests of these functions for average runtimes for
# sizes of n trials for 10, 100, and 1000 revealed inconsistent results. Each
# function's average runtime was consistenly equal to, greater than, or less
# than the other function with no pattern. Moving start_time and closing the
# file had no affect on the comparitive runtimes of each function.

# The code in main() to find the average runtime was nested in an if statement
# with a value set to false. The current runtimes printed to the terminal are
# not the average runtimes, and should not be considered a reflection on the
# efficiency of the scanning methods tested; simply as a representation of the
# time taken my each method for the time it was run.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
