from gtts import gTTS


def synthesize(text):
    tts = gTTS(text=text, lang='en')
    path_to_save_sound_track = "./resources/sounds/{}.mp3".format(text.replace(' ', '_').replace('!', ''))
    tts.save(path_to_save_sound_track)
    return path_to_save_sound_track
