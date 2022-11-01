#!/usr/bin/python

"""
A weird collection of RAMQ number-related things.

Eventually including:
    1. sanity-checking RAMQ number against name and birthdate
    2. generate a RAMQ number from name, birthdate, assigned sex
    3. generate a random RAMQ number that follows the rules
    
"""

import datetime
import random
import faker
import unidecode

# Sample RAMQ Number and related information
my_ramq = "TREL 8602 0211"
my_first_name = "Luc-Antoine"
my_last_name = "Trembley"
my_birthdate = "1986-02-02"
sex = "m"

# Make a RAMQ Number from name and birthdate
def makeRAMQ(birthdate , last_name , first_name , last_two , sex , date_format="%Y-%m-%d"):
    # If it is a deterministic number we're looking for, we specify the last
    # two digits, otherwise we generate them at random.
    bd_dt = datetime.datetime.strptime(birthdate, date_format)
    first_initial = unidecode.unidecode(first_name[0].upper(), "utf-8")
    short_lastname = unidecode.unidecode(last_name[0:3].upper(), "utf-8")
    aleatoire_bit = last_two
    year = bd_dt.strftime("%y")
    month = bd_dt.strftime("%m")
    if sex == "m":
        pass
    else:
        month = str(int(month) + 50)
    day_aleatoire = bd_dt.strftime("%d") + str(aleatoire_bit)
    new_ramq = short_lastname + first_initial + year + month + day_aleatoire

    return new_ramq

#print(makeRAMQ(my_birthdate,my_last_name,my_first_name))

def randomRAMQ(startdate="1910-01-01" , enddate="2020-01-01" , format="%Y-%m-%d" , full=False):
    # Use faker to create a name and birthdate, then call makeRAMQ
    fake = faker.Faker("fr_CA")
    start = datetime.datetime.strptime(startdate , format)
    end = datetime.datetime.strptime(enddate , format)
    birthdate = datetime.datetime.strftime(fake.date_between( start , end ),format)
    sex = "m" if (random.randint(0,1) == 0) else "f"
    last_name = fake.last_name()
    if sex == "m":
        first_name = fake.first_name_male()
    else:
        first_name = fake.first_name_female()
    aleatoire_bit = "%02d" % random.randint(0,99)
    date_format = "%Y-%m-%d"
    new_ramq = makeRAMQ(birthdate, last_name, first_name, aleatoire_bit, sex , date_format)
    if full == True:
        result = f"""
Birthdate: {birthdate}
Last Name: {last_name}
First Name: {first_name}
Sex: {sex}
RAMQ: {new_ramq}
"""
    else:
        result = new_ramq
    return result

#print(randomRAMQ())

# Check a RAMQ number against name, birthdate
def checkRAMQ(ramq_number , birthdate , last_name , first_name , sex , date_format="%Y-%m-%d"):
    # Make a RAMQ number from the information provided
    last_two = ramq_number[-2:]
    generated_ramq_number = makeRAMQ(birthdate, last_name, first_name, last_two, sex, date_format)

    # Remove any spaces in the RAMQ Number
    ramq_number = ramq_number.replace(" ","")

    if (generated_ramq_number == ramq_number):
        #print("RAMQ Numbers Match: " + ramq_number + " : " + generated_ramq_number)
        return True
    else:
        #print("ERROR: RAMQ Numbers Do Not Match: " + ramq_number + " : " + generated_ramq_number + "!")
        return False

    

#checkRAMQ(my_ramq, my_birthdate, my_last_name, my_first_name)
if __name__ == "__main__":
    print(randomRAMQ("1950-01-01","2022-01-01",full=True))