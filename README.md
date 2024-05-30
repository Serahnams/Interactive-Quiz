# Interactive Quiz Application

This is an interactive quiz application built with Flask, a lightweight WSGI web application framework in Python. The application allows users to register, log in, and take quizzes. The project is structured to be scalable and easy to maintain.

## Table of Contents

- [Project Structure](#project-structure)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Structure

The project directory structure is as follows:

Interactive-Quiz/
│
├── app/
│ ├── init.py
│ ├── models.py
│ ├── routes.py
│ ├── templates/
│ │ ├── base.html
│ │ ├── home.html
│ │ ├── login.html
│ │ └── register.html
│ └── static/
│ ├── css/
│ │ └── style.css
│ └── js/
│ └── script.js
├── venv/
├── migrations/
├── .flaskenv
├── config.py
├── run.py
└── README.md


## Features

- User Registration
- User Login and Authentication
- Taking Quizzes
- Flash Messages for Feedback
- Database Migration Support with Flask-Migrate

## Requirements

- Python 3.9 or higher
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-Bcrypt
- Flask-Login

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your_username/Interactive-Quiz.git
   cd Interactive-Quiz
   
Set up a virtual environment:
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`

Install dependencies:
pip install -r requirements.txt

Set up the database:
flask db init
flask db migrate -m "Initial migration."
flask db upgrade

Set environment variables:
Create a .flaskenv file in the root directory with the following content:

FLASK_APP=run.py
FLASK_ENV=development

Usage
Run the application:

flask run
The application will be accessible at http://127.0.0.1:5000.

Access the application in your web browser:
Open http://127.0.0.1:5000 in your web browser.

Contributing
Fork the repository
Create a new branch for your feature or bug fix:

git checkout -b feature-name
Commit your changes:

git commit -m "Description of your changes"
Push to the branch:

git push origin feature-name
Create a pull request
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
If you have any questions or suggestions, feel free to contact us at [serahnams@gmail.com].






