import cv2
import requests
#from pprint import pprint
import PySimpleGUI as sg
from datetime import datetime
from tqdm import tqdm
import time

sg.theme('DarkBlue4')
list = []
def auto():
    cap = cv2.VideoCapture(0)
    frameWidth = 640
    frameHeight = 480
    nPlateCascade = cv2.CascadeClassifier("/Users/parvnarang/PycharmProjects/NUMBERPLATEPROJECT/Resources/haarcascade_russian_plate_numb.xml")
    minArea = 200
    color = (255, 0, 255)
    cap.set(3, frameWidth)
    cap.set(4, frameHeight)
    cap.set(10, 150)
    count = 0

    while True:
        ret, img = cap.read()
        cv2.imshow("Camera", img)
        if not ret:
            break
        k = cv2.waitKey(2)
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        numberPlates = nPlateCascade.detectMultiScale(imgGray, 1.1, 10)
        cv2.waitKey(300)
        cv2.waitKey(300)
        if cv2.waitKey(1000) == ord("q"):
            cv2.destroyAllWindows()
            cap.release()
            print("CAMERA WINDOW CLOSED.")
            break

        for (x, y, w, h) in numberPlates:
            area = w * h
            if area > minArea:
                print("DETECTED")
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255),
                              2)  # cv2.putText(img, "Number Plate", (x, y - 5),                                                                               #           cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)
                imgRoi = img[y:y + h, x:x + w]
                cv2.imshow("f", img)
                cv2.imshow("g", imgRoi)

                for i in range(1):
                    cv2.waitKey(200)
                    img_name = "n.png".format(count)
                    cv2.imwrite(img_name, imgRoi)
                    s = datetime.now()
                    print(s)
                    # print("{} written!".format(img_name))
                    cv2.imwrite("Resources/" + str(s) + ".jpg", imgRoi)
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

                    for i in tqdm(range(1)):
                        time.sleep(0.0001)
                        animate()
                        pass

                    print(plate_number.upper())
                    j = plate_number.upper()
                    fi = open("f", "r")
                    t = fi.read()
                    x = j[:2]
                    print(x)
                    y = open("g", "a")
                    y.write(j)
                    y.write(" came at this day and at this time ")
                    y.write(str(s))
                    y.write('\t\n\n')
                    y.close()
                    list.append(j)

                    if x == "DL" or x == "HR" or x == "MH" or x == "PB" or x == "UP" or x == "TN":
                        if len(j) == 9:
                            f = j[-7:]
                            print("last 7 characters are - ", f)
                        if len(j) == 10:
                            f = j[-8:]
                            print("last 8 characters are - ", f)

                    if x == "MH":
                        print("Registered in Maharashtra.")

                    if x == "DL":
                        print("Registered in Delhi.")

                    if x == "UP":
                        print("Registered in Uttar Pradesh.")

                    if x == "TN":
                        print("Registered in Punjab.")

                    if x == "HR":
                        print("Registered in Harayana.")

                    # w = open(f, "r")
                    # z = w.read()
                    if j in t:
                        w = open(f, "r")
                        z = w.read()
                        print(" YES IT IS PRESENT ")
                        print(" This car can go ")
                        layout = [[sg.Text('.......ALLOWED.......',font='Times')]]
                        window = sg.Window("Permission", layout)
                        event, values = window.read()
                        window.close()
                        break

def animate():
    g1 = r'/Users/parvnarang/PycharmProjects/NUMBERPLATEPROJECT/Resources/x.gif'
    gifs = [g1]
    layout = [[sg.Image(background_color='white', key='-IMAGE-', right_click_menu=['UNUSED', 'Exit'])],
              [sg.Text('              ... LOADING ...  ', key='smptex')]]
    window = sg.Window('LOADING', layout, finalize=True)
    image = window['-IMAGE-']  # type: sg.Image
    for i in tqdm(range(40)):
        time.sleep(0.000001)
        event, values = window.read(timeout=100)
        if event == 'Exit':
            window.close()
            break
        image.update_animation(g1, 100)
        pass
    window.close()

def all():
    e = open("g", "r")
    p = e.read()
    animate()
    print(p)
    layout1 = [[sg.Text(" All the number plates till now - ")],
               [sg.Text(p)],
               [sg.Cancel("BACK", size=(6, 0), font='Arial')]]

    form1 = sg.Window('ALL NUMBERPLATES (DATE_TIME)',size=(600,600)).Layout([[sg.Column(layout1, scrollable=True,size=(600,600))]])
    form1.Read()
    form1.close()

def g():
    print(list)
    m = ', '.join(str(a) for a in list)
    layout = [[sg.Text(" All the number plates till now - ")],
              [sg.Text(m, font='Times', size=(30, 0))]]
    form = sg.Window('ALL NUMBERPLATES (DATE_TIME)',size=(500,500)).Layout([[sg.Column(layout, scrollable=True,size=(400,400))], [sg.Button("  CLICK  ", font='Arial')],
                    [sg.Cancel("BACK",size=(6,0) ,font='Arial')]])
    event, values = form.Read()
    form.close()

while True:
    layout = [[sg.Text(" \n\t\t\t\t        N      U      M      B      E      R      P      L      A      T      E   \n\t\t\t\t\t                  A    P    P  ",background_color='navy',text_color='Dark Grey',font='Impact',key='-DISPLAY-',size= (175,5),justification='left')],
              [sg.Text("\n\tThis is our NUMPLATE Application for automatic recognition of number plates and reading its specific information.")],
              [sg.Text("\n\tA vehicle registration plate, also known as a number plate (British English) or license plate (American English),")],
              [sg.Text("\n\tis a metal or plastic plate attached to a motor vehicle or trailer for official identification purposes.")],
              [sg.Text("\n\tIndian number plates come in five different colour combinations. Plates for private vehicles have black lettering,")],
              [sg.Text("\n\ton a white background.Commercial vehicles, such as taxis, buses and lorries, have black lettering on a yellow background.")],
              [sg.Text("\n\tFor commercial and public vehicles, a yellow background with black typeface.")],
              [sg.Text("\tFor private vehicles, a black background with white typeface.")],
              [sg.Text("\tFor government vehicles, a red background with white typeface.")],
              [sg.Text("\tDealer plates are white background with red typeface, usually for vehicles yet to have legal and confirmed information and owner.")],
              [sg.Text('\n\nClick on the Camera Option down below - \n',justification='left')],
              [sg.Button(" OPTIONS",font='Arial',size=(140,2))],[sg.Cancel("EXIT",font='Arial',size=(140,2))]]
    window = sg.Window("NUMBERPLATE APP",layout,size=(700,550))
    event, values = window.read()
    window.close()

    if event == " OPTIONS":
        layout = [[sg.Text("                                     Click on one of the following options.    ", font='Arial')],
                  [sg.Text("                            *Press Spacebar when numberplate is detected.\n", font='Arial')],
                  [sg.Button(" CAMERA ", font='Arial', size=(60, 2))],
                  [sg.Button(" ALL NUMBERPLATES TODAY ", font='Arial', size=(60, 2))],
                  [sg.Button(" ALL NUMBERPLATES WITH TIMESTAMP ", font='Arial', size=(60, 2))],
                  [sg.Button(" AUTOMATIC ", font='Arial', size=(60, 2))],
                  [sg.Cancel("EXIT", font='Arial', size=(60, 2))]]
        window = sg.Window("Information", layout, size=(540, 400))
        event, values = window.read()
        window.close()
        if event == "CAMERA":
            continue

        if event == " ALL NUMBERPLATES TODAY ":
            g()
            continue

        if event == " ALL NUMBERPLATES WITH TIMESTAMP ":
            all()
            continue

        if event == " AUTOMATIC ":
            cv2.waitKey(3000)
            auto()

    if event == "EXIT" or event == sg.WIN_CLOSED:
        exit()

    cap = cv2.VideoCapture(0)
    frameWidth = 640
    frameHeight = 480
    nPlateCascade = cv2.CascadeClassifier("/Users/parvnarang/PycharmProjects/NUMBERPLATEPROJECT/Resources/haarcascade_russian_plate_numb.xml")
    minArea = 200
    color = (255, 0, 255)
    cap.set(3, frameWidth)
    cap.set(4, frameHeight)
    cap.set(10, 150)
    count = 0

    while True:
        if cv2.waitKey(1) == 27:
            cv2.destroyAllWindows()
            cap.release()
            print("CAMERA WINDOW CLOSED.")
            break
        ret, img = cap.read()
        cv2.imshow("Camera", img)
        if not ret:
            break
        k = cv2.waitKey(2)
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        numberPlates = nPlateCascade.detectMultiScale(imgGray, 1.1, 10)
        for (x, y, w, h) in numberPlates:
            area = w * h
            if area > minArea:
                print("DETECTED")
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)                 #cv2.putText(img, "Number Plate", (x, y - 5),                                                                               #           cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)
                imgRoi = img[y:y + h, x:x + w]
                cv2.imshow("f",img)
                cv2.imshow("g",imgRoi)

                if k % 256 == 32:
                    img_name = "n.png".format(count)
                    cv2.imwrite(img_name, imgRoi)
                    s = datetime.now()
                    print(s)
                    #print("{} written!".format(img_name))
                    cv2.imwrite("Resources/" + str(s) + ".jpg", imgRoi)
                    print("Saved.")
                    cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
                    cv2.putText(img, "Scan Saved",(150, 265), cv2.FONT_HERSHEY_DUPLEX,
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

                    for i in tqdm(range(10000)):
                        time.sleep(0.0001)
                        pass

                    print(plate_number.upper())
                    j = plate_number.upper()
                    fi = open("f", "r")
                    t = fi.read()
                    x = j[:2]
                    print(x)
                    y = open("g", "a")
                    y.write(j)
                    y.write(" came at this day and at this time ")
                    y.write(str(s))
                    y.write('\t\n\n')
                    y.close()
                    list.append(j)

                    if x == "DL" or x == "HR" or x == "MH" or x == "PB" or x == "UP" or x == "TN":
                        if len(j) == 9:
                            f = j[-7:]
                            print("last 7 characters are - ",f)
                        if len(j) == 10:
                            f = j[-8:]
                            print("last 8 characters are - ",f)

                    if x == "MH":
                        print("Registered in Maharashtra.")

                    if x == "DL":
                        print("Registered in Delhi.")

                    if x == "UP":
                        print("Registered in Uttar Pradesh.")

                    if x == "TN":
                        print("Registered in Punjab.")

                    if x == "HR":
                        print("Registered in Harayana.")

                    #w = open(f, "r")
                    #z = w.read()
                    if j in t:
                        w = open(f, "r")
                        z = w.read()
                        print(" YES IT IS PRESENT ")
                        print(" This car can go ")

                        layout = [[sg.Text("\t           It can go just press the \n\tbutton of camera for storing information - \n\n")],
                                  [sg.Button("Camera", font='Arial', size=(29, 2))],
                                  [sg.Button("Press for details", font='Arial', size=(29, 2))],
                                  [sg.Button("Back", font='Arial', size=(29, 2))]]
                        window = sg.Window("Details", layout, size=(300, 265))
                        event, values = window.read()
                        window.close()
                        if event == "Back":
                            break
                        if event == "Camera":
                            face_cascade = cv2.CascadeClassifier("/Users/parvnarang/PycharmProjects/NUMBERPLATEPROJECT/Resources/front_face_det.xml")

                            cap = cv2.VideoCapture(0)
                            if not (cap.isOpened()):
                                print("Could not open video device:")

                            while True:
                                ret, img = cap.read()
                                if ret == False:
                                    break

                                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                                faces = face_cascade.detectMultiScale(gray, 1.1, 4)

                                for (x, y, w, h) in faces:
                                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

                                cv2.imshow('img', img)

                                key = cv2.waitKey(5)
                                if key % 256 == 32:
                                    s = datetime.now()
                                    print(s)
                                    # print("{} written!".format(img_name))
                                    cv2.imwrite("Faces/" + str(s) + ".jpg", img)
                                    print("Saved.")
                                    cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
                                    cv2.putText(img, str(s), (150, 265), cv2.FONT_HERSHEY_DUPLEX,
                                                2, (0, 0, 255), 2)
                                    # count += 1
                                    cv2.imshow("Result", img)
                                    cv2.waitKey(1000)
                                    s = datetime.now()
                                    layout = [[sg.Text("NAME - ")], [sg.InputText()], [sg.Text("\nNUMBERPLATE - ")],
                                              [sg.InputText(j)], [sg.Button("Enter")]]
                                    window = sg.Window("Details", layout, size=(300, 265))
                                    event, values = window.read()
                                    window.close()
                                    r = str(values)
                                    alphanumeric = ""
                                    for character in r:
                                        if character.isalnum():
                                            alphanumeric += character

                                    res = ''.join([i for i in alphanumeric if not i.isdigit()])
                                    print(res)
                                    e = open("Faces/det", "a")
                                    e.write(str(values))
                                    e.write(" came at ")
                                    e.write(str(s))
                                    e.write(" of number plate ")
                                    e.write(j)
                                    e.write('\t\n\n')
                                    e.close()
                                    cv2.destroyAllWindows()
                                    break

                                if key == ord('q'):
                                    break

                        if event == "Press for details":
                            print(z)
                            layout = [[sg.Text(" Here are the details of the number plate - \n", font='Times')],
                                      [sg.Text(z, font='Times', size=(25, 10))],
                                      [sg.Button("     Show all numberplates     ", font='Arial')],
                                      [sg.Cancel("              Exit                 ", font='Arial')]]
                            window = sg.Window("Details Tab", layout, size=(500, 500))
                            event, values = window.read()
                            window.close()
                            if event == "     Show all numberplates     ":
                                g()
                                '''print(list)
                                m = ', '.join(str(a) for a in list)
                                layout = [[sg.Text(" All the number plates till now - ")],
                                          [sg.Text(m, font='Times', size=(30, 0))]]
                                form = sg.Window('ALL NUMBERPLATES (DATE_TIME)').Layout([[sg.Column(layout, scrollable=True)],[sg.Button("  CLICK  ",font='Arial')],[sg.Cancel("EXIT",size=(5,1),font='Arial')]])
                                event, values = form.Read()
                                form.close()'''
                                if event == "  CLICK  ":
                                    all()
                                    '''e = open("g", "r")
                                    p = e.read()
                                    print(p)
                                    layout1 = [[sg.Text(" All the number plates till now - ")],
                                               [sg.Text(p)],
                                               [sg.Cancel("Exit",size=(5,1),font='Arial')]]

                                    form1 = sg.Window('ALL NUMBERPLATES (DATE_TIME)').Layout([[sg.Column(layout1, scrollable=True)]])
                                    form1.Read()'''

                            r = "NO CRIMINAL RECORDS "
                            q = "CRIMINAL RECORDS PRESENT"
                            if r in z:
                                print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tHE can go to lane 2")
                                layout = [[sg.Text("He can go to lane 2")],[sg.Cancel("Exit",font='Arial',size=(60,2))]]
                                window = sg.Window("Demo", layout, size=(450, 450))
                                event, values = window.read()
                                window.close()
                            if q in z:
                                print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t| Go to lane 1 for further checking |")
                                print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t| &&&&&&& EARLIER RECORD NOT GOOD &&&&&&& |")
                                print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t| Take proper information and recognition of Face and other details. |")
                                layout = [[sg.Text("| Go to lane 1 for further checking |")],
                                          [sg.Text("| &&&&&&& EARLIER RECORD NOT GOOD &&&&&&& |")],
                                          [sg.Text("| Take proper information and recognition of Face and other details. |")],
                                          [sg.Text("\n\n\n\n\n\n\n\n\n\n\n")],
                                          [sg.Text(" Click this button to open camera for picture of face - ")],
                                          # [sg.Text(" ")],
                                          [sg.Button(" Click Photo of face - ", font='Arial', size=(60, 2))],
                                          [sg.Cancel("Exit", font='Arial', size=(60, 2))]]
                                window = sg.Window("Information", layout, size=(450, 450))
                                event, values = window.read()
                                window.close()
                                if event == "Exit" or event == sg.WIN_CLOSED:
                                    exit()

                        if event == "Exit" or event == sg.WIN_CLOSED:
                            exit()

                    else:
                        print(" \t\t\t\t\tTHIS NUMBER PLATE IS NOT PRESENT ")
                        exit()

                    #break
                #break