# Botify Coding Test Software Engineer

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/MaxTobelem/botifyCodingTest
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python -m venv env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ cd botifyCodingTest
(env)$ pip install -r requirements.txt
```

Once `pip` has finished downloading the dependencies:
```sh
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/api/town`.

You will be asked for credentials, use these :
```sh
username : mtobelem
password : password
```

## Tests

To run the tests, `cd` into the directory where `manage.py` is:
```sh
(env)$ python manage.py test 
```