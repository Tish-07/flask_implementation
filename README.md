# flask_implementation
Very basic service model using flask restplus

# <PROJ NAME>
#### Required python version
```sh
$ python --version
Python 3.5.5
```

### Tech
* Flask-RESTPlus

### Steps to setup
Clone repo ...

```sh
$ git clone https://<your-user-id>@bitbucket.org/<proj_name>.git
```

##### Go to folder and remove the .git/ folder

```sh
$ cd <proj_name>
$ rm -r .git/
```

##### Create new virtual env using anaconda
```sh
$ conda create --name <proj_name35> python=3.5
```

##### Activate virtual env
```sh
$ source activate <proj_name35>
```

##### Install libraries

```sh
$ pip install -r requirements.txt
```
##### Run the REST api in local with debug level
```sh
$ python app_server.py --debug
```
##### Run API in production mode
```sh
$ gunicorn --bind 0.0.0.0:5000 wsgi:application -w 1
```

