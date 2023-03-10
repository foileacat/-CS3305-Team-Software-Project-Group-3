import arcade
#watering_can maybe the bonus one might suit if sticking with pixel sounds or maybe FX
water = "assets/assetpacks/sounds/166819__quistard__water-bubble-7.wav"
water_bonus = "assets/assetpacks/ninja/Sounds/Game/Bonus.wav"
water_FX = "assets/assetpacks/ninja/Sounds/Game/Fx.wav"

#sword/pickaxe swing - hit5 could work too if we want to keep the pixel music vibe
swing = "assets/assetpacks/sounds/367182__orangesheepdog__swing.mp3"
hit5 = "assets/assetpacks/ninja/Sounds/Game/Hit5.wav"


#pickaxe hit with rock - hit could work as well if we want to keep the same vibe with the music
pickaxe_collide ="assets/assetpacks/sounds/536104__eminyildirim__sword-hit-heavy.wav"
hit = "assets/assetpacks/ninja/Sounds/Game/Hit.wav"
#hit could also work if we want noise for sword colliding with enemy-used for both pickaxe+sword colliding with rock or enemy


#enemy hit - enemy kinda gives ghast vibes so maybe hit4? 
#any of the hits from 1-6 would kind have that vibe but I think 4 fits better, its less whooshy
#hit7 could work too cus it sounds more like its an actual entity and not just air - or just used hit like above
hit4_enemy_reaction = "assets/assetpacks/ninja/Sounds/Game/Hit4.wav"
hit7_enemy_reaction = "assets/assetpacks/ninja/Sounds/Game/Hit7.wav"
hit = "assets/assetpacks/ninja/Sounds/Game/Hit.wav"

#enemy death - could use any of the hits like above as well
enemy_death = "assets/assetpacks/ninja/Sounds/Game/Spirit.wav"

#adding to inventory voice3 is a short sound might be missed easily so 
#maybe the jump one might work better - longer noise
#or maybe FX as well - longer noise
inv_add_voice3 = "assets/assetpacks/ninja/Sounds/Game/Voice3.wav"
inv_add_jump = "assets/assetpacks/ninja/Sounds/Game/Jump.wav"
inv_add_FX = "assets/assetpacks/ninja/Sounds/Game/Fx.wav"

#walking sound effects maybe not needed if we have background music but just in case since 
#no walking in ninja sound effect batch, I found a pixelly one too

#pixelly steps could work inside or out
#FOR TRANSITION
room_transition = "assets/assetpacks/sounds/501102__evretro__8-bit-footsteps.wav"
steps = "assets/assetpacks/sounds/501102__evretro__8-bit-footsteps.wav"

#walking inside
steps_inside = "assets/assetpacks/sounds/406739__kretopi__steponwood-007.wav"

#walking_outside
steps_outside = "assets/assetpacks/sounds/463854__drowsyprincess__snd_footsteps_grass.wav"

#background music for in general outside music - could be used in houses too - very happy energy maybe too much?
background = "assets/assetpacks/ninja/Musics/3 - Revelation.ogg"
background2 = "assets/assetpacks/ninja/Musics/4 - Village.ogg"
#more calm background music if above too happy - maybe use this one inside buildings, the others for exploring?
background3 = "assets/assetpacks/ninja/Musics/5 - Peaceful.ogg"

#background music for fighting areas with enemies
fight_background = "assets/assetpacks/ninja/Musics/10 - Dark Castle.ogg"
fight_background2 = "assets/assetpacks/ninja/Musics/17 - Fight.ogg"

#fight outside the old_man
fight_background3 = "assets/assetpacks/ninja/Musics/24 - Final Area.ogg"

maze = "assets/assetpacks/ninja/Musics/21 - Dungeon.ogg"
#forest fight
dungeon_fight = "assets/assetpacks/ninja/Musics/2 - The Cave.ogg"
dungeon_fight_after = "assets/assetpacks/ninja/Musics/14 - Curse.ogg"
forest_hideout = "assets/assetpacks/ninja/Musics/14 - Curse.ogg"
#lonely_man
sad_theme = "assets/assetpacks/ninja/Musics/7 - Sad Theme.ogg"
dream = "assets/assetpacks/ninja/Musics/22 - Dream.ogg"

inside_blacksmith_wife_house = "assets/assetpacks/ninja/Musics/18 - Aquatic.ogg"

start_music = "assets/assetpacks/ninja/Musics/1 - Adventure Begin.ogg"
temple = "assets/assetpacks/ninja/Musics/12 - Temple.ogg"
#maybe this could be used for when a dialogue is started with the npc? any of the golds do 1-3
npc_dialogue = "assets/assetpacks/ninja/Sounds/Game/Gold1.wav"
npc_dialogue2 = "assets/assetpacks/ninja/Sounds/Game/Gold2.wav"
npc_dialogue3 = "assets/assetpacks/ninja/Sounds/Game/Gold3.wav"

#starting_room_music = arcade.Sound(start_music)
#dungeon_fight_music = arcade.Sound(dungeon_fight)
#peaceful_music = arcade.Sound("assets/assetpacks/ninja/Musics/11 - Clearing.ogg")

blacksmith_music = "assets/assetpacks/ninja/Musics/23 - Road.ogg"
peaceful_music = arcade.Sound("assets/assetpacks/ninja/Musics/13 - Mystical.ogg")

enemy_house_fight_music = arcade.Sound("assets/assetpacks/ninja/Musics/17 - Fight.ogg")

#enemy_house_victory_music = arcade.Sound("assets/assetpacks/ninja/Musics/20 - Good Time.ogg")
curse_music = arcade.Sound(dungeon_fight_after)
blacksmith_wife_house_music = arcade.Sound(inside_blacksmith_wife_house)
blacksmith_music = arcade.Sound(blacksmith_music)
#lonely_man_after_music = arcade.Sound("assets/assetpacks/ninja/Musics/7 - Sad Theme.ogg")
lonely_man_before_music = arcade.Sound("assets/assetpacks/ninja/Musics/22 - Dream.ogg")
maze_music = arcade.Sound(maze)
dojo_music = arcade.Sound(temple)