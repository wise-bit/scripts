import os
import shutil
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio

source_folder = 'files'
destination_folder = 'files/converted'

os.makedirs(destination_folder, exist_ok=True)

files = os.listdir(source_folder)

for file in files:
  if file.endswith('.mp4'):
    new_file_name = os.path.splitext(file)[0] + '.mp3'

    source_path = os.path.join(source_folder, file)
    destination_path = os.path.join(destination_folder, new_file_name)

    ffmpeg_extract_audio(source_path, destination_path)

print("Conversion and renaming complete.")
