import gzip
import csv
import os

def unzip_gz_and_save_as_csv(gz_file_path, csv_file_path):
    # Unzip the .gz file
    with gzip.open(gz_file_path, 'rb') as f_in:
        with open(csv_file_path, 'wb') as f_out:
            f_out.write(f_in.read())

def txt_to_csv(txt_file_path, csv_file_path):
    # Read the contents of the txt file and split based on spaces
    with open(txt_file_path, 'r') as txt_file:
        data = [line.strip().split() for line in txt_file]

    # Write the data to a CSV file
    with open(csv_file_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(data)

# Example usage
gz_file_path = 'C:/Users/User/Downloads/TCGA.BRCA.sampleMap_HiSeqV2.gz'
csv_file_path = 'D:/Masters Tampere/3rd period/Research project/Cancer Files/file.csv'
unzipped_txt_file_path = 'D:/Masters Tampere/3rd period/Research project/Cancer Files/file.txt'

# Unzip the gz file
unzip_gz_and_save_as_csv(gz_file_path, unzipped_txt_file_path)

# Convert the text file to CSV
txt_to_csv(unzipped_txt_file_path, csv_file_path)


