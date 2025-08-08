import pygame
import os
import sys

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
ZONE_ROWS = 2
ZONE_COLS = 4
ZONE_WIDTH = SCREEN_WIDTH // ZONE_COLS
ZONE_HEIGHT = SCREEN_HEIGHT // ZONE_ROWS

# Load drum sounds
sound_folder = os.path.join(sys.path[0], "sounds")
sounds = []
for i in range(1, 9):
    sound_path = os.path.join(sound_folder, f"sound{i}.wav")
    if os.path.exists(sound_path):
        sounds.append(pygame.mixer.Sound(sound_path))
    else:
        print(f"❌ Missing: {sound_path}")
        sounds.append(None)

# Map numpad keys to zones (NumPad 1–8)
numpad_keys = {
    pygame.K_KP1: 0,
    pygame.K_KP2: 1,
    pygame.K_KP3: 2,
    pygame.K_KP4: 3,
    pygame.K_KP5: 4,
    pygame.K_KP6: 5,
    pygame.K_KP7: 6,
    pygame.K_KP8: 7,
}

# Create window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("NumPad Octopad 🎹🥁")

font = pygame.font.SysFont(None, 36)

def draw_zones(active_zone=None):
    screen.fill((0, 0, 0))
    for i in range(8):
        row = i // ZONE_COLS
        col = i % ZONE_COLS
        x = col * ZONE_WIDTH
        y = row * ZONE_HEIGHT

        if i == active_zone:
            color = (255, 215, 0)  # Highlight: Gold
        else:
            color = (80, 80, 80)

        pygame.draw.rect(screen, color, (x, y, ZONE_WIDTH, ZONE_HEIGHT))
        label = font.render(f"Zone {i+1}", True, (255, 255, 255))
        screen.blit(label, (x + 20, y + 20))

    pygame.display.flip()

# Initial screen
draw_zones()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key in numpad_keys:
                zone = numpad_keys[event.key]
                print(f"🎹 NumPad Key {zone + 1} pressed")
                draw_zones(active_zone=zone)

                if sounds[zone]:
                    pygame.mixer.stop()  # 🔇 Stop any playing sound
                    sounds[zone].play()

pygame.quit()
