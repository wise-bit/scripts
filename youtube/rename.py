import os

folder_path = 'files'
files = os.listdir(folder_path)

for file in files:
  if file.endswith('.mp3'):
    new_file_name = os.path.splitext(file)[0] + '.mp4'
    
    source_path = os.path.join(folder_path, file)
    destination_path = os.path.join(folder_path, new_file_name)
    
    os.rename(source_path, destination_path)

print("Renaming complete.")
