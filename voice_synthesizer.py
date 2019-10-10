from gtts import gTTS


def read_scenario():
    with open("resources/scenario.csv", 'r') as f:
        scenario = f.readlines()

    scenario = map(lambda x: x.replace('\n', '').split(','), scenario)
    scenario = map(lambda x: x[1], scenario)

    return list(scenario)


def synthesize(text):
    tts = gTTS(text=text, lang='en')
    path_to_save_sound_track = "./resources/sounds/{}.mp3".format(text.replace(' ', '_').replace('!', ''))
    tts.save(path_to_save_sound_track)
    return path_to_save_sound_track


texts = read_scenario()
for text in texts:
    synthesize(text)
