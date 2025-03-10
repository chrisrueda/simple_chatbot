# simple_chatbot
To create a new Python file, Click on File Explorer, then right-click in the explorer area and select New File. Name this new file chatbot.py.
## Connect github repository
Step 1. Create a Github repo.

Step 2: Terminal:
```
git config --global user.email "email@example.com"
git config --global user.name "Your Github User Name"
git remote set-url origin https://christianrueda:GENERATED_TOKEN@github.com/chrisrueda/REPOSITORY_NAME.git
```
## Create chatbot directory
Step 1: Installing requirements

Follow these steps to create a Python virtual environment and install the necessary libraries. Open a new terminal first.
Set up your virtual environment:

    pip3 install virtualenv 
    virtualenv my_env # create a virtual environment my_env
    source my_env/bin/activate # activate my_env

For this example, you will be using the transformers library, which is an open-source natural language processing (NLP) toolkit with many useful features, and also let's install a torch library.

    python3 -m pip install transformers==4.30.2 torch

Wait a few minutes to install the packages.

## Create the back-end server with Flask
Step 1: Install Flask
```
python3.11 -m pip install flask
python3.11 -m pip install flask_cors
```
Step 2: Setting the enviroment. Create a script called app.py
```
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
```
Step 3: Execute the python file
`python3.11 app.py`

Step 4: Check the server at localhost:5000
