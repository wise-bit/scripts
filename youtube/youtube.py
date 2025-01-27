# python3 -m pip install git+https://github.com/pytube/pytube  

import sys
from pytube import YouTube, Playlist

if __name__ == "__main__":
  path = "./files"
  if len(sys.argv) < 2:
    link = input("Enter link of video or playlist: ")
  else:
    link = sys.argv[1]

  if "playlist" in link:
    p = Playlist(link)
    try:
      print(f"Downloading: {p.title}")
      index = 1
      for video in p.videos:
        print(f"Downloading audio {index} of {len(p.videos)}")
        index += 1
        video.streams.get_audio_only().download(path)

    except:
      print("Playlist must be unlisted or public, not private!")

  else:
    YouTube(link).streams.get_audio_only().download(path)


# yt.streams.filter(only_audio=True).get_highest_resolution()  # , progressive=True)
# yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download()
# TEST: https://www.youtube.com/watch?v=Vj4Y1c-DSM0