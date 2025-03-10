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

Step 5: Install the libraries into the server
```
python3.11 -m pip install transformers torch
```
Step 6: Implement the chatbot to the server code in the app.py file
```
from flask import Flask, request, render_template
from flask_cors import CORS
import json
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

app = Flask(__name__)
CORS(app)

model_name = "facebook/blenderbot-400M-distill"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
conversation_history = []

@app.route('/chatbot', methods=['POST'])
def handle_prompt():
    data = request.get_data(as_text=True)
    data = json.loads(data)
    input_text = data['prompt']

    # Create conversation history string
    history = "\n".join(conversation_history)

    # Tokenize the input text and history
    inputs = tokenizer.encode_plus(history, input_text, return_tensors="pt")

    # Generate the response from the model
    outputs = model.generate(**inputs, max_length= 60)  # max_length will cause the model to crash at some point as history grows

    # Decode the response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

    # Add interaction to conversation history
    conversation_history.append(input_text)
    conversation_history.append(response)

    return response

if __name__ == '__main__':
    app.run()
```
Step 7: Test the implementation using `curl`to make a POST to HOST:
`curl -X POST -H "Content-Type: application/json" -d '{"prompt": "Hello, how are you today?"}' 127.0.0.1:5000/chatbot`
The output shoud be: `I am doing very well today as well. I am glad to hear you are doing well.`

## Add webpage
Step 1: Install Requirements (LLM Folder)
```
python3.11 -m pip install -r LLM_application_chatbot/requirements.txt
```
Step 2: Move app.py file to this folder `mv app.py LLM/`

Step 3: Move to this folder: `cd LLM`

Step 4: Edit the app.py to redirect to the webpage:
```
from flask import Flask, request, render_template
from flask_cors import CORS
import json
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

app = Flask(__name__)
CORS(app)

model_name = "facebook/blenderbot-400M-distill"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
conversation_history = []

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/chatbot', methods=['POST'])
def handle_prompt():
    data = request.get_data(as_text=True)
    data = json.loads(data)
    print(data) # DEBUG
    input_text = data['prompt']
    
    # Create conversation history string
    history = "\n".join(conversation_history)

    # Tokenize the input text and history
    inputs = tokenizer.encode_plus(history, input_text, return_tensors="pt")

    # Generate the response from the model
    outputs = model.generate(**inputs)

    # Decode the response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

    # Add interaction to conversation history
    conversation_history.append(input_text)
    conversation_history.append(response)

    return response

if __name__ == '__main__':
    app.run()
```
Step 5: In the JS file, point to the project url in line 45:
`https://chsrueda-5000.theianext-0-labs-prod-misc-tools-us-east-0.proxy.cognitiveclass.ai/chatbot`

Step 6: Run flask
