import cv2

from src.vibro_bracelet.vibrations_generator import generate_vibration, init as braces_init

# Sync method for initializing the MI Band
# Recommend to start before any activities
# Sometimes too long
braces_connected = braces_init()
##

from src.headphones.voice_synthesizer import play_sound

path_to_dir_with_sounds = './resources/sounds/'

# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture("resources/response.mp4")

# Check if camera opened successfully
if not cap.isOpened():
    print("Error opening video stream or file")

with open("resources/scenario.txt", 'rb') as f:
    scenario = f.readlines()

i = 0


# Read until video is completed
while cap.isOpened():

    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret:

        # Display the resulting frame
        cv2.imshow('Frame', frame)

        # Press Q on keyboard to  exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            play_sound(path_to_dir=path_to_dir_with_sounds,
                       sound_name="sign_twenty_meters.mp3")
            generate_vibration(2)

        i = i + 1

        event = (0, None, None)
        # TODO uncomment when write a script scenario
        # event = scenario[i]

        if not event[1] is None:
            generate_vibration(event[1])

        if not event[2] is None:
            play_sound(path_to_dir=path_to_dir_with_sounds,
                       sound_name=event[2])

    # Break the loop
    else:
        break

# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()
