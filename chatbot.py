from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
model_name = "facebook/blenderbot-400M-distill"

# Load model (download on first run and reference local installation for consequent runs)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Create the conversation history
conversation_history = []

while True:

    # Transform history to string
    history_string = "\n".join(conversation_history)

    # Fetching user's prompt
    input_text = input("> ")

    # Tokenizing user's prompt for the model
    inputs = tokenizer.encode_plus(history_string, input_text, return_tensors="pt")
    #print(inputs)
    #tokenizer.pretrained_vocab_files_map

    # Generating output from the model
    outputs = model.generate(**inputs)
    print(outputs)

    # Decoding the output -> Convert into words
    response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

    # Show response
    print(response)

    # Update conversation history
    conversation_history.append(input_text)
    conversation_history.append(response)
    print(conversation_history)