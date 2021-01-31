import cv2
import pytesseract
from . import detect
import os
from pathlib import Path
# pathImage = "2.jpg"
#pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

# BASE_DIR = Path(__file__).resolve().parent.parent
MEDIA_ROOT  = 'media/'

def detect_text(img,img_info):
    im=img.copy()
    total_boxes = len(img_info['text'])    #length of total no of blocks detected
    for sequence_number in range(total_boxes):                                        #Looping through blocks
        if int(img_info['conf'][sequence_number])>30:                               #if confidence of box being text if greater than 30 (30-40 is optimal limit)
            (x, y, w, h) = (img_info['left'][sequence_number], img_info['top'][sequence_number], img_info['width'][sequence_number],  img_info['height'][sequence_number])  #get the coordinates of confident blocks
            im = cv2.rectangle(im, (x, y), (x + w, y + h), (0,255, 0), 1)     #Drawing a rectangle box over confident word
    cv2.imshow('identified text',im)                                         #Showing final image
    cv2.waitKey(0)                                                                   #Press any key to exit
    cv2.destroyAllWindows()

def getInfo(img):
    custom_config = r'--oem 3 --psm 6'                                              #Addind oem and psm to custom config
    img_info=pytesseract.image_to_data(img,output_type=pytesseract.Output.DICT,config=custom_config,lang='eng')  #Getting image data from tesseract
    return img_info

def parse(data):
    '''Function to parse data from detected text'''
    parsed=[]
    last_word=''
    for word in data:
        if word!='':
            parsed.append(word)
            last_word=word
        if last_word!='' and word=='':
            parsed.append('\n')
    return " ".join(parsed)

def ocr(img):
    img,pts=detect.cropContour(img)
    # cimg=img.copy()
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img=cv2.threshold(img, 0, 225, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    img_info=getInfo(img)
    #detect_text(cimg,img_info)
    data=parse(img_info['text'])
    return data


# if __name__ == '__main__':
#     print(ocr(path))