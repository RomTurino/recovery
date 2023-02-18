from kivy.core.window import Window
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.text import LabelBase
from database_module import *

Window.size = (400, 600)
Window.clearcolor = (110 / 255, 217 / 255, 106 / 255, 1)
RAZZLE_DAZZLE = (250 / 255, 52 / 255, 200 / 255, 1)
PANTONE_MAGENTA = "#d0417e"
AMATIC_FONT = 'AmaticSC-Bold.ttf'


class ScreenMain(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
 
        logo = Image(source="0000_films/logo.png",
                     pos_hint={"center_y": 0.9})
        button_film = Button(
            text="Да прибудет кино!",
            background_color=RAZZLE_DAZZLE,
            background_down=PANTONE_MAGENTA,
            size_hint=[0.9, 0.2],
            font_name=AMATIC_FONT,
            font_size='35sp',
            pos_hint={"center_y": 0.7, "center_x": .5}
        )
        button_add = Button(
            text="Добавить фильм в список",
            background_color=RAZZLE_DAZZLE,
            background_down=PANTONE_MAGENTA,
            size_hint=[0.9, 0.2],
            font_name=AMATIC_FONT,
            font_size='35sp',
            pos_hint={"center_y": 0.45, "center_x": .5},
            on_press=self.to_button_add
        )
        button_delete = Button(
            text="Удалить просмотренный фильм",
            background_color=RAZZLE_DAZZLE,
            background_down=PANTONE_MAGENTA,
            size_hint=[0.9, 0.2],
            font_name=AMATIC_FONT,
            font_size='35sp',
            pos_hint={"center_y": 0.2, "center_x": .5},
            on_press=self.to_button_delete
        )
        self.add_widget(logo)
        self.add_widget(button_film)
        self.add_widget(button_add)
        self.add_widget(button_delete)
    
    def to_button_add(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'add_screen'
        
    def to_button_delete(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'delete_screen'


class ScreenAdd(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        logo = Image(source="0000_films/logo.png",
                     pos_hint={"center_y": 0.9})

        label = Label(text='Что добавим?',
                      color=RAZZLE_DAZZLE,
                      font_size='45sp',
                      font_name=AMATIC_FONT,
                      pos_hint={"center_y": 0.75, "center_x": .5})
        self.input_title = TextInput(hint_text='Название',
                               multiline=False,
                               size_hint=[0.7, 0.1],
                               pos_hint={"center_y": 0.6, "center_x": .5},
                               font_size='30sp',
                               font_name=AMATIC_FONT,
                               padding_x=15)
        self.input_image = TextInput(hint_text='Ссылка на изображение',
                               multiline=False,
                               size_hint=[0.7, 0.1],
                               pos_hint={"center_y": 0.5, "center_x": .5},
                               font_size='30sp',
                               font_name=AMATIC_FONT,
                               padding_x=15)
        self.input_description = TextInput(hint_text='Описание',
                               multiline=False,
                               size_hint=[0.7, 0.1],
                               pos_hint={"center_y": 0.4, "center_x": .5},
                               font_size='30sp',
                               font_name=AMATIC_FONT,
                               padding_x=15)
        self.status = Label(text='',
                      color=RAZZLE_DAZZLE,
                      font_size='20sp',
                      font_name=AMATIC_FONT,
                      pos_hint={"center_y": 0.3, "center_x": .5})
        self.button_add = Button(
            text="Добавить",
            background_color=RAZZLE_DAZZLE,
            background_down=PANTONE_MAGENTA,
            size_hint=[0.9, 0.1],
            font_name=AMATIC_FONT,
            font_size='40sp',
            pos_hint={"center_y": 0.2, "center_x": .5},
            on_press=self.on_press_add
        )
        self.button_return = Button(
            text="Назад",
            background_color=RAZZLE_DAZZLE,
            background_down=PANTONE_MAGENTA,
            size_hint=[0.9, 0.1],
            font_name=AMATIC_FONT,
            font_size='40sp',
            pos_hint={"center_y": 0.1, "center_x": .5},
            on_press=self.on_back
        )

        self.add_widget(logo)
        self.add_widget(label)
        self.add_widget(self.input_title)
        self.add_widget(self.input_image)
        self.add_widget(self.input_description)
        self.add_widget(self.button_add)
        self.add_widget(self.button_return)
        self.add_widget(self.status)
    
    def on_press_add(self, *args):
        title = self.input_title.text
        image = self.input_image.text
        if not title or not image:
            return None
        description = self.input_description.text
        add_film(title=title, image=image,description=description)
        self.status.text = "Фильм добавлен"
        self.input_title, self.input_description, self.input_image="","",""
        
    
    def on_back(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'main_screen'

class ScreenDelete(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        logo = Image(source="0000_films/logo.png",
                     pos_hint={"center_y": 0.9})

        label = Label(text='Какой фильм просмотрен?',
                      color=RAZZLE_DAZZLE,
                      font_size='45sp',
                      font_name=AMATIC_FONT,
                      pos_hint={"center_y": 0.7, "center_x": .5})
        self.input_data = TextInput(hint_text='Введи название',
                               multiline=False,
                               size_hint=[0.7, 0.1],
                               pos_hint={"center_y": 0.5, "center_x": .5},
                               font_size='30sp',
                               font_name=AMATIC_FONT,
                               padding_x=15)
        button_delete = Button(
            text="Удалить",
            background_color=RAZZLE_DAZZLE,
            background_down=PANTONE_MAGENTA,
            size_hint=[0.9, 0.1],
            font_name=AMATIC_FONT,
            font_size='40sp',
            pos_hint={"center_y": 0.2, "center_x": .5},
            on_press=self.on_button_press_delete
        )
        self.button_return = Button(
            text="Назад",
            background_color=RAZZLE_DAZZLE,
            background_down=PANTONE_MAGENTA,
            size_hint=[0.9, 0.1],
            font_name=AMATIC_FONT,
            font_size='40sp',
            pos_hint={"center_y": 0.1, "center_x": .5},
            on_press=self.on_back
        )
        self.add_widget(logo)
        self.add_widget(label)
        self.add_widget(self.input_data)
        self.add_widget(button_delete)
        self.add_widget(self.button_return)
    
    def on_button_press_delete(self, *args):
        title = self.input_data.text
        delete_film(title=title)
        
    def on_back(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'main_screen'


class FilmApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = 'What to watch'
        init_db()
        

    def build(self):
        sm = ScreenManager()
        sm.add_widget(ScreenMain(name='main_screen'))
        sm.add_widget(ScreenAdd(name='add_screen'))
        sm.add_widget(ScreenDelete(name='delete_screen'))
        return sm


if __name__ == "__main__":
    FilmApp().run()
