from __future__ import unicode_literals
import youtube_dl

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    jls_extract_var = 'https://www.facebook.com/100007345007176/videos/529250288137519/'
    ydl.download([jls_extract_var])