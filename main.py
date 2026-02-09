from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import androidhelper
import datetime
import time

droid = androidhelper.Android()

class NothingApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        self.label = Label(text="I am Nothing")
        self.button = Button(text="Speak")

        self.button.bind(on_press=self.listen)

        self.layout.add_widget(self.label)
        self.layout.add_widget(self.button)
        return self.layout

    def speak(self, text):
        self.label.text = text
        droid.ttsSpeak(text)
        time.sleep(1.5)

    def listen(self, instance):
        result = droid.recognizeSpeech(None, None, None)
        if result and result.result:
            text = result.result[0].lower()
            self.label.text = text

            if "time" in text:
                now = datetime.datetime.now().strftime("%I:%M %p")
                self.speak("The time is " + now)
            else:
                self.speak("I heard you")

NothingApp().run()
