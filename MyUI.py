import os

from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.slider import Slider

from pidev.MixPanel import MixPanel
from pidev.kivy import DPEAButton
from pidev.kivy import ImageButton

from dpeaDPi.DPiComputer import DPiComputer
from dpeaDPi.DPiStepper import *
from time import sleep

MIXPANEL_TOKEN = "x"
MIXPANEL = MixPanel("Project Name", MIXPANEL_TOKEN)

SCREEN_MANAGER = ScreenManager()
MAIN_SCREEN_NAME = 'main'

stepperstate = "Stepper Off"
direction = "Clockwise"

dpiStepper = DPiStepper()
dpiStepper.setBoardNumber(0)
dpiStepper.setMicrostepping(8)

class ProjectNameGUI(App):

    def build(self):

        return SCREEN_MANAGER

Window.clearcolor = (0.78, 0.68, 0.93, 1)

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

    def stepperbutton(self, stepperstate):
        if stepperstate == "Stepper On":
            stepperstate = "Stepper Off"
            dpiStepper.enableMotors(False)
        else:
            stepperstate = "Stepper On"
            dpiStepper.enableMotors(True)
        return str(stepperstate)

    def directionbutton(self,direction):
        if direction == "Clockwise":
            direction = "Counterclockwise"
        else:
            direction = "Clockwise"

Builder.load_file('MyUI.kv')
SCREEN_MANAGER.add_widget(MainScreen(name=MAIN_SCREEN_NAME))

if __name__ == "__main__":
    ProjectNameGUI().run()