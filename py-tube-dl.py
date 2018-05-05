'''

Uses youtube-dl and python to download songs directly without copy pasting URLs. Works for both windows and linux

'''

import os
import glob
import urllib.request
import urllib.parse
import re


def renamer(filename, number_preexisting):
	os.rename(max(glob.iglob('songs/*'), key=os.path.getctime), filename[0:6] + "00" + str(number_preexisting) + " " + filename[6:-16] + ".mp3")


def tube():
	s = input("Enter name of video, or 9 for downloading a playlist: ")
	try:
		if int(s) == 9:
			link = input("Enter playlist link: ")
			os.system("youtube-dl -x --audio-format mp3 --audio-quality 0 -o \"%(playlist_index)s-%(title)s.%(ext)s\" " + link)
			print("Playlist fetched")
			return 0
	except:
		print("Not a playlist, continuing...")
	query_string = urllib.parse.urlencode({"search_query" : s})
	html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
	search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
	i = 0
	loop = 0
	used = []
	num = int(input("How many songs with the query would you like to download (Default = 1): ") or "1")
	while loop < num:
		if search_results[i] in used:
			None
		else:
			link = "http://www.youtube.com/watch?v=" + search_results[i]
			used.append(search_results[i])
			#print(link, " ", i)
			os.system("cd songs & C:\\Users\\satra\\Documents\Programs\\Scripts\youtube-dl.exe -x --audio-format mp3 --audio-quality 0 " + link + " & cd ..")
			newest = max(glob.iglob('songs/*'), key=os.path.getctime)
			l = len(glob.glob('songs/*'))
			renamer(newest, l+1)
			loop += 1
		i += 1
	return 0

tube()
