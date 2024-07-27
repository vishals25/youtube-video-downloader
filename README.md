# YouTube Downloader App

## Overview

The YouTube Downloader App is a graphical user interface (GUI) application built using Kivy that allows users to download videos, playlists, and audio from YouTube. The application features a modern design with rounded corners, custom styles, and an easy-to-use interface. The app also leverages tkinter for selecting download directories.

## Features

- Download individual YouTube videos.
- Download entire YouTube playlists.
- Download videos as audio (MP3).
- Download playlists as MP3.
- Custom styled interface with rounded corners and modern design.
- Simple file path selection using a graphical file dialog.

## Requirements

- Python 3.x
- Kivy
- tkinter

## Usage

1. Run the application:

    ```sh
    python main.py
    ```

2. Using the Application:

    - **Select Download Type**: Choose between "Download Video", "Download Playlist", "Download Video as Audio", and "Download Playlist as MP3" from the spinner.
    - **Enter YouTube URL**: Input the URL of the video or playlist you wish to download.
    - **Select Save Path**: Click the "Browse" button to choose a directory where the downloads will be saved.
    - **Start Download**: Click the "Download" button to begin downloading. The message label will update with the download status.
![alt text](<image.png>)
