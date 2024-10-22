import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Indian Constitution Quiz Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (169, 169, 169)

# Fonts
font = pygame.font.Font(None, 36)
button_font = pygame.font.Font(None, 30)

# Questions and answers
questions = [
    {"question": "Which article of the Indian Constitution guarantees the Right to Equality?", 
     "options": ["Article 14", "Article 19", "Article 21", "Article 22"], 
     "answer": 0},
    {"question": "The Right to Freedom of Speech and Expression is provided under which article of the Indian Constitution?", 
     "options": ["Article 15", "Article 19", "Article 21", "Article 25"], 
     "answer": 1},
    # ... add remaining questions here
]

# Function to display text
def display_text(text, x, y, color=BLACK, size=36, font_type=font):
    text_surface = font_type.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Function to draw buttons
def draw_buttons(buttons, option_texts, y_offset):
    button_rects = []
    for i, text in enumerate(option_texts):
        rect = pygame.Rect(100, y_offset + i * 60, 600, 50)
        button_rects.append(rect)
        pygame.draw.rect(screen, GRAY, rect)
        display_text(text, 110, y_offset + i * 60, color=BLACK, size=30, font_type=button_font)
    return button_rects

# Main game function
def game_loop():
    current_question = 0
    score = 0
    while True:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for i, rect in enumerate(button_rects):
                    if rect.collidepoint(pos):
                        if i == questions[current_question]['answer']:
                            score += 1
                            feedback_color = GREEN
                        else:
                            feedback_color = RED
                        pygame.time.wait(1000)  # Wait for 1 second to show feedback
                        current_question += 1
                        if current_question >= len(questions):
                            print(f"Game Over! Your score: {score}/{len(questions)}")
                            pygame.quit()
                            sys.exit()
                        break

        # Display current question
        question_text = questions[current_question]['question']
        display_text(question_text, 100, 50, color=BLACK, size=36)

        # Display answer options
        option_texts = questions[current_question]['options']
        button_rects = draw_buttons(buttons, option_texts, y_offset=150)

        pygame.display.flip()

if __name__ == "_main_":
    game_loop()