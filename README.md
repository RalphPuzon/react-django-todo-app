# Simple Todo React-Django ToDo App
*NOTE: This is NOT a production grade script, so please do not utilize for projects that contain sensitive information.*

This is a working example of Digital Ocean's todo app that utilizes react.js and django. React will handle the UI, as well as the getting and setting of data via requests, while django serves the backend API via the django rest framework.  Django is using the defaulted sqlite3 database.

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## How to use:
1. inside the top level directory, run the backend server via command line:
    > python manage.py runserver

2. inside the frontend directory, run the react server via command line (in this example we will be using yarn for simplicity):
    > yarn start

3. Visit http://localhost:3000 to see the running app. 
