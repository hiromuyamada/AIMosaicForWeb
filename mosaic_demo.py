import os
import glob
import tkinter as tk
import base64
from tkinter import filedialog
from itsdangerous import base64_encode
import matplotlib.pyplot as plt
import cv2
from mosaic import mosaic as mosaic
from functools import partial
from PIL import Image
from io import BytesIO


def main(file):
    data = file['image']
    print(data)
    # data = data.replace('data:image/png;base64,','')
    data = data.split(',')[1]
    data += "=" * (-len(data) % 4)
    data = base64.b64decode(data)

    # data = base64.b64decode(data.encode())
    
    # with open("python-logo2.png", 'bw') as f4:
    #     f4.write(data)

    # filename = os.path.splitext(os.path.basename(file_path1))[0]
    cascade_file = "./cascade/haarcascade_frontalface_alt.xml"
    cascade = cv2.CascadeClassifier(cascade_file)

    # with open(file,'r') as f:
    #     data = f.read()

    # img = cv2.imread(data)
    img = Image.open(BytesIO(data))
    # img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_gray = img.convert('L')
    
    #顔認識実行
    face_list = cascade.detectMultiScale(img_gray)
    if len(face_list) == 0:
        quit()

    for (x,y,w,h) in face_list:
        img = mosaic(img, (x,y,x+w, y+h), 7) 
    
    return base64.b64encode(img)
    
    #保存、表示
    os.makedirs("mosaiced",exist_ok=True)
    cv2.imwrite(os.path.join("mosaiced",filename+"-mosaiced.png"), img)
    plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
    showimg = Image.open(os.path.join("mosaiced",filename+"-mosaiced.png"))
    showimg.show()


    
    
# def button1_clicked():
#     global file_path1
#     idir = "C:\\Users"
#     ftype = [("","*.png"),("","*.jpg"),("","*.jpeg")]
#     file_path1 = tk.filedialog.askopenfilename(filetypes=ftype,initialdir = idir)
#     #file_entry1["text"] = file_path1
#     file_entry1.insert(tk.END,file_path1)
    
    
#     return file_path1

# root = tk.Tk()
# root.title("mosaic")
# root.resizable(False,False)
# frame1 = tk.Frame(
#     root,
#     relief='sunken',
#     borderwidth=5
# )
# frame1.grid()

# #GOボタン
# buttongo = tk.Button(
#     frame1,
#     text = "GO MOSAIC",
#     width = 10,
#     command = partial(main)
#     )
# buttongo.grid(row=4,column=0,columnspan=15,rowspan=15)

# #ファイル選択
# file_entry1 = tk.Entry(
#     frame1,
#     width = 40,
#     text=""
#     )
# file_entry1.grid(row=0,column=0)

# button1 = tk.Button(
#     frame1,
#     text="Browse",
#     command = button1_clicked
#     )
# button1.grid(row=0,column=1)

# #余白用ラベル
# labelempty1 = tk.Label(
#     frame1,
#     height=2,
#     text=""
#     )
# labelempty1.grid(row=2,column=0)



# root.mainloop()
