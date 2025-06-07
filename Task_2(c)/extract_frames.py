import os
import subprocess

video_path = "video_download/input_video.mp4"
frames_dir = "video_frames"
os.makedirs(frames_dir, exist_ok=True)

# Extract 1 frame per second
command = [
    "ffmpeg",
    "-i", video_path,
    "-vf", "fps=1",
    os.path.join(frames_dir, "frame_%04d.png")
]

try:
    subprocess.run(command, check=True)
    print(f"✅ Frames extracted successfully to {frames_dir}")
except subprocess.CalledProcessError as e:
    print(f"❌ Error extracting frames: {e}")
