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
 A(Start) --> B[/User input/]
 B --> C[Call GPT API]
 C --> D[Generate video from script]
 C --> E[Call Azure text-to-speech API]
 D  & E --> F[Combine video and audio with FFmpeg]
 F --> G(Display video on web UI)
```

## Gantt Chart

<!-- FIXME -->
```mermaid
gantt
    todayMarker
    dateFormat  YYYY-MM-DD

    section 專題進度
    找尋專題老師       :  2022-12-07, 6d
    蒐集相關文獻      : 2022-12-20, 70d
    確認專題方向      : 2023-02-28, 7d
    串聯必要 API 測試 : 2023-03-07, 7d
    尋找適合模型         : 2023-03-14, 18d
    整合系統             : 2023-04-01, 152d
    測試與展現初步成果  : active, 2023-04-15, 30d
    專題（一）期末報告       : crit, milestone, 2023-06-08,  8min
    製作網頁         : 2023-06-08, 42d
    將系統整合至網頁    : 2023-07-20, 42d
    測試及排除問題    : 2023-08-31, 28d
    公開測試         : 2023-09-21, 28d

    section 報告書
    檢查格式             : 2023-05-12, 1w
    第二章初稿          : 2023-02-21, 28d
    第二章定稿          : 2023-03-21, 1w
    第三章初稿          : 2023-03-28, 28d
    第三章定稿          : 2023-04-25, 1w
    第四、五章初稿          : active, 2023-05-02, 1w
    專題企劃書定稿          : 2023-05-09, 5d
    撰寫最終報告書          : 2023-10-19, 28d
    完成專題報告書          : 2023-11-16, 45d
    收件截止日期          : milestone, 2023-05-30, 1d
```

## Text and voice

### AzureOpenaiFuntion.py

This program will modify the user's text and generate speech. It will generate two files, `text.txt` and `voice.wav`, to store the modified text and the corresponding speech, respectively.

#### add your api key to environment variable

```shell
export OPENAI_API_KEY=<YOUR_OPENAI_API_KEY>
```

```shell
export AZURE_SPEECH_KEY=<YOUR_AZURE_SPEECH_KEY>
```

Windows:

```shell
setx OPENAI_API_KEY "REPLACE_WITH_YOUR_KEY_VALUE_HERE" 
```

```shell
setx OPENAI_API_BASE "REPLACE_WITH_YOUR_ENDPOINT_HERE" 
```

```shell
setx AZURE_SPEECH_KEY "YOUR_AZURE_SPEECH_KEY"
```

Notes:

If there is an error with ``` AZURE_SPEECH_REGION ```, please change it to ``` eastasia ```.

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
