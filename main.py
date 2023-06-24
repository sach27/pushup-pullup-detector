import cv2
import mediapipe as mp
import datetime as dt
import tkinter as tk
root=tk.Tk()
name_label = tk.Label(root, text = 'Username')
def selection():
    def pushup():

        font = cv2.FONT_HERSHEY_SIMPLEX
        draw = mp.solutions.drawing_utils
        mppose = mp.solutions.pose
        pose = mppose.Pose()
        cap = cv2.VideoCapture(vid.get())
        check=False
        count=0

        while True:
            success, image = cap.read()
            try:
                image = cv2.resize(image,(1280,720))
                imageRGB = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
            except:
                pass
            result = pose.process(imageRGB)


            if (result.pose_landmarks):
                points={}
                draw.draw_landmarks(image,result.pose_landmarks,mppose.POSE_CONNECTIONS)
                for id, lm in enumerate(result.pose_landmarks.landmark):
                    h,w,c=image.shape
                    cx, cy = int(lm.x*w), int(lm.y*h)
                    #print(id,lm,cx,cy)
                    points[id]=(cx,cy)
                cv2.circle(image, points[11], 15, (255, 0, 0), cv2.FILLED)
                cv2.circle(image,points[12],15,(255,0,0),cv2.FILLED)
                cv2.circle(image, points[13], 15, (255, 0, 0), cv2.FILLED)
                cv2.circle(image, points[14], 15, (255, 0, 0), cv2.FILLED)
                cv2.circle(image, points[23], 15, (255, 0, 0), cv2.FILLED)
                cv2.circle(image, points[24], 15, (255, 0, 0), cv2.FILLED)
                cv2.circle(image, points[25], 15, (255, 0, 0), cv2.FILLED)
                cv2.circle(image, points[26], 15, (255, 0, 0), cv2.FILLED)
                a11=points[11]
                a12=points[12]
                a13=points[13]
                a14=points[14]
                a23=points[23]
                a24=points[24]
                if((a13[1]<a11[1] and a13[1]<a12[1] and a13[1]<a23[1] and a13[1]<a23[1] and a13[1]<a24[1] ) or (a14[1]<a11[1] and a14[1]<a12[1] and a14[1]<a23[1] and a14[1]<a23[1] and a14[1]<a24[1])):
                    check=True

                    #print("Check")
                elif((a13[1]>a11[1] and a13[1]>a12[1] and a13[1]>a23[1] and a13[1]>a23[1] and a13[1]>a24[1] ) or (a14[1]>a11[1] and a14[1]>a12[1] and a14[1]>a23[1] and a14[1]>a23[1] and a14[1]>a24[1])):
                    #print(check)

                    if(check==True):
                        count=count+1
                        check=False
                        time = dt.datetime.now()

                try:#as time variable might not exist initally
                    #print(dt.datetime.now())
                    k=dt.datetime.now()-time
                    k=k.seconds
                    if(k>15):
                        cv2.putText(image, 'not doing pushup', (900, 100), fontFace=font, fontScale=1, color=(0, 255, 0),thickness=3)
                        cv2.putText(image, 'Total pushups done:' + str(count), (900, 155), fontFace=font, fontScale=1,
                                            color=(0, 255, 0),thickness=3)
                        cv2.imshow("image", image)

                    else:
                        cv2.putText(image, 'doing pushup', (900, 100), fontFace=font, fontScale=1, color=(0, 255, 0),thickness=3)
                        cv2.putText(image, 'Total pushups done:' + str(count), (900, 155), fontFace=font, fontScale=1,
                                    color=(0, 255, 0),thickness=3)
                        cv2.imshow("image", image)
                        cv2.waitKey(10)
                except:
                    cv2.putText(image, 'not doing pushup', (900, 100), fontFace=font, fontScale=1, color=(0, 255, 0),thickness=3)
                    cv2.putText(image, 'Total pushups done:'+str(count), (900, 155), fontFace=font, fontScale=1, color=(0, 255, 0),thickness=3)
                    cv2.imshow("image", image)
                    cv2.waitKey(10)
    def pullup():
        font = cv2.FONT_HERSHEY_SIMPLEX
        draw = mp.solutions.drawing_utils
        mppose = mp.solutions.pose
        pose = mppose.Pose()
        cap = cv2.VideoCapture(vid.get())
        check = False
        count = 0

        while True:
            success, image = cap.read()
            try:
                image = cv2.resize(image, (1280, 720))
                imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            except:
                pass
            result = pose.process(imageRGB)

            if (result.pose_landmarks):
                points = {}
                try:
                    draw.draw_landmarks(image, result.pose_landmarks, mppose.POSE_CONNECTIONS)
                except:
                    pass
                for id, lm in enumerate(result.pose_landmarks.landmark):
                    h, w, c = image.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    # print(id,lm,cx,cy)
                    points[id] = (cx, cy)
                a11 = points[11]
                a12 = points[12]
                a15 = points[15]
                a16 = points[16]
                a9=points[9]
                a10=points[10]
                a911=(a9[1]+a11[1])//2
                a1012=(a10[1]+a12[1])//2
                corrd1=(a11[0],a911)
                corrd2=(a12[0],a1012)
                cv2.circle(image, points[15], 15, (255, 0, 0), cv2.FILLED)
                cv2.circle(image, points[16], 15, (255, 0, 0), cv2.FILLED)
                cv2.circle(image, corrd1, 15, (255, 0, 0), cv2.FILLED)
                cv2.circle(image, corrd2, 15, (255, 0, 0), cv2.FILLED)
                if(corrd1[1]<a15[1] and corrd2[1]<a16[1]):
                    check=True
                elif(corrd1[1]>a15[1] and corrd2[1]>a16[1]):
                    if(check==True):
                        time=dt.datetime.now()
                        check=False
                        count+=1

                try:  # as time variable might not exist initally
                    # print(dt.datetime.now())
                    k = dt.datetime.now() - time
                    k = k.seconds
                    if (k > 15):
                        cv2.putText(image, 'not doing pullup', (900, 100), fontFace=font, fontScale=1,
                                    color=(0, 2, 0),thickness=3)
                        cv2.putText(image, 'Total pullup done:' + str(count), (900, 155), fontFace=font, fontScale=1,
                                    color=(0, 255, 0),thickness=3)
                        cv2.imshow("image", image)

                    else:
                        cv2.putText(image, 'doing pullup', (900, 100), fontFace=font, fontScale=1, color=(255, 0, 0),thickness=3)
                        cv2.putText(image, 'Total pullup done:' + str(count), (900, 155), fontFace=font, fontScale=1,
                                    color=(0, 255, 0),thickness=3)
                        cv2.imshow("image", image)
                        cv2.waitKey(10)
                except:
                    cv2.putText(image, 'not doing pullup', (900, 100), fontFace=font, fontScale=1, color=(0, 255, 0),thickness=3)
                    cv2.putText(image, 'Total pullup done:' + str(count), (900, 155), fontFace=font, fontScale=1,
                                color=(0, 255, 0),thickness=3)
                    cv2.imshow("image", image)
                    cv2.waitKey(10)
    b1=tk.Button(root,text="FOR PUSHUP DETECTOR",command = pushup)
    b2=tk.Button(root,text="FOR PULLUP DETECTOR", command=pullup)
    l1=tk.Label(root,text="SELECT ONE OF THE FOLLOWING")
    l1.grid(row=2,column=1)
    b1.grid(row=3,column=0)
    b2.grid(row=3,column=2)

vid = tk.StringVar()
en=tk.Entry(root, textvariable=vid)
bu=tk.Button(root, text="Enter", command=selection)
en.grid(row=0,column=0)
bu.grid(row=1,column=0)
root.mainloop()