# from pytube import Playlist
# from moviepy.editor import VideoFileClip
# import os

# # Function to download and convert a single video to mp3
# def download_and_convert_to_mp3(video_url, output_folder):
#     try:
#         yt = YouTube(video_url)
#         video = yt.streams.filter(only_audio=True).first()
#         out_file = video.download(output_path=output_folder)

#         # Convert the downloaded file to mp3 using moviepy
#         base, ext = os.path.splitext(out_file)
#         mp3_file = base + ".mp3"

#         # Convert to MP3 using moviepy
#         video_clip = VideoFileClip(out_file)
#         audio_clip = video_clip.audio
#         audio_clip.write_audiofile(mp3_file)
        
#         # Clean up and remove the original mp4 file
#         video_clip.close()
#         audio_clip.close()
#         os.remove(out_file)

#         print(f"Downloaded and converted: {yt.title}")
#     except Exception as e:
#         print(f"Error downloading {video_url}: {e}")

# # Main function to download playlist
# def download_playlist(playlist_url, output_folder):
#     playlist = Playlist(playlist_url)
    
#     print(f"Downloading playlist: {playlist.title}")
    
#     # Create output directory if it doesn't exist
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)
    
#     # Download each video in the playlist and convert it to mp3
#     for video_url in playlist.video_urls:
#         download_and_convert_to_mp3(video_url, output_folder)

# # Example usage
# if __name__ == "__main__":
#     playlist_url = input("Enter YouTube playlist URL: ")
#     output_folder = input("Enter the folder where you want to save MP3s: ")
#     download_playlist(playlist_url, output_folder)


import yt_dlp
import os

# Function to download the playlist as MP3
def download_playlist_as_mp3(playlist_url, output_folder):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # yt-dlp options for downloading MP3
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': False,
        'noplaylist': False,  # This ensures the entire playlist is downloaded
    }

    # Download the playlist
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

# Example usage
if __name__ == "__main__":
    playlist_url = input("Enter YouTube playlist URL: ")
    output_folder = input("Enter the folder where you want to save MP3s: ")
    download_playlist_as_mp3(playlist_url, output_folder)
