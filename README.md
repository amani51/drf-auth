# LAB - Class 28

## Project: Games API

### Author: Amani M AL-Zoubi

### Links and Resources
- [Django REST framework](https://www.django-rest-framework.org/)
- [JWT Debugger](https://jwt.io/)


### Setup
- use python version 3.10.7

#### `.env` requirements (where applicable)
- For this lab I did not use .env 

#### How to initialize/run your application (where applicable)
- I used docker , so you need to run it from docker container
    `docker-compose up` to run it from your machine 
- Use `http://127.0.0.1:8000/api/v1/games/` to get Games API 
- you need to sign in, I create four users:
    1. admin: username: Amani , password:amani
    2. staff : username: Eslam, password:eslam12345
    3. normal users : 
        1. username:Eman , password:eman12345
        2. username: Esraa, password: esraa12345
- for specific Game add it's id to your path like `http://127.0.0.1:8000/api/v1/games/1`


#### How to use your library (where applicable)
- I used Django Rest framework , psycopg2 ,whitenoise, simplejwt ; docker will install them automatically 


#### Tests
##### Use Postman : Steps to manually test 
- By using UserName and Password
    - Use `http://127.0.0.1:8000/api/v1/games/` with `post` method from ` Authorization` select type: Basic auth -> put username and password 
- By using access token and refresh token :
    - Use `http://127.0.0.1:8000/api/token/` with `post` method from ` Authorization` select type: Bearer auth and inside body put UserName and password using JSON format for example: 
    ```JSON
           {
    "username":"Amani",
    "password":"amani"
    }
    ```
    you will get response of encoded access token and refresh token as JSON format for example:
    ```JSON
           {
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3MTQ4MTkwNiwiaWF0IjoxNjcxMzk1NTA2LCJqdGkiOiJkZjY3ZmFkM2E4YTg0ZWJmOWFlNWRlZTJlMmZlN2ZjYyIsInVzZXJfaWQiOjF9.1L8Csdw9Id0fXg8Y0liLRZ5fCMhlE2yPy1um1Q5K_i4",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcxMzk1ODA2LCJpYXQiOjE2NzEzOTU1MDYsImp0aSI6ImNiYjljYzg0OGQ1ZTQzZDlhYTlmMDBkZTAwYjk3Zjk0IiwidXNlcl9pZCI6MX0.sAQ-FpHGkLIeaVoBJfn-Dbmw3RTzSRhCuoVOr8xgvYU"
    }
    ```
    - Note that access token expires after 5 mins and refresh token expires after 24 hours
- get a new access token :
    - Use `http://127.0.0.1:8000/api/token/refresh/` with `post` method from ` Authorization` select type: Bearer auth and inside body put refresh token using JSON format for example: 
    ```JSON
        "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3MTQ4MTkwNiwiaWF0IjoxNjcxMzk1NTA2LCJqdGkiOiJkZjY3ZmFkM2E4YTg0ZWJmOWFlNWRlZTJlMmZlN2ZjYyIsInVzZXJfaWQiOjF9.1L8Csdw9Id0fXg8Y0liLRZ5fCMhlE2yPy1um1Q5K_i4"
    ```
    - you will get a new access token as response for example:
    ```JSON
        "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcxMzk2MzczLCJpYXQiOjE2NzEzOTU1MDYsImp0aSI6IjcyODQ1NjY0YzEwNTRjOGI5YTY0YjMxODdmZmRmNzE0IiwidXNlcl9pZCI6MX0.CFDFlyFbE9AvUsxTbAvdK6TNV5S8GB2_0LDNQpogBCE"
    ```

#### Pull Requests
- [PULL REQUEST LINK](https://github.com/amani51/drf-api-permissions-postgres/pull/1)