# NumberPlate Reading Web App
This is an updated version of my previous vehicle numberplate reading project.

# Objective
The aim of this project was to make a web app that reads the numberplate of a vehicle that enters the parking of a building/society & store it's details like the RTO code, time of entry & whether or not it belongs to the particular building.

Written in : **Python**

Requirements
  - OpenCV
  - Flask
  - DateTime
  - Requests
  - Json
  - Russian Number Plate xml file (used for detecting the numberplate)

Uses an **API Token** from ( https://platerecognizer.com/ )
### Launch Screen
As soon as the numberplate is detected in the camera feed, click the button to capture the image, it saves the image with the current time & calls the api function to recognise the characters on the numberplate.

Image1
### Check the numberplate
After the numberplate is recognised, all the details related to it are listed.

Image2
### Update Info
You can also register, update & delete details about a vehicle.

Image3
### All Numberplates
It shows all the vehicles that have made an entry till now.

Image4
### Registered Vehicles
A table of all the registered vehicles

Image5