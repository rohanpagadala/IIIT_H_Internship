import os
from yt_dlp import YoutubeDL

download_dir = "video_download"
os.makedirs(download_dir, exist_ok=True)

video_url = 'https://www.youtube.com/watch?v=IdSD3wNm1zQ'

ydl_opts = {
    'format': 'mp4',
    'outtmpl': os.path.join(download_dir, 'input_video.mp4'),
    'noplaylist': True,
}

try:
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
    print(f"✅ Video downloaded successfully to {download_dir}/input_video.mp4")
except Exception as e:
    print(f"❌ Failed to download video: {e}")
