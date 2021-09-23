# MockData
Create a CSV of simulated data to design your analysis on, while you wait for
real data

The basic premise is that while simulating data is not difficult, it is 
usually done in a bespoke manner, one project at a time.  With this utility, 
we're hoping to create a quick and easy way to take a sample header row from 
the data that we are simulating, and set a few parameters (ranges, factor 
lists, data descriptions) and create as many example rows as we expect will 
be necessary so that analysis code can be written long before a given 
experiment is finished.

The most mature program to run is mockData.py, but there are good ideas in
fakeData.py as well, which is gives similar results but requires more programming
skill to use.

There are a couple of useful tools to simulate or validate RAMQ numbers (health 
system access numbers in Quebec, Canada (Régie de l’assurance maladie)), which are
important for the authors' work, and remain here for use if they are needed.

Details: 
The output file is opened up for appending, so you can run the program many 
times, making your file longer each time.  If that isn't the result you want, 
be sure to delete the evidence of earlier attempts.

The format for dates is the standard Python formatting codes from the datetime 
module, documented here: 

https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes

Prerequisites:
This is a Python program, to install Python, go to https://python.org
It uses 4 modules (programs that extend the basic Python language):
    csv, random, datetime, faker
The first three are included in standard Python, but the last one is found here:
https://pypi.org/project/Faker/

TODO:
Add a distribution (triangle, Gaussian, Gamma, Weibull, etc.) specifier for "number" data
