import pandas as pd
import csv
#import regex as re
#from itertools import islice

#df1 = pd.read_csv('BLCA.csv')
df2 = pd.read_csv('mir-gene-interaction.csv')

Chromosome_Location = df2['Sites_Loci'].tolist()
miRNA_ID=df2['MiRNA_ID'].tolist()
Target_Gene=df2['Gene_ID'].tolist()
Spearman_Correlation=df2['Spearman_Correlation'].tolist()
Score=df2['Sites_Score'].tolist()
P_Value=df2['Pvalue'].tolist()
Sites_Number=df2['Sites_Number'].tolist()
#Sites_Loci=df2['Sites_Loci'].tolist()
#Sites_Score=df2['Sites_Score'].tolist()
FDR_a = df2['FDR'].tolist()
Cancer_type = df2['Cancer_type'].tolist()


header_list=["Chromosome","Begin Position","End Position","Chromosome Stand","Sites_Score","miRNA_ID","Target_Gene","P_Value","Spearman_Correlation","FDR","Cancer_type"]

with open('Target.csv', 'w', newline='') as f:
# Create a CSV writer object that will write to the file 'f'
    csv_writer = csv.writer(f)    
# Write the field names (column headers) to the first row of the CSV file
    csv_writer.writerow(header_list)

for i in range(len(Chromosome_Location)):   
   restOfRow=[miRNA_ID[i],Target_Gene[i],P_Value[i],Spearman_Correlation[i],FDR_a[i],Cancer_type[i]]  
   
   occurrences = Chromosome_Location[i].split(';')
   ScoreNew = Score[i].split(';')


   for i in range(len(ScoreNew)):
            # Split the occurrence into its components based on ':'
            parts = occurrences[i].split(':')       

            # Extract the chromosome, start position, end position, and subtraction sign
            chromosome = parts[0]
            try:
                start_position, end_position = parts[1].split('-')
                Strand = parts[2]   
                NewRow= [chromosome, start_position, end_position, Strand, ScoreNew[i]]
                NewRow.extend(restOfRow)
                #write rows into Target file
                with open('Target.csv', 'a', newline='') as f:  
                    csv_writer = csv.writer(f) 
                    csv_writer.writerow(NewRow)
            except IndexError as e:
                break
   

       

