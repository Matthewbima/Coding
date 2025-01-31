import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2
SPRITE_SCALING_NEGATIVE_COIN = 0.2  # Scaling for the negative coin
COIN_COUNT = 50
NEGATIVE_COIN_COUNT = 20  # Number of negative coins

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # Variables that will hold sprite lists
        self.player_list = None
        self.coin_list = None
        self.negative_coin_list = None  # List for negative coins

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.negative_coin_list = arcade.SpriteList()  # Initialize negative coin list

        # Score
        self.score = 0

        # Set up the player
        self.player_sprite = arcade.Sprite("character.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the positive coins
        for i in range(COIN_COUNT):
            coin = arcade.Sprite("coin_01.png", SPRITE_SCALING_COIN)
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)
            self.coin_list.append(coin)

        # Create the negative coins
        for i in range(NEGATIVE_COIN_COUNT):
            negative_coin = arcade.Sprite("coin_01.png", SPRITE_SCALING_NEGATIVE_COIN)
            negative_coin.center_x = random.randrange(SCREEN_WIDTH)
            negative_coin.center_y = random.randrange(SCREEN_HEIGHT)
            # Change color of negative coin
            negative_coin.color = arcade.color.RED  # You can modify the color if needed
            self.negative_coin_list.append(negative_coin)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.coin_list.draw()
        self.negative_coin_list.draw()  # Draw negative coins
        self.player_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time):
        """ Movement and game logic """
        self.coin_list.update()
        self.negative_coin_list.update()  # Update negative coins

        # Check for collisions with positive coins
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1

        # Check for collisions with negative coins
        negative_coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.negative_coin_list)
        for negative_coin in negative_coins_hit_list:
            negative_coin.remove_from_sprite_lists()
            self.score -= 1  # Decrease score for negative coins


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
