from kivy.graphics import Color, Rectangle
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.scatterlayout import ScatterLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.config import Config

Builder.load_file('action.kv')
Config.set('kivy', 'exit_on_escape', '0')

visited_screens = []


class DefaultScreen(Screen):
    def add_screen(self, screen):
        visited_screens.append(screen)

    def go_to_picture(self, screen, source):
        global pictureScreen
        sm.transition.direction = 'left'
        sm.current = 'picture'
        self.add_screen(screen)

        pictureScreen.clear_widgets()
        pictureScreen.canvas.add(Color(.20, .20, .20, 1))
        pictureScreen.canvas.add(
            Rectangle(pos=self.pos, size=self.size, source='source/pictures/picture_background.png'))

        scatter = ScatterLayout(do_rotation=False)
        image = Image(source=source, allow_stretch=True, anim_delay=0.1)
        scatter.add_widget(image)
        pictureScreen.add_widget(scatter)

        if 'menu' not in visited_screens:
            visited_screens.insert(0, 'menu')


class MenuScreen(DefaultScreen):
    pass


class StartScreen(DefaultScreen):
    pass


class RedScreen(DefaultScreen):
    pass


class GreenScreen(DefaultScreen):
    pass


class BlueScreen(DefaultScreen):
    pass


class BlackScreen(DefaultScreen):
    pass


class DefenceScreen(DefaultScreen):
    pass


class PictureScreen(Screen):
    pass


class PersonalScreen(DefaultScreen):
    pass

class TrainScreen(DefaultScreen):
    pass


pictureScreen = PictureScreen(name='picture')

sm = ScreenManager()


def hook_keyboard(window, key, *largs):
    if key == 27:
        if sm.current == 'menu':
            if not App.dialog:
                dial = MDDialog(
                    title='[size=70][font=source/font/DejaVuSans-BoldOblique.ttf]Выйти?[/font][/size]',
                    text="[size=50][font=source/font/DejaVuSans.ttf]Вы действительно хотите выйти?[/font][/size]",
                    size_hint_x=0.9,
                    radius=[20, 20, 20, 20],
                    buttons=[
                        MDFlatButton(
                            text="[size=50][color=#FA8C1C][font=source/font/DejaVuSans.ttf]ДА[/font][/color][/size]",
                            on_release=lambda x: quit(),
                            font_name='source/font/DejaVuSans.ttf',
                        ),
                        MDFlatButton(
                            text="[size=50][color=#FA8C1C][font=source/font/DejaVuSans.ttf]НЕТ[/font][/color][/size]",
                            on_release=lambda x: App.dialog.dismiss(),
                            font_name='source/font/DejaVuSans.ttf',
                        ),
                    ],
                )
                App.dialog = dial
            App.dialog.open()
        else:
            sm.transition.direction = 'right'
            sm.current = visited_screens.pop()
            return True


def post_build_init(ev):
    from kivy.base import EventLoop
    EventLoop.window.bind(on_keyboard=hook_keyboard)


class App(MDApp):
    dialog = None

    def build(self):
        self.bind(on_start=post_build_init)
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(StartScreen(name='start'))
        sm.add_widget(RedScreen(name='red'))
        sm.add_widget(GreenScreen(name='green'))
        sm.add_widget(BlueScreen(name='blue'))
        sm.add_widget(BlackScreen(name='black'))
        sm.add_widget(DefenceScreen(name='defence'))
        sm.add_widget(pictureScreen)
        sm.add_widget((PersonalScreen(name='personal')))
        sm.add_widget(TrainScreen(name='train'))
        return sm


if __name__ == '__main__':
    App().run()
