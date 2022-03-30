import json
def write_json():
    screen_from_file = 1
    pos_from_file = 3000
    form_width = 215
    form_height = 100
    pic_width = 200
    pic_height = 80
    timer = 500
    data = {
        "animation_on_screen": {
            "screen_from_file": screen_from_file,
            "pos_from_file": pos_from_file,
            "form_width": form_width,
            "form_height": form_height,
            "pic_width": pic_width,
            "pic_height": pic_height,
            "timer": timer
        }
    }
    with open("settings.json", "w") as write_file:
        json.dump(data, write_file)

def load_settings():
    # Opening JSON file
    f = open('settings.json')
    # returns JSON object as
    # a dictionary
    data = json.load(f)

    # Iterating through the json
    # list
    print(data['animation_on_screen']['screen_from_file'])


    # Closing file
    f.close()

load_settings()