
# Prototype ML  

**Machine Learning For Everyone**

Django app to expose interface of scikit-learn through API

> Update : Refactored code to dynamically fetch model classes mentioned by the user in API. Theoretically, all models in scikit learn can be tested now. 

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

Consider the 

``` bash
POST /api/model/
Content-Type: application/json
Accept: application/json
Authorization: JWT abcd12345

{
  "model_path": "sklearn.linear_model.LinearRegression",
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
POST /api/model/
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
