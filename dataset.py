import os
import zipfile
import pandas as pd

# Step 1: Define paths
zip_path = "C:/Users\Harshal Trivedi\Desktop/LLM_projects/project2/sep-28k.zip"  # Update with your actual path
extract_path = "C:/Users/Harshal Trivedi/Desktop/LLM_projects/project2/extract_data"  # Update to your desired extraction directory

# Step 2: Extract the ZIP file
if not os.path.exists(extract_path):
    os.makedirs(extract_path)

print("Extracting the dataset...")
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)
print("Extraction completed.")

# Step 3: Check extracted files
print("Files in the extraction directory:")
print(os.listdir(extract_path))

# Step 4: Load the dataset (assuming CSV or relevant file format)
csv_file = os.path.join(extract_path, "sep_28k.csv")  # Replace with the correct file name

if os.path.exists(csv_file):
    print("Loading the dataset...")
    data = pd.read_csv(csv_file)
    print("Dataset loaded successfully. Here are the first 5 rows:")
    print(data.head())
else:
    print("Dataset file not found. Check the extracted files and update the file path.")
