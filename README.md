# Currency Convertor

This is the Readme for Paul Hadchiti and Sean Minson's currency converter. This app allows users to convert any amount of one currency into the correct amount in a different currency. The conversion rates are based on real-time currency rate data for over 150 different currencies. 

# Accessing the converter on the website: 
Go to the link below to access the app
```sh
https://currency-server-123.herokuapp.com/
```
# On the App
Once on the app there is a welcome page. In the top right corner of the welcome page is a button which provides options to 3 other pages. The about page has a description of the app. The options page has a list of all the currencies in the world and their corresponding symbols. The symbols of the selected currency can be inputted in the currency form page. 

# Currency Form Page
The currency form page allows the user to input symbols for the base currency and what currency you want to convert to as well as the amount you want converted. After pressing the submit button, a results page will appear showing how much of the base currency is in the new currency. 

# Code Climate Results
Our code climate results for code simplification grading is linked below. Code Climate awarded us with an A, having no smells or duplications
https://codeclimate.com/github/pah73/currency-converter

# Deploying the app and setting up the app and repository 

# Prerequisites:
```sh
Anaconda 3.7+
Python 3.7+
Pip
```

# Instalation 
Fork this remote repository under your own control, then clone remote copy onto your local computer using the GitHub desktop app.

Navigate to the repository from the command line (subsequent commands assume you are running them from the local repository's root directory). If you saved the repository to your desktop use the following code or else you will have to adjust the code to wherever the repository is saved:

```sh
cd ~/Desktop/currency-converter
```

# Create and activate virtual enviorment
Use Anaconda to create and activate a new virtual environment, perhaps called "currency-env":

```sh
conda create -n currency-env python=3.8
conda activate currency-env
```
From inside the virtual environment, install package dependencies. The requirmemnts.txt file has the Dotenv package which is needed to load enviorment variables as well as the requests package which is nrequest data from the internet:

```sh
pip install -r requirements.txt
```

# Setup local variables
In the root directory of your local repository, create a new file called ".env". The program needs an API key to issue requests to Fixer.io API. Follow this link and the instructions to get a free API key: https://fixer.io/ and create a variable called CURRENCY_API_KEY in the .env file with your API key. Also add a variable call APP_ENV and set it in production mode:

```sh
CURRENCY_API_KEY=" Your API Key"
APP_ENV="production"
```

# Running the app locally
To run the app locally, enter the following code into the command-line
```sh
FLASK_APP=web_app flask run
```
After running this a url will appear bringing you to the app.

# Testing
In order to run tests on the program enter the following.
```sh
python -m pytest
```

# Deploying to Production
After demonstrating the ability to run the app locally we can deploy the source code to heroku. You can use the online Heroku Dashboard or the command line to create an application server.
Please reference instructions here: 

https://devcenter.heroku.com/articles/getting-started-with-python
https://devcenter.heroku.com/articles/python-gunicorn

You can alternitively use the command line to create a unique username:

```sh
heroku create unique-username
```

To verify the app has ben created:
```sh
heroku apps
```
To verify the local repo is associated with Heroku:
```sh
git remote -v
```

To deploy to the Heroku Server:
```sh
git push heroku main
```

You are now all set to run your app on heroku.