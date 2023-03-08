import arcade
import arcade.gui

class TypewriterTextWidget(arcade.gui.UITextArea):
    def __init__(self,*,
                 x: float = 0,
                 y: float = 0,
                 width: float = 400,
                 height: float = 40,
                 text: str = "Empty Text",
                 font_name=('Arial',),
                 font_size: float = 12,
                 text_color: arcade.Color = arcade.color.BLACK,
                 multiline: bool = True,
                 scroll_speed: float = None,
                 size_hint=None,
                 size_hint_min=None,
                 size_hint_max=None,
                 **kwargs):
        super().__init__(x=x, y=y, width=width, height=height, text=text, font_name=font_name, font_size=font_size, text_color=text_color,
                         multiline=multiline, scroll_speed=scroll_speed, size_hint=size_hint, size_hint_min=size_hint_min, size_hint_max=size_hint_max)
        self.current_char = 0
        self.full_text="Nothing"

    def display_text(self,text):
        if self.full_text != text:
            self.full_text = text
            self.current_char=0
        if self.current_char >= len(text):
            self.current_char=len(text)
            self.trigger_full_render()
            return
        self.current_char+=1
        self.text = text[:self.current_char]
        self.trigger_full_render()

    def reset(self):
        self.current_char=0
        self.full_text=""

    def not_fully_displayed(self):
        if self.current_char <= len(self.full_text) - 1:
            return True
        else:
            return False

    def display_full_text(self):
        self.text = self.full_text
        self.current_char = len(self.full_text)
        self.trigger_full_render()


#a = TypewriterTextWidget(x=350, y=130, text_color=(0, 0, 0), text="")
#ass = arcade.gui.UITextArea(x,y,width,height,text,font_name,font_size,text_color,multiline,scroll_speed,size_hint,size_hint_min,size_hint_max,style)
