import yt_dlp


def download_single_video(url, save_path):
    try:
        ydl_opts = {
            'outtmpl': save_path + '/%(title)s.%(ext)s',
            'restrictfilenames': True,
            'merge_output_format': 'mp4',
            'verbose': True
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f'Download completed! Video saved in {save_path}')

    except Exception as e:
        print(f"An error occurred: {e}")
    #---------#


def download_video_as_audio(url, save_path):

    try:
        print("Accessing YouTube URL...")
        # Create a yt-dlp options dictionary
        ydl_opts = {
            'outtmpl': save_path + '/%(title)s.%(ext)s',
            'format': 'bestaudio/best',  # Select the best audio format
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',  # Convert to MP3
                'preferredcodec': 'mp3',
                'preferredquality': '192'
            }]
        }
        # Create a yt-dlp object
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Download the audio
            ydl.download([url])           
        print("Download and conversion complete!")

    except Exception as e:
        print(f"An error occurred: {e}+Audio")
        
    #---------#
def download_playlist(url, save_path):
    try:
    # Create a yt-dlp options dictionary
        ydl_opts = {
            'outtmpl': save_path + '/%(title)s.%(ext)s',
            'restrictfilenames': True,
            'merge_output_format': 'mp4',
            'verbose': True
        }
        # Create a yt-dlp object
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Extract the playlist info
            info = ydl.extract_info(url, download=False)
            # Check if the URL is a playlist
            if 'entries' in info:
                # Download each video in the playlist
                for entry in info['entries']:
                    ydl.download([entry['webpage_url']])
            else:
                # Download the single video
                ydl.download([url])

        print("All videos downloaded in MP4 format!")

    except Exception as e:
        print(f"An error occurred: {e}+play")


def download_playlist_as_audio(url, save_path):
    try:
        print("Accessing YouTube URL...")
        
        # Create a yt-dlp options dictionary
        ydl_opts = {
            'outtmpl': save_path + '/%(title)s.%(ext)s',
            'format': 'bestaudio/best',  # Select the best audio format
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',  # Convert to MP3
                'preferredcodec': 'mp3',
                'preferredquality': '192'
            }]
        }
        
        # Create a yt-dlp object
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Extract the playlist info
            info = ydl.extract_info(url, download=False)
            # Check if the URL is a playlist
            if 'entries' in info:
                # Download each video in the playlist
                for entry in info['entries']:
                    ydl.download([entry['webpage_url']])
            else:
                # Download the single video
                ydl.download([url])
        
        print("Download and conversion complete!")
        
    except Exception as e:
        print(f"An error occurred: {e}+play Audio")
        
    #---------#


##Example

xy='https://www.youtube.com/watch?v=NFxqAGCsSkU'#'https://www.youtube.com/playlist?list=PLH-do-y953IiystRnbK49ot5y0lfBYxSd'
xy2='C:/Users/visha/OneDrive/Documents/GitHub/video-downloader/text/play'

if __name__=="__main__":
    download_single_video(xy,xy2)
