
# Prototype ML  

**Machine Learning For Everyone**
Django app to expose interface of scikit-learn through API

## Features

 - Independent login for users
 - Dashboard for users
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
  
https://github.com/PyMySQL/mysqlclient-python  
  
Install MongoDB  
  
https://www.digitalocean.com/community/tutorials/how-to-install-mongodb-on-ubuntu-16-04  
  
Create virtual environment and run locally  
  
```  
python -m venv myenv  
source myenv/bin/activate  
  
cd ml_webapp  
  
pip install --upgrade pip  
pip install -r requirements.txt  
  
python manage.py makemigrations  
python manage.py migrate  
python manage.py runserver  
```  

## Screens

### Home Page
![Home Page](http://ramansah.com/img/screen1.png)

### Model Page
![Linear Regression](http://ramansah.com/img/screen2.png)

### Dashboard
![Dashboard](http://ramansah.com/img/screen3.png)  

### Issues in production  
  
http://stackoverflow.com/questions/16823388/using-scipy-in-django-with-apache-and-mod-wsgi