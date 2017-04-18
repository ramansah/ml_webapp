## Latest Version hosted here
http://ml4everyone.com

## Install & Develop

```
git clone https://github.com/ramansah/ml_webapp.git

sudo apt-get install mysql-server
mysql -uroot -p
create schema ml_webapp;
exit

nano ~/mysql.cnf
[client]
database = ml_webapp
user = root
password = ****
default-character-set = utf8
```

### Install mysqlclient-python

https://github.com/PyMySQL/mysqlclient-python

### Install MongoDB

https://www.digitalocean.com/community/tutorials/how-to-install-mongodb-on-ubuntu-16-04

### Create virtual environment and test locally

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

### Issues in production

http://stackoverflow.com/questions/16823388/using-scipy-in-django-with-apache-and-mod-wsgi
