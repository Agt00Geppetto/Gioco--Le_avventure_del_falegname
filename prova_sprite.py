import arcade
import os
import random
#import inventario

"""
class Item:
    def __init__(self, name, texture_path, quantity=1):
        self.name = name
        self.texture = arcade.load_texture(texture_path)
        self.quantity = quantity

class UIInventory(arcade.Window):
    def __init__ (self):
        super().__init__()
    pass
"""

class MyGame(arcade.Window):
    #impaginazione globale
    SCREEN_WIDTH : int = 900
    SCREEN_HEIGHT : int = 600

    def __init__(self, width, height, title):
        super().__init__(width, height, title, fullscreen=True,)

        #sprites
        self.p1 = None
        self.barile = None
        self.secchio = None

        #fisica del gioco (base)
        self.pyshics_engine = None
        self.lista_p1 = arcade.SpriteList()
        self.lista_muri = arcade.SpriteList(use_spatial_hash=True)
        self.lista_piattafforme = arcade.SpriteList()
        self.lista_scale = arcade.SpriteList()

        self.jump_since_ground = 0
        self.max_jumps = 2
        
        self.setup()

    def setup(self):
        #self.camera = arcade.Camera2D()
        self.p1 = arcade.Sprite("./assets/Geppetto.png")
        self.p1.center_x = 100
        self.p1.center_y = 315
        self.p1.scale = 0.5
        self.lista_p1.append(self.p1)
        
        self.crea_muri()

        self.physics_engine = arcade.PhysicsEnginePlatformer(
            player_sprite = self.p1,
            walls = self.lista_muri,
            platforms = self.lista_piattafforme,
            ladders = self.lista_scale,
            gravity_constant = 1.0,
        )

        self.physics_engine.enable_multi_jump(1)
        

        self.background = arcade.load_texture("./assets/sfondoG3.png")

    def on_update(self, delta_time):
        self.lista_p1.update()
        self.physics_engine.update()

        #self.camera.position = self.p1.position

        if self.physics_engine.can_jump():  
             self.jump_since_ground = 0

    def crea_muri(self):
        self.barile = arcade.Sprite("./assets/barile.png")
        self.barile.center_x = random.randint(50, 500)
        self.barile.center_y = 200
        self.barile.scale = 0.75
        self.lista_muri.append(self.barile)
        
        self.secchio = arcade.Sprite("./assets/secchio.png")
        self.secchio.center_x = random.randint(50, 500)
        self.secchio.center_y = 170
        self.secchio.scale = 0.5
        self.lista_muri.append(self.secchio)

        for x in range (-10000, 10000, 1000):
            terreno = arcade.Sprite("./assets/terreno.png")
            terreno.center_x = x
            terreno.center_y = 75
            terreno.scale = 1.75
            self.lista_muri.append(terreno)

    def jump(self):
        if self.physics_engine.can_jump() or self.jump_since_ground < self.max_jumps:
            self.physics_engine.jump(10)

            self.jump_since_ground += 1
 
    def on_draw(self):
        self.clear() 
        arcade.draw_texture_rect(
            self.background,
            arcade.LBWH(0,0,1400,800)
            # types.Viewport(self.camera.position[0] - MyGame.SCREEN_WIDTH/1.4, 
            # self.camera.position[1] - MyGame.SCREEN_HEIGHT/3,
            # MyGame.SCREEN_WIDTH + 500, 
            # MyGame.SCREEN_HEIGHT + 200)
        )
        

        self.lista_p1.draw()
        self.lista_muri.draw()
        
        #self.camera.use()
        
    def on_key_press(self, tasto, modificatori):
        if tasto == arcade.key.SPACE:
            # self.jump()
            pass
        elif tasto == arcade.key.A:
            self.p1.change_x = -5
        elif tasto == arcade.key.D:
            self.p1.change_x = +5

    def on_key_release(self, tasto, modificatori):
        if tasto == arcade.key.SPACE:
            self.jump()
        elif tasto in (arcade.key.A, arcade.key.D):
            self.p1.change_x = 0


def main():
    game = MyGame(
        800, 800, "Il mio giochino"
    )
    arcade.run()


if __name__ == "__main__":
    main()