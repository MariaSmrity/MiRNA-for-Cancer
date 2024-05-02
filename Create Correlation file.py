import pandas as pd
from scipy.stats import pearsonr
from scipy.stats import spearmanr
import matplotlib.pyplot as plt

def create_correlation_files(Cancertype):
    # Read CSV files into pandas DataFrames
    p2 = pd.read_csv('../Cancer Files/' + Cancertype + '.target_ex.csv')
    p1 = pd.read_csv('../Cancer Files/' + Cancertype+ '.mir_ex.csv')

    # Extract values from DataFrames
    common_columns = list(set(p1.columns) & set(p2.columns))  # Get common columns
    # Initialize an empty list to store data
    data = []

    # Create DataFrame
    df_pearson = pd.DataFrame(columns=['target', 'mirID', 'Pearson_correlation', 'Pearson_p_val','Spearman_corr','Spearman_pval'])

    # Function to process x and y values for each column
    def process_values(x, y, mirID, Target):
        pearson_corr, pearson_p_value = pearsonr(x, y)
        #print("Pearson correlation coefficient:", correlation_coefficient)

        # calculate Spearman's correlation coefficient and p-value
        spearman_corr, spearman_pval = spearmanr(x, y)

        # Insert rows
        data.append({'mirID': mirID, 'target': Target, 'Pearson_correlation': pearson_corr, 'Pearson_p_val': pearson_p_value,'Spearman_corr': spearman_corr, 'Spearman_pval': spearman_pval })

    # Loop over rows and extract values for common columns
    for index, row in p1.iterrows():
        x = []
        y = []
        for column in common_columns:
            x_val = row[column]
            y_val = p2.at[index, column] if index in p2.index else None  # Check if index exists in p2
            if pd.notnull(x_val) and pd.notnull(y_val) and isinstance(x_val, (int, float)) and isinstance(y_val, (int, float)):  # Check if neither x nor y is null
                x.append(x_val)
                y.append(y_val)
            elif(isinstance(x_val,str) and isinstance(y_val,str)):
                target = y_val
                mirID = x_val
        if(len(x)>2):
            process_values(x, y,mirID,target)

    # Create DataFrame from the list of dictionaries
    df_pearson = pd.DataFrame(data)

    # Write DataFrame to CSV
    df_pearson.to_csv(Cancertype + '_Mir_Target_Correlation.csv', index=False)


# Open the file in read mode
with open('../Cancer Files/CancerType.txt', 'r') as file:
    # Read the contents of the file
    Cancername = file.read().splitlines()

for i in range(len(Cancername)):
    create_correlation_files(Cancername[i])
