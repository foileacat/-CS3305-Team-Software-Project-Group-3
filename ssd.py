import arcade

FPS = 60

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640
SCREEN_TITLE = "Pipi"

CHARACTER_SCALING = 1.5
TILE_SCALING = 1.5

SPRITE_PIXEL_SIZE = 128
GRID_PIXEL_SIZE = SPRITE_PIXEL_SIZE * TILE_SCALING

PLAYER_MOVEMENT_SPEED = 3.5
GRAVITY = 1
PLAYER_JUMP_SPEED = 15

PLAYER_START_X = 64
PLAYER_START_Y = 128

LAYER_NAME_PLATFORMS = "Platforms"
LAYER_NAME_BACKGROUND = "Background"
LAYER_NAME_PLAYER = "Player"


class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.tile_map = None

        self.scene = None

        self.player_sprite = None

        self.physics_engine = None

        self.camera = None

        self.gui_camera = None

        self.end_of_map = 0

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):

        self.camera = arcade.Camera()
        self.gui_camera = arcade.Camera()

        self.scene = arcade.Scene()

        map_name = ":resources:tiled_maps/map.json"

        layer_options = {
            "Platforms": {
                "use_spatial_hash": True,
            },
        }

        self.tile_map = arcade.load_tilemap(map_name, TILE_SCALING, layer_options)

        self.scene = arcade.Scene.from_tilemap(self.tile_map)

        image_source = ":resources:images/animated_characters/female_person/femalePerson_idle.png"
        self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
        self.player_sprite.center_x = PLAYER_START_X
        self.player_sprite.center_y = PLAYER_START_Y
        self.scene.add_sprite("Player", self.player_sprite)

        if self.tile_map.background_color:
            arcade.set_background_color(self.tile_map.background_color)

        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite, gravity_constant=GRAVITY, walls=self.scene["Platforms"]
        )

    def on_draw(self):

        arcade.start_render()

        self.clear()

        self.camera.use()

        self.scene.draw()

        self.gui_camera.use()

    def on_key_press(self, key: int, modifiers: int):

        if key == arcade.key.SPACE or key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = PLAYER_JUMP_SPEED
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):

        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def center_camera_to_player(self):
        screen_center_x = self.player_sprite.center_x - (self.camera.viewport_width / 2)
        screen_center_y = self.player_sprite.center_y - (
                self.camera.viewport_height / 2
        )
        if screen_center_x < 0:
            screen_center_x = 0
        if screen_center_y < 0:
            screen_center_y = 0
        player_centered = screen_center_x, screen_center_y

        self.camera.move_to(player_centered)

    def on_update(self, delta_time):

        self.physics_engine.update()

        self.center_camera_to_player()


def main():
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()