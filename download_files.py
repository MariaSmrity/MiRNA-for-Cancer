import csv
import webbrowser

def open_links_from_csv(csv_file, link_column_index):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header if present
        for row in reader:
            link = row[link_column_index]
            webbrowser.open_new_tab(link)
            print(f"Opened link: {link}")

# Example usage:
csv_file = 'InFormiR_TCGA-data-download-link 1.csv' # Specify the path to your CSV file
link_column_index = 0  # Specify the column index containing the links (0-indexed)
open_links_from_csv(csv_file, 2)
open_links_from_csv(csv_file, 3)


"""p2 = pd.read_csv('InFormiR_TCGA-data-download-link 1.csv')

target_url_list = p2['target_exp']
mir_url_list = p2['mir_exp']
filename_list = p2['cancer']

def downloadfile(url):
    # Example usage:
    url = 'http://example.com/file.zip'  # Replace with the URL of the file you want to download
    filename = 'file.zip'  # Specify the filename to save the downloaded file
    download_file(url, filename)

for i in range(len(mir_url_list)):
    download_file(mir_url_list[i],filename_list[i]+'_mir_ex')
    download_file(target_url_list[i],filename_list[i]+'_target_ex')
"""