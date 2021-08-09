#!/usr/bin/python

"""Create mock data matching the parameters of your projected real data, to 
test your analyses on. Parameters are written in a CSV file, mock data is 
written into a CSV file."""

import pandas
import random
import faker

def integer(name , start , end):
    number = random.randint( start , end)
    return (name , number)

def factor(name , factors):
    return (name , random.choice(factors))

def string(name , length):
    fake = faker.Faker()
    return (name , fake.text(length))


def mockData(parameterfile , count , filename = None):
    if filename == None:
        filename = "mockdata.csv"
    else:
        pass
    with open(filename , "a") as output , open(parameterfile , "r") as params:

        parameters = pandas.read_csv(params , index_col=0)
        print(parameters)

        out_array = []
        df = pandas.DataFrame(out_array)
        df.to_csv(output)
    return True

#mockData("parameters.csv" , 100)

print(integer("a",0,304))
print(factor("a",("red","yellow","blue","green")))
print(string("a",200))
