Convert PDF to Audio MP3
https://www.youtube.com/watch?v=Q0lHb-FCATk

pyPDF2 is not good for this task, use pdfplumber.

pip install pdfplumber gtts art
art is not necessary, it is used for nice logo to terminal

from pathlib import Path - to check and fine pathways of files.

from art import tprint - it is used to show logo
Example:
tprint('PDF>>TO>>MP3', font='bulbhead')

 ____  ____   ____ __  __   ____  _____ __  __   __  __  ____  ___
(  _ \(  _ \ ( ___)\ \ \ \ (_  _)(  _  )\ \ \ \ (  \/  )(  _ \(__ )
 )___/ )(_) ) )__)  > > > >  )(   )(_)(  > > > > )    (  )___/ (_ \
(__)  (____/ (__)  /_/ /_/  (__) (_____)/_/ /_/ (_/\/\_)(__)  (___/
