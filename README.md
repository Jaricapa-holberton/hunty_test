# Hunty_Test

#### Description:
Hunty_Test is an api designed to query vacancies and available companies in a test database. This was developed as a technical test for the Hunty company.

* Retrive all the companies or vacancies from the test database
* Retrive specific companies or vacancies from the test database

#### Environment:
This project is interpreted/tested on Ubuntu 14.04 LTS using python3 (version 3.4.3)

#### Installation:
* Clone this repository: `git clone "git@github.com:Jaricapa-holberton/hunty_test.git"`
* Access Hunty_Test: `cd hunty_test`
* Create the virtual environment: `virtualenv venv`
* Activate virtualenv: `source venv/bin/activate`
* install dependencies: `pip install -r requirements.txt`
* install ngrok: `curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null && echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | sudo tee /etc/apt/sources.list.d/ngrok.list && sudo apt update && sudo apt install ngrok`  
* Start a tunnel `ngrok http 8000`         
* Activate local server: `python3 manage.py runserver`
* Open the web app in a browser: `http://127.0.0.1:8000/`

#### Examples of use:
interact with the application in the browser writing the necessary endpoints in the browser

#### Bugs:
No known bugs at this time. 

#### Authors:
Jaime Aricapa - [Github](https://github.com/Jaricapa-holberton)

#### License:
Public Domain. No copy write protection. 
