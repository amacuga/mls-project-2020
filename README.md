# mls-project-2020

This repository contains my solution to the Project 2020 for the module Machine Learning and Statistics at GMIT.



## Linux

export FLASK_APP=app.py

python3 -m flask run

## Windows

set FLASK_APP=app.py

python -m flask run

docker build . -t app-image

docker run --name app-container -d -p 5000:5000 app-image