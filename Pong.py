import pygame
from random import randint as R_randint
pygame.font.init()

# Game settings;
FPS = 240
WIDTH, HEIGHT = 600, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
PLAYER_MOVEMENT_VEL = 3
PLAYER_HEIGHT = 70
PLAYER_WIDTH = 12
GAME_BALL_SIZE = 10
GAME_BALL_STATE = {"x": (WIDTH//2)-GAME_BALL_SIZE//2, "y": (HEIGHT//2)-GAME_BALL_SIZE//2}
GAME_HAS_STARTED = False
GAME_BALL_VELOCITY = 1
GAME_BALL_MOVE_SIDE = ""

# Colors;
RED = (255, 0, 0)
BLACK = (0,0,0)
WHITE = (255,255,255)

# Players;
PLAYER_ONE = pygame.Rect(10, (HEIGHT//2)-7, PLAYER_WIDTH, PLAYER_HEIGHT)
PLAYER_TWO = pygame.Rect(WIDTH-24, (HEIGHT//2)-7, PLAYER_WIDTH, PLAYER_HEIGHT)
PLAYER_ONE_AIMING = "right"
PLAYER_TWO_AIMING = "left"

# App settings;
pygame.display.set_caption("Pong")

def gameEndsFunc(whoWon):
    comicFont = pygame.font.SysFont('Comic Sans MS', 70)
    WIN.blit(comicFont.render(str(whoWon) + " wins!", 1, (RED)), ((WIDTH//2)-220, 200))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

                
# The ball moving settings;
def moveBallF():
    global GAME_BALL_MOVE_SIDE
    # print(GAME_BALL_STATE)
    
    if GAME_BALL_MOVE_SIDE == "left":
        GAME_BALL_STATE["x"]-=GAME_BALL_VELOCITY
        if GAME_BALL_STATE["x"] == PLAYER_ONE.x+PLAYER_WIDTH and GAME_BALL_STATE["y"] < PLAYER_ONE.y+PLAYER_HEIGHT and GAME_BALL_STATE["y"] > PLAYER_ONE.y-PLAYER_HEIGHT:
            if PLAYER_ONE_AIMING == "up":
                GAME_BALL_MOVE_SIDE = "upright"
            else:
                GAME_BALL_MOVE_SIDE = "downright"

    elif GAME_BALL_MOVE_SIDE == "right":
        GAME_BALL_STATE["x"]+=GAME_BALL_VELOCITY
        if GAME_BALL_STATE["x"] == PLAYER_TWO.x-PLAYER_WIDTH and GAME_BALL_STATE["y"] < PLAYER_TWO.y+PLAYER_HEIGHT and GAME_BALL_STATE["y"] > PLAYER_TWO.y-PLAYER_HEIGHT:
            if PLAYER_TWO_AIMING == "up":
                GAME_BALL_MOVE_SIDE = "upleft"
            else:
                GAME_BALL_MOVE_SIDE = "downleft"

    elif GAME_BALL_MOVE_SIDE == "upleft":
        GAME_BALL_STATE["x"]-=GAME_BALL_VELOCITY
        GAME_BALL_STATE["y"]-=GAME_BALL_VELOCITY

        if GAME_BALL_STATE["x"] == PLAYER_ONE.x+PLAYER_WIDTH and GAME_BALL_STATE["y"] < PLAYER_ONE.y+PLAYER_HEIGHT and GAME_BALL_STATE["y"] > PLAYER_ONE.y-PLAYER_HEIGHT:
            if PLAYER_ONE_AIMING == "up":
                GAME_BALL_MOVE_SIDE = "upright"
            else:
                GAME_BALL_MOVE_SIDE = "downright"

    elif GAME_BALL_MOVE_SIDE == "upright":
        GAME_BALL_STATE["x"]+=GAME_BALL_VELOCITY
        GAME_BALL_STATE["y"]-=GAME_BALL_VELOCITY
        if GAME_BALL_STATE["x"] == PLAYER_TWO.x-PLAYER_WIDTH and GAME_BALL_STATE["y"] < PLAYER_TWO.y+PLAYER_HEIGHT and GAME_BALL_STATE["y"] > PLAYER_TWO.y-PLAYER_HEIGHT:
            if PLAYER_TWO_AIMING == "up":
                GAME_BALL_MOVE_SIDE = "upleft"
            else:
                GAME_BALL_MOVE_SIDE = "downleft"

    elif GAME_BALL_MOVE_SIDE == "downleft":
        GAME_BALL_STATE["x"]-=GAME_BALL_VELOCITY
        GAME_BALL_STATE["y"]+=GAME_BALL_VELOCITY
        if GAME_BALL_STATE["x"] == PLAYER_ONE.x+PLAYER_WIDTH and GAME_BALL_STATE["y"] < PLAYER_ONE.y+PLAYER_HEIGHT and GAME_BALL_STATE["y"] > PLAYER_ONE.y-PLAYER_HEIGHT:
            if PLAYER_ONE_AIMING == "up":
                GAME_BALL_MOVE_SIDE = "upright"
            else:
                GAME_BALL_MOVE_SIDE = "downright"

    elif GAME_BALL_MOVE_SIDE == "downright":
        GAME_BALL_STATE["x"]+=GAME_BALL_VELOCITY
        GAME_BALL_STATE["y"]+=GAME_BALL_VELOCITY
        if GAME_BALL_STATE["x"] == PLAYER_TWO.x+PLAYER_WIDTH and GAME_BALL_STATE["y"] < PLAYER_TWO.y+PLAYER_HEIGHT and GAME_BALL_STATE["y"] > PLAYER_TWO.y-PLAYER_HEIGHT:
            if PLAYER_TWO_AIMING == "up":
                GAME_BALL_MOVE_SIDE = "upleft"
            else:
                GAME_BALL_MOVE_SIDE = "downleft"

    # border colisions;
    if GAME_BALL_MOVE_SIDE == "upleft" and GAME_BALL_STATE["y"] <= 80+GAME_BALL_SIZE:
        GAME_BALL_MOVE_SIDE = "downleft"
    elif GAME_BALL_MOVE_SIDE == "upright" and GAME_BALL_STATE["y"] <= 80+GAME_BALL_SIZE:
        GAME_BALL_MOVE_SIDE = "downright"
    elif GAME_BALL_MOVE_SIDE == "downleft" and GAME_BALL_STATE["y"] > HEIGHT:
        GAME_BALL_MOVE_SIDE = "upleft"
    elif GAME_BALL_MOVE_SIDE == "downright" and GAME_BALL_STATE["y"] > HEIGHT:
        GAME_BALL_MOVE_SIDE = "upright"

    # Checking for wins
    if GAME_BALL_STATE["x"] > WIDTH:
        gameEndsFunc("Player-1")
    if GAME_BALL_STATE["x"] < 0:
        gameEndsFunc("Player-2")

def reRenderScreen(hpText, topBorder, fpsText):
    # Refreshing the screen;
    WIN.fill(BLACK)

    # The top text and borders;
    WIN.blit(hpText, ((WIDTH//2)-50, 0))
    pygame.display.set_caption("Pong [FPS:" + str(fpsText) + "]")
    pygame.draw.rect(WIN, WHITE, topBorder)
    # Rendering the players;
    pygame.draw.rect(WIN, RED, PLAYER_ONE)
    pygame.draw.rect(WIN, RED, PLAYER_TWO)

    # The *ball* for the game;
    pygame.draw.circle(WIN, WHITE, (GAME_BALL_STATE["x"], GAME_BALL_STATE["y"]), GAME_BALL_SIZE)

    pygame.display.update()

def movePlayerOne(keys_pressed):
    global PLAYER_ONE_AIMING
    if keys_pressed[pygame.K_w] and PLAYER_ONE.y > 90:
        PLAYER_ONE.y -= PLAYER_MOVEMENT_VEL
        PLAYER_ONE_AIMING = "up"
    if keys_pressed[pygame.K_s] and PLAYER_ONE.y < HEIGHT-PLAYER_HEIGHT:
        PLAYER_ONE.y += PLAYER_MOVEMENT_VEL
        PLAYER_ONE_AIMING = "down"

def movePlayerTwo(keys_pressed):
    global PLAYER_TWO_AIMING
    if keys_pressed[pygame.K_UP] and PLAYER_TWO.y > 90:
        PLAYER_TWO.y -= PLAYER_MOVEMENT_VEL
        PLAYER_TWO_AIMING = "up"
    if keys_pressed[pygame.K_DOWN] and PLAYER_TWO.y < HEIGHT-PLAYER_HEIGHT:
        PLAYER_TWO.y += PLAYER_MOVEMENT_VEL
        PLAYER_TWO_AIMING = "down"

def main():
    global GAME_HAS_STARTED, GAME_BALL_MOVE_SIDE
    isRunning = True
    gameClock = pygame.time.Clock()
    while isRunning:
        gameClock.tick(FPS)
        print(gameClock)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # The pong text;
        comicFont = pygame.font.SysFont('Comic Sans MS', 50)
        pongText = comicFont.render('Pong', 1, (255, 255, 255))

        # The top border;
        topBorder = pygame.Rect(0, 80, WIDTH, 10)

        # Checking for movements;
        keys_pressed = pygame.key.get_pressed() # Getting the pressed keys;
        # Setting the aiming to right-left now so if the players dont move their aiming values are neutral;
        movePlayerOne(keys_pressed)
        movePlayerTwo(keys_pressed)

        # Checking if game started is false so we can do the ball movement startup now;
        if not(GAME_HAS_STARTED):
            GAME_HAS_STARTED = True
            # Making a simple random-generation to know which side to start the ball to;
            if R_randint(0, 1) == 0:
                GAME_BALL_MOVE_SIDE = "left"
            else:
                GAME_BALL_MOVE_SIDE = "right"

        moveBallF()

        # ReRenderF
        reRenderScreen(pongText, topBorder, str(gameClock.get_fps()))
    
    # Quiting the game
    pygame.quit()

if __name__ == "__main__":
    main()
