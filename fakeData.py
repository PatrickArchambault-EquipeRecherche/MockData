from faker import Faker
import pandas as pd
faker = Faker(['en_CA'])
import csv

##generer une liste of fake data qui sera stocké dans le tableau dataframe (DF)
df = []

for n in range(50):
    df.append({
               #'RAMQ': faker.number(),
        'First_Name': faker.first_name(),
        'Last_Name': faker.last_name(),
        'DDN': faker.date_of_birth(),
        'CodePostal': faker.postcode(),
        'Date_Heure_sortie':faker.date_time(),
        'Date_Heure_index':faker.date_time(),
        'Date_Gem':faker.date_time(),
        'Adresse': faker.street_address(),
        'No_dossier': faker.random_number(),
        'Territoire_CLSC': faker.city(),
        'RAMQ': faker.lexify(text='Random Identifier: ????12345678', letters='ABCDEFGHIJKLMOPQRSTUVS')
              })

df = pd.DataFrame(df)
df = df[['First_Name','Last_Name', 'DDN','CodePostal','Date_Heure_sortie',
         'Date_Heure_index','Date_Gem','Adresse','No_dossier','Territoire_CLSC','RAMQ']]
print(df)

##on veux écrire ce tableau dans un fichier CSV pour le lire sur excel
df.to_csv("DataFrame.csv")

