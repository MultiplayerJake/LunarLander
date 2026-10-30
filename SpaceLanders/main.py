# funkce init(start hry); main game loop; results connected to init and Start; Quit
import math
import pygame
import random

SCREENSIZE = (800, 400)
FPS = 60

BASEIMG = pygame.image.load('assets/lander.png')
MAINENGINE = pygame.image.load('assets/main_engine.png')
RCSLEFT = pygame.image.load('assets/rcs_left.png')
RCSRIGHT = pygame.image.load('assets/rcs_right.png')

PLAYERSIZE = (50, 50)
GRAVITY = 2 / FPS
ROLL_FORCE = 7 / FPS
THRUST = 7 / FPS
MAX_FUEL = 10


programIcon = pygame.image.load('assets/rocket.png')
pygame.display.set_icon(programIcon)

HEIGHT_POINT_COUNT = int(SCREENSIZE[0] / PLAYERSIZE[0])
POINT_DISTANCE = PLAYERSIZE[0]
FLAT_POINTER_IMG = pygame.image.load("assets/flat_pointer.png")



pygame.init()

#text
FONT = pygame.font.Font("assets/boldpixels.boldpixels.ttf", 20)
start_text = FONT.render("PRESS ↑ TO START", False, "Yellow")
start_undetext = FONT.render("↑ TO FLY UP | ←/→ TO TURN LEFT/RIGHT", False ,"White")


screen = pygame.display.set_mode(SCREENSIZE)
screen.set_colorkey("Black")
pygame.display.set_caption("Lander")
clock = pygame.time.Clock()
running = True

screen.blit(start_text, (300, 70))
screen.blit(start_undetext, (180, 100))
pygame.display.flip()

def init():
    global running, player_position, player_velocity, player_roll, plyer_roll_rate, heightmap, flatpoint, start_text, MAX_FUEL, fuel
    fuel = MAX_FUEL
    player_position = [50, 100]
    player_velocity = [0, 0]
    player_roll = 0
    plyer_roll_rate = 0
    heightmap = [random.randint(SCREENSIZE[1]- 130, SCREENSIZE[1] - 60) for i in range(HEIGHT_POINT_COUNT)]
    flatpoint = random.randint(1, HEIGHT_POINT_COUNT - 2)
    heightmap[flatpoint-1] = heightmap[flatpoint]
    heightmap[flatpoint+1] = heightmap[flatpoint]
    running = True


def game_loop():
    global  running, player_position, player_velocity, player_roll, plyer_roll_rate, heightmap, flatpoint, start_text, fuel
    if not running:
        return
    playing = True

    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                playing = False

        current_img = BASEIMG.copy()
        rotated_player = pygame.transform.rotate(current_img, player_roll)
        player_mask = pygame.mask.from_surface(rotated_player)

        keys = pygame.key.get_pressed()
        if fuel > 0:
            if keys[pygame.K_LEFT]:
                plyer_roll_rate += ROLL_FORCE
                current_img.blit(RCSLEFT, (0, 0))
                fuel -= 1 / FPS

            if keys[pygame.K_UP]:
                player_velocity[0] -= THRUST * math.sin(math.radians(player_roll))
                player_velocity[1] -= THRUST * math.cos(math.radians(player_roll))
                current_img.blit(MAINENGINE, (0, 0))
                fuel -= 1 / FPS
            if keys[pygame.K_RIGHT]:
                plyer_roll_rate -= ROLL_FORCE
                current_img.blit(RCSRIGHT, (0, 0))
                fuel -= 1 / FPS

        player_velocity[1] += GRAVITY
        player_roll += plyer_roll_rate
        player_position[1] += player_velocity[1]
        player_position[0] += player_velocity[0]
        player_position[0] %= SCREENSIZE[0]

        rotated_player = pygame.transform.rotate(current_img, player_roll)

        screen.fill("black")

        if fuel > 3:
            fuel_text = FONT.render("You have %.2f " % fuel + " fuel", False, "Green")
        else:
            fuel_text = FONT.render("You have %.2f " % fuel + " fuel", False, "Red")
        screen.blit(fuel_text, (300, 360))

        for i in range(HEIGHT_POINT_COUNT):
            pygame.draw.line(screen, "white", (i*POINT_DISTANCE, heightmap[i]), ((i+1)*POINT_DISTANCE, heightmap[(i+1)%HEIGHT_POINT_COUNT]), 4)
        screen.blit(FLAT_POINTER_IMG, (flatpoint * POINT_DISTANCE - FLAT_POINTER_IMG.get_width()/2, heightmap[flatpoint]+15))

        map_mask = pygame.mask.from_surface(screen)
        if map_mask.overlap_area(player_mask, (player_position[0] - rotated_player.get_width()/2, player_position[1] - rotated_player.get_height()/2)) != 0:
            playing = False


        screen.blit(rotated_player, (player_position[0] - rotated_player.get_width()/2, player_position[1] - rotated_player.get_height()/2))
        pygame.display.flip()

        clock.tick(FPS)

def results():
    global flatpoint
    retry_text = FONT.render("PRESS ↑ TO RETRY", False, "Yellow")
    landing_velocity_text = FONT.render("LANDING VELOCITY: %.2f m/s" % (((player_velocity[0] ** 2 + player_velocity[1] ** 2) ** 0.5) / 10), False,"white")
    landing_roll_text = FONT.render("LANDING ROLL: %.2f°" % player_roll, False, "white")

    landing_distance = abs((player_position[0] - flatpoint * PLAYERSIZE[0]) / 10)
    landing_distance_text = FONT.render("OFFSET FROM TARGET: %.2f m" % landing_distance, False, "white")


    screen.blit(retry_text, (280, 70))
    screen.blit(landing_velocity_text, (280, 100))
    screen.blit(landing_roll_text, (280, 130))
    screen.blit(landing_distance_text, (280, 160))


    pygame.display.flip()


while running:
    init()
    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            running = False
            break
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            break

    game_loop()
    results()


pygame.quit()