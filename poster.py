import cv2
img = cv2.imread("solar-system.jpg")
crop = img[120:360,400:500]


text="SUN"
cv2.putText(img,text,
(40,110),
fontFace=cv2.FONT_HERSHEY_DUPLEX,
fontScale=2,
color=(123,255,199))

text="MERCURY"
cv2.putText(img,text,
(90,250),
fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
fontScale=0.6,
color=(123,255,199))


text="VENUS"
cv2.putText(img,text,
(160,190),
fontFace=cv2.FONT_HERSHEY_DUPLEX,
fontScale=0.9,
color=(123,255,199))



text="EARTH"
cv2.putText(img,text,
(250,280),
fontFace=cv2.FONT_HERSHEY_DUPLEX,
fontScale=0.9,
color=(123,255,199))



text="MARS"
cv2.putText(img,text,
(350,190),
fontFace=cv2.FONT_HERSHEY_DUPLEX,
fontScale=0.9,
color=(123,255,199))




text="JUPTER"
cv2.putText(img,text,
(450,350),
fontFace=cv2.FONT_HERSHEY_DUPLEX,
fontScale=0.9,
color=(123,255,199))




text="SATURN"
cv2.putText(img,text,
(750,120),
fontFace=cv2.FONT_HERSHEY_DUPLEX,
fontScale=0.9,
color=(123,255,199))









text="URANS"
cv2.putText(img,text,
(950,350),
fontFace=cv2.FONT_HERSHEY_DUPLEX,
fontScale=0.9,
color=(123,255,199))




text="NEPTUNE"
cv2.putText(img,text,
(1100,120),
fontFace=cv2.FONT_HERSHEY_DUPLEX,
fontScale=0.9,
color=(123,255,199))


















cv2.imshow("output",img)
cv2.waitKey(0)