import moviepy.editor 
from pathlib import Path 

# video = moviepy.editor.VideoFileClip('video.avi')
# audio = video.audio 
# audio.write_audiofile('audio.mp3')

video_file = Path('video.avi')

video = moviepy.editor.VideoFileClip(f'{video_file}')
audio = video.audio 
audio.write_audiofile(f'{video_file.stem}.mp3')
