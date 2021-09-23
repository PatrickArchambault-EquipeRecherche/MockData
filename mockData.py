#!/usr/bin/python

"""Create mock data matching the parameters of your projected real data, to 
test your analyses on. Parameters are written in a CSV file, mock data is 
written into a CSV file."""

import csv
import random
import faker
import datetime

# Here is the basic function to create a single cell of data
def fakeIt(type , start=None , end=None , length=None , description=None):
    if (type == "boolean"):
        return (random.randint( 0 , 1))
    elif (type == "integer"):
        my_integer = random.randint( int(start) , int(end) )
        return (my_integer)
    elif (type == "string"):
        fake = faker.Faker()
        return (fake.text(int(length))) 
    elif (type == "factor"):
        description = description.split( "|" )
        return (random.choice( description ))
    elif (type == "number"):
        return (random.uniform( int(start) , int(end) ))
    elif (type == "name"):
        if description == None:
            fake = faker.Faker()
            return (fake.name())
        else:
            fake = faker.Faker(description)
            return (fake.name())
    elif (type == "date"):
        fake = faker.Faker()
        start = datetime.datetime.strptime(start , description)
        end = datetime.datetime.strptime(end , description)
        my_date = fake.date_between( start , end )
        return (my_date.strftime(description))
    else:
        print("Unknown 'type', looks like: " + type)
        return False

# Here is the function for reading and writing the CSV file.
def mockData(parameterfile , count , filename = None):
    if filename == None:
        filename = "mockdata.csv"
    else:
        pass
    with open(filename , "a+", newline='') as output , open(parameterfile , "r") as params:

        parameters = csv.reader(params)
        param_grid = []
        output_grid = []
        for row in parameters:
            param_grid.append(row)
        columnname = param_grid[0]
        datatype = param_grid[1]
        range_start = param_grid[2]
        range_end = param_grid[3]
        length = param_grid[4]
        description = param_grid[5]
        number_of_final_columns = len(columnname)
        
        csv_output = csv.writer(output, delimiter=',')
        
        csv_output.writerow(columnname[1:])

        for j in range(1,count+1):
            tmp_row = []
            for i in range(1, number_of_final_columns):
                tmp_row.append(fakeIt(  type=datatype[i],
                                        start=range_start[i],
                                        end=range_end[i],
                                        length=length[i],
                                        description=description[i]))
            output_grid.append(tmp_row)
        
        #print(output_grid)
        csv_output.writerows(output_grid)

    return True

# Example for testing
mockData("parameters.csv" , 100)

# fakeIt examples, based on defined code in the default parameters.csv file
#print(fakeIt(name="a",type="integer",start=0,end=304))
#print(fakeIt(name="b",type="factor",description="red|yellow|blue|green"))
#print(fakeIt(name="c",type="string",length=200))
#print(fakeIt(name="d",type="number",start=90,end=200))
#print(fakeIt(name="e",type="date",start="2021-08-10",end="2021-12-10",description="%Y-%m-%d"))
