import streamlit as st
import os
from backend import *

# Function to get the default downloads folder
def get_downloads_folder():
    if os.name == 'nt':  # Windows
        return os.path.join(os.getenv('USERPROFILE'), 'Downloads')
    else:  # MacOS/Linux
        return os.path.join(os.path.expanduser('~'), 'Downloads')
default_save_path = get_downloads_folder()

st.set_page_config(page_title="Youtube Video Downloader",page_icon='robot_face')

st.title('Youtube Video Downloader')

url=st.text_input(label="Youtube Url",placeholder='Paste:www.youtube.com')

download_type = st.selectbox(
    label="Download Type",
    options=["Download Video", "Download Playlist", "Download Video as Audio", "Download Playlist as MP3"]
)

save_path = st.text_input("Enter the path to save the downloaded file:", value=default_save_path)


if st.button(label="Download"):
    st.write(url)
    st.write(save_path)
    st.write(download_type)
    try:
        if download_type == 'Download Video':
            download_single_video(url, save_path)
        elif download_type == 'Download Playlist':
            download_playlist(url, save_path)
        elif download_type == 'Download Video as Audio':
            download_video_as_audio(url, save_path)
        elif download_type == 'Download Playlist as MP3':
            download_playlist_as_audio(url, save_path)

        st.write('Download started! Check your downloads folder.')
    except Exception as e:
        st.write(f'Error: {str(e)}')
        print("Error details:", str(e))