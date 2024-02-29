# Basic Web App using Flask

### Objective

Create a basic user authentication app using Flask.  The website allows users to create accounts, log into their account, utilize a basic note app once logged in.  The back-end is built with Python and Flask framework.  The front-end uses HTML and CSS bootstrapping.  This little project taught me basic concepts in web development:front-end-back-end, databases, integrations, HTML templates.

### Files
`main.py` creates the web application and running the file runs the webpage.

##### Websites
`__init__.py` provides functions that create the web application and create back-end databases.
`views.py` contains Blueprint objects that creates website routes.
`auth.py` that contains login, logout, and sign up functions.
`models.py` set up backend database models to store user data

##### Templates
`base.html` provides basic HTML structure that other pages can over-ride
`sign_up.html` provides HTML structure for the sign-up page
`login.html` provides HTML structure for login page
`home.html` provides HTML structure for home page

##### Statics
`index.js` update the home page when user deletes a note

### Accessing Website

Link: http://127.0.0.1:5000



