import pytube

link = input("pass the link: ") 
yt = pytube.YouTube(link)

ys = yt.streams.get_highest_resolution()

print("Downloading...")
ys.download(filename="video.mp4")
print("Download completed!!")