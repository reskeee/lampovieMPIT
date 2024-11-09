from moviepy.editor import *
import os

def MP4ToMP3(mp4, mp3):
    project_dir = os.path.dirname(__file__)
    FILETOCONVERT = AudioFileClip(f"{project_dir}/{mp4}")
    FILETOCONVERT.write_audiofile(f"{project_dir}/{mp3}")
    FILETOCONVERT.close()                 

if __name__ == "__main__":
    MP4ToMP3("video/video_2024-11-02_13-54-23.mp4", "audio/convert.mp3")
    # print(os.path.dirname(__file__))
