import PIL.Image as pilimg
import PIL.ImageDraw as pildraw
import face_recognition as fr

a=input("file address:")

im = pilimg.open(a)
im=fr.load_image_file(a)


locations=fr.face_locations(im)


landmark_list=fr.face_landmarks(im)



number_of_faces=len(locations)
print("number of faces in the current photo displaying: {}".format(number_of_faces))

#numberoffaces=len(landmark_list)



img = pilimg.fromarray(im)



 
for locs in locations:
    top, right, bottom, left = locs
    print("top:{} \n right:{} \n bottom:{}\n left:{}\n".format(top,right,bottom,left))
    drw=pildraw.Draw(img)
    drw.rectangle([top,right,bottom,left], outline="red")
 

for i in landmark_list:
    for name, point in i.items():
        print(f"{name}'s points:{point}")
        drawing=pildraw.Draw(img)
        drawing.line(point,fill="red",width=2)
    
img.show()

