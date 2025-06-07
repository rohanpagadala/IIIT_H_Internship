import subprocess
import os

input_folder = "segmented_frames"
output_video = "output_segmented_video.mp4"

if not os.path.exists(input_folder):
    print(f"❌ Folder '{input_folder}' does not exist")
    exit(1)

ffmpeg_cmd = [
    "ffmpeg",
    "-y",
    "-framerate", "1",
    "-i", os.path.join(input_folder, "frame_%04d.jpg"),
    "-c:v", "libx264",
    "-pix_fmt", "yuv420p",
    output_video
]

print("▶️ Creating video from segmented frames...")
try:
    subprocess.run(ffmpeg_cmd, check=True)
    print(f"✅ Video saved as '{output_video}'")
except subprocess.CalledProcessError as e:
    print("❌ Error creating video:", e)
