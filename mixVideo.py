from moviepy.editor import *

def merge_video_audio(video_input, audio_input, output_file, loop=False):
    #找需要合併之檔案位置
    video = VideoFileClip(video_input)
    audio = AudioFileClip(audio_input)

    if loop:
        video = video.loop(duration=audio.duration)

    final_video = video.set_audio(audio)

    #libx264是一種影像編碼格式，aac是一種音訊編碼格式
    final_video.write_videofile(output_file, codec='libx264', audio_codec='aac')
