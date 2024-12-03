"""
    Name: lucky7_1.py
    Author:
    Date:
    Purpose: Lucky 7 One Armed Bandit
"""

# pip install pygame-ce
import pygame
from random import randint


class Lucky7:
    PLAYERS_BET = 3
    BLACK = (0, 0, 0)
    BLUE = (41, 128, 185)

    def __init__(self):
        self.player_score = 20
        # Initialize pygame engine
        pygame.init()

        # Surface width and height constants
        self.SURFACE_WIDTH = 340
        self.SURFACE_HEIGHT = 400
        # Set screen width and height as a tuple
        self.SURFACE = pygame.display.set_mode(
            (self.SURFACE_WIDTH, self.SURFACE_HEIGHT)
        )
        pygame.display.set_caption("Lucky 7")
        # Define the clock to keep the game running at a set speed
        self.CLOCK = pygame.time.Clock()

        self.init_game()

#-------------------------- INIT GAME ------------------------------------ #
    def init_game(self):
        """
            Load images, get rect, set initial position
        """
        # Load program png icon
        self.slot_machine_ico = pygame.image.load(
            "./assets/slot_machine_ico.png").convert_alpha()
        # Set program icon and caption
        pygame.display.set_icon(self.slot_machine_ico)

        self.font_medium = pygame.font.Font("./assets/freesansbold.ttf", 18)
        # Player money
        self.player_text = self.font_medium.render(
            f"Player: ${self.player_score}", True, Lucky7.BLACK)
        self.player_rect = self.player_text.get_rect()
        self.player_rect.center = (100, 300)

        self.spin_btn = pygame.image.load(
            "./assets/button.png").convert_alpha()
        self.spin_btn_rect = self.spin_btn.get_rect()
        # Center spin button horizontally
        self.spin_btn_rect.centerx = self.SURFACE_WIDTH // 2
        self.spin_btn_rect.y = 150

        # Load the spin number image and get rectangle
        self.spin_img_1 = pygame.image.load(
            "./assets/0.png").convert_alpha()
        self.spin_img_2 = pygame.image.load(
            "./assets/0.png").convert_alpha()
        self.spin_img_3 = pygame.image.load(
            "./assets/0.png").convert_alpha()

        # Get rectangle around spin number image for easier manipulation
        self.spin_rect_1 = self.spin_img_1.get_rect()
        self.spin_rect_2 = self.spin_img_2.get_rect()
        self.spin_rect_3 = self.spin_img_3.get_rect()

        # Set numbers to 0 to start the game
        self.spin_rect_1.centerx = self.SURFACE_WIDTH // 4
        self.spin_rect_1.centery = 80

        self.spin_rect_2.centerx = self.SURFACE_WIDTH // 2
        self.spin_rect_2.centery = 80

        self.spin_rect_3.centerx = self.SURFACE_WIDTH // 4 * 3
        self.spin_rect_3.centery = 80

#------------------------------- SPIN -----------------------------------------#
    def spin(self):
        spin_1 = randint(1, 9)
        spin_2 = randint(1, 9)
        spin_3 = randint(1, 9)

        # Load the spin number image and get rectangle
        self.spin_img_1 = pygame.image.load(
            f"./assets/{spin_1}.png").convert_alpha()
        self.spin_img_2 = pygame.image.load(
            f"./assets/{spin_2}.png").convert_alpha()
        self.spin_img_3 = pygame.image.load(
            f"./assets/{spin_3}.png").convert_alpha()

        # Determine player score
        if spin_1 == 7 and spin_2 == 7 and spin_3 == 7:
            self.player_score += 300
        elif (spin_1 == 7 and spin_2 == 7) or (spin_2 == 7 and spin_3 == 7) or (spin_1 == 7 and spin_3 == 7):
            self.player_score += 100
        elif spin_1 == 7 or spin_2 == 7 or spin_3 == 7:
            self.player_score += 20
        else:
            self.player_score -= Lucky7.PLAYERS_BET

        self.player_text = self.font_medium.render(
            f"Player: ${self.player_score}", True, (0, 0, 0))

#------------------------------- GAME LOOP -----------------------------------------#
    def game_loop(self):
        """
            Infinite game loop
        """
        while True:
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONUP:
                    if self.spin_btn_rect.collidepoint(mouse):
                        self.spin()

            # Get list of keys being pressed
            # key_input = pygame.key.get_pressed()
            # If up cursor pressed, move up 5 pixels
            # if key_input[pygame.K_UP]:

        #------------------------- DRAW ----------------------------------#
            # Draw everything on the backbuffer first
            # Fill the display surface with blue
            self.SURFACE.fill(Lucky7.BLUE)

            # Draw all images to the backbuffer
            self.SURFACE.blit(self.spin_btn, self.spin_btn_rect)

            self.SURFACE.blit(
                self.spin_img_1,    # Source image
                self.spin_rect_1    # Destination location of image
            )
            self.SURFACE.blit(
                self.spin_img_2,    # Source image
                self.spin_rect_2    # Destination location of image
            )

            self.SURFACE.blit(
                self.spin_img_3,    # Source image
                self.spin_rect_3    # Destination location of image
            )

            # Display player money
            self.SURFACE.blit(
                self.player_text,
                self.player_rect
            )

            #----------------- UPDATE SURFACE FROM BACKBUFER -------------#
            pygame.display.update()
            self.CLOCK.tick(60)


# Program entry point, main function
def main():
    # Create Lucky7 program object
    lucky7_app = Lucky7()
    # Start infinite game loop
    lucky7_app.game_loop()


# Start the program
main()
