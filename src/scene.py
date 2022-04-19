from abc import ABC, abstractmethod


class Scene(ABC):

    def __init__(self, screen):
        super().__init__()
        self.screen = screen

    @abstractmethod
    def on_key_down(self, event):
        pass

    @abstractmethod
    def on_key_up(self, event):
        pass

    @abstractmethod
    def on_draw(self):
        pass
