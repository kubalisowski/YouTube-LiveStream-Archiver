# YouTube-LiveStream-Archiver
Application created basing on youtube-dl (https://github.com/ytdl-org/youtube-dl) and ffmpeg libraries.
Both need to be installed to use the app!

App checks if channels specified in config.py file are broadcasting live stream and if yes, video is recording.
There are different authentication keys specified in config to communicate with YouTube API.

Archiver creates a foler under specified location named by date of executing code.

App might be run constantly or execute as an scheduled task.
