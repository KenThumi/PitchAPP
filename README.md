# Pitch Application
## Description
Welcome to this Pitch application. The app is a platform whereby registered users can post their pitches <br>
based on any categories. Others users can like and comment (provided they are registered).

## Author
- [Kenneth Thumi](https://github.com/KenThumi)

## Contact
Email:kenthumi@gmail.com

## Setup instructions
Below are steps to follow:
1. Open cli, navigate to your project folder and clone the project: <br/>
    `git clone https://github.com/KenThumi/PitchAPP.git`
2. Install python, preferably python3.
3. Create a virtual environment: <br/>
    `python3 -m venv virtual`
4. To activate the virtual environment run:<br/>
    `source virtual/bin/activate`
5. Now, in the virtual environment, install Flask to the project using the following command:<br/>
    `pip install flask`
6. Install flak bootstrap and flask script respectively:<br/>
        `pip install flask-bootstrap4`<br/>
        `pip install flask_script`
7. Head over to [New API](https://newsapi.org/) and generate API key. To generate SECRET KEY 
    , open REPL by typing command `python3`. Enter these commands: <br/>
            `import secrets` <br/>
            `secrets.token_hex(16)`<br/>
    Where 16 is key length. Copy the keys to somewhere.
8. To register the API KEY and SECRET KEY to OS for use, enter these command. Enter the respective key where necessary <br/>
   
    `export SECRET_KEY='secret key generated'`

9. Inside the same folder,  type following commands to start the application:<br/>
    `python3 manage.py server`
10. Open browser and input `http://127.0.0.1:5000`
11. To edit, use IDE of your choice to work with the project, e.g VsCode, Sublime text ,etc.

## Technologies Used
In this project, below is a list of technologies used:
- [Python version 3](https://www.python.org/)

alembic==1.5.8
blinker==1.4
click==7.1.2
dnspython==2.1.0
dominate==2.6.0
email-validator==1.1.2
Flask==1.1.2
Flask-Bootstrap4==4.0.2
Flask-Login==0.5.0
Flask-Mail==0.9.1
Flask-Migrate==2.7.0
Flask-Script==2.0.6
Flask-SQLAlchemy==2.5.1
Flask-Uploads==0.2.1
Flask-WTF==0.14.3
greenlet==1.0.0
idna==3.1
itsdangerous==1.1.0
Jinja2==2.11.3
Mako==1.1.4
MarkupSafe==1.1.1
psycopg2==2.8.6
python-dateutil==2.8.1
python-editor==1.0.4
six==1.15.0
SQLAlchemy==1.4.11
visitor==0.1.3
Werkzeug==0.16.0
WTForms==2.3.3

## License info
[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
- Copyright 2021 © Pitch Application