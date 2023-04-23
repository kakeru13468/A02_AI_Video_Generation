# AI Video Capstone Project(WIP)

## TODO

- [ ] 報告書第三章
- [ ] 完成系統架構圖
- [ ] 完成系統流程圖
- [ ] 完成甘特圖
- [ ] 測試 frame interpolation
- [ ] 將 ChatGPT 與 Model 結合自動化
- [ ] 整合系統

## Architecture

```mermaid
flowchart TD
    A[User Interface] -->|text| B
    B[Server] -->|video with narration| A
    B --->|text| E[video generator]
    E -->|video| B
    B --->|text prompt| C[GPT]
    C -->|video script,\n text narration| B
    B --->|text| D[Azure]
    D -->|generated voice| B
```

## Flowchart

```mermaid
flowchart TD
 A(Start) --> B[User input]
 B --> C[GPT]
 C --> D[Video generator]
 C --> E[Azure]
 D --> F[Video]
 E --> F
 F --> G(End)
```

## Gantt Chart

<!-- FIXME -->
```mermaid
gantt
    todayMarker
    dateFormat  YYYY-MM-DD

    section Section
    尋找適合模型         : a1, 2023-03-21, 30d
    整合系統             : active, after a1, 30d
    第一次期末報告       : crit, milestone, 2023-06-08,  8min
    第二次期末報告       : crit, milestone, 2024-01-08,  8min %%FIXME

    section 報告書
    檢查格式             : 2023-05-12, 1w
    收件截止日期          : milestone, 2023-05-30, 1d
```

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

### MixVideo.py

You need to pip `FFmpeg Python` and `Moviepy` first.

```shell
pip install python-ffmpeg 
```

```shell
pip install moviepy
```

And confirm the path for your `VOICE` and `VIDEO`

The video will be saved in your root directory, You can also change the path according to your own needs.
