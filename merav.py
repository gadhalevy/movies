import os

from moviepy.editor import *
import cv2,string
import numpy as np,random
from PIL import ImageFont, ImageDraw, Image
audio=AudioFileClip("merav.mp3")
def write_hebrew(t):
    # Create black mask using Numpy and convert from BGR (OpenCV) to RGB (PIL)
    # image = cv2.imread('1.png') # If you were using an actual image
    status=False
    color=random.choice(['red','blue','green','purple','brown','orange','yellow','white'])
    image = np.zeros((100,800, 3), dtype=np.uint8)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(image)

    # Draw non-ascii text onto image
    font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSans.ttf", 60)
    draw = ImageDraw.Draw(pil_image)
    draw.text((0, 0), t, font=font,fill=color,align="center")
    pil_image.save('tmp.jpg')
    status=True
    yield status
    # image = np.asarray(pil_image)
    #
    # image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    # cv2.imshow('image', image)
    # cv2.waitKey()

    # Convert back to Numpy array and switch back from RGB to BGR
    # image = np.asarray(pil_image)
    # image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

# clips=[]
def make_video(txt,zman):
    # blank_image = np.zeros((600, 800, 3), np.uint8)
    # img=cv2.putText(blank_image,t[::-1],(100,400),cv2.FONT_HERSHEY_SIMPLEX,5,(0,0,255),3)
    files=os.listdir('merav')
    for status in write_hebrew(txt):
        if status:
            img=cv2.imread('merav/'+random.choice(files))
            img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            img=cv2.resize(img,(800,600))
            clip=ImageClip(img,duration=float(zman))
            text_clip=ImageClip('tmp.jpg',duration=float(zman))
            # clip2 = ImageClip(img, duration=5)
            # txt_clip = ImageClip(img,duration=5)
            # txt_clip = txt_clip.set_pos('center').set_duration(5)
            clip=clip.resize(0.30)
            video = clips_array([[clip], [text_clip]]).resize(height=600)
            return  video
        # clips.append(video)
with open('/home/cimlab/Downloads/meravi.txt',encoding='utf-8') as f, open ('times.txt') as k:
    txt=f.read()
    times=k.read().split('\n')
clips=[]
for i,t in enumerate (txt.split('.')):
    print(t)
    try:
        video=make_video(t,times[i])
        clips.append(video)
    except:
        continue
tClips=concatenate_videoclips(clips)
part1=tClips.subclip(0,60*1.55)
part1=part1.set_audio(audio)
part2=tClips.subclip(60*1.55)
part2=part2.set_audio(audio)
final=concatenate_videoclips([part1,part2])
final.write_videofile("merav.mp4",fps=5)

