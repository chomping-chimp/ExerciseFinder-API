# Exercise API
## Overview
The goal of this API is to help solve some issues that many fitness enthusiasts face. Our list of features are expanding, but for now, we can help users search for exercises through our Exercise database. This API also serves the Activity Scoreboard for the Discord bot I am working on ([JarvisBot](https://github.com/sir-typesalot/JarvisBot)) and I plan to make that feature more robust so it can be accessible to many more users.

## Architecture 
This project uses the Flask framework and is deployed in a Docker container that is hosted on AWS Lightsail. The Database layer is hosted on AWS as well. Deployment to Lightsail is done locally, most of it automated with a bash script.

## Features
For a more in depth explanation for each of the endpoints, please visit the [Wiki](https://github.com/sir-typesalot/ExerciseFinder-API/wiki/Wiki) It's being worked on still, so please bear with me!
- `exercise/get-all` - Get all the exercises in the Database
- `exercise/get-one` - Get one exercise or a group of exercises that match a name
- `exercise/filter` - Filter exercises by criteria (muscle group, category, difficulty, etc..)

## Setup
This project has a few pre-requisites:
- Need to have Docker installed
- Python >= 3.9 installed
- Make sure port 5000 is available   

To work on this you will need to run a python virtual env. All the required packages are listed in the requirements.txt file.   
Documentation to set up and start up virtual environment <a href="https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/">here</a>   
The Python version used in this project is 3.9
