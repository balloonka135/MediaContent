#MediaContent

##This is a media content feed project created with Django.

##Description
It allows you to upload photos and videos, and then view them on the feed page 'Home'.
Users can upload content from local machine or share it by Instagram post URL.

##User has 2 roles:
1. Viewer
2. Authenticated user

Viewer can review the content feed and the detailed page of the media content.
Authenticated user can upload new content, share it from Instagram, edit and delete posts.
In order to authenticate, users must create their account with 'Sign Up' or 'Log in', if the account already exists.

##Cloud server
Check this out on the cloud server [PythonAnywhere](<link>)

##To run locally:

Clone git repository
```git clone <link>```

Create virtualenv inside of the project and activate it
```
virtualenv --python=python3.6 venv
sourve venv/bin/activate
```

Run the requirements.txt to install python packages
```pip install -r requirements.txt```

Run the local server
```python manage.py runserver```



