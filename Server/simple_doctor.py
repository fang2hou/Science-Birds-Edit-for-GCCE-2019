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
    ],
    "none": [
        "(O_O)? Oops, I could not recognizing your drawing, sorry i will continue to learn and grow."
    ]
}

def get_type(word):
    pass


def get_type_with_api(word):
    if word == "none":
        return "none"
    
    api_key = "your-api"
    api_url = "https://dictionaryapi.com/api/v3/references/collegiate/json/"
    response = requests.get(url=api_url+word, params={"key": api_key})
    word_details = json.loads(response.text)
    functional_label = word_details[0]['fl']

    if functional_label == "noun" and "mammal" in response.text:
        return "animal"
    else:
        return None


def generate_sentences(word, useDictionaryAPI):
    if useDictionaryAPI:
        predicted_type = get_type_with_api(word)
    else:
        predicted_type = get_type(word)

    if predicted_type == None:
        predicted_type = "things"

    if templates[predicted_type]:
        selected_template = random.choice(templates[predicted_type])
        output = selected_template.replace("%word%", word)
        return output


if __name__ == "__main__":
    word = 'cat'
    print(generate_sentences(word))