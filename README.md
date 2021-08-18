# DevOps Apprenticeship: Project Exercise

System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install poetry using one of the following commands (as instructed by the poetry documentation):

# Poetry installation (Bash)

curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
Poetry installation (PowerShell)

(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python
Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

    $ poetry install

You'll also need to clone a new .env file from the .env.template to store local configuration options. This is a one-time operation on first setup. use the command below for the first time only.

    $ cp .env.template .env  

The .env file is used by flask to set environment variables when running flask run. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a SECRET_KEY variable which is used to encrypt the flask session cookie.

# Running The App

Once the all dependencies have been installed, start the Flask app in development mode within the poetry environment by running:

    $ poetry run flask run

# Vagrant

ensure virtual box and vagrant are installed prior to runnig the 'vagrant up' command. virtual box - https://www.virtualbox.org/ vagrant - https://www.vagrantup.com

to run this app using vagrant: 

    $ vagrant up

You should see output similar to the following:

 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
Now visit http://localhost:5000/ in your web browser to view the app.


# Docker

Install Docker
    
    https://www.docker.com/products/docker-desktop

**Development**

To build:
    
    $ docker build --target development --tag todo-app:dev .

To run:

    $ docker run -d --env-file ./.env -p 5000:5000 --mount type=bind,source="$(pwd)"/todo_app,target=/app/todo_app todo-app:dev

NB in development the app is run using the flask development server. A bind mount is also defined to allow the container to access the project directory on the host machine. 

**Production**

To build:
    
    $ docker build --target production --tag todo-app:prod .

To run:

    $ docker run -d --env-file ./.env -p 5000:5000 todo-app:prod

NB in Production the app is run using a GUnicorn production server. 
