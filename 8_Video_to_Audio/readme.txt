Substract audia from video
https://www.youtube.com/watch?v=4w4sSabOjl0&list=PLqGS6O1-DZLoAADhgzzkvc8ifKsKG4G-T&index=37

pip install moviepy
Docs: https://zulko.github.io/moviepy/

import moviepy.editor - Allows edit video in different ways: substract audio, cut, compress etc.

To create audio with the name of video:
from pathlib import Path 
Docs: https://docs.python.org/3/library/pathlib.html#basic-use

fideo_file.stem - stem delete expansion: video.avi => video