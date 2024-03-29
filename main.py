import arcade
import arcade.gui
import os
from gui.health_gui import setup_health_gui, update_health_bar, reposition_health_bar
from gui.inspect_gui import setup_inspect_gui
from gui.npc_chat_gui import setup_npc_gui
from gui.draw_inventory import draw_inventory
from gui.character_creator_gui import setup_character_creator_gui
from classes.PlayerCharacter import PlayerCharacter
from items import *
from maps import *
from constants import *
from npc_dialogue.load_npc_dialogue import load_npc_dialogue
from quests.setup_quests import setup_quests
import sound_constants
import json_functions


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title, resizable=True)
        arcade.enable_timings()
        # Set the working directory
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        self.current_room_name = "starting_room"
        self.conversation_list = json_functions.get_one_conversation(
            "npc_dialogue/main_room.json", "first_convo")
        self.set_minimum_size(MIN_SCREEN_WIDTH, MIN_SCREEN_HEIGHT)
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
        self.respawn_timer = 0
        self.current_song = sound_constants.peaceful_music
        self.music_player = arcade.play_sound(
            self.current_song, volume=VOLUME, looping=True)
        setup_quests(self)

    def on_resize(self, width, height):
        self.camera_sprites.resize(int(width), int(height))
        self.camera_gui.resize(int(width), int(height))
        super().on_resize(width, height)
        self.inventory_bar.resize(self)
        print(f"Window resized to: {width}, {height}")

    def setup(self):
        """ Set up the game and initialize variables. """
        self.character_creator_open = False
        self.inspect_text = "ok"

        # imports game font. name of font is "NinjaAdventure"
        arcade.load_font(FONT_PATH)
        self.player_sprite = PlayerCharacter()
        self.player_accessory_list = self.player_sprite.accessory_list
        setup_health_gui(self)
        self.inventory_bar = self.player_sprite.inventory_bar
        self.inventory = self.player_sprite.inventory

        setup_inspect_gui(self)
        setup_character_creator_gui(self)
        setup_npc_gui(self)
        self.rooms = [starting_room.setup(self), main_room.setup(self), cave_outside.setup(self), cave_inside.setup(self), dojo_outside.setup(self), dojo.setup(
            self), blacksmith.setup(self), living_room.setup(self), bedroom.setup(self), kitchen.setup(self), forest.setup(self), enemy_house.setup(self),
            dungeon.setup(self), forest_hideout.setup(self), lonely_house.setup(self), maze.setup(self)]

        self.current_room_index = 0
        self.current_room_name = "starting_room"
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

        if self.current_room.has_mineable:
            self.scene["Ore List"].clear()
            for item in list(self.scene["pickaxe_inventory"]):

                if item.properties["item_id"] == "amber_ore" or item.properties["item_id"] == "amethyst_ore":
                    if item.properties["pickaxe_condition"] >= 3:
                        filename = "assets/customassets/" + \
                            item.properties["item_id"]+"_full.png"
                        ore = arcade.Sprite(
                            filename=filename, scale=4, center_x=item.center_x, center_y=item.center_y)
                        self.scene["Ore List"].append(ore)
                    elif item.properties["pickaxe_condition"] >= 1:
                        filename = "assets/customassets/" + \
                            item.properties["item_id"]+"_half.png"
                        ore = arcade.Sprite(
                            filename=filename, scale=4, center_x=item.center_x, center_y=item.center_y)
                        self.scene["Ore List"].append(ore)
                else:
                    if item.properties["pickaxe_condition"] == 3:
                        filename = "assets/customassets/" + \
                            item.properties["item_id"]+"_full.png"
                        ore = arcade.Sprite(
                            filename=filename, scale=SPRITE_SCALING+0.1, center_x=item.center_x, center_y=item.center_y)
                        self.scene["Ore List"].append(ore)
                    elif item.properties["pickaxe_condition"] >= 1:
                        # assets/customassets/emerald_ore_full.png
                        filename = "assets/customassets/" + \
                            item.properties["item_id"]+"_half.png"
                        ore = arcade.Sprite(
                            filename=filename, scale=SPRITE_SCALING+0.1, center_x=item.center_x, center_y=item.center_y)
                        self.scene["Ore List"].append(ore)

        if self.current_room.has_enemies:
            for enemy in self.current_room.enemy_list:
                walls = arcade.check_for_collision_with_list(enemy,self.current_room.wall_sprite_list)
                if walls:
                    enemy.check_in_bounds()
                if self.player_sprite.health > 0:
                    if arcade.has_line_of_sight(point_1=self.player_sprite.position,
                                                point_2=enemy.position,
                                                walls=self.current_room.wall_sprite_list,
                                                check_resolution=5,
                                                max_distance=10 * SPRITE_SIZE):
                        if self.player_sprite.health <= 0:
                            enemy.following = False
                        else:
                            enemy.following = True
                            enemy.target = self.player_sprite
                    else:
                        enemy.following = False

            enemies = arcade.check_for_collision_with_list(self.player_sprite,
                                                           self.scene["Enemy"])
            
            if enemies:
                enemy = enemies[0]
                if self.player_sprite.using_tool:
                    enemy.take_damage(self.player_sprite)
                else:
                    self.player_sprite.take_damage(enemy)
                    enemy.reset_cooldown()

        if self.player_sprite.is_holding_item():
            if self.player_sprite.current_item().is_tool == False:
                filename = self.inventory_bar.current_slot().item.filename
                holding_item = arcade.Sprite(filename=filename,
                                             center_x=self.player_sprite.center_x,
                                             center_y=self.player_sprite.center_y+20,
                                             scale=3)
                holding_item.draw(pixelated=True)

        if self.player_sprite.currently_inspecting:
            self.camera_gui.use()
            self.inspect_message_UI.display_text(self.inspect_text)
            self.gui_inspect_manager.draw()

        elif self.player_sprite.currently_npc_interacting:
            self.camera_gui.use()
            load_npc_dialogue(self, self.current_npc)
            self.current_npc.generate_floating_head(100, 100)
            self.npc_message_UI.display_text(
                self.current_npc.get_current_conversation()[self.count])
            self.gui_npc_manager.draw()
            center_x = self.width // 2
            center_y = self.height // 2
            self.current_npc.generate_floating_head(
                center_x-283, center_y-230).draw(pixelated=True)

        elif self.character_creator_open == True:
            self.camera_gui.use()
            self.background_sprite.draw(pixelated=True)
            self.gui_character_creator_manager.draw()
        else:
            self.camera_gui.use()
            self.inventory_bar.draw()
        self.camera_sprites.use()

        if interactableObjects:
            interactable = interactableObjects[0]
            self.inspect_item_symbol_UI.center_x = interactable.center_x
            self.inspect_item_symbol_UI.center_y = interactable.center_y + \
                (interactable.height//2)+20
            if interactable.properties["on_interact"] == "room_transition":
                self.inspect_item_symbol_UI.color = arcade.csscolor.INDIANRED
            elif interactable.properties["on_interact"] == "character_creator":
                self.inspect_item_symbol_UI.color = arcade.csscolor.INDIGO
            else:
                self.inspect_item_symbol_UI.color = arcade.color.CORNFLOWER_BLUE
            if interactable.properties["on_interact"] == "renovate":
                self.inspect_item_symbol_UI.color = arcade.color.YELLOW
                if self.allowed_to_renovate(interactable):
                    self.inspect_item_symbol_UI.draw(pixelated=True)
            else:
                self.inspect_item_symbol_UI.draw(pixelated=True)
        # NOAH CODE

        elif self.current_room.has_mineable or self.current_room.has_inventory:
            if self.current_room.has_mineable:
                pickaxeObjects = arcade.check_for_collision_with_list(
                    self.player_sprite, self.scene["pickaxe_inventory"])
                if pickaxeObjects and self.player_sprite.using_tool:
                    pickaxeInteractable = pickaxeObjects[0]
                    if pickaxeInteractable.properties["pickaxe_condition"] > 0:
                        self.player_sprite.mine(pickaxeInteractable)
                elif pickaxeObjects:
                    pickaxeInteractable = pickaxeObjects[0]
                    self.inspect_item_symbol_UI = arcade.Sprite(filename="assets/assetpacks/ninja/HUD/Arrow.png", scale=3,
                                                                center_x=pickaxeInteractable.center_x, center_y=pickaxeInteractable.center_y+(pickaxeInteractable.height//2)+20)
                    self.inspect_item_symbol_UI.draw(pixelated=True)
            if self.current_room.has_inventory:
                inventoryObjects = arcade.check_for_collision_with_list(
                    self.player_sprite, self.scene["inventory"])
                if inventoryObjects:
                    invInteractable = inventoryObjects[0]
                    self.inspect_item_symbol_UI = arcade.Sprite(filename="assets/assetpacks/ninja/HUD/Arrow.png", scale=3,
                                                                center_x=invInteractable.center_x, center_y=invInteractable.center_y+(invInteractable.height//2)+20)
                    self.inspect_item_symbol_UI.draw(pixelated=True)
            else:
                return

        elif self.current_room.has_npcs:
            npcs = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.scene["NPC"])
            if npcs:
                npc = npcs[0]
                self.inspect_item_symbol_UI.center_x = npc.center_x
                self.inspect_item_symbol_UI.center_y = npc.center_y + \
                    (npc.height//2)-20
                self.inspect_item_symbol_UI.color = arcade.csscolor.SEA_GREEN
                self.inspect_item_symbol_UI.draw(pixelated=True)

        if self.inventory_open:
            self.camera_gui.use()
            draw_inventory(self)
        self.camera_gui.use()
        if self.player_sprite.currently_inspecting == False and self.player_sprite.currently_npc_interacting == False and self.inventory_open == False and self.character_creator_open == False:
            update_health_bar(self)
            self.health_bar.draw()


    def allowed_to_renovate(self, interactable):
        if self.lonely_man_quest.steps[interactable.properties["quest"]].is_active():
            if interactable.properties["complete"] == False:
                return True
        else:
            return False

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if self.inventory_open:
            if key == INVENTORY_BAR_CURSOR_LEFT:
                self.inventory.move_cursor("left")
            elif key == INVENTORY_BAR_CURSOR_RIGHT:
                self.inventory.move_cursor("right")
            elif key == INVENTORY_BAR_CURSOR_UP:
                self.inventory.move_cursor("up")
            elif key == INVENTORY_BAR_CURSOR_DOWN:
                self.inventory.move_cursor("down")
        elif self.player_unpaused() and self.player_sprite.dead==False and self.player_sprite.dying==False and self.player_sprite.using_tool==False:
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
            elif key == arcade.key.C:
                self.use_selected_item()
        if key == arcade.key.I:
            self.inventory_bar.resize(self)
            self.inventory_open = not self.inventory_open
        if key == INTERACT_KEY:
            self.handle_interact()

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == UP_KEY or key == DOWN_KEY:
            self.player_sprite.change_y = 0
        elif key == LEFT_KEY or key == RIGHT_KEY:
            self.player_sprite.change_x = 0

    def use_selected_item(self):
        if self.player_sprite.is_holding_item():
            if self.player_sprite.current_item().is_tool:
                self.player_sprite.use_tool()
            if self.player_sprite.current_item().is_consumable:
                self.player_sprite.use_consumable()
        return

    def handle_interact(self):
        """
        Runs when a player presses the interact key next to an interactable object. 
        It will run the function named in the interactable objects on_interact attribute, from the tmx file
        """
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0
        if self.player_sprite.using_tool:
            return
        if self.current_room.has_npcs:
            npcs = arcade.check_for_collision_with_list(
                self.player_sprite, self.scene["NPC"])
            for npc in npcs:
                self.handle_npc_interaction(npc)

        interactables = arcade.check_for_collision_with_list(
            self.player_sprite, self.scene["interactables"])

        # change
        if interactables:
            interactable = interactables[0]
            getattr(self, interactable.properties['on_interact'])(interactable)

        if self.current_room.has_mineable or self.current_room.has_inventory:
            if self.current_room.has_mineable:
                pickaxeInteractables = arcade.check_for_collision_with_list(
                    self.player_sprite, self.scene["pickaxe_inventory"])
                if pickaxeInteractables:
                    pickaxeInteractable = pickaxeInteractables[0]
                    getattr(self, pickaxeInteractable.properties['on_interact'])(
                        pickaxeInteractable)
            if self.current_room.has_inventory:
                invInteractables = arcade.check_for_collision_with_list(
                    self.player_sprite, self.scene["inventory"])
                if invInteractables:
                    invInteractable = invInteractables[0]
                    getattr(self, invInteractable.properties['on_interact'])(
                        invInteractable)

        return

    def renovate(self, interactable):
        if self.allowed_to_renovate(interactable):
            renovation_dict = {1: "renovation1", 2: "renovation2", 3: "renovation3", 4: "renovation4",
                               5: "renovation5", 6: "renovation6", 7: "renovation7", 8: "renovation8", 9: "renovation9"}
            renovation = renovation_dict[int(
                interactable.properties["renovate_num"])]
            self.current_room.scene[renovation].visible = True
            if renovation == 2 and self.current_room.scene["renovation2_replace"]:
                self.current_room.scene["renovation2_replace"].visible = not (
                    self.current_room.scene["renovation2"].visible)
            interactable.properties["complete"] = True
            self.lonely_man_quest.check_subquest(self, interactable)
            consumable_item = interactable.properties["consumable_item"]
            quantity = interactable.properties["quantity"]
            if consumable_item == "None":
                return
            else:
                self.player_sprite.remove_from_inventory(
                    consumable_item, quantity=quantity)

    def check_pickaxe_condition(self, pickaxeInteractable):
        if self.player_sprite.currently_inspecting:
            if self.inspect_message_UI.not_fully_displayed():
                self.inspect_message_UI.display_full_text()
            else:
                self.player_sprite.currently_inspecting = False
            return
        else:
            ore_type = pickaxeInteractable.properties["item_id"]
            if ore_type == "amber_ore" or ore_type == "amethyst_ore":
                max_ore = 5
            else:
                max_ore = 3
            if pickaxeInteractable.properties["pickaxe_condition"] == max_ore:
                self.player_sprite.currently_inspecting = True
                self.inspect_message_UI.reset()
                if self.player_sprite.has_item("Old Pickaxe"):
                    self.inspect_text = "I think this is what the blacksmith wanted! Maybe I should use the pickaxe on it?"
                else:
                    self.inspect_text = "Oooo sparkly! These are so pretty!"

            elif pickaxeInteractable.properties["pickaxe_condition"] == 0:
                self.player_sprite.currently_inspecting = True
                self.inspect_message_UI.reset()
                self.inspect_text = "Nice! I think ive gathered everything I can from this rock."
            else:
                self.player_sprite.currently_inspecting = True
                self.inspect_message_UI.reset()
                self.inspect_text = "I think theres still some ore I can mine in this..."

    def check_inv_condition(self, invInteractable):
        if self.player_sprite.currently_inspecting:
            if self.inspect_message_UI.not_fully_displayed():
                self.inspect_message_UI.display_full_text()
            else:
                self.player_sprite.currently_inspecting = False
            return
        else:
            if invInteractable.properties["collected"]:
                self.player_sprite.currently_inspecting = True
                self.inspect_message_UI.reset()
                self.inspect_text = invInteractable.properties["item_collected_message"]
            else:
                if invInteractable.properties["conditional"]:
                    required_item = invInteractable.properties["inv_condition"]
                    if self.player_sprite.has_item(required_item):
                        self.player_sprite.currently_inspecting = True
                        self.player_sprite.remove_from_inventory(required_item)
                        self.inspect_message_UI.reset()
                        self.inspect_text = invInteractable.properties["item_collection_message"]
                        if required_item == "Gem Key":
                            self.blacksmith_quest.steps["get_gem"].make_complete(
                            )
                            self.blacksmith_quest.complete = True
                            self.player_sprite.gem_2 = True
                            invInteractable.properties["collected"] = True
                        else:
                            self.player_sprite.add_to_inventory(
                                get_item(invInteractable.properties["item_id"]))
                            invInteractable.properties["collected"] = True
                    else:
                        self.player_sprite.currently_inspecting = True
                        self.inspect_message_UI.reset()
                        self.inspect_text = invInteractable.properties["item_refuse_message"]
                else:
                    item = invInteractable.properties["item_id"]
                    if item == "white_flower quest" or item == "yellow_flower_quest" or item == "red_flower_quest":
                        if self.blacksmith_quest.steps["collect_flowers"].is_active() == False:
                            self.player_sprite.currently_inspecting = True
                            self.inspect_message_UI.reset()
                            self.inspect_text = "This is lovely, but so delicate! I won't touch it, I don't wanna damage it!"
                            return
                    self.player_sprite.currently_inspecting = True
                    self.inspect_message_UI.reset()
                    self.inspect_text = invInteractable.properties["item_collection_message"]
                    self.player_sprite.add_to_inventory(
                        get_item(invInteractable.properties["item_id"]))
                    invInteractable.properties["collected"] = True

    def character_creator(self, interactable):
        if self.character_creator_open == True:
            self.character_creator_open = False
            self.gui_character_creator_manager.disable()
            return
        else:
            self.player_sprite.character_face_direction = FORWARD_FACING
            setup_character_creator_gui(self)
            self.character_creator_open = True
            self.gem_quest.steps["customise"].make_complete()
            self.gem_quest.steps["talk_to_mom"].activate()

    def room_transition(self, interactable):
        """
        Currently unfinished. Runs when player interacts with a transitional interactable object .
        Transitions player from one room to the next.

        """
        if self.player_sprite.currently_inspecting:
            if self.inspect_message_UI.not_fully_displayed():
                self.inspect_message_UI.display_full_text()
            else:
                self.player_sprite.currently_inspecting = False
            return
        if self.room_transition_allowed(interactable.properties["transition_id"]) == True:
            entrance = interactable.properties["transition_id"]
            entrance_coordinates = self.current_room.entrances[entrance]
            self.player_sprite.center_x = entrance_coordinates[0]
            self.player_sprite.center_y = entrance_coordinates[1]
            self.current_room_index = int(
                interactable.properties["destination_room"])
            self.current_room = self.rooms[self.current_room_index]
            self.current_room_name = interactable.properties["transition_id"]
            self.scene = self.current_room.scene

            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.current_room.wall_list)
            self.player_sprite.character_face_direction = int(
                interactable.properties["transition_direction"])
        else:
            deny_text = self.room_transition_allowed(
                interactable.properties["transition_id"])
            self.player_sprite.currently_inspecting = True
            self.inspect_message_UI.reset()
            self.inspect_text = deny_text

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
            if self.inspect_message_UI.not_fully_displayed():
                self.inspect_message_UI.display_full_text()
            else:
                self.player_sprite.currently_inspecting = False
                self.inspect_message_UI.reset()
            return
        else:
            self.player_sprite.currently_inspecting = True
            self.inspect_message_UI.reset()
            self.inspect_text = interactable.properties["inspect_text"]
            if interactable.properties["item_id"] == "wifes_diary_flower":
                if self.blacksmith_quest.steps["read_diary"].is_active():
                    self.blacksmith_quest.diary_read = True
                    self.blacksmith_quest.steps["read_diary"].make_complete()
                    self.blacksmith_quest.steps["tell_blacksmith"].activate()

    def handle_npc_interaction(self, npc):
        if self.player_sprite.currently_npc_interacting:
            if self.npc_message_UI.not_fully_displayed():
                self.npc_message_UI.display_full_text()
            else:
                self.current_npc = npc
                if self.count == len(self.current_npc.get_current_conversation()) - 1:
                    self.player_sprite.currently_npc_interacting = False
                    npc.interacting = False
                    if self.dojo_quest.steps["challenge_of_wisdom"].is_active():
                        if self.current_npc.id == "sensei":
                            self.dojo_quest.wisdom_challenge_complete = True
                    npc.end_convo()
                    self.count = 0
                    return
                else:
                    self.count += 1
        else:
            self.npc_message_UI.reset()
            self.player_sprite.currently_npc_interacting = True
            self.count = 0
            npc.interacting = True
            self.current_npc = npc
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
        if self.player_sprite.dead:
            if self.respawn_timer > 100:
                self.player_sprite.respawn(self)
                self.current_room.reload_enemies()
                self.respawn_timer = 0
            else:
                self.respawn_timer += 1
        """ Movement and game logic. Runs constantly when anything changes."""
        if self.current_room.has_npcs:
            npcs = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.scene["NPC"])
            if npcs:
                pass
            else:
                if self.player_sprite.bottom > self.current_room.npc.center_x:
                    self.scene.move_sprite_list_after("NPC", "Player Stuff")
                    self.scene.move_sprite_list_after("NPC Stuff", "NPC")
                else:
                    self.scene.move_sprite_list_after("Player", "NPC Stuff",)
                    self.scene.move_sprite_list_after("Player Stuff", "Player")
        self.physics_engine.update()
        self.scene.on_update(delta_time=1/60)
        if self.current_room.has_npcs:
            self.scene.update_animation(delta_time, ["NPC"])
        if self.current_room.has_enemies:
            self.current_room.enemy_list.update()
            self.scene.update_animation(delta_time, ["Enemy"])

        self.scene.update_animation(delta_time, ["Animation", "Player"])
        self.scroll_to_player()
        self.determine_music()

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

    def room_transition_allowed(self, destination_room):
        """start quests when entering rooms:"""
        if destination_room == "forest":
            if self.gem_quest.steps["witch"].is_active() or self.gem_quest.steps["witch"].is_completed():
                if self.witch_quest.active == False:
                    self.witch_quest.start()
                    return True
            else:
                return "I dont know what's over here, I'll wait for mom to tell me to go here."

        if destination_room == "cave_outside":
            if self.gem_quest.steps["blacksmith"].is_active() or self.gem_quest.steps["blacksmith"].is_completed():
                if self.blacksmith_quest.active == False:
                    self.blacksmith_quest.start()
                    return True
            else:
                return "I hear wailing! I'll wait for mom to tell me to go here."

        if destination_room == "dungeon":
            if self.gem_quest.steps["lonely"].is_active() or self.gem_quest.steps["lonely"].is_completed():
                if self.lonely_man_quest.active == False:
                    self.lonely_man_quest.start()
                    return True
            else:
                return "This place is spooky, I'll wait for mom to tell me to go here."

        if destination_room == "dojo_outside":
            if self.gem_quest.steps["dojo"].is_active() or self.gem_quest.steps["dojo"].is_completed():
                if self.dojo_quest.active == False:
                    self.dojo_quest.start()
                    return True
            else:
                return "I think the Dojo is this way. I'll wait for mom to tell me to go here."

        "Wont let you leave area with incomplete quest:"
        if destination_room == "main_room":
            if self.current_room_name == "starting_room":
                if self.gem_quest.steps["customise"].is_completed() == False:
                    return "I dont feel like myself. I should change my outfit at my dresser!"
            if self.current_room_name == "forest":
                if self.witch_quest.complete == False:
                    return "No, I should stay here until I can get the gem from the witch."

            if self.current_room_name == "cave_outside":
                if self.blacksmith_quest.complete == False:
                    return "I don't want to leave before I can find the gem here!."

            if self.current_room_name == "dojo_outside":
                if self.dojo_quest.complete == False:
                    return "I think I'll stay here until I find the gem"

        if destination_room == "dungeon":
            if self.current_room_name == "forest_hideout":
                if self.lonely_man_quest.complete == False:
                    return "I'll stay here until I find out what's up with this family, and get the gem."
        """Witch quest logic"""
        if destination_room == "enemy_house":
            if self.witch_quest.steps["talk_to_witch"].is_active():
                return "I should talk to the witch outside first."

        "Blacksmith Logic"
        if self.current_room_name == "cave_outside":
            if destination_room == "living_room":
                if self.blacksmith_quest.steps["speak_to_blacksmith"].is_active():
                    return "I came here to see the blacksmith, I'll go there first."

        if self.current_room_name == "living_room":
            if destination_room == "bedroom":
                if self.blacksmith_quest.steps["speak_to_wife"].is_active():
                    return "I dont want to be rude. I'll talk to the blacksmiths wife first."

            if destination_room == "cave_outside":
                if self.blacksmith_quest.steps["read_diary"].is_active():
                    return "I need to figure out that flower. I can't leave until I find a clue!"
        "Dojo Logic"
        if destination_room == "dojo":
            if self.current_room_name == "maze":
                self.dojo_quest.maze_complete = True

            if self.current_room_name == "dojo_outside":
                if self.dojo_quest.steps["talk_to_apprentice"].is_active():
                    return "I should talk to the apprentice outside first."

        if self.current_room_name == "dojo":
            if destination_room == "dojo_outside":
                if self.dojo_quest.steps["talk_to_sensei"].is_active():
                    return "I should talk to the sensei first"
                if self.dojo_quest.steps["challenge_of_wisdom"].is_completed() == False:
                    return "I should see what the next challenge is!"
                if self.dojo_quest.steps["challenge_of_courage"].is_completed() == False:
                    if self.dojo_quest.steps["challenge_of_strength"].is_completed():
                        return "I should do the last challenge before I leave!"
            if destination_room == "maze":
                if self.dojo_quest.steps["challenge_of_courage"].is_active() == False:
                    return "This is spooky. I shouldn't go in here without asking the sensei first."

        return True

    def determine_music(self):
        if self.current_room_name == "enemy_house":
            enemy_room = self.rooms[11]
            if len(enemy_room.enemy_list) == 0:
                song = sound_constants.peaceful_music
            else:
                song = sound_constants.enemy_house_fight_music
        elif self.current_room_name == "blacksmith":
            song = sound_constants.blacksmith_music
        elif self.current_room_name == "living_room" or self.current_room_name == "bedroom" or self.current_room_name == "kitchen":
            song = sound_constants.blacksmith_wife_house_music
        elif self.current_room_name == "dungeon":
            enemy_room = self.rooms[12]
            if self.lonely_man_quest.complete:
                song = sound_constants.lonely_man_before_music
            else:
                song = sound_constants.curse_music
        elif self.current_room_name == "forest_hideout":
            if self.lonely_man_quest.complete:
                song = sound_constants.lonely_man_before_music
            else:
                song = sound_constants.curse_music
        elif self.current_room_name == "lonely_house":
            if self.lonely_man_quest.complete:
                song = sound_constants.lonely_man_before_music
            else:
                song = sound_constants.curse_music
        elif self.current_room_name == "dojo_outside" or self.current_room_name == "dojo":
            song = sound_constants.dojo_music
        elif self.current_room_name == "maze":
            song = sound_constants.maze_music
        else:
            song = sound_constants.peaceful_music
        if self.current_song == song:
            return
        else:
            arcade.stop_sound(self.music_player)
            self.current_song = song
            self.music_player = arcade.play_sound(
                self.current_song, VOLUME, looping=True)


def main():
    """ Main function """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
