import pygame
from pynput import keyboard
from sound_list import sounds

# Initialize pygame mixer
pygame.mixer.init()

# Set to track pressed keys
pressed_keys = set()

# Function to play sound
def play_sound(key):
    try:
        sound = pygame.mixer.Sound(sounds[key])
        sound.play()
    except KeyError:
        print(f"No sound mapped to key: {key}")
    except Exception as e:
        print(f"Error playing sound: {e}")

# Function to handle key press
def on_press(key):
    try:
        # If key is not already in the pressed_keys set, play the sound
        if key.char not in pressed_keys:
            pressed_keys.add(key.char)
            play_sound(key.char)
    except AttributeError:
        # Special keys (like shift) do not have 'char' attribute
        pass

# Function to handle key release
def on_release(key):
    try:
        # Remove the key from the pressed_keys set when released
        if key.char in pressed_keys:
            pressed_keys.remove(key.char)
    except AttributeError:
        pass
    if key == keyboard.Key.esc:
        return False

# Start listening to keyboard inputs
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("Press keys to play sounds. Press ESC to exit.")
    listener.join()
