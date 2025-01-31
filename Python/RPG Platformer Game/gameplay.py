import arcade

"""
Resource from the arcade game relate to music, sprite, etc.
https://kenney.nl/
https://api.arcade.academy/en/latest/resources.html
https://www.myinstants.com/
"""


#MAP
GRID_PIXEL_SIZE = 64
DEFAULT_SCREEN_WIDTH = 100 * GRID_PIXEL_SIZE
DEFAULT_SCREEN_HEIGHT = 10 * GRID_PIXEL_SIZE
SCREEN_TITLE = "Platformers Game by Laudza"

#Window
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 640
WINDOW_HALF_WIDTH = WINDOW_WIDTH // 2
#Initialize Sprite and Tile Scaling
SPRITE_SCALING = 1
TILE_SCALING = 1
GRAVITY = 0.25
PLAYER_MOVEMENT_SPEED = 5

#Enemy Boundary for Movement
LIMIT_TOP = 400
LIMIT_BOTTOM = 50

class StartScreen(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        self.clear()
        arcade.draw_text("Platformer Game", WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2,
                         arcade.color.BLACK, font_size=35, anchor_x="center")
        arcade.draw_text("Press Space to Continue", WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 - 75,
                         arcade.color.GRAY, font_size=20, anchor_x="center")
        arcade.draw_text("Python 2 Personal Project \n Mufty Laudza Farhan", WINDOW_WIDTH / 2, 10, arcade.color.BLACK, font_size=15, anchor_x="center")

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.SPACE:
            game_view = GameScreen()
            game_view.setup()
            self.window.show_view(game_view)

class GameScreen(arcade.View):
    def __init__(self):
        super().__init__()
        #Controlling
        self.physic_engine = None
        self.left_pressed = None
        self.right_pressed = None
        #tilemap and window
        self.tile_map = None
        self.game_over = None
        #score
        self.score = 0
        self.lives = 5
        self.key = 0

        #Sounds
        #sound
        self.background_sound = arcade.load_sound("Assets/sounds/new/background1.mp3")
        self.play_sound_bg = arcade.play_sound(self.background_sound, volume= 0.1, looping=True)
        self.jump_sound = arcade.load_sound('Assets/sounds/new/jump.mp3')
        self.items = arcade.load_sound('Assets/sounds/new/coin.mp3')
        self.bloods = arcade.load_sound('Assets/sounds/new/bloods.mp3')
        self.key_sound = arcade.load_sound('Assets/sounds/new/key.wav')

    def setup(self):
        self.tile_map = arcade.load_tilemap('level1.json', scaling=TILE_SCALING)
        self.background = self.tile_map.sprite_lists['Background']
        self.acc = self.tile_map.sprite_lists['Acc']
        self.guide = self.tile_map.sprite_lists['Guide']
        self.decoration = self.tile_map.sprite_lists['Decoration']
        self.ladder = self.tile_map.sprite_lists['Ladder']
        self.obstacles = self.tile_map.sprite_lists['Obstacles']
        self.collect = self.tile_map.sprite_lists['Collect']
        self.ground = self.tile_map.sprite_lists['Ground']
        self.enemies = self.tile_map.sprite_lists['Enemy']
        self.enemy = self.enemies[0]
        self.enemy_1 = self.enemies[1]
        self.enemy_2 = self.enemies[2]
        self.players = self.tile_map.sprite_lists['Players']
        self.player = self.players[0]
        self.flag = self.tile_map.sprite_lists['Flag']
        self.finish = self.tile_map.sprite_lists['Finish']
        self.keys = self.tile_map.sprite_lists['Key']

        #Create the gravity
        self.physic_engine = arcade.PhysicsEnginePlatformer(
            self.player,
            self.ground,
            gravity_constant= GRAVITY,
            ladders=self.ladder
        )
        #set player first position
        self.player.center_x = 50
        self.player.center_y = 500
        self.player.scale = 0.8

    def on_draw(self):
        """Render the screen."""
        arcade.start_render()
        self.background.draw()
        self.acc.draw()
        self.guide.draw()
        self.decoration.draw()
        self.ground.draw()
        self.keys.draw()
        self.ladder.draw()
        self.obstacles.draw()
        self.collect.draw()
        self.enemies.draw()
        self.players.draw()
        self.flag.draw()
        self.finish.draw()
        self.enemies.update()
        self.enemies.update_animation()

        # Add score
        arcade.draw_text(f"Score : {self.score}",arcade.get_viewport()[0] + 25, arcade.get_viewport()[2]+ 600, arcade.csscolor.WHITE, bold= True, font_size= 30 )
        arcade.draw_text(f"Lives : {self.lives}",arcade.get_viewport()[0] + 25, arcade.get_viewport()[2]+ 550, arcade.csscolor.WHITE, bold= True, font_size= 30 )

    def clamp(self, value, mini, maxi):
        return max(min(value, maxi), mini)

    def on_update(self, delta_time: float):
        self.physic_engine.update()
        self.player.update()
        self.player.center_x = self.clamp(self.player.center_x, 0, DEFAULT_SCREEN_WIDTH)
        #player movement
        self.player.change_x = 0
        if self.left_pressed and not self.right_pressed:
            self.player.change_x = -PLAYER_MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player.change_x = PLAYER_MOVEMENT_SPEED

        #Create Scrolling Screen
        """
            If the player position is > Window half width
        """
        if self.player.center_x > WINDOW_HALF_WIDTH and self.player.center_x < DEFAULT_SCREEN_WIDTH - GRID_PIXEL_SIZE - WINDOW_HALF_WIDTH:
            change_view = True
        else:
            change_view = False
        if change_view:
            arcade.set_viewport(self.player.center_x - WINDOW_HALF_WIDTH, self.player.center_x + WINDOW_HALF_WIDTH + 50, 0, WINDOW_HEIGHT)

        #Check the collision with collect items
        star_hit = arcade.check_for_collision_with_list(
            self.player,
            self.collect
        )
        if star_hit:
            for star in star_hit:
                arcade.play_sound(self.items)
                self.score += 1
                star.remove_from_sprite_lists()

        #check collision with obstacle
        obstacle_hit = arcade.check_for_collision_with_list(
            self.player,
            self.obstacles
        )
        if obstacle_hit:
            arcade.play_sound(self.bloods)
            self.lives -= 1
            self.player.center_x = 50
            self.player.center_y = 500
            arcade.set_viewport(0, WINDOW_WIDTH, 0,
                                WINDOW_HEIGHT)

        #check collision with enemy
        enemy_hit = arcade.check_for_collision_with_list(
            self.player,
            self.enemies
        )
        if enemy_hit:
            arcade.play_sound(self.bloods)
            self.lives -= 1
            self.player.center_x = 50
            self.player.center_y = 500
            arcade.set_viewport(0, WINDOW_WIDTH, 0,
                                WINDOW_HEIGHT)

        key_hit = arcade.check_for_collision_with_list(
            self.player,
            self.keys
        )

        if key_hit :
            self.key += 1
            for key in self.keys:
                arcade.play_sound(self.key_sound)
                key.remove_from_sprite_lists()

        #create a collision for the door
        finish_hit = arcade.check_for_collision_with_list(
            self.player,
            self.finish
        )

        if self.key == 1 and finish_hit:
            arcade.stop_sound(self.play_sound_bg)
            arcade.set_viewport(0, WINDOW_WIDTH, 0,
                                WINDOW_HEIGHT)
            win = WinnerScreen()
            self.window.show_view(win)



        #ENEMY1
        if self.enemy.center_y > LIMIT_BOTTOM and self.enemy.center_y < LIMIT_TOP :
            self.enemy.change_y += 0.1
        if self.enemy.center_y > LIMIT_TOP:
            self.enemy.change_y -= 0.1

        #ENEMY2
        if self.enemy_1.center_y > LIMIT_BOTTOM and self.enemy_1.center_y < LIMIT_TOP :
            self.enemy_1.change_y += 0.1
        if self.enemy_1.center_y > LIMIT_TOP:
            self.enemy_1.change_y -= 0.1

        # ENEMY3
        LIMIT_ENEMY3_LEFT = 2800
        LIMIT_ENEMY3_RIGHT = 3244
        if self.enemy_2.center_x > LIMIT_ENEMY3_LEFT and self.enemy_2.center_x < LIMIT_ENEMY3_RIGHT:
            self.enemy_2.change_x += 0.1
        if self.enemy_2.center_x > LIMIT_ENEMY3_RIGHT:
            self.enemy_2.change_x -= 0.1

        ### IF GAME OVER
        if self.lives <= 0 :
            self.game_over = True
        if self.game_over == True :
            arcade.stop_sound(self.play_sound_bg)
            lose_view = GameOverScreen()
            self.window.show_view(lose_view)
            self.score = 0
            self.lives = 5
            self.game_over = False

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.SPACE:
            if self.physic_engine.can_jump():
                arcade.play_sound(self.jump_sound)
                self.player.change_y = 7

        if symbol == arcade.key.A:
            self.left_pressed = True
        if symbol == arcade.key.D:
            self.right_pressed = True

        if symbol == arcade.key.W:
            if self.physic_engine.is_on_ladder():
                self.player.change_y = 1

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.A:
            self.left_pressed = False
        if symbol == arcade.key.D:
            self.right_pressed =  False
        if symbol == arcade.key.W:
            if self.physic_engine.is_on_ladder():
                self.player.change_y = 0
        if symbol == arcade.key.ESCAPE:
            self.paused = False

class GameOverScreen(arcade.View):

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        self.clear()
        arcade.draw_text("Game Over ", WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2,
                         arcade.color.WHITE, font_size=35, anchor_x="center")
        arcade.draw_text("Do you want to restart?", WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 - 75,
                         arcade.color.GRAY, font_size=20, anchor_x="center")
        arcade.draw_text("Type 'R' to restart or 'Q' to Quit!", WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 - 100,
                         arcade.color.GRAY, font_size=20, anchor_x="center")

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.R:
            game_view = GameScreen()
            game_view.setup()
            self.window.show_view(game_view)

        if symbol == arcade.key.Q:
            arcade.close_window()

class WinnerScreen(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        self.clear()
        arcade.draw_text("YOU WIN !!! ", WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2,
                         arcade.color.WHITE, font_size=35, anchor_x="center")
        arcade.draw_text("Do you want to restart?", WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 - 75,
                         arcade.color.WHITE, font_size=20, anchor_x="center")
        arcade.draw_text("Type 'R' to restart or 'Q' to Quit!", WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 - 100,
                         arcade.color.WHITE, font_size=20, anchor_x="center")
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.R:
            game_view = GameScreen()
            game_view.setup()
            self.window.show_view(game_view)

        if symbol == arcade.key.Q:
            arcade.close_window()



def main():
    window = arcade.Window(WINDOW_WIDTH,WINDOW_HEIGHT,SCREEN_TITLE)
    menuview = StartScreen()
    window.show_view(menuview)
    arcade.run()

if __name__ == '__main__':
    main()

# FILE_PATH = os.path.dirname(os.path.abspath(__file__))
# SOUND_BG = os.path.join(FILE_PATH, 'Assets',"HarvestOst.mp3")
# LOGO = os.path.join(FILE_PATH,'Assets', "Title.png")
#
#
# def setup(self):
#     arcade.play_sound(self.sound, looping=True, volume=0.1)
#     self.logo.py = arcade.load_texture(LOGO)""
# self.sound = arcade.load_sound(SOUND_BG, streaming=True)
# arcade.draw_text(f"Item : {self.total_item}", 50, 600 , arcade.csscolor.WHITE, font_size=20)