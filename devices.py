import pygame
import pyaudio
import sys
from sound_list import sounds

# Function to list audio devices using pyaudio
def list_audio_devices():
    p = pyaudio.PyAudio()
    devices = []
    for i in range(p.get_device_count()):
        info = p.get_device_info_by_index(i)
        devices.append(info['name'])
    p.terminate()
    return devices

# Get the list of available audio devices
devices = list_audio_devices()
print("Available audio devices:")
for i, device in enumerate(devices):
    print(f"{i}: {device}")

# Prompt the user to select a device
device_index = int(input("Enter the number of the audio device you want to use: "))

# Validate the user input
if device_index < 0 or device_index >= len(devices):
    print("Invalid device number. Using default device.")
    device_name = None
else:
    device_name = devices[device_index]

# Initialize Pygame
pygame.init()

# Initialize Pygame mixer with the specific device name (if provided)
if device_name:
    pygame.mixer.init(devicename=device_name)
else:
    pygame.mixer.init()

# Set screen dimensions (not used directly, but required by Pygame)
screen_width, screen_height = 1200, 900
screen = pygame.display.set_mode((screen_width, screen_height))

# Function to play sound
def play_sound(key):
    try:
        sound_path = sounds.get(key)
        if sound_path:
            sound = pygame.mixer.Sound(sound_path)
            sound.play()
        else:
            print(f"No sound mapped to key: {key}")
    except Exception as e:
        print(f"Error playing sound: {e}")

# Main loop
def main():
    # Set to track pressed keys
    pressed_keys = set()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key < 256:  # Only handle ASCII keys
                    char = pygame.key.name(event.key)  # Get the character representation of the key
                    if len(char) == 1:  # Check if it's a single character key
                        if event.mod & pygame.KMOD_SHIFT:  # Check if Shift is pressed
                            char = char.upper()  # Convert to uppercase if Shift is pressed
                        else:
                            char = char.lower()  # Convert to lowercase if Shift is not pressed

                        if char not in pressed_keys:
                            pressed_keys.add(char)
                            play_sound(char)
            elif event.type == pygame.KEYUP:
                if event.key < 256:
                    char = pygame.key.name(event.key)
                    if len(char) == 1:
                        if event.mod & pygame.KMOD_SHIFT:
                            char = char.upper()
                        else:
                            char = char.lower()

                        if char in pressed_keys:
                            pressed_keys.remove(char)

        pygame.time.wait(10)  # Control the loop speed

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    print("Press keys to play sounds. Press ESC to exit.")
    main()
