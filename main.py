import cv2
import requests
from pprint import pprint

#############################################
frameWidth = 640
frameHeight = 480
nPlateCascade = cv2.CascadeClassifier("/Users/parvnarang/Desktop/haarcascades/haarcascade_russian_plate_number.xml")
minArea = 200
color = (255, 0, 255)
###############################################

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)
count = 0


while True:
    ret, img = cap.read()
    cv2.imshow("sd", img)
    if not ret:
        break
    k = cv2.waitKey(2)
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    numberPlates = nPlateCascade.detectMultiScale(imgGray, 1.1, 10)
    for (x, y, w, h) in numberPlates:
        area = w * h
        if area > minArea:
            print("Recognised")
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)                 #cv2.putText(img, "Number Plate", (x, y - 5),                                                                               #           cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)
            imgRoi = img[y:y + h, x:x + w]
            cv2.imshow("f",img)
            cv2.imshow("g",imgRoi)

            if k % 256 == 32:
                img_name = "n.png".format(count)
                cv2.imwrite(img_name, imgRoi)
                #print("{} written!".format(img_name))
                #cv2.imwrite("Resources/" + str(count) + ".jpg", imgRoi)
                print("Saved.")
                cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, "Scan Saved", (150, 265), cv2.FONT_HERSHEY_DUPLEX,
                            2, (0, 0, 255), 2)
                count += 1
                cv2.imshow("Result", img)
                cv2.waitKey(1000)
                cv2.destroyAllWindows()

                regions = ['in']  # Change to your country
                with open('n.png', 'rb') as fp:  # location can be changed
                    response = requests.post(
                        'https://api.platerecognizer.com/v1/plate-reader/',
                        data=dict(regions=regions),  # Optional
                        files=dict(upload=fp),
                        headers={'Authorization': 'Token f2cd2223560ae4182a4476f32d2b835c941e3827'})
                # pprint(response.json())
                plate_number = response.json()['results'][0]['plate']
                print(plate_number.upper())
                j = plate_number.upper()
                fi = open("f", "r")
                #o = open("", "r")
                t = fi.read()
                x = j[:2]
                print(x)
                if x == "DL" or x == "HR" or x == "MH" or x == "PB" or x == "UP" or x == "TN":
                    if len(j) == 9:
                        f = j[-7:]
                        print("last 7 characters are - ",f)
                    if len(j) == 10:
                        f = j[-8:]
                        print("last 8 characters are - ",f)

                if x == "MH":
                    print("\t\t\t\t\t\t\t\tRegistered in Maharashtra.")

                if x == "DL":
                    print("\t\t\t\t\t\t\t\tRegistered in Delhi.")

                if x == "UP":
                    print("\t\t\t\t\t\t\t\tRegistered in Uttar Pradesh.")

                if x == "TN":
                    print("\t\t\t\t\t\t\t\tRegistered in Punjab.")

                if x == "HR":
                    print("\t\t\t\t\t\t\t\tRegistered in Harayana.")

                #w = open(f, "r")
                #z = w.read()
                if j in t:
                    w = open(f, "r")
                    z = w.read()
                    print(" YES IT IS PRESENT ")
                    u = input(" DO YOU WANT ITS DETAILS ? ")
                    if u == "yes" or u == "YES" or u == "Yes":
                        print(z)
                        u = "NO CRIMINAL RECORDS "
                        q = "CRIMINAL RECORDS PRESENT"
                        if u in z:
                            print("HE can go to lane 2")
                        if q in z:
                            print("\t\t\t\t\t\t\t\t| Go to lane 1 for further checking |")
                            print("\t\t\t\t\t\t\t\t| &&&&&&& EARLIER RECORD NOT GOOD &&&&&&& |")
                            print("\t\t\t\t\t\t\t\t| Take proper information and recognition of Face and other details. |")

                        exit()

                    elif u == "NO" or u == "no" or u == "No":
                        print(" OK BYE ")
                        exit()

                    else:
                        print(" \t\t\t\t\tSORRY COULD NOT GET YOU TRY AGAIN ")
                        exit()

                else:
                    print(" \t\t\t\t\tTHIS NUMBER PLATE IS NOT PRESENT ")
                    exit()

                break
            break





                # This code is from platerecognizer.com
                #
                # parvnarang11@gmail.com
                # zomato123
                #
                # API key - f2cd2223560ae4182a4476f32d2b835c941e3827
                #
                # API limit 2500 per month
                #
                # Used - 40 till now
                #
                #
