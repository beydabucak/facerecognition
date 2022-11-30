import PIL.Image as pilimage
import PIL.ImageDraw as pildraw
import face_recognition as fr

a=input("file path:")
im=pilimage.open(a)
im=fr.load_image_file(a)


landmark_list=fr.face_landmarks(im)
numberoffaces=len(landmark_list)
print("number of faces: {}".format(numberoffaces))


pilim=pilimage.fromarray(im)
draw=pildraw.Draw(pilim)

for i in landmark_list:

    for name, point in i.items():
        
        print(f"{name}'s points:{point}")
        
        draw.line(point,fill="red",width=2)
        
pilim.show()
