import yt_dlp
import os
import threading

download_folder = "downloads"
downloads = []

if not os.path.exists(download_folder):
    os.makedirs(download_folder)


def progress_hook(d):
    if d['status'] == 'downloading':
        percent = d.get('_percent_str', '0%')
        speed = d.get('_speed_str', '0')
        eta = d.get('_eta_str', '0')

        print(f"Downloading: {percent} | Speed: {speed} | ETA: {eta}")

    if d['status'] == 'finished':
        print("Download completed\n")


def download_video(url, quality):
    ydl_opts = {
        'outtmpl': f'{download_folder}/%(title)s.%(ext)s',
        'progress_hooks': [progress_hook],
    }

    if quality == "best":
        ydl_opts['format'] = "bestvideo+bestaudio/best"
    else:
        ydl_opts['format'] = f"bestvideo[height<={quality}]+bestaudio/best"

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def download_playlist(url, quality, limit=None):
    ydl_opts = {
        'outtmpl': f'{download_folder}/%(playlist_title)s/%(title)s.%(ext)s',
        'progress_hooks': [progress_hook],
        'ignoreerrors': True,
    }

    if quality == "best":
        ydl_opts['format'] = "bestvideo+bestaudio/best"
    else:
        ydl_opts['format'] = f"bestvideo[height<={quality}]+bestaudio/best"

    if limit:
        ydl_opts['playlistend'] = limit

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def change_download_folder():
    global download_folder
    folder = input("Enter new download folder path: ")
    download_folder = folder
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
    print("Download folder changed\n")


def start_download():
    url = input("Paste YouTube video or playlist URL: ")

    quality = input("Select quality (144/360/720/1080/best): ")

    mode = input("1 = Single Video | 2 = Playlist : ")

    if mode == "1":
        thread = threading.Thread(target=download_video, args=(url, quality))
        thread.start()
        downloads.append(thread)

    elif mode == "2":
        limit = input("How many videos from playlist? (Enter for all): ")

        limit = int(limit) if limit else None

        thread = threading.Thread(target=download_playlist, args=(url, quality, limit))
        thread.start()
        downloads.append(thread)


def show_downloads():
    print("\nActive Downloads:", len(downloads))
    for i, d in enumerate(downloads):
        print(f"Download {i+1} running: {d.is_alive()}")
    print()


def main():
    while True:
        print("\n===== YOUTUBE DOWNLOAD MANAGER =====")
        print("1 Download Video / Playlist")
        print("2 Change Download Folder")
        print("3 Show Active Downloads")
        print("4 Exit")

        choice = input("Select option: ")

        if choice == "1":
            start_download()

        elif choice == "2":
            change_download_folder()

        elif choice == "3":
            show_downloads()

        elif choice == "4":
            break


if __name__ == "__main__":
    main()
