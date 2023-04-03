# AI Video Capstone Project

## TODO

- [ ] 實驗 LLaMA 模型
- [x]  報告書第二章初稿
- [x] 找如何結合聲音與影片
- [ ] 找到適合的影片生成模型
- [ ] A 計畫：生成真的影片
- [ ] B 計畫：用多張圖片串成幻燈片
  
## Text and voice

### AzureOpenai.py

this will write text to `text.txt` and voice to `voice.wav`

type `bye` to save text and voice

#### add your api key to environment variable

```shell
export OPENAI_API_KEY=<YOUR_OPENAI_API_KEY>
```

```shell
export AZURE_SPEECH_KEY=<YOUR_AZURE_SPEECH_KEY>
```

## Video Audio Mixing

### MixVideo.py ###

You need to pip `FFmpeg Python` and `Moviepy` first.

```shell
pip install python-ffmpeg 
```

```shell
pip install moviepy
```

And confirm the path for your `VOICE` and `VIDEO`

The video will be saved in your root directory, You can also change the path according to your own needs.
