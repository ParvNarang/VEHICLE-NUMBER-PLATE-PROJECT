# VEHICLE-NUMBER-PLATE PROJECT

A program that allows automatic entry of vehicles in a building/society with proper authentication.

# Objective

The aim of this project was to make vehicles enter in a building/society automatically with proper authentication of the vehicle by using its Number Plate. The system checks the vehicle’s records whether or not it belongs to the society and lets it enter only if the number plate is recognised by the camera and that the number is located in the directory.

Written in - Python

Requirements 
  - OpenCV
  - SimpleGUI
  - DateTime
  - tqdm
  - Requests
  - PyTesseract (in the initial Version)
  - Russian Number Plate xml file

Now the current version of program uses an API Token(from https://platerecognizer.com/) that recognises the number-plates pretty well as compared to using the Pytesseract Library.

# Working

The Launch Screen                
                                                                                                 
![Screenshot 2021-01-12 at 1 03 26 AM](https://user-images.githubusercontent.com/56078295/104637078-4b33ca80-56ca-11eb-8701-c34fb584f747.png)

When the ‘options’ button is clicked then it shows 5 options - 

![Screenshot 2021-01-12 at 1 03 52 AM](https://user-images.githubusercontent.com/56078295/104637134-630b4e80-56ca-11eb-920d-b262a078bdbf.png)
   

1) CAMERA.

2) ALL NUMBER-PLATES TODAY.

3) ALL NUMBER-PLATES WITH TIMESTAMP.

4) AUTOMATIC.

5) EXIT.

  - “Camera” option is used for manual checking of number plates.

  - “All number plates today” shows the number plates on that particular day only.
  
  - “All number plates with timestamp” show all the number plates till now with timestamp.
  
  - “Automatic” option is used to automatically check the number plates entering the building.

As the CAMERA or AUTOMATIC option is clicked it opens the camera window it first detects the number plate using russian number plate haarcascade xml file and then clicks a photo and sends requests to recognise the number plate.

![Screenshot 2021-01-12 at 12 59 31 AM](https://user-images.githubusercontent.com/56078295/104637298-a1a10900-56ca-11eb-8cf2-b202c309e96b.png)

![Screenshot 2021-01-12 at 12 56 52 AM](https://user-images.githubusercontent.com/56078295/104637376-b9788d00-56ca-11eb-9151-aa6dda39b8e8.png)

After the scan is saved it stores the image, processes it and then checks for it in its directory. If it is found then it shows the following - 

![Screenshot 2021-01-12 at 12 57 36 AM](https://user-images.githubusercontent.com/56078295/104637451-d0b77a80-56ca-11eb-96d7-bff3466a46c9.png)

It shows that it is present with “MH” as its state and the last 8 characters. 

“Press for details” option shows the details of the number plate that is stored in the text files - 

![Screenshot 2021-01-12 at 12 59 59 AM](https://user-images.githubusercontent.com/56078295/104637533-edec4900-56ca-11eb-90bf-4f9b84f7d5ff.png)

All the number plates recorded with timestamp :-

![Screenshot 2021-01-12 at 1 04 40 AM](https://user-images.githubusercontent.com/56078295/104637636-14aa7f80-56cb-11eb-8e3b-d83ac3e9b28d.png)

In the text file :-

![Screenshot 2021-01-12 at 1 05 50 AM](https://user-images.githubusercontent.com/56078295/104637744-3277e480-56cb-11eb-814b-7c61d9e37d56.png)

# Future Plan

To use a web-camera with JETSON-NANO/RASPBERRY-PI 4
