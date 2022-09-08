from flask import Flask, Response, render_template, request
import cv2
import requests
from datetime import datetime
import json
app = Flask(__name__)
cap = cv2.VideoCapture(0)
frameWidth = 640
frameHeight = 480
nPlateCascade = cv2.CascadeClassifier(
    "static/russian_numplate.xml")
minArea = 200
color = (255, 0, 255)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 110)
count = 0
listObj1 = []
registered_vehicles = []

d = {
    "region": None,
    "state": None,
    "numberplate": None,
    "time": None,
    "vehicle-of-building": None,
    "phone-number": None
}

register_a_veh = [None, None, None]


def read_json2():
    global registered_vehicles
    with open("reg-vehicles.json") as fp2:
        registered_vehicles = json.load(fp2)


read_json2()


@app.route("/", methods=["GET", "POST"])
def index():
    global count
    if request.method == "POST":
        if request.form.get("enter"):
            print("enter")
            count = 1
    return render_template('home.html')


def api1():
    global d
    regions = ['in']  # Change to your country
    with open('n.png', 'rb') as fp:  # location can be changed
        response = requests.post('https://api.platerecognizer.com/v1/plate-reader/', data=dict(regions=regions),
                                 files=dict(upload=fp), headers={'Authorization': 'Token add-your-key-here'})
        # plate_number = response.json()['results'][0]['plate']
    d["numberplate"] = response.json()['results'][0]['plate']
    d["numberplate"] = d["numberplate"].upper()
    d["time"] = str(datetime.now())
    print("Number Plate = " + d["numberplate"])
    # read_json2()
    for i in registered_vehicles:
        if i[0] == d["numberplate"]:
            print("yes")
            d["vehicle-of-building"] = "Yes"
            d["phone-number"] = i[1]
            break
        else:
            continue
    else:
        d["vehicle-of-building"] = "No"

    state_list = {"DL": "Delhi", "MH": "Maharashtra", "HP": "Himachal Pradesh", "TN": "Tamil Nadu",
                  "HR": "Harayana", "UP": "Uttar Pradesh", "GJ": "Gujarat", "RJ": "Rajasthan", "WB": "West Bengal",
                  "MP": "Madhya Pradesh", "KA": "Karanataka", "KL": "Kerala", "AP": "Andhra Pradesh", "UK": "Uttrakhand",
                  "OD": "Odhisha", "PB": "Punjab", "GA": "Goa", "JH": "Jharkhand", "AS": "Assam", "BR": "Bihar"}
    for i in state_list:
        if d["numberplate"][:2] == i:
            d["state"] = state_list[i]
            d["region"] = i
            break
        else:
            continue
    write_to_json()


@app.route("/num", methods=["GET", "POST"])
def res():
    return render_template('res.html', json_object=d)


@app.route("/all_veh", methods=["GET", "POST"])
def all_veh():
    read_json1()
    return render_template('all_veh.html', lst=listObj1, len=len(listObj1))


@app.route("/reg_veh", methods=["GET", "POST"])
def reg_veh():
    return render_template('reg_veh.html', reg=registered_vehicles)


@app.route("/register")
def register():
    return render_template('register.html')


@app.route("/registered", methods=["POST"])
def registered():
    global register_a_veh
    register_a_veh[0] = request.form["num"]
    register_a_veh[1] = request.form["phone"]
    register_a_veh[2] = request.form["address"]
    write_to_json2()
    read_json2()
    if suc:
        return render_template('error.html')
    else:
        return render_template('done.html')


@app.route("/deleted", methods=["POST"])
def delete():
    global num_to_delete
    l1 = len(registered_vehicles)
    num_to_delete = request.form["num1"]
    delete_from_json()
    read_json2()
    if len(registered_vehicles) == l1:
        return render_template('error.html')
    else:
        return render_template('deleted.html')


@app.route("/updated", methods=["POST"])
def update():
    global num_to_update
    global num1_to_update
    global phone_to_update
    global address_to_update
    num_to_update = request.form["num2"]
    num1_to_update = request.form["num3"]
    phone_to_update = request.form["phone2"]
    address_to_update = request.form["address2"]
    update_json()
    read_json2()
    if suc1:
        return render_template("error.html")
    else:
        return render_template("updated.html")


def read_json1():
    global listObj1
    with open("sample.json") as fp1:
        listObj1 = json.load(fp1)


def write_to_json():
    listObj = []
    with open("sample.json") as fp:
        listObj = json.load(fp)
    listObj.append(d)
    with open("sample.json", 'w') as json_file:
        json.dump(listObj, json_file,
                  indent=4,
                  separators=(',', ': '))


def write_to_json2():
    global suc
    suc = False
    listObj2 = []
    with open("reg-vehicles.json") as fp3:
        listObj2 = json.load(fp3)
    if register_a_veh[0] != "" and register_a_veh[1] != "" and register_a_veh[2] != "":
        listObj2.append(register_a_veh)
    else:
        suc = True
        pass
    with open("reg-vehicles.json", 'w') as json_file:
        json.dump(listObj2, json_file,
                  indent=4,
                  separators=(',', ': '))


def delete_from_json():
    listObj3 = []
    with open("reg-vehicles.json") as fp4:
        listObj3 = json.load(fp4)
    for i in listObj3:
        if i[0] == str(num_to_delete):
            listObj3.remove(i)
            print("deleted")
            break
        else:
            continue
    with open("reg-vehicles.json", 'w') as json_file:
        json.dump(listObj3, json_file,
                  indent=4,
                  separators=(',', ': '))


def update_json():
    global suc1
    suc1 = False
    listObj4 = []
    with open("reg-vehicles.json") as fp5:
        listObj4 = json.load(fp5)
    for i in listObj4:
        if i[0] == str(num_to_update):
            if num1_to_update != "":
                i[0] = num1_to_update
            if phone_to_update != "":
                i[1] = phone_to_update
            if address_to_update != "":
                i[2] = address_to_update
            else:
                pass
            print("updated")
            break
        if num1_to_update == "" and phone_to_update == "" and address_to_update == "" and num_to_update == "":
            suc1 = True
        else:
            continue
    with open("reg-vehicles.json", 'w') as json_file:
        json.dump(listObj4, json_file,
                  indent=4,
                  separators=(',', ': '))


def gen(cap):
    global count
    while True:
        ret, img = cap.read()
        if not ret:
            break
        k = cv2.waitKey(2)
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        numberPlates = nPlateCascade.detectMultiScale(imgGray, 1.1, 10)
        for (x, y, w, h) in numberPlates:
            area = w * h
            if area > minArea:
                print("DETECTED")
                img = cv2.rectangle(
                    img, (x, y), (x + w, y + h), (255, 0, 255), 2)
                imgRoi = img[y:y + h, x:x + w]
                if count == 1:
                    img_name = "n.png"
                    cv2.imwrite(img_name, imgRoi)
                    print("saved")
                    count = 0
                    api1()
                else:
                    continue

        ret, jpeg = cv2.imencode('.jpg', img)
        frame = jpeg.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    global cap
    return Response(gen(cap),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234, threaded=True)
