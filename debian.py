import pygame
from pynput import keyboard
import os

# Define a dictionary mapping keys to sound file paths
sounds = {
  '1': '/home/mendel/piano/sounds/1Do.mp3',
  '2': '/home/mendel/piano/sounds/1Re_b.mp3',
  '3': '/home/mendel/piano/sounds/1Re.mp3',
  '4': '/home/mendel/piano/sounds/1Mi_b.mp3',
  '5': '/home/mendel/piano/sounds/1Mi.mp3',
  '6': '/home/mendel/piano/sounds/1Fa.mp3',
  '7': '/home/mendel/piano/sounds/1Sol_b.mp3',
  '8': '/home/mendel/piano/sounds/1Sol.mp3',
  '9': '/home/mendel/piano/sounds/1La_b.mp3',
  '0': '/home/mendel/piano/sounds/1La.mp3',
  'q': '/home/mendel/piano/sounds/1Si_b.mp3',
  'w': '/home/mendel/piano/sounds/1Si.mp3',
  'e': '/home/mendel/piano/sounds/2Do.mp3',
  'r': '/home/mendel/piano/sounds/2Re_b.mp3',
  't': '/home/mendel/piano/sounds/2Re.mp3',
  'y': '/home/mendel/piano/sounds/2Mi_b.mp3',
  'u': '/home/mendel/piano/sounds/2Mi.mp3',
  'i': '/home/mendel/piano/sounds/2Fa.mp3',
  'o': '/home/mendel/piano/sounds/2Sol_b.mp3',
  'p': '/home/mendel/piano/sounds/2Sol.mp3',
  'a': '/home/mendel/piano/sounds/2La_b.mp3',
  's': '/home/mendel/piano/sounds/2La.mp3',
  'd': '/home/mendel/piano/sounds/2Si_b.mp3',
  'f': '/home/mendel/piano/sounds/2Si.mp3',
  'g': '/home/mendel/piano/sounds/3Do.mp3',
  'h': '/home/mendel/piano/sounds/3Re_b.mp3',
  'j': '/home/mendel/piano/sounds/3Re.mp3',
  'k': '/home/mendel/piano/sounds/3Mi_b.mp3',
  'l': '/home/mendel/piano/sounds/3Mi.mp3',
  'z': '/home/mendel/piano/sounds/3Fa.mp3',
  'x': '/home/mendel/piano/sounds/3Sol_b.mp3',
  'c': '/home/mendel/piano/sounds/3Sol.mp3',
  'v': '/home/mendel/piano/sounds/3La_b.mp3',
  'b': '/home/mendel/piano/sounds/3La.mp3',
  'n': '/home/mendel/piano/sounds/3Si_b.mp3',
  'm': '/home/mendel/piano/sounds/3Si.mp3',
  'Q': '/home/mendel/piano/sounds/4Do.mp3',
  'W': '/home/mendel/piano/sounds/4Re_b.mp3',
  'E': '/home/mendel/piano/sounds/4Re.mp3',
  'R': '/home/mendel/piano/sounds/4Mi_b.mp3',
  'T': '/home/mendel/piano/sounds/4Mi.mp3',
  'Y': '/home/mendel/piano/sounds/4Fa.mp3',
  'U': '/home/mendel/piano/sounds/4Sol_b.mp3',
  'I': '/home/mendel/piano/sounds/4Sol.mp3',
  'O': '/home/mendel/piano/sounds/4La_b.mp3',
  'P': '/home/mendel/piano/sounds/4La.mp3',
  'A': '/home/mendel/piano/sounds/4Si_b.mp3',
  'S': '/home/mendel/piano/sounds/4Si.mp3',
  'D': '/home/mendel/piano/sounds/5Do.mp3',
  'F': '/home/mendel/piano/sounds/5Re_b.mp3',
  'G': '/home/mendel/piano/sounds/5Re.mp3',
  'H': '/home/mendel/piano/sounds/5Mi_b.mp3',
  'J': '/home/mendel/piano/sounds/5Mi.mp3',
  'K': '/home/mendel/piano/sounds/5Fa.mp3',
  'L': '/home/mendel/piano/sounds/5Sol_b.mp3',
  'Z': '/home/mendel/piano/sounds/5Sol.mp3',
  'X': '/home/mendel/piano/sounds/5La_b.mp3',
  'C': '/home/mendel/piano/sounds/5La.mp3',
  'V': '/home/mendel/piano/sounds/5Si_b.mp3',
  'B': '/home/mendel/piano/sounds/5Si.mp3',
  'N': '/home/mendel/piano/sounds/6Do.mp3',
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
