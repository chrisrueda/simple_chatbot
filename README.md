# simple_chatbot
Step 1: Installing requirements

Follow these steps to create a Python virtual environment and install the necessary libraries. Open a new terminal first.
Set up your virtual environment:

    pip3 install virtualenv 
    virtualenv my_env # create a virtual environment my_env
    source my_env/bin/activate # activate my_env

For this example, you will be using the transformers library, which is an open-source natural language processing (NLP) toolkit with many useful features, and also let's install a torch library.

    python3 -m pip install transformers==4.30.2 torch

Wait a few minutes to install the packages.
To create a new Python file, Click on File Explorer, then right-click in the explorer area and select New File. Name this new file chatbot.py.
