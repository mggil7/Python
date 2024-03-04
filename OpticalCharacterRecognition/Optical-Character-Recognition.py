# não rodou no PC, mas funciona no Google Colab - 
# notebook jupyter - Optical Character Recognition with EasyOCR.ipynb
# testado com manômetros

import cv2 
import matplotlib.pyplot as plt 
import easyocr 


#path = "Open-CV/Optical character recognition/sign.jpg"
path="11.jpg"
img = cv2.imread(path)



# create detector
reader = easyocr.Reader(['en'], gpu=False)

# detect text on the image
myText = reader.readtext(img)
print(myText)

minThresholdForDisplay = 0.25

for numerator , detectedText in enumerate(myText):
    print(detectedText)

    bbox , text , score = detectedText
    pos1 = bbox[0]
    pos2 = bbox[2]

    if score > minThresholdForDisplay :
        #cv2.rectangle(img,pos1,pos2, (0,0,0), 5)
        #cv2.putText(img,text,pos1,cv2.FONT_HERSHEY_PLAIN, 5, (255,0,0), 5)
        cv2.rectangle(img,(int(pos1[0]), int(pos1[1])),(int(pos2[0]),int(pos2[1])), (0,0,0),2)
        cv2.putText(img,text,(int(pos1[0]), int(pos1[1])),cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0), 2)

#cv2.imwrite("c://home/earth/App/Python/OpticalCharacterRecognition/temp/opticalRecog.png",img)
cv2.imwrite("opticalRecog.png",img)
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.show()