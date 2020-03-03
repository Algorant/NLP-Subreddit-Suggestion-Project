- Create an environment and pip install the libraries in requirements.txt

- To get access to REDDIT API, you need to complete the following fields.
Make a file named ".env" and paste this:

reddit_api_key = ''
reddit_api_secret = ''
app_name = ''
user_name = ''
login_password = ''

- Fill out each '' with the information in your developer application which can be found here:

https://old.reddit.com/prefs/apps/

(Give Brandon your reddit username to be added to an existing developer app or use your own.
If you make your own, be sure to select Script and make the redirect uri "http://localhost:8080")

-In your terminal, run FLASK_APP=app.py Flask run

Useful PRAW documentation: https://praw.readthedocs.io/en/latest/index.html
