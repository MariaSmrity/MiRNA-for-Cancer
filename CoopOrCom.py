import pandas as pd
import csv

df = pd.read_csv('Target.csv')
Chromosome = df['Chromosome'].tolist()

header_list=["Mir1","Mir2","Target","Distance","Interaction Type","Chromosome","Chromosome Stand","Mir1 Begin Position","Mir1 End Position","Mir1 Score","Mir1 Pvalue","Mir2 Begin Position","Mir2 End Position","Mir2 Score","Mir2 Pvalue", 'Cancer Type']

with open('Final.csv', 'w', newline='') as f:
# Create a CSV writer object that will write to the file 'f'
    csv_writer = csv.writer(f)    
# Write the field names (column headers) to the first row of the CSV file
    csv_writer.writerow(header_list)

def Insert_Row(i, type, distance):
    Mir1 = df['miRNA_ID'][i]
    Mir2 = df['miRNA_ID'][i+1]
    Target = df['Target_Gene'][i]
    Interaction_Type = type
    Distance = distance
    Chromosome = df['Chromosome'][i]
    Chromosome_Stand = df['Chromosome Stand'][i]
    Mir1_Begin_Position = df['Begin Position'][i]
    Mir1_End_Position = df['End Position'][i]
    Mir1_Score = df['Sites_Score'][i]
    Mir1_Pvalue =df['P_Value'][i]

    Mir2_Begin_Position =df['Begin Position'][i+1]
    Mir2_End_Position =df['End Position'][i+1]
    Mir2_Score =df['Sites_Score'][i+1]
    Mir2_Pvalue =df['P_Value'][i+1]
    Cancer_type = df['Cancer_type'][i]
    NewRow = [Mir1, Mir2, Target,  Distance, Interaction_Type, Chromosome,Chromosome_Stand,Mir1_Begin_Position,Mir1_End_Position,Mir1_Score,Mir1_Pvalue, Mir2_Begin_Position,Mir2_End_Position,Mir2_Score,Mir2_Pvalue,Cancer_type]
    with open('Final.csv', 'a', newline='') as f:  
                    csv_writer = csv.writer(f) 
                    csv_writer.writerow(NewRow)

def ComparativeOrCompititive(i):
    
            if(df['Target_Gene'][i]==df['Target_Gene'][i+1] and df['Chromosome'][i]==df['Chromosome'][i+1]):
                try:
                    start = df['Begin Position'][i]
                    end =  df['Begin Position'][i+1]
                    distance = int(start)-int(end)
                    distance= (abs(distance))
                    #print(distance)
                    if ((distance>=8) & (distance<=500)):
                        Insert_Row(i,'Co-Operative',distance)

                    if((distance>=0) & (distance<=8)):
                        Insert_Row(i,'Competitive',distance)
                    else:
                        Insert_Row(i,'Neutral',distance)
                except KeyError as e:
                    return 0
            else:
                return 0                


for i in range(len(Chromosome)):
     if(i+1 < len(Chromosome)):
        ComparativeOrCompititive(i+1)