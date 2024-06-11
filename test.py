import pygame
from pynput import keyboard
import os

# Define a dictionary mapping keys to sound file paths
sounds = {
  '1': 'sounds/1Do.mp3',
  '2': 'sounds/1Re_b.mp3',
  '3': 'sounds/1Re.mp3',
  '4': 'sounds/1Mi_b.mp3',
  '5': 'sounds/1Mi.mp3',
  '6': 'sounds/1Fa.mp3',
  '7': 'sounds/1Sol_b.mp3',
  '8': 'sounds/1Sol.mp3',
  '9': 'sounds/1La_b.mp3',
  '0': 'sounds/1La.mp3',
  'q': 'sounds/1Si_b.mp3',
  'w': 'sounds/1Si.mp3',
  'e': 'sounds/2Do.mp3',
  'r': 'sounds/2Re_b.mp3',
  't': 'sounds/2Re.mp3',
  'y': 'sounds/2Mi_b.mp3',
  'u': 'sounds/2Mi.mp3',
  'i': 'sounds/2Fa.mp3',
  'o': 'sounds/2Sol_b.mp3',
  'p': 'sounds/2Sol.mp3',
  'a': 'sounds/2La_b.mp3',
  's': 'sounds/2La.mp3',
  'd': 'sounds/2Si_b.mp3',
  'f': 'sounds/2Si.mp3',
  'g': 'sounds/3Do.mp3',
  'h': 'sounds/3Re_b.mp3',
  'j': 'sounds/3Re.mp3',
  'k': 'sounds/3Mi_b.mp3',
  'l': 'sounds/3Mi.mp3',
  'z': 'sounds/3Fa.mp3',
  'x': 'sounds/3Sol_b.mp3',
  'c': 'sounds/3Sol.mp3',
  'v': 'sounds/3La_b.mp3',
  'b': 'sounds/3La.mp3',
  'n': 'sounds/3Si_b.mp3',
  'm': 'sounds/3Si.mp3',
  'Q': 'sounds/4Do.mp3',
  'W': 'sounds/4Re_b.mp3',
  'E': 'sounds/4Re.mp3',
  'R': 'sounds/4Mi_b.mp3',
  'T': 'sounds/4Mi.mp3',
  'Y': 'sounds/4Fa.mp3',
  'U': 'sounds/4Sol_b.mp3',
  'I': 'sounds/4Sol.mp3',
  'O': 'sounds/4La_b.mp3',
  'P': 'sounds/4La.mp3',
  'A': 'sounds/4Si_b.mp3',
  'S': 'sounds/4Si.mp3',
  'D': 'sounds/5Do.mp3',
  'F': 'sounds/5Re_b.mp3',
  'G': 'sounds/5Re.mp3',
  'H': 'sounds/5Mi_b.mp3',
  'J': 'sounds/5Mi.mp3',
  'K': 'sounds/5Fa.mp3',
  'L': 'sounds/5Sol_b.mp3',
  'Z': 'sounds/5Sol.mp3',
  'X': 'sounds/5La_b.mp3',
  'C': 'sounds/5La.mp3',
  'V': 'sounds/5Si_b.mp3',
  'B': 'sounds/5Si.mp3',
  'N': 'sounds/6Do.mp3',
}


# Initialize pygame mixer
pygame.mixer.init()

# Set to track pressed keys
pressed_keys = set()

# Function to play sound
def play_sound(key):
    try:
        sound_path = sounds[key]
        if os.path.exists(sound_path):
            sound = pygame.mixer.Sound(sound_path)
            sound.play()
        else:
            print(f"Sound file not found: {sound_path}")
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
