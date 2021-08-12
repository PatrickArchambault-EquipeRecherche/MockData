from faker import Faker
import pandas as pd
import random
import datetime
from random import choice
from string import ascii_uppercase
faker = Faker(['en_CA'])
import csv

#Fonction qui genere un numero de ramq
def ramq_generator(DDN,last_name,first_name,sex, admin_code):
    ramq = last_name[0:3].upper()
    ramq = ramq + first_name[0].upper()
    ddn = DDN
    year = ddn[0:4]
    month = ddn[5:7]
    day = ddn[8:10]
    ramq = ramq + year[2:4]
    if sex == "M" :
        ramq = ramq + month
    if sex == "F" :
        ramq = ramq + str((int(month) + 50))
    ramq = ramq + day
    ramq = ramq + admin_code
    return ramq

#generer une liste de fake data qui sera stocke dans le tableau dataframe (DF)
df = []
for n in range(50):
    if random.randint(0, 1) == 0:
        sex = "M"
    else:
        sex = "F"
        RecordID = faker.random_number()
        First_Name = faker.first_name_male() if sex == "M" else faker.first_name_female()
        Last_Name = faker.last_name()
        DDN = str(faker.date_of_birth(minimum_age = 18, maximum_age = 115))
        CodePostal = faker.postcode()
        Date_Heure_Sortie = faker.date_time()
        Date_Heure_index = faker.date_time()
        Date_Gem = faker.date_time()
        Adresse = faker.street_address()
        No_dossier = faker.random_number()
        Territoire_CLSC = faker.city()
    df.append({
        'RecordID': RecordID,
        'Sex': sex,
        'First_Name': First_Name,
        'Last_Name': Last_Name,
        'DDN': DDN,
        'CodePostal': CodePostal,
        'Date_Heure_sortie':Date_Heure_Sortie,
        'Date_Heure_index':Date_Heure_index,
        'Date_Gem':Date_Gem,
        'Adresse': Adresse,
        'No_dossier': No_dossier,
        'Territoire_CLSC': Territoire_CLSC,
        'RAMQ': ramq_generator(DDN, Last_Name, First_Name, sex, admin_code=str(random.randint(10, 99)))
              })

df = pd.DataFrame(df)
df = df[['RecordID','First_Name','Last_Name', 'DDN','CodePostal','Date_Heure_sortie',
         'Date_Heure_index','Date_Gem','Adresse','No_dossier','Territoire_CLSC','RAMQ']]
print(df)

#Ecrire ce tableau dans un fichier CSV pour le lire sur excel
df.to_csv("DataFrame.csv")

import random

#liste de numeros random pour prenom, nom et record ID

liste = random.sample(range(100000,999999), 150)

with open('ListeNoRandom.txt', 'w') as file:

    for i in liste:

        if i not in open('ListeNoRandom.txt','r'):

            file.write(str(i) + '\n')





