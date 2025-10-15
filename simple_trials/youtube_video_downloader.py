from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        highest_res_stream = yt.streams.filter(progressive=True, file_extension="mp4").get_highest_resolution()

        highest_res_stream.download(output_path=save_path)
       
        print("Video downloaded successfully!")

    except Exception as e:
        print(e)

url="https://www.youtube.com/watch?v=CJkDKIsvROM&pp=0gcJCfsJAYcqIYzv"
save_path = "C:/Users/lead/Desktop/python-projects"

download_video(url, save_path)    