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
            for video in p.videos:
                video.streams.get_audio_only().download(path)
                
        except:
            print("Playlist must be unlisted or public, not private!")

    else:
        YouTube(link).streams.get_audio_only().download(path)


# ys = yt.streams.filter(only_audio=True).get_highest_resolution()  # , progressive=True)
# https://www.youtube.com/watch?v=Vj4Y1c-DSM0
