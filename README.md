# 使用教程

## 简介

此项目可以用于在B站的PC端一键式下载一个完整MP4格式的视频文件

## 硬件环境

项目基于Window11系统开发，使用python版本3.12.3

## 前置要求

#### 安装ffmpeg

使用该项目必须要先在电脑中安装ffmpeg，请确保ffmpeg的环境变量配置正确。具体操作参考教程[【Python】ffmpeg的安装配置和python中使用ffmpy（保姆级图文）-CSDN博客](https://blog.csdn.net/u011027547/article/details/122490254)

#### 安装相关依赖

``````bash
pip install requests
``````

## 开始使用

#### 第一步

打开B站官网，先登录个人的B站账号，然后回到B站首页：[哔哩哔哩 (゜-゜)つロ 干杯~-bilibili](https://www.bilibili.com/)

#### 第二步

来到首页后，按键盘上的F12键打开开发者界面，然后点进network(网络)

![image-20241208172212009](https://github.com/user-attachments/assets/b977c31b-5de0-423a-a7a7-6c55e38b0493)

此时按键盘上的F5键刷新首页，获取网页请求信息，然后点击第一个请求

![image-20241208172434852](https://github.com/user-attachments/assets/35120707-98d4-46be-90db-ae5e65720c0b)

然后复制cookie中的所有内容，将其记下来，如红框所示

![image-20241208172620900](https://github.com/user-attachments/assets/45fef931-657d-41f7-a547-c457c427421e)

#### 第三步

点开想要下载的视频页面，复制网址中的BV号，并将其记下

![image-20241208172818869](https://github.com/user-attachments/assets/31a19988-d647-4bba-90a2-5269729ea4f6)

#### 第四步

进入项目的根目录，将上述的BV号和cookie作为参数执行命令

``````bash
python main.py BV_id your_cookie
``````

#### 第五步

视频文件会下载到根目录中video文件夹里
