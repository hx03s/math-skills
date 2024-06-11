""" Provides statistical analysis functions for a list of numbers.
Contains functions to calculate average, median, variance,
and standard deviation. Reads numbers from a file, runs
analysis, and prints results. """

import statistics
def Avg(num):
    try:
        avg = sum(num) / len(num)
        return round(avg)
    except ZeroDivisionError:
        print("Error: Can't divide by zero")
        return None
    except:
        print("Error occurred in Avg")


def Med(num):
    try:
        med = statistics.median(num)
        return round(med)
    except:
        print("Error occurred in Med")
        return None


def Var(num):
    try:
        var = statistics.pvariance(num)
        return round(var)
    except:
        print("Error occurred in Var")
        return None


def Stdv(num):
    try:
        sd = statistics.pstdev(num)
        return round(sd)
    except:
        print("Error occurred in Stdv")
        return None


with open('data.txt', 'r') as file:
    numbers = [int(line.strip()) for line in file]

try:
    print("Average: " + str(Avg(numbers)))
    print("Median: " + str(Med(numbers)))
    print("Variance: " + str(Var(numbers)))
    print("Standard Deviation:" + str(Stdv(numbers)))
except:
    print("Error occurred printing results")
