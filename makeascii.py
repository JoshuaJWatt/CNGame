import os
from PIL import Image
import cv2

CODE_LIB = r"B8&WM#YXQO{}[]()I1i!pao;:,.    "
count = len(CODE_LIB)

def transform_ascii(image_file): 
    image_file = image_file.convert("L") # convert image to gray
    code_pic = '' # result ASCII code
    for h in range(0,image_file.size[1]):
        for w in range(0,image_file.size[0]): 
            gray = image_file.getpixel((w,h))
            code_pic = code_pic + CODE_LIB[int(((count-1)*gray)/256)]
        code_pic = code_pic + "\n" 
    return code_pic

def convert_image():
    fn = input("input file name : ")
    hratio = float(input("input height zoom ratio(default 1.0) : ") or "1.0")
    wratio = float(input("input width zoom ratio(default 1.0) : ") or "1.0")
    image_file = Image.open(fn)
    image_file=image_file.resize((int(image_file.size[0]*wratio), int(image_file.size[1]*hratio)))
    print(u'Size info:',image_file.size[0],' ',image_file.size[1],' ')
    fo = open('result.txt','w')
    trans_data = transform_ascii(image_file)
    print(trans_data)
    fo.write(trans_data)
    fo.close()

def convert_video():
    fn = input("input file name : ")
    hratio = float(input("input height zoom ratio(default 1.0) : ") or "1.0")
    wratio = float(input("input width zoom ratio(default 1.0) : ") or "1.0")
    cap = cv2.VideoCapture(fn) 
    i = 0
    if(os.path.isdir("./out") == False):
        os.makedirs("./out")
    while(cap.isOpened()): 
        ret, frame = cap.read() 
        if ret == False:
             break
        cv2.imshow('image', frame) 
        k = cv2.waitKey(5)

        os.system('cls') 
        i += 1
        tmp = open('./out/RES('+str(i)+').txt','w') 
        frame = cv2.resize(frame, (0,0), fx=wratio, fy=hratio)
        frame = Image.fromarray(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)) 
        trans_data = transform_ascii(frame) 
        print(trans_data) 
        tmp.write(trans_data) 
        tmp.close() 

        if (k & 0xff == ord('q')): 
            break 
    cap.release() 
    cv2.destroyAllWindows()


convert_image()