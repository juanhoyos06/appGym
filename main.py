
import kivy
import kivy.app
import kivy.uix.label

class appGym(kivy.app.App):

    def build(self):
        return kivy.uix.label.Label(text="Hi kivy")

appGym().run()
