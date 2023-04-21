import json
import os
import shutil
import argparse
import tempfile

# create argument parser
parser = argparse.ArgumentParser(description='Merge JSON files with similar structures.')
parser.add_argument('dir', nargs='?', default='.', help='Directory containing JSON files (default: current directory)')
args = parser.parse_args()

# get the path of the directory containing the JSON files
dir_path = os.path.abspath(args.dir)

# check if merged_data directory already exists
merged_dir_path = os.path.join(dir_path, 'merged_data')
if os.path.exists(merged_dir_path):
    print('Error: merged_data directory already exists. Please remove it and try again.')
    exit()

# create merged_data directory
os.makedirs(merged_dir_path)

# create a temporary directory to store intermediate files
temp_dir = tempfile.mkdtemp()

# merge JSON files
merged_data = {}
for filename in os.listdir(dir_path):
    if filename.endswith('.json'):
        file_path = os.path.join(dir_path, filename)
        with open(file_path) as f:
            data = json.load(f)
            merged_data.update(data)

# write merged data to a temporary file
temp_file_path = os.path.join(temp_dir, 'temp_merged.json')
with open(temp_file_path, 'w') as f:
    json.dump(merged_data, f, indent=4)

# move temporary file to merged_data directory
shutil.move(temp_file_path, os.path.join(merged_dir_path, 'merged_data.json'))

# delete temporary directory and its contents
shutil.rmtree(temp_dir)

print('JSON files merged successfully.')
