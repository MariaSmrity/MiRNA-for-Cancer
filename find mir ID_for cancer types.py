import pandas as pd
import csv
import numpy as np

colnames=['mir_no', 'miR_id', 'species_head', 'species_tail', 'iden'] 

df1 = pd.read_csv('../Cancer Files/KIRC.csv')
df2 = pd.read_csv('mir-id.csv', names=colnames, header=None)
indx = -1
mir1 = df1['Mir1'].tolist()
mir2 = df1['Mir2'].tolist()
mir_No = []
mir_Identifier = []
miRna_1_id = []
miRna_2_id = []

#print(mir2)
#df1.insert(2, miRna1_ID, value)

type = df2['species_head'].tolist()

for i in range(len(type)):
   if(type[i]=='Homo'):
      mir_No.append(df2['mir_no'][i].lstrip('>').lower())
      mir_Identifier.append(df2['miR_id'][i])
with open("Homo.txt", "w") as txt_file:
    for line in mir_No:
        txt_file.write((line) + "\n") 

# Create a dictionary for mir_No values
mir_mapping = dict(zip(mir_No, mir_Identifier))

# Initialize lists to store mir_Identifier values corresponding to mir1
mir1_identifier = []
mir2_identifier = []
# Iterate through mir1 and check for matches in mir_No
for mir in mir1:
    if mir in mir_mapping:
        mir1_identifier.append(mir_mapping[mir])
    else:
        mir1_identifier.append('N/A')

for mir in mir2:
    if mir in mir_mapping:
        mir2_identifier.append(mir_mapping[mir])
    else:
        mir2_identifier.append('N/A')

try:
   df1.insert(1, "miR 1_ID", mir1_identifier)
   df1.insert(3, "miR 2_ID", mir2_identifier)
except:
   print('')

df1.to_csv('../Cancer Files/KIRC.csv',index=False)

