import pandas as pd
import csv

df = pd.read_csv('Final.csv')
CancerType = df['Cancer Type'].tolist()
Now_Cancer_Type = 'BLCA'

"""# insert the list to the set
list_set = set(CancerType)
# convert the set to the list
unique_list = (list(list_set))
with open("CancerTYpe.txt", "w") as txt_file:
    for line in unique_list:
        txt_file.write((line) + "\n") 
print(unique_list)"""

header_list=["Mir1","Mir2","Target","Distance","Interaction Type","Chromosome","Chromosome Stand","Mir1 Begin Position","Mir1 End Position","Mir1 Score","Mir1 Pvalue","Mir2 Begin Position","Mir2 End Position","Mir2 Score","Mir2 Pvalue", 'Cancer Type']

"""def SeperateFileForCancerType(i, cancertype):
    with open( cancertype + '.csv', 'a', newline='') as f:
    # Create a CSV writer object that will write to the file 'f'
        csv_writer = csv.writer(f)    
    # Write the field names (column headers) to the first row of the CSV file
        csv_writer.writerow(df.values[i])

def WriteHeader(cancertype):
    with open( cancertype + '.csv', 'w', newline='') as f:
    # Create a CSV writer object that will write to the file 'f'
        csv_writer = csv.writer(f)    
    # Write the field names (column headers) to the first row of the CSV file
        csv_writer.writerow(header_list)"""

file = open("CancerType.txt", "r")
content = file.readlines()

#print(content[5].strip())
file.close()

#def InitiateCancerWrite(Now_Cancer_Type):
"""for i in range(len(CancerType)):
        if(Now_Cancer_Type == CancerType[i]):
            print(Now_Cancer_Type, CancerType[i])
            #SeperateFileForCancerType(i, CancerType[i])
        else:
            #Now_Cancer_Type = CancerType[i]
            WriteHeader(Now_Cancer_Type)
           # SeperateFileForCancerType(i, CancerType[i])
"""

#for k in range(28,30):
now_cancerType = 'UCS'  #content[k].strip()
with open( now_cancerType + '.csv', 'w', newline='') as f:
# Create a CSV writer object that will write to the file 'f'
    csv_writer = csv.writer(f)    
# Write the field names (column headers) to the first row of the CSV file
    csv_writer.writerow(header_list)
for i in range(len(CancerType)):
    if(CancerType[i]== now_cancerType):
        with open( now_cancerType + '.csv', 'a', newline='') as f:
        # Create a CSV writer object that will write to the file 'f'
            csv_writer = csv.writer(f)    
        # Write the field names (column headers) to the first row of the CSV file
            csv_writer.writerow(df.values[i])

