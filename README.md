# Galleria


## By **[mburuBeatrice](https://github.com/mburuBeatrice)**

## Description
This is application that you display your photos for others to see.

## User Stories
As a user of the application I should be able to:
* View different photos that interest me.
* Click on a single photo to expand it and also view the details of the photo.
* Search for different categories of photos. (ie. people,transport)
*Copy a link to the photo to share with my friends.
* View photos based on the location they were taken.

## Setup/Installation Requirements

### Prerequisites
* Python 3.6.3
* Virtual environment
* Postgres Database
* Internet Connection


### Installation Process
1. Copy repolink
2. Run `git clone REPO-URL` in your terminal
3. Write `cd galleria`
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
CREATE DATABASE pixwall
```
9. Change the database informatioin in `car/settings.py`
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'galleria',
        'USER': *POSTGRES_USERNAME*,
        'PASSWORD': *POSTGRES_USERNAME*,
    }
}
```
10. Run `./manage.py runserver` or `python3.6 manage.py runserver` to run the application

## Support and Contacts

In case You have any issues using this code please do no hesitate to get in touch with me through mburubeatricewanjiru@gmail.com or leave a commit here on github.

## Known Bugs

 No known bugs

## Technologies Used
- Python 3.6.3
- Django 1.11
- Postgres Database
- UI kit
- Heroku

### License
### MIT License.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.*

Copyright (c) 2017 Beatrice Mburu
