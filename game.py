import pygame
from datetime import datetime
import time
import numpy

print("Welcome to Reaction Game by Behrad Moniri\n")
N = int(input("Number of Stimuli:\t"))
p = float(input("Probability:\t"))
time_between_stimuli = float(input("Time between stimuli:\t"))

FileName = input("Results Filename (*.csv):\t")
# Random Sequence Generation
sequence = numpy.random.binomial(1, p, size=N)

# Reaction Times List
reaction_times = []

# Starting pygame
pygame.init()
screen = pygame.display.set_mode((640, 640), pygame.FULLSCREEN)  # Set Screen Size
screen.fill((255, 255, 255))  # Clear Screen

# Show Welcome Text on The Screen:
font = pygame.font.SysFont('Arial', 20)  # create font
text = font.render(" Reaction Time Game by Behrad Moniri from AirLab", 0, (0, 0, 0))  # create green text
text_rect = text.get_rect(center=screen.get_rect().center)  # get text (rectangle) size and move to center of screen
screen.blit(text, text_rect)  # Put Text on Screen
pygame.display.flip()  # Display the screen
time.sleep(5)  # Wait for 5 Seconds

for x in range(N):

    screen.fill((255, 255, 255))  # Send Screen on Monitor
    pygame.display.flip()

    # Wait 3 Seconds
    time.sleep(time_between_stimuli)

    if sequence[x] == 1:
        pygame.draw.circle(screen, (0, 0, 100), (420, 240), 20)

    if sequence[x] == 0:
        pygame.draw.circle(screen, (100, 0, 0), (220, 240), 20)

    # Show Circles
    pygame.display.flip()
    reaction_start = datetime.now()

    # wait for the correct key press
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == 276 and sequence[x] == 0:
                    reaction_end = datetime.now()
                    running = False
                if event.key == 275 and sequence[x] == 1:
                    reaction_end = datetime.now()
                    running = False
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

    # Save results
    reaction_times.append(reaction_end - reaction_start)
    print(reaction_end - reaction_start)

# Clear screen
screen.fill((255, 255, 255))

# Create goodbye text
text = font.render("PRESS ANY KEY TO EXIT", 0, (100, 0, 0))
text_rect = text.get_rect(center=screen.get_rect().center)
screen.blit(text, text_rect)
pygame.display.flip()

# Wait for key to close program
state = True
while state:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = False
        if event.type == pygame.KEYDOWN:
            state = False

# Save the results
f = open(FileName, "w")
f.write("Prob = {}\t Time = {}\n".format(p, time_between_stimuli))
for i in range(len(sequence)):
    f.write("{}\t{}\n".format(sequence[i], reaction_times[i]))

# End game
pygame.quit()
