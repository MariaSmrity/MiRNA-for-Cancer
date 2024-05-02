import os
import gzip
import csv

def get_tcga_zip_folders(directory):
    tcga_zip_folders = []
    for filename in os.listdir(directory):
        if filename.startswith('TCGA') and filename.endswith('.gz'):
            index = filename.rfind('.')
            if index != -1:  # If period found
                tcga_zip_folders.append(filename[:index])
            #tcga_zip_folders.append(filename)
    return tcga_zip_folders

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

def generate_csv_filename(input_string):
    # Define transformation rules
    transformations = {
        "sampleMap_HiSeqV2": "target_ex",
        "sampleMap_miRNA_HiSeq_gene": "mir_ex"
    }    
     # Remove "TCGA." prefix
    input_string = input_string.replace("TCGA.", "")
    # Iterate through transformation rules
    for key, value in transformations.items():
        if key in input_string:
            return input_string.replace(key, value)

# path to read folder name
zip_folders_address = 'C:/Users/User/Downloads'
# path to extract zip files
extract_to_path = 'D:/Masters Tampere/3rd period/Research project/Cancer Files'
tcga_zip_folders = get_tcga_zip_folders(zip_folders_address)

#print("Zip folders in the download folder starting with 'TCGA':")
for folder in tcga_zip_folders:
    print(folder)
    filename =  generate_csv_filename(folder)
    print(filename)
    zip_file_path = zip_folders_address + '/'+ folder + '.gz'
    extract_file_path = extract_to_path + '/'+ filename + '.csv'
    text_file_path = zip_folders_address + '/'+ folder + '.txt' 
    # Unzip the gz file
    unzip_gz_and_save_as_csv(zip_file_path, text_file_path)
    # Convert the text file to CSV
    txt_to_csv(text_file_path, extract_file_path)



    #unzip_gz_file(zip_file_path, extract_file_path)

