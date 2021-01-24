from youtube_dl import YoutubeDL

audio_downloader = YoutubeDL({'format':'bestaudio'})
audio_downloader.extract_info(input('Enter youtube url :  '))