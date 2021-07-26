#!/usr/bin/python

"""Create mock data matching the parameters of your projected real data, to 
test your analyses on. Parameters are written in a CSV file, mock data is 
written into a CSV file."""

import pandas
import numpy
import random

# Read the parameters.csv file into a dataframe
parameters = pandas.read_csv("parameters.csv" , index_col=0)

print(parameters)
