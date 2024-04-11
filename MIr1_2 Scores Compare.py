import matplotlib.pyplot as plt
import pandas as pd
#import csv
import seaborn as sns

df = pd.read_csv('BLCA.csv')
data_x = df['Mir1 Score']
data_y = df['Mir2 Score']

"""sns.kdeplot(df['Mir1 Score'], fill=True)
sns.kdeplot(df['Mir2 Score'], fill= True)"""

fig, ax = plt.subplots()

sns.kdeplot(data=data_x.squeeze(), ax=ax, color='red', fill=True, label='MiRNA 1 Score')
sns.kdeplot(data=data_y.squeeze(), ax=ax, color='green', fill=True, label='MiRNA 2 Score')

ax.legend(bbox_to_anchor=(1.02, 1.02), loc='upper left')
plt.tight_layout()
plt.xlabel('MiRNA Score Comparison for Cancer type BLCA')
plt.show()

# Calculate Pearson correlation coefficient
#correlation_coefficient = np.corrcoef(data_x, data_y)[0, 1]

#print("Pearson correlation coefficient:", correlation_coefficient)

