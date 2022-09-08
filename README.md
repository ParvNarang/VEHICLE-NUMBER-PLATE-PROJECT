# Vehicle Numberplate Reading Web App
This is an updated version of my previous vehicle-numberplate-reading/vehicle management project.

## Objective
The aim of this project was to make a web app that manages vehicles entering the parking of a building/society & store it's details like the RTO code, time of entry & whether or not it belongs to the particular building by reading it's numberplate.

Written in : **Python**

**Requirements**
  - OpenCV
  - Flask
  - DateTime
  - Requests
  - Json
  - Russian Number Plate xml file (used for detecting the numberplate)

Uses an **API Token** from ( https://platerecognizer.com/ )
### Launch Screen
As soon as the numberplate is detected in the camera feed, click the button to capture the image, it saves the image with the current time & calls the api function to recognise the characters on the numberplate.

<p align="center">
  <img src="https://github.com/ParvNarang/VEHICLE-NUMBER-PLATE-PROJECT/blob/0f6e6843ba3af7a626e13ad17333ce897c56a850/assets/1.png">
</p>

### Check the numberplate
After the numberplate is recognised, all the details related to it are listed.

<p align="center">
  <img src="https://github.com/ParvNarang/VEHICLE-NUMBER-PLATE-PROJECT/blob/0f6e6843ba3af7a626e13ad17333ce897c56a850/assets/2.png">
</p>

### Update Info

You can also register, update & delete details about a vehicle.

<p align="center">
  <img src="https://github.com/ParvNarang/VEHICLE-NUMBER-PLATE-PROJECT/blob/0f6e6843ba3af7a626e13ad17333ce897c56a850/assets/3.png">
</p>

### All Numberplates

It shows all the vehicles that have made an entry till now.
<p align="center">
  <img src="https://github.com/ParvNarang/VEHICLE-NUMBER-PLATE-PROJECT/blob/0f6e6843ba3af7a626e13ad17333ce897c56a850/assets/4.png">
</p>

### Registered Vehicles

A table showcasing all the registered vehicles
<p align="center">
  <img src="https://github.com/ParvNarang/VEHICLE-NUMBER-PLATE-PROJECT/blob/0f6e6843ba3af7a626e13ad17333ce897c56a850/assets/5.png">
</p>