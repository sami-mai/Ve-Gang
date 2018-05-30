# Ve-Gang
### A web application that lists sources of vegan, vegetarian and healthy food. Access is free to users, who can also provide content with restaurant listings and reviews.


## By **[Samirah Maison](https://github.com/sami-mai)**

## Description
[This](https://avegang.herokuapp.com/) is a web application that lists sources of vegan, vegetarian and healthy food. Access is free to users, who can also provide content with restaurant listings and reviews. Built using Django 1.11.

## User Stories
* Sign in with the application to start using.
* Set up a profile
*
*
*
*
*


## Setup/Installation Requirements

### Prerequisites
* Python 3.6.2
* Virtual environment
* Postgres Database
* Internet


### Installation Process
1. Copy repolink
2. Run `git clone REPO-URL` in your terminal
3. Write `cd vegang`
4. Create a virtual environment with `virtualenv virtual` or try `python3.6 -m venv virtual`
5. Create .env file `touch .env` and add the following:
```
SECRET_KEY=<your secret key>
DEBUG=True
```
6. Enter your virtual environment `source virtual/bin/activate`
7. Run `pip install -r requirements.txt` or `pip3 install -r requirements.txt`
8. Create Postgres Database

```
psql
CREATE DATABASE gram
```
9. Change the database information in `instaProject/settings.py`
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'vegang',
        'USER': *POSTGRES_USERNAME*,
        'PASSWORD': *POSTGRES_USERNAME*,
    }
}
```
10. Run `./manage.py runserver` or `python3.6 manage.py runserver` to run the application


## Known Bugs

No known bugs


## Technologies Used
- Python3.6
- Django
- Bootstrap
- Postgres Database
- CSS
- HTML
- Heroku

### License
This project is licensed under the MIT License - see the LICENSE.md file for details
MIT (c) 2018 **[Samirah Maison](https://github.com/sami-mai)**

## Acknowledgements
* Moringa School
