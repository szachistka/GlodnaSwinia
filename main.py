import pgzrun
import random

TITLE = "Gra Złap Świnię"
WIDTH = 800
HEIGHT = 800

pig = Actor("pig_down")
pig.x = 400
pig.y = 400
pig.v = 3
pig.vx = 0
pig.vy = 0
pig.points = 0
pig.dead = False

beet = Actor("beetroot")
beet.x = 600
beet.y = 300

game_over_timer = 0

def draw():
    screen.blit("bg.png", (0,0))
    pig.draw()

    if pig.dead == False:
        beet.draw()
        screen.draw.text(text="Punkty " +str(pig.points),center = (WIDTH/3, 70), fontsize = 40, color = "#000000", fontname = "kenney_bold", angle = 10, gcolor = "brown")
    #screen.draw.text(text="Punkty " +str(pig.points),center = (WIDTH/3, 70), fontsize = 40, color = "#000000", fontname = "kenney_bold", angle = 10, gcolor = "brown")
    if pig.dead == True:
        if game_over_timer < 40:
            screen.draw.text(f"GAME OVER", center = (WIDTH/2, HEIGHT /2), fontsize = 90, color = "#000000", fontname = "kenney_bold", gcolor = "red" )
        screen.draw.text(text="Punkty " + str(pig.points), center=(WIDTH / 2, 3* (HEIGHT/4)), fontsize=40, color="#000000",
                         fontname="kenney_bold", gcolor="brown")
        screen.draw.text(f"Press SPACE to try again", center = (WIDTH / 2, HEIGHT - 30), fontsize = 30, color = "#000000")

def update():
    global game_over_timer

    if pig.dead:
        game_over_timer += 1
        sounds.funeral_march.play()
        if game_over_timer == 60:
            game_over_timer = 0
        return

    pig.x += pig.vx
    pig.y += pig.vy

    if pig.colliderect(beet):
        beet.x = random.randint(50, WIDTH - 50)
        beet.y = random.randint(50, HEIGHT - 50)
        pig.v += 0.8
        pig.points += 1
        sounds.pig.play()

    if pig.x < 0 or pig.x > WIDTH or pig.y <0 or pig.y > HEIGHT:
       pig.dead = True
       pig.x = WIDTH /2
       pig.y = HEIGHT /3
       pig.image = "pig_dead"



def on_key_down(key):
    if pig.dead:
        if key == keys.SPACE:
            restart()

        return

    if key == keys.LEFT:
        pig.vx = -pig.v
        pig.vy = 0
        pig.image = "pig_left"

    if key == keys.RIGHT:
        pig.vx = pig.v
        pig.vy = 0
        pig.image = "pig_right"

    if key == keys.UP:
        pig.vx = 0
        pig.vy = -pig.v
        pig.image = "pig_up"

    if key == keys.DOWN:
        pig.vx = 0
        pig.vy = pig.v
        pig.image = "pig_down"


def restart():
    pig.image = "pig_down"
    pig.x = 400
    pig.y = 400
    pig.v = 3
    pig.vx = 0
    pig.vy = 0
    pig.points = 0
    pig.dead = False
    sounds.funeral_march.stop()



pgzrun.go()