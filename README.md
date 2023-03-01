# NVMP-Capstone-Project
I was the one doing the login function using Jquery and login API using RESTful Web API

This is a group project, the following are done by me:
1.  server side validatior.py
    
    This is to check for a valid JWT token and role, if there is an invalid JWT token or incorrect role, access will be denied.
    
2.  login.html and register.html
    
    At the login page, once logged in you will be redirected to the landing page.
    
    At the register page, enter a email and password, once submitted the SQL database will be updated with the login credentials, this then will redirect you
    to the login page.
    
3.  server side settings.py
    
    This contains the secret key for the JWT token
  
4.  server side app.py
    
    The follow app routes are done by me :
    
    /register - to post new user email and password into the SQL database
    
    /users/login - for user to login
    
5.  server side user.py
    
    login class - if user email and password match, return the JWT token
    
    insertuser class - insert user email and password into SQL database 
