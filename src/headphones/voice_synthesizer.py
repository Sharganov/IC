import os
import time
import vlc
import threading


def play_sound(path_to_dir, sound_name):
    play_thread = threading.Thread(target=generate_voice, args=(path_to_dir, sound_name))
    play_thread.start()
    play_thread.join()


def generate_voice(path_to_dir, sound_name):
    p = vlc.MediaPlayer(os.path.join(path_to_dir, sound_name))
    p.play()
    duration = p.get_length() / 1000
    time.sleep(duration)
