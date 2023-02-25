import arcade
import arcade.gui
from arcade.experimental.lights import Light, LightLayer
import os
import character_lists
from gui.inspect_gui import setup_inspect_gui
from gui.npc_chat_gui import setup_npc_gui
from gui.character_creator_gui import setup_character_creator_gui
from classes.PlayerCharacter import PlayerCharacter
from classes.Inventory import Inventory
from classes.InventoryBar import InventoryBar
from classes.Item import Item
from maps import *
from constants import *
from gui.TypewriterText import TypewriterTextWidget
arcade.enable_timings()

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title, resizable=True)

        # Set the working directory
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        self.draw_performance = False
        self.perf_graph_list = None
        self.conversation_list = ["sdsdd","bijfjkdfkj sds sdsd sd d dd sd sdsss sd sd sd sd sdsdssd sds ds dsdsdsds ds d sds dsdsdsds sd s ds dsdsds sd sd sd sdsd sd sd sd s dsdsdsfwrg wrg rg wg ew ew gw gwe g kfjdkjfj", "ckdjfdkjfjk dfjkdjfk", "dksdsjkdjk dkjsdjk", "eskjdsjkd sdkjsdjk"]
        self.frame_count = 0
        self.current_room_index = 0
        self.rooms = None
        self.player_sprite = None
        self.physics_engine = None
        self.camera_sprites = arcade.Camera(
            SCREEN_WIDTH, SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(
            SCREEN_WIDTH, SCREEN_HEIGHT)
        self.count = 0 
        "dumb"
        self.any_sprite_x=700
        self.any_sprite_y=510

    def on_resize(self, width, height):
        self.camera_sprites.resize(int(width), int(height))
        self.camera_gui.resize(int(width), int(height))
        #update_constants(self)
        super().on_resize(width, height)

        print(f"Window resized to: {width}, {height}")

    def setup(self):
        """ Set up the game and initialize variables. """
        self.character_creator_open = False
        self.inspect_text = "ok"
        
        # imports game font. name of font is "NinjaAdventure"
        arcade.load_font(FONT_PATH)
        self.player_sprite = PlayerCharacter()
        self.player_sprite.set_hit_box(self.player_sprite.points)
        self.player_accessory_list = self.player_sprite.accessory_list
        
        self.inventory_bar = self.player_sprite.inventory_bar
    
        setup_inspect_gui(self)
        setup_character_creator_gui(self)
        setup_npc_gui(self)
        self.rooms = [starting_room.setup(self), main_room.setup(self), cave_outside.setup(self), cave_inside.setup(self), dojo_outside.setup(self), dojo.setup(
            self), blacksmith.setup(self), living_room.setup(self), bedroom.setup(self), kitchen.setup(self), forest.setup(self), enemy_house.setup(self)]
        
        self.current_room_index = 1
        self.current_room = self.rooms[self.current_room_index]
        self.scene = self.current_room.scene

        # used for the scrolling camera
        self.view_left = 0
        self.view_bottom = 0

        #####
        self.inventory_open = False
        ###
        # #create physics engine - adds collision
        self.physics_engine = arcade.PhysicsEngineSimple(
            self.player_sprite, walls=self.current_room.wall_list)
        
        '''''Performance Metrics'''
        self.perf_graph_list = arcade.SpriteList()

        # Create the FPS performance graph
        graph = arcade.PerfGraph(GRAPH_WIDTH, GRAPH_HEIGHT, graph_data="FPS")
        graph.center_x = GRAPH_WIDTH / 2
        graph.center_y = self.height - GRAPH_HEIGHT / 2
        self.perf_graph_list.append(graph)

        # Create the on_update graph
        graph = arcade.PerfGraph(
            GRAPH_WIDTH, GRAPH_HEIGHT, graph_data="update")
        graph.center_x = GRAPH_WIDTH / 2 + (GRAPH_WIDTH + GRAPH_MARGIN)
        graph.center_y = self.height - GRAPH_HEIGHT / 2
        self.perf_graph_list.append(graph)

        # Create the on_draw graph
        graph = arcade.PerfGraph(
            GRAPH_WIDTH, GRAPH_HEIGHT, graph_data="on_draw")
        graph.center_x = GRAPH_WIDTH / 2 + (GRAPH_WIDTH + GRAPH_MARGIN) * 2
        graph.center_y = self.height - GRAPH_HEIGHT / 2
        self.perf_graph_list.append(graph)

        """Preliminary Lighting Code - For later"""
        # self.light_layer = LightLayer(SCREEN_WIDTH, SCREEN_HEIGHT)
        # light = Light(736, 400, 100, (120,30,0), "soft")
        # light2 = Light(95*4, 650, 400, (80,80,100), "soft")
        # self.light_layer.add(light)
        # self.light_layer.add(light2)
        self.inspect_item_symbol_UI = arcade.Sprite(filename="assets/assetpacks/ninja/HUD/Arrow.png", scale=3,
                                                    center_x=0, center_y=0)

    def on_draw(self):
        # This command has to happen before we start drawing
        self.clear()
        # this camera is used for everything except the gui
        self.camera_sprites.use()
        self.scene.draw(pixelated=True)
        interactableObjects = arcade.check_for_collision_with_list(
            self.player_sprite, self.scene["interactables"])
        
        if self.player_sprite.is_holding_item():
                filename = self.inventory_bar.current_slot().item.filename
                holding_item = arcade.Sprite(filename=filename,
                                            center_x=self.player_sprite.center_x,
                                            center_y=self.player_sprite.center_y+20,
                                            scale=3)
                holding_item.draw(pixelated=True)
        # self.spritea = arcade.Sprite(filename="assets/guiassets/CustomAssets/qq1map.png",center_y=100,center_x=500,scale=6)
        # self.spritea.draw(pixelated=True)
        #self.player_sprite.generate_floating_head(180,130).draw(pixelated=True)
        
        if self.player_sprite.currently_inspecting:
            self.camera_gui.use()
            self.inspect_message_UI.display_text(self.inspect_text)
            self.gui_inspect_manager.draw()

        elif self.player_sprite.currently_npc_interacting:
            self.camera_gui.use()
            self.npc_message_UI.display_text(self.conversation_list[self.count])
            self.gui_npc_manager.draw()

        elif self.character_creator_open == True:
            self.camera_gui.use()
            self.gui_character_creator_manager.draw()

        elif interactableObjects:
            interactable = interactableObjects[0]
            self.inspect_item_symbol_UI.center_x=interactable.center_x
            self.inspect_item_symbol_UI.center_y=interactable.center_y+(interactable.height//2)+20
            if interactable.properties["on_interact"] == "room_transition":
                self.inspect_item_symbol_UI.color = arcade.csscolor.INDIANRED
            elif interactable.properties["on_interact"] == "character_creator":
                self.inspect_item_symbol_UI.color = arcade.csscolor.INDIGO
            self.inspect_item_symbol_UI.draw(pixelated=True)
            self.camera_gui.use()
            self.inventory_bar.draw()

        elif self.current_room.has_npcs:
            npcs = arcade.check_for_collision_with_list(self.player_sprite, 
                                                        self.scene["NPC"])
            if npcs:
                npc = npcs[0]
                self.inspect_item_symbol_UI.center_x=npc.center_x
                self.inspect_item_symbol_UI.center_y=npc.center_y+(npc.height//2)-20
                self.inspect_item_symbol_UI.color = arcade.csscolor.SEA_GREEN
                self.inspect_item_symbol_UI.draw(pixelated=True)
            self.camera_gui.use()
            self.inventory_bar.draw()

        else:
            self.camera_gui.use()
            self.inventory_bar.draw()

        if self.draw_performance:
            self.draw_performance_graph()
        self.camera_gui.use()
        self.inventory_experiment()

    def inventory_experiment(self):
        if self.inventory_open:
            self.book = arcade.Sprite(filename="assets/guiassets/CustomAssets/Larger-Book-Test-2.png", scale=5,center_x=600,center_y=400)
            self.book.draw(pixelated=True)
            self.inventory_cursor=arcade.Sprite(filename=INVENTORY_BAR_CURSOR_ASSET,scale=4,center_x=700,center_y=510)
            self.inventory_cursor2=arcade.Sprite(filename=INVENTORY_BAR_CURSOR_ASSET,scale=4,center_x=700+70,center_y=510)
            self.inventory_cursor3=arcade.Sprite(filename=INVENTORY_BAR_CURSOR_ASSET,scale=4,center_x=700+140,center_y=510)
            self.inventory_cursor4=arcade.Sprite(filename=INVENTORY_BAR_CURSOR_ASSET,scale=4,center_x=700+210,center_y=510)
            self.inventory_cursor5=arcade.Sprite(filename=INVENTORY_BAR_CURSOR_ASSET,scale=4,center_x=700+280,center_y=510)
            self.inventory_text=arcade.Text(text="Inventory",start_x=750,start_y=580,color=arcade.color.BLACK,font_name="NinjaAdventure",font_size=26)
            self.inventory_cursor.draw(pixelated=True)
            self.inventory_text.draw()
            self.inventory_cursor2.draw(pixelated=True)
            self.inventory_cursor3.draw(pixelated=True)
            self.inventory_cursor4.draw(pixelated=True)
            self.inventory_cursor5.draw(pixelated=True)
            
    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if self.player_unpaused():
            if key == UP_KEY:
                self.player_sprite.change_y = MOVEMENT_SPEED
            elif key == DOWN_KEY:
                self.player_sprite.change_y = -MOVEMENT_SPEED
            elif key == LEFT_KEY:
                self.player_sprite.change_x = -MOVEMENT_SPEED
            elif key == RIGHT_KEY:
                self.player_sprite.change_x = MOVEMENT_SPEED
            elif key == INVENTORY_BAR_CURSOR_LEFT:
                self.inventory_bar.move_cursor("left")
                self.player_sprite.using_tool = False
            elif key == INVENTORY_BAR_CURSOR_RIGHT:
                self.inventory_bar.move_cursor("right")
                self.player_sprite.using_tool = False
            elif INVENTORY_BAR_SLOT_A <= key <= INVENTORY_BAR_SLOT_H:
                self.inventory_bar.select_slot(key)
                self.player_sprite.using_tool = False
        if key == arcade.key.I:
            self.inventory_open = not self.inventory_open
        if key == arcade.key.C:
            self.player_sprite.use_tool()
        if key == INTERACT_KEY:
            self.handle_interact()
        if key == arcade.key.B:
            self.draw_performance = not self.draw_performance

        "For inventory configuration - in progress"

        if key == arcade.key.T:
            self.any_sprite_y+=10
            print("x= ", self.any_sprite_x, ", y= ",self.any_sprite_y)
        if key == arcade.key.G:
            self.any_sprite_y-=10
            print("x= ", self.any_sprite_x, ", y= ",self.any_sprite_y)
        if key == arcade.key.F:
            self.any_sprite_x-=10
            print("x= ", self.any_sprite_x, ", y= ",self.any_sprite_y)
        if key == arcade.key.H:
            self.any_sprite_x+=10
            print("x= ", self.any_sprite_x, ", y= ",self.any_sprite_y)
        
    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
      
        if key == UP_KEY or key == DOWN_KEY:
            self.player_sprite.change_y = 0
        elif key == LEFT_KEY or key == RIGHT_KEY:
            self.player_sprite.change_x = 0

    def handle_interact(self):
        """
        Runs when a player presses the interact key next to an interactable object. 
        It will run the function named in the interactable objects on_interact attribute, from the tmx file
        """
        if self.current_room.has_npcs:
            npcs = arcade.check_for_collision_with_list(
                self.player_sprite, self.scene["NPC"])
            for npc in npcs:
                self.handle_npc_interaction(npc)
        interactables = arcade.check_for_collision_with_list(
            self.player_sprite, self.scene["interactables"])
        for interactable in interactables:
            getattr(self, interactable.properties['on_interact'])(interactable)
        return

    def character_creator(self, interactable):
        if self.character_creator_open == True:
            self.character_creator_open = False
            return
        else:
            self.player_sprite.character_face_direction = FORWARD_FACING
            self.character_creator_open = True

    def room_transition(self, interactable):
        """
        Currently unfinished. Runs when player interacts with a transitional interactable object .
        Transitions player from one room to the next.

        """

        entrance = interactable.properties["transition_id"]
        entrance_coordinates = self.current_room.entrances[entrance]
        self.player_sprite.center_x = entrance_coordinates[0]
        self.player_sprite.center_y = entrance_coordinates[1]
        self.current_room_index = int(
            interactable.properties["destination_room"])
        self.current_room = self.rooms[self.current_room_index]

        self.scene = self.current_room.scene

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                         self.current_room.wall_list)
        self.player_sprite.character_face_direction = int(
            interactable.properties["transition_direction"])
        
    def player_unpaused(self):
        if self.player_sprite.currently_inspecting:
            return False
        if self.character_creator_open:
            return False 
        if self.player_sprite.currently_npc_interacting:
            return False
        return True
    

    def show_message(self, interactable):
        if self.player_sprite.currently_inspecting:
            self.player_sprite.currently_inspecting = False
            return
        else:
            self.player_sprite.currently_inspecting = True
            self.inspect_message_UI.reset()
            self.inspect_text = interactable.properties["inspect_text"]

    

    def handle_npc_interaction(self, npc):
        if self.player_sprite.currently_npc_interacting:
            if self.count == len(self.conversation_list) - 1:
                self.player_sprite.currently_npc_interacting=False
                npc.interacting = False
                return
            else:
                self.count+=1
                print(self.conversation_list[self.count])
                self.inspect_message_UI.display_text(self.conversation_list[self.count])
        else:
            self.inspect_message_UI.reset()
            self.player_sprite.currently_npc_interacting = True
            self.count = 0
            npc.interacting = True
            x_diff = self.player_sprite.center_x - npc.center_x
            y_diff = self.player_sprite.center_y - npc.center_y
            self.player_sprite.currently_npc_interacting
            if x_diff < 0 and abs(x_diff) > abs(y_diff):
                self.player_sprite.character_face_direction = RIGHT_FACING
                npc.character_face_direction = LEFT_FACING
            elif x_diff > 0 and abs(x_diff) > abs(y_diff):
                self.player_sprite.character_face_direction = LEFT_FACING
                npc.character_face_direction = RIGHT_FACING
            elif y_diff > 0 and abs(x_diff) < abs(y_diff):
                self.player_sprite.character_face_direction = FORWARD_FACING
                npc.character_face_direction = BACKWARD_FACING
            elif y_diff < 0 and abs(x_diff) < abs(y_diff):
                self.player_sprite.character_face_direction = BACKWARD_FACING
                npc.character_face_direction = FORWARD_FACING
            return
         

    def on_update(self, delta_time):
        """ Movement and game logic. Runs constantly when anything changes."""
        self.physics_engine.update()
        self.scene.on_update(delta_time=1/60)
        if self.current_room.has_npcs:
            self.scene.update_animation(delta_time, ["NPC"])
        self.scene.update_animation(delta_time, ["Animation", "Player"])
        self.scroll_to_player()

    def scroll_to_player(self):
        """
        Manages scrolling camera. Runs constantly from the on_update function
        """
        # Scroll left
        left_boundary = self.view_left + VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left

        # Scroll right
        right_boundary = self.view_left + self.width - VIEWPORT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary

        # Scroll up
        top_boundary = self.view_bottom + self.height - VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary

        # Scroll down
        bottom_boundary = self.view_bottom + VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom

        # Scroll to the proper location
        position = self.view_left, self.view_bottom
        self.camera_sprites.move_to(position, CAMERA_SPEED)

    def draw_performance_graph(self):
        self.camera_gui.use()
        self.perf_graph_list.draw()
        text = f"FPS: {arcade.get_fps(60):5.1f}"
        arcade.draw_text(text, 10, 10, arcade.color.BLACK, 22)

def main():
    """ Main function """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()