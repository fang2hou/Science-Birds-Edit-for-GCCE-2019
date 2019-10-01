import requests
import json
import random

templates = {
    "animal": [
        "Wow, you just drawed a %word%, it is so cool.",
        "The %word% is so cute, nice job!",
    ],
    "fruit": [
        "It looks like %word%, I can't wait to eat this!",
    ],
    "things": [
        "You just drawed a %word%, I guess it is very important for you, right?",
    ]
}

def get_type(word):
    api_key = "your-api"
    api_url = "https://dictionaryapi.com/api/v3/references/collegiate/json/"
    response = requests.get(url=api_url+word, params={"key": api_key})
    word_details = json.loads(response.text)
    functional_label = word_details[0]['fl']

    if functional_label == "noun" and "mammal" in response.text:
        return "animal"
    else:
        return None


def generate_sentences(predicted_type, word):
    if predicted_type == None:
        predicted_type = "things"

    if templates[predicted_type]:
        selected_template = random.choice(templates[predicted_type])
        output = selected_template.replace("%word%", word)
        return output


if __name__ == "__main__":
    READER_DIRECTORY = "tmp/"
    filename = "results.txt"
    word = "cat"
    with open(READER_DIRECTORY+filename, 'r') as output_file:
        word = output_file.readline()
    
    pred = generate_sentences(get_type(word), word)

    with open("site/predict.html", 'w') as output_file:
        output_file.write(pred)

    print(pred)
    
