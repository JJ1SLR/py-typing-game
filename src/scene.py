class Scene():

    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.widget_list = []

    def add_widget(self, widget):
        self.widget_list.append(widget)

    def on_key_down(self, event):
        pass

    def on_key_up(self, event):
        pass

    def on_draw(self):
        self.screen.fill((0, 0, 0))
        for widget in self.widget_list:
            widget.draw(self.screen)
