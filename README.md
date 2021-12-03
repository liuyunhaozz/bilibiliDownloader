# bilibiliDownloader
> 利用bilibili API批量下载视频和音频并合成



## 0 目的

最近突然想起了小时候经常玩的摩尔庄园，其中的很多bgm现在听起来仿佛回到了过去那段快乐的时光，在很多地方都没有找到完整的资源，最后在b站找到了，但是在网上没有找到批量下载b站音频和视频的办法，于是萌生了利用API获取的想法。

## 1. 主要功能

输入视频BV号，批量下载B站视频中的资源，通过在终端中输入不同的参数选择 `仅下载音频 | 仅下载视频 | 下载音频和视频并合成为视频`

## 2. Python版本与依赖库

Python 3.8

requests, urllib, time, argparse

## 3. 使用方法

1. `clone` 本项目
2. 根据需要选择不同的 `flag ` 运行

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

3. 若使用 `all` flag 运行，则需先下载依赖 [ffmpeg](https://www.ffmpeg.org/download.html) 并将其加入环境变量

## 4. Demo

```shell
# 下载 BV 号为 BV1eq4y1K7QS 的视频和音频，合成后放入 demo 文件夹中
$ python main.py all --bvid BV1eq4y1K7QS --save demo
```



```shell
# 下载 BV 号为 BV1Zs411X7ik 视频列表的全部音频，放入 demo 文件夹中
$ python main.py audio --bvid BV1Zs411X7ik --save demo --list
```

## 5. 声明

请尊重原视频的作者的版权，禁止用于任何商业用途！

本项目参考了 [bilibiliAudioDownloader]( https://github.com/nuster1128/bilibiliAudioDownloader) ，感谢作者!

## 6. 准备加入下载某一个up主页所有视频功能tag

