@namespace
class SpriteKind:
    coin = SpriteKind.create()
    coin10 = SpriteKind.create()
    flyingenemy = SpriteKind.create()
    attak = SpriteKind.create()
    tests = SpriteKind.create()
    life = SpriteKind.create()
    superenemy = SpriteKind.create()

def on_on_overlap(sprite3, otherSprite):
    info.change_score_by(10)
    otherSprite.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.coin10, on_on_overlap)

def on_overlap_tile(sprite, location):
    sprite.vy += -25
scene.on_overlap_tile(SpriteKind.flyingenemy,
    assets.tile("""
        myTile1
    """),
    on_overlap_tile)

def on_up_pressed():
    global heals
    if heals > 2:
        if info.life() < 5:
            info.change_life_by(1)
            heals += -3
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_b_pressed():
    global sword_attak
    sword_attak = 1
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_on_overlap2(sprite8, otherSprite3):
    tiles.place_on_random_tile(sprite8, assets.tile("""
        myTile21
    """))
sprites.on_overlap(SpriteKind.flyingenemy,
    SpriteKind.flyingenemy,
    on_on_overlap2)

def on_a_pressed():
    if player1.vy == 0:
        player1.vy = -100
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap3(sprite2, otherSprite2):
    tiles.place_on_random_tile(otherSprite2, assets.tile("""
        myTile24
    """))
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.superenemy, on_on_overlap3)

def on_hit_wall(sprite5, location4):
    sprite5.vx = randint(-100, 100)
    sprite5.vy = randint(-100, 100)
scene.on_hit_wall(SpriteKind.enemy, on_hit_wall)

def on_overlap_tile2(sprite4, location2):
    tiles.place_on_random_tile(player1, assets.tile("""
        myTile24
    """))
    info.change_life_by(-2)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile25
    """),
    on_overlap_tile2)

def on_overlap_tile3(sprite6, location3):
    global _true, boss1, ENIMYliFe123
    if _true == 1:
        _true = 0
        boss1 = sprites.create(img("""
                .......ff.......
                            .....ff11ff.....
                            ....f111111f....
                            ...f11111111f...
                            ...f12111121f...
                            ..f1122112211f..
                            ..f1111111111f..
                            ...f11111111f...
                            ...f11111111f...
                            ....f111111f....
                            .....ff11ff.....
                            ....f25ff45f....
                            ....f254525f....
                            ...f45545252f...
                            ...f45245454f...
                            ...f25225455f...
                            ..f2254554454f..
                            ..f5544544554f..
                            ..f4445544522f..
                            ..f5555225522f..
                            ..f4442225444f..
                            ..ffffffffffff..
                            ..ffffffff.fff..
                            ..f.fff.ff..ff..
                            ..f..f..f...ff..
                            .....f.......f..
                            ................
                            ................
                            ................
                            ................
                            ................
                            ................
            """),
            SpriteKind.superenemy)
        ENIMYliFe123 = 1000
        tiles.place_on_random_tile(boss1, assets.tile("""
            myTile23
        """))
        boss1.vx = randint(-100, 100)
        boss1.set_bounce_on_wall(True)
        tiles.set_wall_at(tiles.get_tile_location(29, 15), True)
        tiles.set_wall_at(tiles.get_tile_location(29, 16), True)
        BOSSESZ()
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile3
    """),
    on_overlap_tile3)

def on_on_overlap4(sprite11, otherSprite5):
    tiles.place_on_random_tile(sprite11, assets.tile("""
        myTile19
    """))
sprites.on_overlap(SpriteKind.coin, SpriteKind.coin, on_on_overlap4)

def on_on_overlap5(sprite7, otherSprite4):
    global heals
    if sword_attak == 1:
        otherSprite4.destroy()
        info.change_score_by(1)
        music.zapped.play()
        if heals < 9:
            heals += 1
sprites.on_overlap(SpriteKind.attak, SpriteKind.enemy, on_on_overlap5)

def on_on_overlap6(sprite12, otherSprite6):
    info.change_life_by(-1)
    otherSprite6.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap6)

def on_overlap_tile4(sprite10, location6):
    sprite10.destroy(effects.fire, 1000)
scene.on_overlap_tile(SpriteKind.flyingenemy,
    assets.tile("""
        myTile18
    """),
    on_overlap_tile4)

def on_on_overlap7(sprite9, otherSprite7):
    global heals
    if sword_attak == 1:
        otherSprite7.destroy()
        info.change_score_by(2)
        music.zapped.play()
        if heals < 9:
            heals += 1
sprites.on_overlap(SpriteKind.attak, SpriteKind.flyingenemy, on_on_overlap7)

def on_on_overlap8(sprite62, otherSprite22):
    info.change_score_by(2)
    otherSprite22.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.coin, on_on_overlap8)

def on_overlap_tile5(sprite42, location32):
    info.change_life_by(-2)
    tiles.place_on_random_tile(player1, assets.tile("""
        myTile17
    """))
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile18
    """),
    on_overlap_tile5)

def on_overlap_tile6(sprite22, location22):
    sprite22.vx += 25
scene.on_overlap_tile(SpriteKind.flyingenemy,
    assets.tile("""
        myTile20
    """),
    on_overlap_tile6)

def on_down_pressed():
    player1.vy += 75
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def on_overlap_tile7(sprite72, location5):
    sprite72.destroy(effects.fire, 1000)
scene.on_overlap_tile(SpriteKind.enemy,
    assets.tile("""
        myTile18
    """),
    on_overlap_tile7)

def BOSSESZ():
    pass

def on_on_overlap9(sprite13, otherSprite8):
    global ENIMYliFe123, heals
    if sword_attak == 1:
        music.zapped.play()
        ENIMYliFe123 += -50
        boss1.set_position(boss1.x + sword_dir * 50, boss1.y)
        if ENIMYliFe123 <= 0:
            boss1.destroy(effects.fire, 500)
        if heals < 9:
            heals += 1
        pause(1000)
sprites.on_overlap(SpriteKind.attak, SpriteKind.superenemy, on_on_overlap9)

def on_hit_wall2(sprite52, location42):
    boss1.vx = randint(-100, 100)
    boss1.vy = randint(-100, 100)
scene.on_hit_wall(SpriteKind.superenemy, on_hit_wall2)

def on_on_overlap10(sprite14, otherSprite9):
    global heals
    if sword_attak == 1:
        otherSprite9.destroy()
        music.zapped.play()
        if heals < 9:
            heals += 1
sprites.on_overlap(SpriteKind.attak, SpriteKind.tests, on_on_overlap10)

def on_on_overlap11(sprite92, otherSprite42):
    info.change_life_by(-1)
    otherSprite42.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.flyingenemy, on_on_overlap11)

mySprite2: Sprite = None
sword_pos_x = 0
sword_dir = 0
ENIMYliFe123 = 0
boss1: Sprite = None
sword_attak = 0
heals = 0
coinz10: Sprite = None
coinz: Sprite = None
flybug: Sprite = None
_true = 0
player1: Sprite = None
player1 = sprites.create(img("""
        . . . . . . . f f . . . . . . .
            . . . . . f f 1 1 f f . . . . .
            . . . . f 1 1 1 1 1 1 f . . . .
            . . . . f 1 f 1 1 f 1 f . . . .
            . . . f 1 1 f 1 1 f 1 1 f . . .
            . . . f 1 1 1 1 1 1 1 1 f . . .
            . . . . f 1 1 1 1 1 1 f . . . .
            . . . . f 1 1 1 1 1 1 f . . . .
            . . . . . f f f f f f . . . . .
            . . . . f d f d d f d f . . . .
            . . . . f d f 5 5 f d f . . . .
            . . . f d f d 5 5 d d f f . . .
            . . . f d f d d f d f d f . . .
            . . . f d d f d d f f d f . . .
            . . . f d f d d f d d f f . . .
            . . . . f f f f f f f f . . . .
    """),
    SpriteKind.player)
scene.set_background_image(img("""
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd1111111dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd1bbbbbbb1dddddddddddddddddddddddddddddddddddddddddddddddddddd1111111dddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd1bbbbbbb1dddddddddddddddddddddddddddddddddddddddddddddddddd11bbbbbbb11dddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd1bbbbbbb1ddddddddddddddddddddddddddddddddddddddddddddddddd1bbbbbbbbbbb1ddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd1bbbbbbb1ddddddddddddddddddddddddddddddddddddddddddddddddd1bbbbbbbbbbb1ddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd1bbbbbbb1dddddddddddddddddddddddddddddd1111111ddddddddddd1bbbbbbbbbbbbb1dddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd1bbbbbbb1ddddddddddddddddddddddddddddd1bbbbbbb1dddddddddd1bbbbbbbbbbbbb1dddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd1bbbbbbb1ddddddddddddddddddddddddddddd1bbbbbbb1dddddddddd1bbbbbbbbbbbbb1dddddddddddddddddddddd
        dddddddd11111dddddddddddddddddddddddddddddddddddddddddddddddddddddd1111111dddddddddddddddddddddddddddddd1bbbbbbb1dddddddddd1bbbbbbbbbbbbb1dddddddddddddddddddddd
        dddddddd1bbb1dddddd1111111dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd1bbbbbbb1dddddddddd1bbbbbbbbbbbbb1dddddddddddddddddddddd
        dddddddd1bbb1ddddd1bbbbbbb1ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd1bbbbbbb1dddddddddd1bbbbbbbbbbbbb1dddddddddddddddddddddd
        dddddddd1bbb1dddd1bbbbbbbbb1dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd1bbbbbbb1dddddddddd1bbbbbbbbbbbbb1dddddddddddddddddddddd
        dddddddd11111ddd1bbbbbbbbbbb1ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd1bbbbbbb1ddddddddddd1bbbbbbbbbbb1ddddddddddddddddddddddd
        dddddddddddddddd1bbbbbbbbbbb1ddddddddd1111111dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd1111111dddddddddddd1bbbbbbbbbbb1ddddddddddddddddddddddd
        dddddddddddddddd1bbbbbbbbbbb1dddddddd1bbbbbbb1ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd11bbbbbbb11dddddddddddddddddddddddd
        dddddddddddddddd1bbbbbbbbbbb1dddddddd1bbbbbbb1ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd1111111dddddddddddddddddddddddddd
        dddddddddddddddd1bbbbbbbbbbb1dddddddd1bbbbbbb1dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddd1bbbbbbbbbbb1dddddddd1bbbbbbb1dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddd1bbbbbbbbbbb1dddddddd1bbbbbbb1dddddddddddddddddddddddddddddd1111111ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddd1bbbbbbbbb1ddddddddd1bbbbbbb1ddddddddddddddddddddddddddddd1bbbbbbb1dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddd1bbbbbbb1dddddddddd1bbbbbbb1ddddddddddddddddddddddddddddd1bbbbbbb1dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddddd1111111dddddddddddd1111111dddddddddddddddddddddddddddddd1bbbbbbb1dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd1bbbbbbb1dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd1bbbbbbb1dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd1bbbbbbb1dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd1bbbbbbb1dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd1111111ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd111111111dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd11bbbbbbbbb11dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd1bbbbbbbbbbbbb1ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd1bbbbbbbbbbbbbbb1dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd1bbbbbbbbbbbbbbbbb1ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddd111ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd1bbbbbbbbbbbbbbbbbbb1dddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddd1b1ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd1bbbbbbbbbbbbbbbbbbb1dddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddd111dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd1bbbbbbbbbbbbbbbbbbbbb1ddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddd1111111dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd1bbbbbbbbbbbbbbbbbbbbb1ddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddd1bbbbbbb1ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd1bbbbbbbbbbbbbbbbbbbbb1dddddddddddddddddddddddddddddd1111111dddddddddddddddddddd
        ddddddddd1bbbbbbbbb1dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd1bbbbbbbbbbbbbbbbbbbbb1ddddddddddddddddddddddddddddd1bbbbbbb1ddddddddddddddddddd
        dddddddd1bbbbbbbbbbb1dddddddddddddd11111dddddddddddddddddddddddddddddddddddddddd1bbbbbbbbbbbbbbbbbbbbb1dddddddddddddddddddddddddddd1bbbbbbbbb1dddddddddddddddddd
        dddddddd1bbbbbbbbbbb1ddddddddddddd1bbbbb1ddddddddddddddddddddddddddddddddddddddd1bbbbbbbbbbbbbbbbbbbbb1dddddddddddddddddddddddddddd1bbbbbbbbb1dddddddddddddddddd
        dddddddd1bbbbbbbbbbb1ddddddddddddd1bbbbb1ddddddddddddddddddddddddddddddddddddddd1bbbbbbbbbbbbbbbbbbbbb1dddddddddddddddddddddddddddd1bbbbbbbbb1dddddddddddddddddd
        dddddddd1bbbbbbbbbbb1ddddddddddddd1bbbbb1ddddddddddddddddddddddddddddddddddddddd1bbbbbbbbbbbbbbbbbbbbb1dddddddddddddddddddddddddddd1bbbbbbbbb1dddddddddddddddddd
        dddddddd1bbbbbbbbbbb1ddddddddddddd1bbbbb1ddddddddddddddddddddddddddddddddddddddd1bbbbbbbbbbbbbbbbbbbbb1dddddddddddddddddddddddddddd1bbbbbbbbb1dddddddddddddddddd
        dddddddd1bbbbbbbbbbb1ddddddddddddd1bbbbb1dddddddddddddddddddddddddddddddddddddddd1bbbbbbbbbbbbbbbbbbb1ddddddddddddddddddddddddddddd1bbbbbbbbb1dddddddddddddddddd
        dddddddd1bbbbbbbbbbb1dddddddddddddd11111dddddddddddddddddddd11111dddddddddddddddd1bbbbbbbbbbbbbbbbbbb1ddddddddddddddddddddddddddddd1bbbbbbbbb1dddddddddddddddddd
        ddddddddd1bbbbbbbbb1dddddddddddddddddddddddddddddddddddddddd1bbb1ddddddddddddddddd1bbbbbbbbbbbbbbbbb1ddddddddddddddddddddddddddddddd1bbbbbbb1ddddddddddddddddddd
        dddddddddd1bbbbbbb1ddddddddddddddddddddddddddddddddddddddddd1bbb1dddddddddddddddddd1bbbbbbbbbbbbbbb1ddddddddddddddddddddddddddddddddd1111111dddddddddddddddddddd
        ddddddddddd1111111dddddddddddddddddddddddddddddddddddddddddd1bbb1ddddddddddddddddddd1bbbbbbbbbbbbb1ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd11111dddddddddddddddddddd11bbbbbbbbb11dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd111111111dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddd1111111dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddd11bbbbbbb11dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddd1bbbbbbbbbbb1ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddd1bbbbbbbbbbb1dddddddddddddddddddddddddddddddddddddddd1111111dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddd1bbbbbbbbbbbbb1dddddddddddddddddddddddddddddddddddddd1bbbbbbb1ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddd1111111dddddddddddddddddd1bbbbbbbbbbbbb1ddddddddddddddddddddddddddddddddddddd1bbbbbbbbb1dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddd1bbbbbbb1ddddddddddddddddd1bbbbbbbbbbbbb1dddddddddddddddddddddddddddddddddddd1bbbbbbbbbbb1ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddd1bbbbbbbbb1dddddddddddddddd1bbbbbbbbbbbbb1dddddddddddddddddddddddddddddddddddd1bbbbbbbbbbb1ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddd1bbbbbbbbb1dddddddddddddddd1bbbbbbbbbbbbb1dddddddddddddddddddddddddddddddddddd1bbbbbbbbbbb1ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddd1bbbbbbbbb1dddddddddddddddd1bbbbbbbbbbbbb1dddddddddddddddddddddddddddddddddddd1bbbbbbbbbbb1ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddd1bbbbbbbbb1dddddddddddddddd1bbbbbbbbbbbbb1dddddddddddddddddddddddddddddddddddd1bbbbbbbbbbb1ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddd1bbbbbbbbb1ddddddddddddddddd1bbbbbbbbbbb1ddddddddddddddddddddddddddddddddddddd1bbbbbbbbbbb1dddddddddddddddddd111111111dddddddddddddddddddddddddddddddd
        dddddddddd1bbbbbbbbb1ddddddddddddddddd1bbbbbbbbbbb1ddddddddddddddddddddddddddddddddddddd1bbbbbbbbbbb1ddddddddddddddddd1bbbbbbbbb1ddddddddddddddddddddddddddddddd
        dddddddddd1bbbbbbbbb1dddddddddddddddddd11bbbbbbb11dddddddddddd1111111dddddddddddddddddddd1bbbbbbbbb1ddddddddddddddddd1bbbbbbbbbbb1dddddddddddddddddddddddddddddd
        ddddddddddd1bbbbbbb1ddddddddddddddddddddd1111111ddddddddddddd1bbbbbbb1dddddddddddddddddddd1bbbbbbb1ddddddddddddddddd1bbbbbbbbbbbbb1ddddddddddddddddddddddddddddd
        dddddddddddd1111111dddddddddddddddddddddddddddddddddddddddddd1bbbbbbb1ddddddddddddddddddddd1111111ddddddddddddddddd1bbbbbbbbbbbbbbb1dddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd1bbbbbbb1ddddddddddddddddddddddddddddddddddddddddddddd1bbbbbbbbbbbbbbb1dddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd1bbbbbbb1ddddddddddddddddddddddddddddddddddddddddddddd1bbbbbbbbbbbbbbb1dddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd1bbbbbbb1ddddddddddddddddddddddddddddddddddddddddddddd1bbbbbbbbbbbbbbb1dddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd1bbbbbbb1ddddddddddddddddddddddddddddddddddddddddddddd1bbbbbbbbbbbbbbb1dddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd1bbbbbbb1ddddddddddddddddddddddddddddddddddddddddddddd1bbbbbbbbbbbbbbb1dddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd1111111dddddddddddddddddddddddddddddddddddddddddddddd1bbbbbbbbbbbbbbb1dddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd1bbbbbbbbbbbbbbb1dddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd1bbbbbbbbbbbbbbb1dddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd1bbbbbbbbbbbbb1ddddddddddddddddddddddddddddd
        dddddddddddd111111111dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd1bbbbbbbbbbb1dddddddddddddddddddddddddddddd
        ddddddddddd1bbbbbbbbb1dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd1bbbbbbbbb1ddddddddddddddddddddddddddddddd
        dddddddddd1bbbbbbbbbbb1dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd111111111dddddddddddddddddddddddddddddddd
        ddddddddd1bbbbbbbbbbbbb1dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddd1bbbbbbbbbbbbbbb1ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddd1bbbbbbbbbbbbbbb1ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddd1bbbbbbbbbbbbbbb1ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddd1bbbbbbbbbbbbbbb1ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddd1bbbbbbbbbbbbbbb1ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddd1bbbbbbbbbbbbbbb1ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddd1bbbbbbbbbbbbbbb1dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd111dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddd1bbbbbbbbbbbbbbb1ddddddddddddddddddddddddddddddddddddd1111111dddddddddddddddddddddddddd1b1dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddd1bbbbbbbbbbbbbbb1dddddddddddddddddddddddddddddddddddd1bbbbbbb1ddddddddddddddddddddddddd111dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        ddddddddd1bbbbbbbbbbbbb1ddddddddddddddddddddddddddddddddddddd1bbbbbbb1dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddd1bbbbbbbbbbb1ddddddddddd1111111dddddddddddddddddddd1bbbbbbb1dddddddddddddddddddddddddddddddddddddddddddddddddddddddd11111ddddddddddddddddddddddddddddd
        ddddddddddd1bbbbbbbbb1ddddddddddd1bbbbbbb1ddddddddddddddddddd1bbbbbbb1ddddddddddddddddddddddddddddddddddddddddddddddddddddddd1bbbbb1dddddddddddddddddddddddddddd
        dddddddddddd111111111ddddddddddd1bbbbbbbbb1dddddddddddddddddd1bbbbbbb1ddddddddddddddddddddddddddddddddddddddddddddddddddddddd1bbbbb1dddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddd1bbbbbbbbb1dddddddddddddddddd1bbbbbbb1ddddddddddddddddddddddddddddddddddddddddddddddddddddddd1bbbbb1dddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddd1bbbbbbbbb1dddddddddddddddddd1bbbbbbb1ddddddddddddddddddddddddddddddddddddddddddddddddddddddd1bbbbb1dddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddd1bbbbbbbbb1ddddddddddddddddddd1111111ddddddddddddddddddddddd1111111dddddddddddddddddddddddddd1bbbbb1dddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddd1bbbbbbbbb1dddddddddddddddddddddddddddddddddddddddddddddddd1bbbbbbb1dddddddddddddddddddddddddd11111ddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddd1bbbbbbbbb1ddddddddddddddddddddddddddddddddddddddddddddddd1bbbbbbbbb1ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddd1bbbbbbbbb1dddddddddddddddddddddddddddddddddddddddddddddd1bbbbbbbbbbb1dddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddd1bbbbbbb1ddddddddddddddddddddddddddddddddddddddddddddddd1bbbbbbbbbbb1dddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddd1111111dddddddddddddddddddddddddddddddddddddddddddddddd1bbbbbbbbbbb1dddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd1bbbbbbbbbbb1dddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd1bbbbbbbbbbb1dddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd1bbbbbbbbbbb1dddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd1bbbbbbbbbbb1dddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd1bbbbbbbbb1ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd1bbbbbbb1dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd1111111ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
"""))
_true = 1
test = sprites.create(img("""
        . . . . . . . . . . b 5 b . . .
            . . . . . . . . . b 5 b . . . .
            . . . . . . b b b b b b . . . .
            . . . . . b b 5 5 5 5 5 b . . .
            . . . . b b 5 d 1 f 5 5 d f . .
            . . . . b 5 5 1 f f 5 d 4 c . .
            . . . . b 5 5 d f b d d 4 4 . .
            . b b b d 5 5 5 5 5 4 4 4 4 4 b
            b d d d b b d 5 5 4 4 4 4 4 b .
            b b d 5 5 5 b 5 5 5 5 5 5 b . .
            c d c 5 5 5 5 d 5 5 5 5 5 5 b .
            c b d c d 5 5 b 5 5 5 5 5 5 b .
            . c d d c c b d 5 5 5 5 5 d b .
            . . c b d d d d d 5 5 5 b b . .
            . . . c c c c c c c c b b . . .
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.tests)
test.ay = 100
controller.move_sprite(player1, 100, 0)
scene.camera_follow_sprite(player1)
tiles.set_tilemap(tilemap("""
    level1
"""))
player1.ay = 100
tiles.place_on_random_tile(player1, assets.tile("""
    myTile17
"""))
info.set_life(5)
Lives = 1
sword = sprites.create(img("""
        . . . . 6 6 . . . .
            . . 6 6 8 8 6 6 . .
            . 6 8 8 8 8 8 8 6 .
            . 6 8 9 9 9 9 8 6 .
            6 8 8 9 5 5 9 8 8 6
            6 8 8 9 5 5 9 8 8 6
            . 6 8 9 9 9 9 8 6 .
            . 6 8 8 8 8 8 8 6 .
            . . 6 6 8 8 6 6 . .
            . . . . 6 6 . . . .
    """),
    SpriteKind.attak)
sword.set_flag(SpriteFlag.GHOST_THROUGH_WALLS, True)
for index in range(5):
    flybug = sprites.create(img("""
            . . . . 7 7 . . . . . 7 7 . . . .
                    . . . . 7 . . . . . . . 7 . . . .
                    . . . . 7 7 . . . . . 7 7 . . . .
                    . . . . . 7 7 . . . 7 7 . . . . .
                    . . . . . f f f f f f f . . . . .
                    . . . . f a a a a a a a f . . . .
                    . f . . f a 2 a a a 2 a f . . f .
                    f 1 f . f a 2 2 a 2 2 a f . f 1 f
                    f 1 f . f a a a a a a a f . f 1 f
                    f 1 1 f . f f f f f f f . f 1 1 f
                    f 1 1 1 f f b b b b b f f 1 1 1 f
                    f 1 1 f b b b c 3 c b b b b 1 1 f
                    . f f b b b b c 3 c b b b b f f .
                    . . f b b f b b b b b f b b f . .
                    . . f b f f b b b b b f f b f . .
                    . . . f . f f f f f f f . f . . .
        """),
        SpriteKind.flyingenemy)
    tiles.place_on_random_tile(flybug, assets.tile("""
        myTile21
    """))
    flybug.follow(player1)
for index2 in range(11):
    coinz = sprites.create(img("""
            . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . 5 5 5 . . . . . .
                    . . . . . 5 5 4 4 4 5 5 . . . .
                    . . . . 5 4 4 5 8 5 4 4 5 . . .
                    . . . . 5 4 5 5 8 5 5 4 5 . . .
                    . . . 5 4 5 5 1 9 1 5 5 4 5 . .
                    . . . 5 4 8 8 9 6 9 8 8 4 5 . .
                    . . . 5 4 5 5 1 9 1 5 5 4 5 . .
                    . . . . 5 4 5 5 8 5 5 4 5 . . .
                    . . . . 5 4 4 5 8 5 4 4 5 . . .
                    . . . . . 5 5 4 4 4 5 5 . . . .
                    . . . . . . . 5 5 5 . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.coin)
    tiles.place_on_random_tile(coinz10, assets.tile("""
        myTile19
    """))
for index3 in range(1):
    coinz10 = sprites.create(img("""
            . . . . . . . 5 2 5 . . . . . .
                    . . . . . 5 5 4 4 4 5 5 . . . .
                    . . . . b 4 4 b 5 b 4 4 b . . .
                    . . . b 4 5 5 4 4 4 5 5 4 b . .
                    . . 5 4 5 4 4 5 8 5 4 4 5 4 5 .
                    . . 5 4 5 4 5 5 8 5 5 4 5 4 5 .
                    . 5 4 b 4 5 5 1 9 1 5 5 4 b 4 5
                    . 2 4 5 4 8 8 9 6 9 8 8 4 5 4 2
                    . 5 4 b 4 5 5 1 9 1 5 5 4 b 4 5
                    . . 5 4 5 4 5 5 8 5 5 4 5 4 5 .
                    . . 5 4 5 4 4 5 8 5 4 4 5 4 5 .
                    . . . b 4 5 5 4 4 4 5 5 4 b . .
                    . . . . b 4 4 b 5 b 4 4 b . . .
                    . . . . . 5 5 4 4 4 5 5 . . . .
                    . . . . . . . 5 2 5 . . . . . .
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.coin10)
    tiles.place_on_random_tile(coinz10, assets.tile("""
        myTile22
    """))
life_1 = sprites.create(img("""
        . . . . . f f f f f . . . . . .
            . . . f f . . . . . f f . . . .
            . . f . . . . . . . . . f . . .
            . f . . . . . . . . . . . f . .
            . f . . . . . . . . . . . f . .
            f . . . . . . . . . . . . . f .
            f . . . . . . . . . . . . . f .
            f . . . . . . . . . . . . . f .
            f . . . . . . . . . . . . . f .
            f . . . . . . . . . . . . . f .
            . f . . . . . . . . . . . f . .
            . f . . . . . . . . . . . f . .
            . . f . . . . . . . . . f . . .
            . . . f f . . . . . f f . . . .
            . . . . . f f f f f . . . . . .
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.life)
life_1.set_flag(SpriteFlag.GHOST, True)
life_1.set_flag(SpriteFlag.RELATIVE_TO_CAMERA, True)
life_1.x = 10
life_1.y = 20

def on_forever():
    global sword_dir, sword_pos_x, sword_attak
    if player1.vx > 1:
        sword.set_image(img("""
            . . . . 6 6 . . . .
                        . . 6 6 8 8 6 6 . .
                        . 6 8 8 8 8 8 8 6 .
                        . 6 8 9 9 9 9 8 6 .
                        6 8 8 9 5 5 9 8 8 6
                        6 8 8 9 5 5 9 8 8 6
                        . 6 8 9 9 9 9 8 6 .
                        . 6 8 8 8 8 8 8 6 .
                        . . 6 6 8 8 6 6 . .
                        . . . . 6 6 . . . .
        """))
        sword_dir = 1
        sword_pos_x = 12
    elif player1.vx < -1:
        sword.set_image(img("""
            . . . . 6 6 . . . .
                        . . 6 6 8 8 6 6 . .
                        . 6 8 8 8 8 8 8 6 .
                        . 6 8 9 9 9 9 8 6 .
                        6 8 8 9 5 5 9 8 8 6
                        6 8 8 9 5 5 9 8 8 6
                        . 6 8 9 9 9 9 8 6 .
                        . 6 8 8 8 8 8 8 6 .
                        . . 6 6 8 8 6 6 . .
                        . . . . 6 6 . . . .
        """))
        sword_dir = -1
        sword_pos_x = -12
    if controller.B.is_pressed():
        sword.set_velocity(sword_dir * 50, 100)
        pause(50)
    else:
        sword_attak = 0
    sword.set_position(player1.x + sword_pos_x, player1.y + -1)
forever(on_forever)

def on_forever2():
    if Lives == 0:
        pause(2000)
        game.over(False, effects.melt)
forever(on_forever2)

def on_forever3():
    global mySprite2
    mySprite2 = sprites.create(img("""
            . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . 7 7 . . . . .
                    . . . . . 5 5 5 5 7 5 5 . . . .
                    . . . . 5 5 5 5 5 5 f 1 5 . . .
                    . . 5 5 5 5 5 5 5 5 f f 5 . . .
                    . 5 5 . 5 1 1 1 1 1 5 5 5 . . .
                    . 5 . . 5 . 5 . . . 5 . 5 . . .
                    . . . . 5 . 5 . . . 5 . 5 . . .
        """),
        SpriteKind.enemy)
    mySprite2.ay = 100
    tiles.place_on_random_tile(mySprite2, assets.tile("""
        myTile17
    """))
    pause(5000)
forever(on_forever3)

def on_forever4():
    global flybug
    flybug = sprites.create(img("""
            . . . . 7 7 . . . . . 7 7 . . . .
                    . . . . 7 . . . . . . . 7 . . . .
                    . . . . 7 7 . . . . . 7 7 . . . .
                    . . . . . 7 7 . . . 7 7 . . . . .
                    . . . . . f f f f f f f . . . . .
                    . . . . f a a a a a a a f . . . .
                    . f . . f a 2 a a a 2 a f . . f .
                    f 1 f . f a 2 2 a 2 2 a f . f 1 f
                    f 1 f . f a a a a a a a f . f 1 f
                    f 1 1 f . f f f f f f f . f 1 1 f
                    f 1 1 1 f f b b b b b f f 1 1 1 f
                    f 1 1 f b b b c 3 c b b b b 1 1 f
                    . f f b b b b c 3 c b b b b f f .
                    . . f b b f b b b b b f b b f . .
                    . . f b f f b b b b b f f b f . .
                    . . . f . f f f f f f f . f . . .
        """),
        SpriteKind.flyingenemy)
    flybug.follow(player1)
    flybug.ay = 100
    tiles.place_on_random_tile(flybug, assets.tile("""
        myTile17
    """))
    pause(10000)
forever(on_forever4)

def on_forever5():
    pass
forever(on_forever5)

def on_forever6():
    if heals == 1:
        life_1.set_image(img("""
            . . . . . f f f f f . . . . . .
                        . . . f f . . . . . f f . . . .
                        . . f . . . . . . . . . f . . .
                        . f . . . . . . . . . . . f . .
                        . f . . . . . . . . . . . f . .
                        f . . . . . . . . . . . . . f .
                        f . . . . . . . . . . . . . f .
                        f . . . . . . . . . . . . . f .
                        f . . . . . . . . . . . . . f .
                        f . . . . . . . . . . . . . f .
                        . f . . . . . . . . . . . f . .
                        . f . . . . . . . . . . . f . .
                        . . f b b b b b b b b b f . . .
                        . . . f f b b b b b f f . . . .
                        . . . . . f f f f f . . . . . .
                        . . . . . . . . . . . . . . . .
        """))
    if heals == 2:
        life_1.set_image(img("""
            . . . . . f f f f f . . . . . .
                        . . . f f . . . . . f f . . . .
                        . . f . . . . . . . . . f . . .
                        . f . . . . . . . . . . . f . .
                        . f . . . . . . . . . . . f . .
                        f . . . . . . . . . . . . . f .
                        f . . . . . . . . . . . . . f .
                        f . . . . . . . . . . . . . f .
                        f . . . . . . . . . . . . . f .
                        f . . . . . . . . . . . . . f .
                        . f . . . . . . . . . . . f . .
                        . f b b b b b b b b b b b f . .
                        . . f b b b b b b b b b f . . .
                        . . . f f b b b b b f f . . . .
                        . . . . . f f f f f . . . . . .
                        . . . . . . . . . . . . . . . .
        """))
    if heals == 3:
        life_1.set_image(img("""
            . . . . . f f f f f . . . . . .
                        . . . f f . . . . . f f . . . .
                        . . f . . . . . . . . . f . . .
                        . f . . . . . . . . . . . f . .
                        . f . . . . . . . . . . . f . .
                        f . . . . . . . . . . . . . f .
                        f . . . . . . . . . . . . . f .
                        f . . . . . . . . . . . . . f .
                        f . . . . . . . . . . . . . f .
                        f . . . . . . . . . . . . . f .
                        . f 1 1 1 1 1 1 1 1 1 1 1 f . .
                        . f 1 1 1 1 1 1 1 1 1 1 1 f . .
                        . . f 1 1 1 1 1 1 1 1 1 f . . .
                        . . . f f 1 1 1 1 1 f f . . . .
                        . . . . . f f f f f . . . . . .
                        . . . . . . . . . . . . . . . .
        """))
    if heals == 4:
        life_1.set_image(img("""
            . . . . . f f f f f . . . . . .
                        . . . f f . . . . . f f . . . .
                        . . f . . . . . . . . . f . . .
                        . f . . . . . . . . . . . f . .
                        . f . . . . . . . . . . . f . .
                        f . . . . . . . . . . . . . f .
                        f . . . . . . . . . . . . . f .
                        f . . . . . . . . . . . . . f .
                        f b b b b b b b b b b b b b f .
                        f b b b b b b b b b b b b b f .
                        . f 1 1 1 1 1 1 1 1 1 1 1 f . .
                        . f 1 1 1 1 1 1 1 1 1 1 1 f . .
                        . . f 1 1 1 1 1 1 1 1 1 f . . .
                        . . . f f 1 1 1 1 1 f f . . . .
                        . . . . . f f f f f . . . . . .
                        . . . . . . . . . . . . . . . .
        """))
    if heals == 5:
        life_1.set_image(img("""
            . . . . . f f f f f . . . . . .
                        . . . f f . . . . . f f . . . .
                        . . f . . . . . . . . . f . . .
                        . f . . . . . . . . . . . f . .
                        . f . . . . . . . . . . . f . .
                        f . . . . . . . . . . . . . f .
                        f . . . . . . . . . . . . . f .
                        f b b b b b b b b b b b b b f .
                        f b b b b b b b b b b b b b f .
                        f b b b b b b b b b b b b b f .
                        . f 1 1 1 1 1 1 1 1 1 1 1 f . .
                        . f 1 1 1 1 1 1 1 1 1 1 1 f . .
                        . . f 1 1 1 1 1 1 1 1 1 f . . .
                        . . . f f 1 1 1 1 1 f f . . . .
                        . . . . . f f f f f . . . . . .
                        . . . . . . . . . . . . . . . .
        """))
    if heals == 6:
        life_1.set_image(img("""
            . . . . . f f f f f . . . . . .
                        . . . f f . . . . . f f . . . .
                        . . f . . . . . . . . . f . . .
                        . f . . . . . . . . . . . f . .
                        . f . . . . . . . . . . . f . .
                        f . . . . . . . . . . . . . f .
                        f 1 1 1 1 1 1 1 1 1 1 1 1 1 f .
                        f 1 1 1 1 1 1 1 1 1 1 1 1 1 f .
                        f 1 1 1 1 1 1 1 1 1 1 1 1 1 f .
                        f 1 1 1 1 1 1 1 1 1 1 1 1 1 f .
                        . f 1 1 1 1 1 1 1 1 1 1 1 f . .
                        . f 1 1 1 1 1 1 1 1 1 1 1 f . .
                        . . f 1 1 1 1 1 1 1 1 1 f . . .
                        . . . f f 1 1 1 1 1 f f . . . .
                        . . . . . f f f f f . . . . . .
                        . . . . . . . . . . . . . . . .
        """))
    if heals == 7:
        life_1.set_image(img("""
            . . . . . f f f f f . . . . . .
                        . . . f f . . . . . f f . . . .
                        . . f . . . . . . . . . f . . .
                        . f . . . . . . . . . . . f . .
                        . f b b b b b b b b b b b f . .
                        f b b b b b b b b b b b b b f .
                        f 1 1 1 1 1 1 1 1 1 1 1 1 1 f .
                        f 1 1 1 1 1 1 1 1 1 1 1 1 1 f .
                        f 1 1 1 1 1 1 1 1 1 1 1 1 1 f .
                        f 1 1 1 1 1 1 1 1 1 1 1 1 1 f .
                        . f 1 1 1 1 1 1 1 1 1 1 1 f . .
                        . f 1 1 1 1 1 1 1 1 1 1 1 f . .
                        . . f 1 1 1 1 1 1 1 1 1 f . . .
                        . . . f f 1 1 1 1 1 f f . . . .
                        . . . . . f f f f f . . . . . .
                        . . . . . . . . . . . . . . . .
        """))
    if heals == 8:
        life_1.set_image(img("""
            . . . . . f f f f f . . . . . .
                        . . . f f . . . . . f f . . . .
                        . . f . . . . . . . . . f . . .
                        . f b b b b b b b b b b b f . .
                        . f b b b b b b b b b b b f . .
                        f b b b b b b b b b b b b b f .
                        f 1 1 1 1 1 1 1 1 1 1 1 1 1 f .
                        f 1 1 1 1 1 1 1 1 1 1 1 1 1 f .
                        f 1 1 1 1 1 1 1 1 1 1 1 1 1 f .
                        f 1 1 1 1 1 1 1 1 1 1 1 1 1 f .
                        . f 1 1 1 1 1 1 1 1 1 1 1 f . .
                        . f 1 1 1 1 1 1 1 1 1 1 1 f . .
                        . . f 1 1 1 1 1 1 1 1 1 f . . .
                        . . . f f 1 1 1 1 1 f f . . . .
                        . . . . . f f f f f . . . . . .
                        . . . . . . . . . . . . . . . .
        """))
    if heals == 9:
        life_1.set_image(img("""
            . . . . . f f f f f . . . . . .
                        . . . f f 1 1 1 1 1 f f . . . .
                        . . f 1 1 1 1 1 1 1 1 1 f . . .
                        . f 1 1 1 1 1 1 1 1 1 1 1 f . .
                        . f 1 1 1 1 1 1 1 1 1 1 1 f . .
                        f 1 1 f f 1 1 1 1 1 f f 1 1 f .
                        f 1 f f f f 1 1 1 f f f f 1 f .
                        f 1 f f f f 1 1 1 f f f f 1 f .
                        f 1 1 f f 1 1 1 1 1 f f 1 1 f .
                        f 1 1 1 1 1 1 1 1 1 1 1 1 1 f .
                        . f 1 1 1 1 1 1 1 1 1 1 1 f . .
                        . f 1 1 1 1 1 1 1 1 1 1 1 f . .
                        . . f 1 1 1 1 1 1 1 1 1 f . . .
                        . . . f f 1 1 1 1 1 f f . . . .
                        . . . . . f f f f f . . . . . .
                        . . . . . . . . . . . . . . . .
        """))
    if heals == 0:
        life_1.set_image(img("""
            . . . . . f f f f f . . . . . .
                        . . . f f . . . . . f f . . . .
                        . . f . . . . . . . . . f . . .
                        . f . . . . . . . . . . . f . .
                        . f . . . . . . . . . . . f . .
                        f . . . . . . . . . . . . . f .
                        f . . . . . . . . . . . . . f .
                        f . . . . . . . . . . . . . f .
                        f . . . . . . . . . . . . . f .
                        f . . . . . . . . . . . . . f .
                        . f . . . . . . . . . . . f . .
                        . f . . . . . . . . . . . f . .
                        . . f . . . . . . . . . f . . .
                        . . . f f . . . . . f f . . . .
                        . . . . . f f f f f . . . . . .
                        . . . . . . . . . . . . . . . .
        """))
forever(on_forever6)
