from pygame.examples.scaletest import SpeedTest

from GameSnake import *

Screen.size(640,360)
Screen.fps = 60

level = TileMap("""
#.........................................................................####
#...................................................................P.....####
#.........................................................................####
#..................##################################################################
#..................#####################.............................................
#..................######.........######.............................................
#..................######.........######.........###......................###########
#..................######...............................................######
#..................##########......................................###....####
#...........................................................###...........####
#....................D..............................###...................####
########################################....###...........................####

""", {"#": "wall"}, tile_size=32, solid="#")

GRAVITY = 0.75
JUMP_POWER = 10
speed = 10





Screen.set_resizable(True)

start_x, start_y = level.find('P')[0]
player = Sprite("player", start_x, start_y)
player.set_hitbox(20,40,0,5)
player.show_hitbox = True

vy = 0
on_ground = False

Stage.camera.follow(player, smooth=10)
Stage.camera.limit_to(level.zone())





# Gameloop
while Screen.running:
    dx = 0
    if Keyboard.held("a"):
        dx -= speed
    if Keyboard.held("d"):
        dx += speed
    player.x += dx
    if player.touching_solid(level):
        player.x -= dx

    if Keyboard.pressed("space") and on_ground:
        vy = -JUMP_POWER

    vy += GRAVITY
    player.y += vy
    on_ground = False
    if player.touching_solid(level):
        player.y -= vy
        if vy > 0:
            on_ground = True
        vy = 0

    if player.y > level.height:
        player.x , player.y = level.find("P")[0]




    Screen.update()
