# MiRNA-for-Cancer

InForMir Code Documentation

Introduction:

Welcome to the documentation for InForMir codes. This document will guide you through the steps necessary to set up and execute the codes successfully.

Prerequisites:

Before running the codes, ensure that the following prerequisites are met:

1. Python
2. Microsoft Excel
Installation:
1. Clone the repository from https://github.com/MariaSmrity/MiRNA-for-Cancer.git to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies using the following command:
   [Your package manager] install [dependencies]

Running the Codes:
Follow these steps to execute the codes:
1. Open your terminal/command prompt.
2. Navigate to the project directory.
3. Have “mir-gene-interaction.csv” in the drive.
a. Run “seperate_chromosome__from_mainFile.py”  // where main file is mir-gene-interaction.csv,  output file is “Target.csv”
b. Run “CoopOrCom.py” //  it will create Final.CSV
c. Run “SeperateFileForCancerType.py”  // it will separate Final.csv into cancertype.csv files
d.Run “Mir1_2 Scores Compare.py” // it will plot and save mir1 and mir2 scores.

4. Have “InFormiR_TCGA-data-download-link 1.csv” in your drive.
	a. Run “download_files.py” //It will download files for sample patients
	b. Run “unzip files.py” to unzip downloaded files to the desired location
	c.Run “Create Correlation file.py” //generate file with desired format from downloaded files 
	d. Run “calculate_correlation.py” // Update file with correlation values
	e. Finally Run “plot_correlation.py” // plot and save files in folder

