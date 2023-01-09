# Wyatt O'Connell (qdy5bq)
# This program represents a fall down game created using gamebox
import pygame
import gamebox
import random
camera = gamebox.Camera(650, 700)

score_int = 0
score = gamebox.from_text(50, 50, str(score_int), 60, 'red')
character = gamebox.from_color(325, 30, "red", 30, 30)
character.speedy = 5
character.speedx = 0
def generate_level():
    """
    This function creates each level that the character moves through with a randomly generated game somewhere within it
    :return: the level as a list of two gameboxes
    """
    a = 0
    b = 0
    while (a+b) != 580:
        a = random.randint(0, 580)
        b = random.randint(0, 580)
    return [gamebox.from_color(0,700, "black", (2*a), 30), gamebox.from_color(650,700, "black", (2*b), 30)]

def end_game(endgame):
    """
    this function is called when the character 'dies' and represents the end of the game
    :param endgame: nothing
    :return: an ending message
    """
    camera.clear('white')
    message = gamebox.from_text(325, 250, "YOU LOSE!", 100, 'red')
    camera.draw(message)
    camera.display()

levels = [
    [gamebox.from_color(0,700, "black", 580, 30), gamebox.from_color(650,700, "black", 580, 30)]
]

def game(keys):
    """
    this function progresses the movements and physics of all gameboxes
    :param keys: the keys pressed by the user
    :return: an updated position of all gameboxes
    """
    global level_speed
    global score_int
    global score
    camera.clear('white')
    if pygame.K_RIGHT in keys:
        if 15 < character.x < 635:
            character.move(5, 0)
        else:
            character.move(-1, 0)
    if pygame.K_LEFT in keys:
        if 15 < character.x < 635:
            character.move(-5, 0)
        else:
            character.move(1, 0)
    for level in levels:
        if level[0].y == 556:
            levels.append(generate_level())
            score_int += 1
        for side in level:
            side.y -= 3
            camera.draw(side)
    character.speedy += 0.5
    for level in levels:
        for side in level:
            if character.bottom_touches(side):
                character.speedy = 0
                character.move_to_stop_overlapping(side)
            if side.y <= 0:
                del side
    if character.y >= 672:
        character.speedy = 0
    score = gamebox.from_text(50, 50, str(score_int), 60, 'red')
    camera.draw(score)
    character.move_speed()
    camera.draw(character)
    camera.display()
    if character.y < -14:
        gamebox.stop_loop()

gamebox.timer_loop(30, game)

gamebox.timer_loop(30, end_game)






