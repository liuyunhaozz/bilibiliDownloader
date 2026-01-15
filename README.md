# bilibiliDownloader
> Uses the bilibili API to batch-download videos and audio, then merge them.


## 1. Main Features

Input the video BV ID to batch download resources from Bilibili. Select options by entering different arguments in the terminal: `Download audio only | Download video only | Download both audio and video and merge them`.

## 2. Python Version & Dependencies

Python 3.8

requests, urllib, time, argparse

## 3. Usage

1. `clone` this project.
2. Run with specific `flags` based on your needs.

```shell
$ python main.py -h                                  
usage: main.py [-h] {audio,video,all} ...

positional arguments:
  {audio,video,all}  commands
    audio            Download only audio file
    video            Download only video file
    all              Download both video and audio file

optional arguments:
  -h, --help         show this help message and exit
  
$ python main.py audio -h
usage: main.py audio [-h] --bvid BVID --save SAVE [--list]

optional arguments:
  -h, --help   show this help message and exit
  --bvid BVID  Enter the 12-bit bvid number
  --save SAVE  Enter the name of your file-dir
  --list       Download a list of videos
```

3. If running with the all flag, you must first download ffmpeg and add it to your environment variables.

## 4. Demo

```shell
# Download video and audio for BV ID BV1eq4y1K7QS, merge them, and save to the 'demo' folder
$ python main.py all --bvid BV1eq4y1K7QS --save demo
```



```shell
# Download all audio from the video list with BV ID BV1Zs411X7ik and save to the 'demo' folder
$ python main.py audio --bvid BV1Zs411X7ik --save demo --list
```

## 5. Disclaimer

Please respect the copyright of the original video authors. Commercial use is strictly prohibited!

This project references [bilibiliAudioDownloader]( https://github.com/nuster1128/bilibiliAudioDownloader). Thanks to the author!

## 6. TODO
Plan to add a feature to download all videos from a specific uploader's homepage

