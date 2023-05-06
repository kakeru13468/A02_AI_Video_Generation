import sys
from moviepy.editor import *


def merge_video_audio(video_input, audio_input, output_file):
    #找需要合併之檔案位置
    video = VideoFileClip(video_input)
    audio = AudioFileClip(audio_input)
    audio.write_audiofile('./voice/audio.mp3') 
    
    final_video = video.set_audio(audio)

    #libx264是一種影像編碼格式，aac是一種音訊編碼格式
    final_video.write_videofile(output_file, codec='libx264', audio_codec='aac')


if __name__ == '__main__':
    #sys.argv從本身檔案名開始看檢查參數數量
    if len(sys.argv) != 4:
        print('使用方法: python video_audio_merge.py <影像檔案> <聲音檔案> <輸出檔案>')
        sys.exit(1)

    video_input = sys.argv[1]
    audio_input = sys.argv[2]
    output_file = sys.argv[3]

    merge_video_audio(video_input, audio_input, output_file)