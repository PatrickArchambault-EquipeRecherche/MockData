#!/usr/bin/python

"""Create mock data matching the parameters of your projected real data, to 
test your analyses on. Parameters are written in a CSV file, mock data is 
written into a CSV file."""

from os import name
import pandas
import random
import faker
import datetime

def fakeIt(name, type , start=None , end=None , length=None , description=None):
    if (type == "boolean"):
        return (name , random.randint( 0 , 1))
    elif (type == "integer"):
        my_integer = random.randint( start , end )
        return (name , my_integer)
    elif (type == "string"):
        fake = faker.Faker()
        return (name , fake.text(length)) 
    elif (type == "factor"):
        description = description.split( "|" )
        return (name , random.choice( description ))
    elif (type == "number"):
        return (name , random.uniform( start , end ))
    elif (type == "date"):
        fake = faker.Faker()
        start = datetime.datetime.strptime(start , description)
        end = datetime.datetime.strptime(end , description)
        my_date = fake.date_between( start , end )
        return (name , my_date.strftime(description))
    else:
        print("Unknown 'type', looks like: " + type)


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

print(fakeIt(name="a",type="integer",start=0,end=304))
print(fakeIt(name="b",type="factor",description="red|yellow|blue|green"))
print(fakeIt(name="c",type="string",length=200))
print(fakeIt(name="d",type="number",start=90,end=200))
print(fakeIt(name="e",type="date",start="2021-08-10",end="2021-12-10",description="%Y-%m-%d"))
