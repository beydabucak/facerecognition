#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 01:47:31 2022

@author: macbookair
"""


import face_recognition as fr
image1=fr.load_image_file("FILE PATH HERE")
image2=fr.load_image_file("FILE PATH HERE")
image3=fr.load_image_file("FILE PATH HERE")

img1=fr.face_encodings(image1)[0]
img2=fr.face_encodings(image2)[0]
img3=fr.face_encodings(image3)[0]

b=[img1,img2,img3]

image=fr.load_image_file("FILE PATH HERE")
img=fr.face_encodings(image)[0]

"""faceloc=fr.face_locations(image,number_of_times_to_upsample=2)
ALLOWS US TO DOUBLE THE SIZE OF THE PHOTO AND GET A MORE PRECISE RESULT BC OF LOW RESOLUTION
"""


for i in img:
    a = fr.compare_faces(b,img)
    name=""
    if a[0]:
        name="NAME HERE"
    elif a[1]:
        name="NAME HERE"
    elif a[2]:
        name="NAME HERE"
    else:
        name="we don't know who"
print("{}'s in the photo.".format(name))
