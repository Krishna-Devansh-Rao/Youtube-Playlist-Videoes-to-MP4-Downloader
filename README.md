# YouTube Download Manager (Python + yt-dlp)

A simple **Python-based YouTube Video & Playlist Downloader** built using **yt-dlp**.
This tool allows you to download **single videos or entire playlists**, select video quality, monitor download progress, and manage multiple downloads.

---

# Features

• Download **Single YouTube Videos**
• Download **Entire Playlists**
• Choose **Video Quality** (144p, 360p, 720p, 1080p, Best)
• **Download Progress Tracking**

* Percentage
* Speed
* Estimated Time Remaining (ETA)

• **Multiple Downloads at the Same Time** (Threading)

• **Playlist Download Limit**

* Download full playlist
* Download first N videos

• **Custom Download Folder**

• **Download Manager**

* Track active downloads
* View running downloads

---

# Requirements

Make sure you have the following installed:

* Python 3.8+
* pip (Python package manager)

---

# Installation

### 1 Install yt-dlp

Open terminal or command prompt:

pip install yt-dlp

---

### 2 Clone or Download the Project

Download the project files or clone the repository.

---

### 3 Run the Program

Navigate to the project folder and run:

python downloader.py

---

# How to Use

After running the script you will see the menu:

===== YOUTUBE DOWNLOAD MANAGER =====

1 Download Video / Playlist
2 Change Download Folder
3 Show Active Downloads
4 Exit

---

## Download Video

1. Choose option **1**
2. Paste the YouTube **Video URL**
3. Select **Quality**
4. Choose **Single Video**

---

## Download Playlist

1. Choose option **1**
2. Paste the **Playlist URL**
3. Select quality
4. Choose **Playlist**
5. Enter number of videos to download or leave empty for full playlist

---

# Download Progress

During download you will see information like:

Downloading: 45% | Speed: 2.3MB/s | ETA: 00:15

---

# Change Download Folder

Select option **2** and enter a new folder path.

Example:

Enter new download folder path: D:/YouTubeVideos

---

# Project Structure

project/

downloader.py
downloads/ (videos are saved here)
README.md

---

# Example Video URLs

Single Video

https://www.youtube.com/watch?v=VIDEO_ID

Playlist

https://www.youtube.com/playlist?list=PLAYLIST_ID

---

# Future Improvements

Possible upgrades for this project:

• GUI Downloader (Tkinter or PyQt)
• Web Dashboard Downloader (Flask + HTML)
• MP3 Audio Downloader
• Download Pause / Resume
• Video Metadata Preview
• IDM-style Download Manager

---

# License

This project is for **educational purposes only**.

Please respect **YouTube Terms of Service** and only download content that you have permission to download.

---

# Author

Created with Python and yt-dlp.
