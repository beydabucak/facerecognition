#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 01:47:31 2022

@author: macbookair
"""
""" PLEASE BE AWARE
You should upload and train-test your own photos with file paths. 
Otherwise It will cause an error.
"""

import face_recognition as fr
image1=fr.load_image_file("/Users/macbookair/Desktop/kurslar/face recognition/resimler/38.jpg")
image2=fr.load_image_file("/Users/macbookair/Desktop/kurslar/face recognition/resimler/e.jpeg")
image3=fr.load_image_file("/Users/macbookair/Desktop/kurslar/face recognition/resimler/k.jpeg")

img1=fr.face_encodings(image1)[0]
img2=fr.face_encodings(image2)[0]
img3=fr.face_encodings(image3)[0]

b=[img1,img2,img3]

image=fr.load_image_file("/Users/macbookair/Desktop/kurslar/face recognition/resimler/ab.jpeg")
img=fr.face_encodings(image)[0]

"""faceloc=fr.face_locations(image,number_of_times_to_upsample=2)
ALLOWS US TO DOUBLE THE SIZE OF THE PHOTO AND GET A MORE PRECISE RESULT BC OF LOW RESOLUTION
"""


for i in img:
    a = fr.compare_faces(b,img)
    name=""
    if a[0]:
        name="beyda"
    elif a[1]:
        name="elif"
    elif a[2]:
        name="kemal"
    else:
        name="we don't know who"
print("{}'s in the photo.".format(name))
