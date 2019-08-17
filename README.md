## Django test assignment
This application creates a simple poll app (just like in a basic Django tutorial), 
with some modifications, such as:
- Bootstrap 4 is used for creating basic layout
- environment is based on docker containers
- MySQL is used as database engine 
- Questions allow multiple selections
- Each visitor is presented with a random question, that can be answered ony once

To run this project, you need to have docker installed in your system 
(see https://docs.docker.com/install/) 

Installing and starting this project is as simply cloning it from this repository
and running the command: ```docker-compose up``` from its main folder.

Docker will create a folder mysql in your main project folder to store all MySQL-related data.
If you need to reset all your data, simply remove this directory and restart the containers.

The web interface of the system will be available at http://localhost:8000/
 
Django admin panel is available at http://localhost:8000/admin with 
username: ```admin```, and password: ```admin```

The admin panel allows you to create and edit Questions, Choice options, as well as see 
Visitor Answers.