import PIL.Image as pilimage
import face_recognition as fr
import PIL.ImageDraw as pildraw

a=fr.load_image_file("YOUR FILE PATH HERE")
b=pilimage.fromarray(a)

lmimg=fr.face_landmarks(a)

numberofmarks=len(lmimg)

d=pildraw.Draw(b,'RGBA')

for i in lmimg:
    d.line(i["left_eyebrow"],fill=(128,0,128,100),width=10)
    d.line(i["right_eyebrow"],fill=(100,0,100,100),width=10)

    d.polygon(i["bottom_lip"],fill="red")
    d.polygon(i["top_lip"],fill="red")
    
    d.line(i["chin"],fill="blue",width=30)
    
    d.polygon(i["left_eye"],fill="black")
    d.polygon(i["right_eye"],fill="black")

    
b.show()
