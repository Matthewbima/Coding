# Importing arcade module
import arcade

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
GRAVITY = 1.0
PLAYER_JUMP_SPEED = 20
PLAYER_MOVEMENT_SPEED = 20
FALL_THRESHOLD = -100  # Player dies if they fall below this point


# Creating MainGame class
class MainGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, title="Platformer with Collision and Jump")

        # Velocity for both players
        self.vel_x = 0
        self.vel_x2 = 0

        # Create a scene object to manage our sprites
        self.scene = None

        # Player sprites
        self.player_sprite = None
        self.player_sprite_2 = None

        # Physics engines for platformer behavior
        self.physics_engine = None
        self.physics_engine_2 = None

        # Set up the game
        self.setup()

    # Setup the game, create the sprites and the scene
    def setup(self):
        # Create a new scene
        self.scene = arcade.Scene()

        # Create sprite lists
        self.scene.add_sprite_list("Player")
        self.scene.add_sprite_list("Platforms", use_spatial_hash=True)
        self.scene.add_sprite_list("Enemies", use_spatial_hash=True)

        # Add player 1 sprite
        self.player_sprite = arcade.Sprite("monster-right.png", 1)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 300  # Start in the middle
        self.scene.add_sprite("Player", self.player_sprite)

        # Add player 2 sprite (enemy)
        self.player_sprite_2 = arcade.Sprite("monster-left.png", 1)
        self.player_sprite_2.center_x = 128
        self.player_sprite_2.center_y = 300  # Start in the middle
        self.scene.add_sprite("Enemies", self.player_sprite_2)

        # Add a platform (ground)
        platform = arcade.Sprite("floor.png", 1)
        platform.center_x = 300
        platform.center_y = 32
        self.scene.add_sprite("Platforms", platform)

        # Add another platform higher up
        platform2 = arcade.Sprite("floor.png", 1)
        platform2.center_x = 500
        platform2.center_y = 300
        self.scene.add_sprite("Platforms", platform2)

        # Add physics engines for both players
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite, self.scene.get_sprite_list("Platforms"), GRAVITY
        )
        self.physics_engine_2 = arcade.PhysicsEnginePlatformer(
            self.player_sprite_2, self.scene.get_sprite_list("Platforms"), GRAVITY
        )

    # Drawing the scene
    def on_draw(self):
        arcade.start_render()
        self.scene.draw()

    # Handle movement and check for falling deaths
    def on_update(self, delta_time):
        # Update players' movement and physics
        self.physics_engine.update()
        self.physics_engine_2.update()

        # Horizontal movement for both players
        self.player_sprite.center_x += self.vel_x * delta_time * PLAYER_MOVEMENT_SPEED
        self.player_sprite_2.center_x += self.vel_x2 * delta_time * PLAYER_MOVEMENT_SPEED

        if arcade.check_for_collision(self.player_sprite, self.player_sprite_2):
            print("Players have collided!")

        # Check if any player falls below the screen
        if self.player_sprite.center_y < FALL_THRESHOLD:
            print("Player 1 has fallen off the platform!")
            self.player_sprite.center_x, self.player_sprite.center_y = 64, 300  # Reset position

        if self.player_sprite_2.center_y < FALL_THRESHOLD:
            print("Player 2 has fallen off the platform!")
            self.player_sprite_2.center_x, self.player_sprite_2.center_y = 128, 300  # Reset position

    # Handle key presses for movement and jump
    def on_key_press(self, symbol, modifier):
        # Player 1 movement
        if symbol == arcade.key.LEFT:
            self.vel_x = -PLAYER_MOVEMENT_SPEED
        elif symbol == arcade.key.RIGHT:
            self.vel_x = PLAYER_MOVEMENT_SPEED
        elif symbol == arcade.key.UP and self.physics_engine.can_jump():
            self.player_sprite.change_y = PLAYER_JUMP_SPEED

        # Player 2 movement
        if symbol == arcade.key.A:
            self.vel_x2 = -PLAYER_MOVEMENT_SPEED
        elif symbol == arcade.key.D:
            self.vel_x2 = PLAYER_MOVEMENT_SPEED
        elif symbol == arcade.key.W and self.physics_engine_2.can_jump():
            self.player_sprite_2.change_y = PLAYER_JUMP_SPEED

    # Stop movement when the key is released
    def on_key_release(self, symbol, modifier):
        if symbol == arcade.key.LEFT or symbol == arcade.key.RIGHT:
            self.vel_x = 0

        if symbol == arcade.key.A or symbol == arcade.key.D:
            self.vel_x2 = 0


# Calling MainGame class
game = MainGame()
arcade.run()
