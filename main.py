import time
import os
import argparse
import subprocess
import shutil
from geturl import getInformation, getMutipleInformation
from download import getAudio, getVideo

# 不使用 list flag 时，也可以修改代码传入 BVList 列表来下载相互独立的几个视频
# BVList=[
#     'BV1dA411L7Kj','BV1aK4y1a7sd','BV1wf4y1k7as',
#     'BV1CK4y1W7Cc','BV12X4y1K7Ys','BV1Fz4y167Ru',
#     'BV17y4y167xu','BV1wD4y1X7fP','BV1wV41117GP'
# ]

def handle_audio(args):    
    print('Downloader Start!')

    st=time.time()

    if args.list:
        getAudio(getMutipleInformation(args.bvid), args.save)
    else:
        getAudio(getInformation([args.bvid]), args.save)

    ed=time.time()

    print('Download Finish All! Time consuming:',str(round(ed-st,2))+' seconds')


def handle_video(args):    
    print('Downloader Start!')

    st=time.time()

    if args.list:
        getVideo(getMutipleInformation(args.bvid), args.save)
    else:
        getVideo(getInformation([args.bvid]), args.save)

    ed=time.time()

    print('Download Finish All! Time consuming:',str(round(ed-st,2))+' seconds')


def handle_all(args):    
    print('Downloader Start!')
    if not os.path.exists('temp'):  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs('temp')
    if not os.path.exists(args.save):
        os.makedirs(args.save)

    st=time.time()

    if args.list:
        getAudio(getMutipleInformation(args.bvid), 'temp')
        getVideo(getMutipleInformation(args.bvid), 'temp')
    else:
        getAudio(getInformation([args.bvid]), 'temp')
        getVideo(getInformation([args.bvid]), 'temp')

    
    names = os.listdir('temp')
    for name in names:
        if name.split('.')[-1] == 'mp4':
            # subprocess.call(f'ffmpeg -i temp/{name} -i temp/{name[:-4]}.mp3 -strict -2 -f mp4 {os.path.join(args.save, name)}', shell=True)
            subprocess.call(f'ffmpeg -i temp/{name} -i temp/{name[:-4]}.mp3 -codec copy {os.path.join(args.save, name)}')
    shutil.rmtree('temp')
    ed=time.time()

    print('Download Finish All! Time consuming:',str(round(ed-st,2))+' seconds')



def main():
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(help='commands')

    audio_parser = subparsers.add_parser(name='audio', help='Download only audio file')
    audio_parser.add_argument('--bvid', required=True, help="Enter the 12-bit bvid number")
    audio_parser.add_argument('--save', required=True, help="Enter the name of your file-dir")
    audio_parser.add_argument('--list', action="store_true", help="Download a list of videos")
    audio_parser.set_defaults(func=handle_audio)	# 绑定处理函数

    video_parser = subparsers.add_parser(name='video', help='Download only video file')
    video_parser.add_argument('--bvid', required=True, help="Enter the 12-bit bvid number")
    video_parser.add_argument('--save', required=True, help="Enter the name of your file-dir")
    video_parser.add_argument('--list', action="store_true", help="Download a list of videos")
    video_parser.set_defaults(func=handle_video)	# 绑定处理函数

    all_parser = subparsers.add_parser(name='all', help='Download both video and audio file')
    all_parser.add_argument('--bvid', required=True, help="Enter the 12-bit bvid number")
    all_parser.add_argument('--save', required=True, help="Enter the name of your file-dir")
    all_parser.add_argument('--list', action="store_true", help="Download a list of videos")
    all_parser.set_defaults(func=handle_all)	# 绑定处理函数

    args = parser.parse_args()
    # 执行函数功能
    args.func(args)


if __name__ == '__main__':
    main()
