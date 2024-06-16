import pygame
import sys
from sound_list import sounds

# Initialize Pygame
pygame.init()

# Initialize Pygame mixer
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)


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
