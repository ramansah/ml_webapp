
# Prototype ML  

**Machine Learning For Everyone**

Django app to expose interface of scikit-learn through API

## Features

- Independent login for users
- Dashboard for users to manage models
- Train and save models through API
- Run predictions through API

## Installation  

``` bash  
git clone https://github.com/ramansah/ml_webapp.git  
```

Configure credentials for MySQL client at `~/mysql.cnf`  

``` bash  
[client]  
database = ml_webapp  
user = username  
password = ****  
default-character-set = utf8  
```

Install mysqlclient-python  
  
<https://github.com/PyMySQL/mysqlclient-python>
  
Install MongoDB
  
<https://www.digitalocean.com/community/tutorials/how-to-install-mongodb-on-ubuntu-16-04>  
  
Create virtual environment and run locally  

``` bash
python -m venv myenv  
source myenv/bin/activate  
  
cd ml_webapp  
  
pip install --upgrade pip  
pip install -r requirements.txt  
  
python manage.py makemigrations  
python manage.py migrate  
python manage.py runserver  
```  

## Usage

Visit <http://localhost:8000> and register a new user

Browse <http://localhost:8000/models/linear_regression/> to see the API for Linear Regressor

Fetch the JWT for current user

``` bash
POST /api/login/
Content-Type: application/json
{
  "username": "username",
  "password": "password"
}

Response
{
  "token": "abcd12345"
}
```

Create a model and save in the DB

Consider the following problem statement

> You are a Physics student who appeared for the final exams and impatient to know your final score. But the teacher who grades you is insanely strict. He has a formula to calculate total score but no one knows it (which is 0.5 * Paper_1 + 2 * Paper_2 + Paper_3). You have a list of your friends' exam scores along with final score and want to calculate yours.

``` bash
POST /api/linear_regression/
Content-Type: application/json
Accept: application/json
Authorization: JWT abcd12345

{
  "action": "new_model",
  "name": "Compute Final Score",
  "input_x": [[95, 87, 69], [99, 48, 54], [85, 57, 98], [90, 95, 91]],
  "input_y": [291, 200, 254, 326]
}

Response
{
  "status": "Trained",
  "model_id": "randommodelid"
}
```

Use this model to predict your score

``` bash
POST /api/linear_regression/
Content-Type: application/json
Accept: application/json
Authorization: JWT abcd12345

{
  "action": "predict",
  "model_id": "randommodelid",
  "input_x": [[90, 95, 91]]
}

Response
{
  "status": "OK",
  "prediction": [
      326
  ]
}
```

Check out your trained models at Dashboard

![Dashboard](http://ramansah.com/img/screen3.png)  

### Issues in production  
  
<http://stackoverflow.com/questions/16823388/using-scipy-in-django-with-apache-and-mod-wsgi>