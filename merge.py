import subprocess
import os

def convert_m4s_to_mp4(input_file, output_file):
    command = [
        'ffmpeg',
        '-i', input_file,
        '-c', 'copy',
        output_file
    ]
    subprocess.run(command, check=True)

def convert_m4s_to_mp3(input_file, output_file):
    command = [
        'ffmpeg',
        '-i', input_file,
        '-q:a', '0',
        '-map', 'a',
        output_file
    ]
    subprocess.run(command, check=True)

def merge_audio_video(video_file, audio_file, output_file):
    command = [
        'ffmpeg',
        '-i', video_file,
        '-i', audio_file,
        '-c:v', 'copy',
        '-c:a', 'aac',
        '-strict', 'experimental',
        output_file
    ]
    subprocess.run(command, check=True)

def clear_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"{file_path} 已清理")
    else:
        print(f"{file_path} 不存在")

def merge(video_m4s, audio_m4s, output_file):
    video_mp4 = "video\\video_tmp.mp4"
    audio_mp3 = "video\\audio_tmp.mp3"

    # 转换视频和音频
    convert_m4s_to_mp4(video_m4s, video_mp4)
    convert_m4s_to_mp3(audio_m4s, audio_mp3)

    # 合并视频和音频
    merge_audio_video(video_mp4, audio_mp3, output_file)

    print(f'合并完成，文件保存在：{output_file}')   

    clear_file(video_m4s)
    clear_file(audio_m4s)
    clear_file(video_mp4)
    clear_file(audio_mp3)