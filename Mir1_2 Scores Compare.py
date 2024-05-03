import matplotlib.pyplot as plt
import pandas as pd
#import csv
import seaborn as sns

# Open the file in read mode
with open('../Cancer Files/CancerType.txt', 'r') as file:
    # Read the contents of the file
    Cancertype = file.read().splitlines()

def PlotMiRNA(cancer):        
    df = pd.read_csv('../Cancer Files/' + cancer + '.csv')
    data_x = df['Mir1 Score']
    data_y = df['Mir2 Score']

    fig, ax = plt.subplots()

    sns.kdeplot(data=data_x.squeeze(), ax=ax, color='red', fill=True, label='MiRNA 1 Score')
    sns.kdeplot(data=data_y.squeeze(), ax=ax, color='green', fill=True, label='MiRNA 2 Score')

    ax.legend(bbox_to_anchor=(1.02, 1.02), loc='upper left')
    plt.tight_layout()
    plt.xlabel('MiRNA Score Comparison for Cancer type ' + cancer)

    # Specify the path where you want to save the PNG file
    save_path = 'OutPut/'

    # Save the figure as a PNG file in the specified folder
    plt.savefig(save_path + cancer + 'mir 1_2_Score.png')
    plt.show()

for i in range(len(Cancertype)):
    PlotMiRNA(Cancertype[i])



