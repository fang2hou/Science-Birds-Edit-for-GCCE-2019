import requests
import json
import random

templates = {
    'animal': [
        'Wow, you just drawed a #word#, it is so cool.',
        'The #word# is so cute, nice job!',
    ],
    'food': [
        'It looks like #word#, I can\'t wait to eat this!',
        'Oh, #word# is my favorite food! I can\'t wait to eat this!',
    ],
    'thing': [
        'You just drawed the #word#, I guess it is very important for you, right?',
    ],
    'sports': [
        'Hmm, it looks like #word#, I guess you are a sports guy!'
    ],
    'none': [
        '(O_O)? Oops, I could not recognizing your drawing, sorry i will continue to learn and grow.'
    ]
}

types = {
    'animal': [
        'butterfly', 'cat', 'bird', 'snake', 'spider'
    ],
    'food': [
        'lollipop', 'ice_cream', 'donut', 'mushroom', 'bread', 'hot_dog', 'pizza', 'grapes', 'cookie'
    ],
    'thing': [
        'screwdriver', 'wristwatch', 'sword', 'table', 'coffee_cup', 'anvil', 'wheel', 'hammer', 'hat', 'paper_clip',
        'traffic_light', 'sun', 'helmet', 'bridge', 'alarm_clock', 'book', 'syringe', 'pants', 'radio' 'rainbow',
        'broom', 'fan', 'cloud', 'tent', 'clock', 'bicycle', 'umbrella', 'moon', 'cell_phone', 'chair', 'candle',
        'stop_sign', 'smiley_face', 'pillow', 'bed', 'saw', 'light_bulb', 'shovel', 'moustache', 'star', 'envelope',
        'door', 'face', 'tree', 'rifle', 'camera', 'lightning', 'flower', 'wheel', 'knife', 'diving_board', 'circle'
        'square', 'cup', 'mountain', 'apple', 'spoon', 'eyeglasses', 'headphones', 'scissors', 'drums', 'key', 'power_outlet',
        'pencil', 'line', 'ladder', 'triangle', 't-shirt', 'dumbbell', 'microphone', 'sock', 'suitcase', 'laptop', 'tooth'
        'frying_pan', 'bench', 'ceiling_fan', 'car', 'beard', 'axe', 'eye', 'airplane'
    ],
    'sports': [
        'basketball', 'baseball', 'shorts', 'tennis_racquet', 'baseball_bat'
    ],
}

def get_type(word):
    for (word_type, word_group) in types.items():
        if word in word_group:
            return word_type

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


def generate_sentences(word, useDictionaryAPI=False):
    if word == 'none':
        predicted_type = 'none'
    elif useDictionaryAPI:
        predicted_type = get_type_with_api(word)
    else:
        predicted_type = get_type(word)

    if predicted_type == None:
        predicted_type = "thing"

    # remove underline in the label
    word = word.replace('_', ' ')

    if templates[predicted_type]:
        selected_template = random.choice(templates[predicted_type])
        output = selected_template.replace("#word#", word)
        return output


if __name__ == "__main__":
    word = 'basketball'
    print(generate_sentences(word))