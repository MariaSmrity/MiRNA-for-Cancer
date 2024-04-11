import pandas as pd
import csv
import numpy as np

df1 = pd.read_csv('miRNA_GA_gene.csv')
df2 = pd.read_csv('HiSeqV2_PANCAN.csv')
df3 = pd.read_csv('BLCA.csv')

#Patient_1 = df1.iloc[0:0]
#Patient_2 = df2.iloc[0:0]


Target_list = df3.Target.unique()#find target list for cancertype
with open("Target.txt", "w") as txt_file:
    for line in Target_list:
        txt_file.write((line) + "\n") 

Target_2 = df2['sample']
specific_rows = [0]
for i in range(len(Target_2)):
    if(Target_2[i] in Target_list):
        specific_rows.extend([i])
df4 = pd.read_csv('HiSeqV2_PANCAN.csv', skiprows = lambda x: x not in specific_rows)
df4.to_csv("Table 1.csv", index=False) 

df5 = pd.read_csv('Table 1.csv')
PatientID_T = list(df5.columns)
PatientID_M = list(df1.columns)
#PetientID = PetientID.pop('sample')
#print(PetientID)
df5.rename(columns={ df5.columns[0]: "Target" }, inplace = True)
df1.rename(columns={ df1.columns[0]: "MirID" }, inplace = True)
header_list = ['Attribute','Val']

def WriteHeader():
    with open( 'newFile.csv', 'w', newline='') as f:
    # Create a CSV writer object that will write to the file 'f'
        csv_writer = csv.writer(f)    
    # Write the field names (column headers) to the first row of the CSV file
        csv_writer.writerow(header_list)
        #csv_writer.writerow(['MirID'])
        #csv_writer.writerow(['Target'])


for col1 in df5.columns:
    #print(col1)
    for col2 in df1.columns:
        if(col1 == col2):
            header_list.append(col1)
           
WriteHeader()


def insertValue(TempP, TargetEntry,MirIDEntry,TargetValuePoint,MirValuePoint, k):
  
    dfn = pd.read_csv('newFile.csv')
    currentrow = k * 2
    nextrow = currentrow + 1
    # Insert the specific values into the desired cells
    dfn.at[currentrow, 'Attribute'] = 'MirID'
    dfn.at[nextrow, 'Attribute'] = 'Target'
    dfn.at[currentrow, 'Val'] = MirIDEntry
    dfn.at[nextrow, 'Val'] = TargetEntry
    dfn.at[currentrow, TempP] = MirValuePoint
    dfn.at[nextrow, TempP] = TargetValuePoint

    # Save the modified DataFrame back to the CSV file
    dfn.to_csv('newFile.csv', index=False)
    currentrow = currentrow+2
    nextrow = nextrow+2


PatientID_T = list(df5.columns)
PatientID_M = list(df1.columns)
Targetlist = df5['Target']
MirIDlist = df1['MirID']


dff = pd.read_csv('newFile.csv')

#v = df5['TCGA-AB-2872-03'].loc[df5.index[0]]
#print(v)

for i in range(len(header_list)):
    temp_P = header_list[i]
    TargetValuePoint=[]
    MirValuePoint = []
    TargetEntry = []
    MirIDEntry = []
    for k in range(len(PatientID_T)):
        if(PatientID_T[k]==temp_P):
            x = Targetlist[k]
            y= MirIDlist[k]
            TargetEntry.append(x)
            MirIDEntry.append(y)
            #TargetValuePoint.append(df5[temp_P].loc[df5.index[k]])
            #MirValuePoint.append(df1[temp_P].loc[df5.index[k]])
            TargetValuePoint = (df5[temp_P].loc[df5.index[k]])
            MirValuePoint = (df1[temp_P].loc[df5.index[k]])
            #print(TargetValuePoint,MirValuePoint)
            array_dtype = MirValuePoint.dtype
            #print(array_dtype)
            has_null_values = np.isnan(MirValuePoint).any()
            if (has_null_values):
                print(MirValuePoint)
            else:
                 #print(TargetValuePoint,MirValuePoint)
                 insertValue(temp_P,x,y,TargetValuePoint,MirValuePoint,i)


# Load the CSV file into a DataFrame
df = pd.read_csv('newFile.csv')

# Remove empty columns
df = df.dropna(axis=1, how='all')

# Save the modified DataFrame back to a CSV file
df.to_csv('newFile.csv', index=False)