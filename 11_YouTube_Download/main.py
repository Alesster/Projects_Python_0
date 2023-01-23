from pytube import YouTube

link = input("Enter YouTube link: ")

yt = YouTube(link)

print(f"Title: {yt.title}")
print(f"Number of views: {yt.views}")
print(f"Length of the video: {yt.length}")

ys = yt.streams.get_highest_resolution()
ys.download()
print("Video downloaded!")