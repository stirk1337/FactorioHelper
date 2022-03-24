from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App

Builder.load_file('action.kv')

visited_screens = []


class DefaultScreen(Screen):
    def add_screen(self, screen):
        visited_screens.append(screen)

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


sm = ScreenManager()


def hook_keyboard(window, key, *largs):
    if key == 27:
        if sm.current == 'menu':
            App.get_running_app().stop()
        sm.transition.direction = 'right'
        sm.current = visited_screens.pop()
        return True


def post_build_init(ev):
    from kivy.base import EventLoop
    EventLoop.window.bind(on_keyboard=hook_keyboard)


class App(MDApp):
    def build(self):
        self.bind(on_start=post_build_init)
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(StartScreen(name='start'))
        sm.add_widget(RedScreen(name='red'))
        sm.add_widget(GreenScreen(name='green'))
        sm.add_widget(BlueScreen(name='blue'))
        sm.add_widget(BlackScreen(name='black'))
        sm.add_widget(DefenceScreen(name='defence'))
        return sm


if __name__ == '__main__':
    App().run()
