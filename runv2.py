import pygame
from pynput import keyboard
from sound_list import sounds

# Initialize pygame mixer
pygame.mixer.init()

# Dictionary to keep track of currently playing sounds
playing_sounds = {}

# Function to play sound
def play_sound(key):
    try:
        sound = pygame.mixer.Sound(sounds[key])
        playing_sounds[key] = sound
        sound.play(loops=-1)  # Loop indefinitely
    except KeyError:
        print(f"No sound mapped to key: {key}")
    except Exception as e:
        print(f"Error playing sound: {e}")

# Function to stop sound
def stop_sound(key):
    if key in playing_sounds:
        playing_sounds[key].stop()
        del playing_sounds[key]

# Function to handle key press
def on_press(key):
    try:
        # Convert key to char and play corresponding sound
        char = key.char
        if char and char not in playing_sounds:
            play_sound(char)
    except AttributeError:
        # Special keys (like shift) do not have 'char' attribute
        pass

# Function to handle key release
def on_release(key):
    try:
        # Convert key to char and stop corresponding sound
        char = key.char
        if char:
            stop_sound(char)
    except AttributeError:
        # Special keys (like shift) do not have 'char' attribute
        pass
    # Stop listener if ESC key is pressed
    if key == keyboard.Key.esc:
        return False

# Start listening to keyboard inputs
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("Press keys to play sounds. Press ESC to exit.")
    listener.join()
