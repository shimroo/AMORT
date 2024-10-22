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
