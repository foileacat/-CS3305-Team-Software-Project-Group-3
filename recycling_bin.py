# code that might be used later, is half written, or might be used for reference
#text based hint
import arcade


def on_draw(self):
        # This command has to happen before we start drawing
        self.clear()
        # this camera is used for everything except the gui
        self.camera_sprites.use()

        """More lighting Code"""
        # with self.light_layer:
        self.scene.draw(pixelated=True)
        # self.current_room.npc.draw_hit_box()
        # self.light_layer.draw(ambient_color=AMBIENT_COLOR)
        # returns interactable objects the player is touching - if we have any, the item has an arrow/text hint
        interactableObjects = arcade.check_for_collision_with_list(
            self.player_sprite, self.scene["interactables"])
        #arcade.gui.UITextArea.w
        # renders inspecting popup/interactable hint if applicable

        if self.player_sprite.currently_inspecting:
            self.camera_gui.use()
            "text formatting"
            #self.inspect_message_UI.text=self.inspect_text
            #self.inspect_message_UI.fit_content()
            self.inspect_message_UI.display_text(self.inspect_text)
            self.gui_inspect_manager.draw()

        elif self.player_sprite.currently_npc_interacting:
            self.camera_gui.use()
            "text formatting"
            #self.inspect_message_UI.text=self.inspect_text
            #self.inspect_message_UI.fit_content()
            self.inspect_message_UI.display_text(self.conversation_list[self.count])
            self.gui_inspect_manager.draw()

        elif self.character_creator_open == True:
            self.camera_gui.use()
            self.gui_character_creator_manager.draw()

        elif interactableObjects:
            interactable = interactableObjects[0]
            self.inspect_item_symbol_UI = arcade.Sprite(filename="assets/assetpacks/ninja/HUD/Arrow.png", scale=3,
                                                        center_x=interactable.center_x, center_y=interactable.center_y+(interactable.height//2)+20)
            if interactable.properties["on_interact"] == "room_transition":
                self.inspect_item_symbol_UI.color = arcade.csscolor.INDIANRED
            elif interactable.properties["on_interact"] == "character_creator":
                self.inspect_item_symbol_UI.color = arcade.csscolor.INDIGO
            self.inspect_item_symbol_UI.draw(pixelated=True)
            self.camera_gui.use()
            self.inventory_bar.draw()

        elif self.current_room.has_npcs:
            npcs = arcade.check_for_collision_with_list(
                self.player_sprite, self.scene["NPC"])
            
            if npcs:
                npc = npcs[0]
                self.inspect_npc_symbol_UI = arcade.Sprite(filename="assets/assetpacks/ninja/HUD/Arrow.png", scale=3,
                                                           center_x=npc.center_x, center_y=(npc.center_y+(npc.height//2)-20))
                self.inspect_npc_symbol_UI.color = arcade.csscolor.SEA_GREEN
                self.inspect_npc_symbol_UI.draw(pixelated=True)
            self.camera_gui.use()
            self.inventory_bar.draw()

        else:
            self.camera_gui.use()
            self.inventory_bar.draw()

        if self.draw_performance:
            self.draw_performance_graph()

"old player char class"
import arcade
from constants import *
import character_lists
from classes.PlayerAccessory import PlayerAccessory

class PlayerCharacterOLD(arcade.Sprite):

    """Creates our player"""

    def __init__(self):
        super().__init__()
        #initialise starting position
        self.center_x = 200
        self.center_y = 500
        self.character_face_direction = RIGHT_FACING
        # Used for flipping between image sequences
        self.cur_texture = 0
        self.scale = CHARACTER_SCALING
        # creates hitbox
        self.points = [[7, -16], [7, -8], [-7, -8], [-7, -16]]

        # Select the desired asset file from our character_lists file
        skintone_file = character_lists.skintones[2]
        hairstyle_file = character_lists.hairstyles[7]
        clothing_file = character_lists.tops[3]
        # initialise accessory list and add PlayerAccesories to it
        self.accessory_list = arcade.SpriteList()
        self.hair = PlayerAccessory(character_lists.hairstyles,7,2)
        self.shirt = PlayerAccessory(character_lists.tops,7,3)
        self.bottoms = PlayerAccessory(character_lists.bottoms,2,6)
        self.full_body = PlayerAccessory(character_lists.full_body,4,6)
        #self.bottoms
        self.shoes = PlayerAccessory(character_lists.shoes,0,1)
        #self.fullbody
        self.accessory_list.append(self.shirt)
        self.accessory_list.append(self.bottoms)
        self.accessory_list.append(self.hair)
        self.accessory_list.append(self.shoes)
        self.accessory_list.append(self.full_body)
        # load textures for standing still and for walking animation
        self.idle_texture_list = load_texture_list(skintone_file, 0, 0, 0)

        self.walk_textures = []
        for frame in range(8):
            texture = load_texture_list(skintone_file, 0, frame, 0)
            self.walk_textures.append(texture)

        self.currently_inspecting = False
    # runs constantly, animates character moving

    def update_animation(self, delta_time: float = 1 / 60):

        # Figure out if we need to flip face left or right
        if self.change_x < 0 and self.change_y == 0:
            self.character_face_direction = LEFT_FACING
        elif self.change_x > 0 and self.change_y == 0:
            self.character_face_direction = RIGHT_FACING
        elif self.change_y < 0 and self.change_x == 0:
            self.character_face_direction = FORWARD_FACING
        elif self.change_y > 0 and self.change_x == 0:
            self.character_face_direction = BACKWARD_FACING

        # Idle animation
        if self.change_x == 0 and self.change_y == 0:
            self.texture = self.idle_texture_list[self.character_face_direction]
            return

        # Walking animation
        self.cur_texture += 1
        if self.cur_texture > 7 * UPDATES_PER_FRAME:
            self.cur_texture = 0
        frame = self.cur_texture // UPDATES_PER_FRAME
        direction = self.character_face_direction
        self.texture = self.walk_textures[frame][direction]


def load_texture_list(filename, row, frame, offset):
    """
    Load a texture list for character skin/hair/accesories. This loads their down,up,right and left facing positions.
    Only loads a single frame.
    Offset is used where multiple colors are in the same sheet - for clothes etc.
    """
    offset = offset*ACCESSORIES_OFFSET
    return [
        arcade.load_texture(filename, x=offset+CHARACTER_NATIVE_SIZE*frame, y=CHARACTER_NATIVE_SIZE *
                            row, width=CHARACTER_NATIVE_SIZE, height=CHARACTER_NATIVE_SIZE),
        arcade.load_texture(filename, x=offset+CHARACTER_NATIVE_SIZE*frame, y=CHARACTER_NATIVE_SIZE*(
            row+1), width=CHARACTER_NATIVE_SIZE, height=CHARACTER_NATIVE_SIZE),
        arcade.load_texture(filename, x=offset+CHARACTER_NATIVE_SIZE*frame, y=CHARACTER_NATIVE_SIZE*(
            row+2), width=CHARACTER_NATIVE_SIZE, height=CHARACTER_NATIVE_SIZE),
        arcade.load_texture(filename, x=offset+CHARACTER_NATIVE_SIZE*frame, y=CHARACTER_NATIVE_SIZE*(
            row+3), width=CHARACTER_NATIVE_SIZE, height=CHARACTER_NATIVE_SIZE)
    ]
