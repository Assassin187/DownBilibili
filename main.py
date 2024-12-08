import requests
import re
import json
import os
import argparse

from time import sleep
from merge import merge

class BilibiliVideo:
    def __init__(self, bvid, cookie):
        self.url = f"https://www.bilibili.com/video/{bvid}/"
        self.cookie = cookie
        self.headers = {
            "Referer": self.url,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            "Cookie": self.cookie
        }
    
    def get_html(self):
        response = requests.get(url=self.url, headers=self.headers)
        html = response.text
        return html
    
    def get_url(self, html):
        title = re.findall('title="(.*?)"', html)[0]
        video_info = re.findall('window.__playinfo__=(.*?)</script>', html)[0]
        info_json = json.loads(video_info)
    
        video_url = info_json['data']['dash']['video'][0]['baseUrl']
        audio_url = info_json['data']['dash']['audio'][0]['baseUrl']
        return title, video_url, audio_url
    
    def download_file(self, url, file_path, chunk_size=1024*1024, retries=5):
        for attempt in range(retries):
            try:
                response = requests.get(url, headers=self.headers, stream=True)
                total_size = int(response.headers.get('content-length', 0))
                print(f"文件大小:{round(total_size/1024/1024, 4)}MB")
                downloaded = 0

                with open(file_path, 'wb') as f:
                    for chunk in response.iter_content(chunk_size):
                        downloaded += len(chunk)
                        f.write(chunk)
                        if total_size:
                            progress = int((downloaded / total_size) * 100)
                            print(f'下载进度: {progress}%')
                break
            except requests.exceptions.ChunkedEncodingError as e:
                print(e)
                print(f"下载失败，重试 {attempt + 1}/{retries} 次...")
                sleep(1)
                if attempt == retries - 1:
                    raise e
    
    def download_video(self):
        html = self.get_html()
        title, video_url, audio_url = self.get_url(html)
        video_path = f"video\\{title}_v.m4s"
        audio_path = f"video\\{title}_a.m4s"
        video = f"video\\{title}.mp4"
        print("开始下载视频文件")
        self.download_file(video_url, video_path)
        print("开始下载音频文件")
        self.download_file(audio_url, audio_path)

        merge(video_path, audio_path, video)

        print("下载完成")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="下载B站视频")
    parser.add_argument('bvid', type=str, help='要下载视频的BV号，如BV18qBZY7EWo')
    parser.add_argument('cookie', type=str, help='登录B站后生成的网页cookie')
    args = parser.parse_args()

    os.mkdir("video")
    bili = BilibiliVideo(args.bvid, args.cookie)
    bili.download_video()