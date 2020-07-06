import cv2
import numpy as np
import os
import math
# Playing video from file:
video_name=input("Enter the video folder in .mov type\n")
cap = cv2.VideoCapture(video_name)

try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print ('Error: Creating directory of data')

currentFrame = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret : break

    # Saves image of the current frame in jpg file
    name = '\\data\\frame' + str(currentFrame) + '.jpg'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)

    # To stop duplicate images
    currentFrame += 1


# CREATION OF FRAMES - STEP 1
import os, shutil
folder = '/Users/Vaishnavi/Desktop/Final_year_Project/TrainYourOwnYOLOABC/Data/Source_Images/Test_Images'
for filename in os.listdir(folder):
       file_path = os.path.join(folder, filename)
       try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
       except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

# When everything done, release the capture
print (currentFrame)
count=math.floor(currentFrame/2)
for i in range (5):
    #print (count)
    img = cv2.imread('\\data\\frame%d.jpg' %count, 1)
    path = '/Users/Vaishnavi/Desktop/Final_year_Project/TrainYourOwnYOLOABC/Data/Source_Images/Test_Images'  #saving frames in test folder
    cv2.imwrite(os.path.join(path , '%d.jpg' %count), img)
    count=count+10
cap.release()
cv2.destroyAllWindows()


# STEP 2 - STANDING WALKING CLASSIFICATION

import os
import pandas as pd

os.system('python /Users/Vaishnavi/Desktop/Final_year_Project/TrainYourOwnYOLOABC/3_Inference/Detector.py')

#Creating the data frame

df = pd.read_csv("/Users/Vaishnavi/Desktop/Final_year_Project/TrainYourOwnYOLOABC/Data/Source_Images/Test_Image_Detection_Results/Detection_Results.csv")

count=0
nocount=0
for i in range(5):
     if(df.at[i,'label']==0):
           count=count+1
     else:
           nocount=nocount+1

#print("no of standing is ",count)
#print(nocount)

#STEP 3 - HUMAN NON HUMAN CLASSIFICATION
import os, shutil
folder = '/Users/Vaishnavi/Desktop/Final_year_Project/TrainYourOwnYOLO/Data/Source_Images/Test_Images'
for filename in os.listdir(folder):
       file_path = os.path.join(folder, filename)
       try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
       except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
if(count>nocount):
     print("Standing")
     count=math.floor(currentFrame/2)
     for i in range (5):
            if(i==3):
               img = cv2.imread('\\data\\frame%d.jpg' %count, 1)
               path = '/Users/Vaishnavi/Desktop/Final_year_Project/TrainYourOwnYOLO/Data/Source_Images/Test_Images'  #saving frames in test folder
               cv2.imwrite(os.path.join(path , '%d.jpg' %count), img)
            count=count+10
     cap.release()
     cv2.destroyAllWindows()

     os.system('python /Users/Vaishnavi/Desktop/Final_year_Project/TrainYourOwnYOLO/3_Inference/Detector.py')

     df = pd.read_csv("/Users/Vaishnavi/Desktop/Final_year_Project/TrainYourOwnYOLO/Data/Source_Images/Test_Image_Detection_Results/Detection_Results.csv")

     count=0
     nocount=0
     for i in range(1):
         if(df.at[i,'label']==1):
           count=count+1
         else:
           nocount=nocount+1

     #print("no of human is ",count)
     #print(nocount)

     #STEP 4 - AGE DETECTION

     if(count>nocount):
         print("Human")
         count=math.floor(currentFrame/2)
         for i in range (5):
             if(i==3):
               img = cv2.imread('\\data\\frame%d.jpg' %count, 1)
               path = '/Users/Vaishnavi/Desktop/Final_year_Project/Main/images'  #saving frames in test folder
               cv2.imwrite(os.path.join(path , '118.jpg'), img)
             count=count+10
         cap.release()
         cv2.destroyAllWindows()

         os.system('python /Users/Vaishnavi/Desktop/Final_year_Project/Main/test.py --input /Users/Vaishnavi/Desktop/Final_year_Project/Main/images/118.jpg')

         f=open("/Users/Vaishnavi/Desktop/Final_year_Project/Main/output.txt","r")
         f1=f.readlines()
         #print(f1)
         if(f1==['Age : (4-6)\n']):
               a=15
               print("CHILD")
               print("TIME ALLOTED : 15s")
         elif(f1==['Age : (8-12)\n']):
               a=15
               print("CHILD")
               print("TIME ALLOTED : 15s")
         elif(f1==['Age : (15-20)\n']):
               a=10
               print("YOUNG")
               print("TIME ALLOTED : 10s")
         elif(f1==['Age : (25-32)\n']):
               a=10
               print("YOUNG")
               print("TIME ALLOTED : 10s")
         elif(f1==['Age : (38-43)\n']):
               a=12
               print("MIDDLE")
               print("TIME ALLOTED : 12s")
         elif(f1==['Age : (48-53)\n']):
               a=12
               print("MIDDLE")
               print("TIME ALLOTED : 12s")
         elif(f1==['Age : (60-100)\n']):
               a=20
               print("OLD")
               print("TIME ALLOTED : 20s")
         else:
               a=10
               print("TIME ALLOTED(DEFAULT) : 10s")
         import tkinter as tk
         import tkinter.font as tkFont
         from PIL import ImageTk, Image
         from tkinter import *
         class ExampleApp(tk.Tk):
            def __init__(self):
               tk.Tk.__init__(self)
               self.label = tk.Label(self, text="", width=10,height=5,font=('digital-7 Mono', 120),fg='red', bg='black')
               #self.label.config(font=("Times New Roman", 65))
               self.label.pack(expand="True")
               self.remaining = 0
               self.countdown(a)

            def countdown(self, remaining = None):
               if remaining is not None:
                 self.remaining = remaining

               if self.remaining <= 0:
                 self.label.configure(text="time's up!")
               else:
                 self.label.configure(text="%d" % self.remaining)
                 self.remaining = self.remaining - 1
                 self.after(1000, self.countdown)

         if __name__ == "__main__":
             app = ExampleApp()
             app.mainloop()

     else:
        print("Animal")
        a=10
        print("Alloted time is 10 seconds")
        import tkinter as tk
        import tkinter.font as tkFont
        from PIL import ImageTk, Image
        from tkinter import *
        class ExampleApp(tk.Tk):
            def __init__(self):
               tk.Tk.__init__(self)
               self.label = tk.Label(self, text="", width=10,height=5,font=('digital-7 Mono', 120),fg='red', bg='black')
               #self.label.config(font=("Times New Roman", 65))
               self.label.pack(expand="True")
               self.remaining = 0
               self.countdown(a)

            def countdown(self, remaining = None):
               if remaining is not None:
                 self.remaining = remaining

               if self.remaining <= 0:
                 self.label.configure(text="time's up!")
               else:
                 self.label.configure(text="%d" % self.remaining)
                 self.remaining = self.remaining - 1
                 self.after(1000, self.countdown)

        if __name__ == "__main__":
             app = ExampleApp()
             app.mainloop()
 
        
else:
      print("Walking away")


exit()

