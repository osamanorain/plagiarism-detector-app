from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import ScreenManager
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from backend import *


class MainWindow(Screen):
    # Main Window ids/widgets
    text_1 = ObjectProperty(None)
    text_2 = ObjectProperty(None)
    test_button = ObjectProperty(None)
    wc_text1 = ObjectProperty(None)
    wc_text2 = ObjectProperty(None)
    jaccard_value = ObjectProperty(None)
    result = ObjectProperty(None)

    # These are static varibles that hold values from the main window to be used in other windows
    text1 = ""
    text2 = ""
    text1wordcount = ""
    text2wordcount = ""
    commonstringlength = ""
    jaccard_value_copy = ""

    def testButtonPressed(self):
        textcount1 = getWordLength(self.text_1.text)
        textcount2 = getWordLength(self.text_2.text)

        self.wc_text1.text = str(textcount1)
        self.wc_text2.text = str(textcount2)

        jaccardvalue = testTexts(self.text_1.text, self.text_2.text)
        self.jaccard_value.text = "%" + str(int(jaccardvalue))

        # If the jaccard value is over 50, then dislay Plagiarism
        if jaccardvalue >= 50:
            self.result.font_size = 50
            self.result.pos_hint = {"x": .42, "top": .09}
            self.result.text = "Plagiarism(similarity >= %50)"
        else:
            self.result.font_size = 50
            self.result.pos_hint = {"x": .30, "top": .10}
            self.result.text = "Looks Fine."

        # Set the static values for other windows to use (secondwindow)
        MainWindow.text1 = self.text_1.text
        MainWindow.text2 = self.text_2.text
        MainWindow.text1wordcount = self.wc_text1.text
        MainWindow.text2wordcount = self.wc_text2.text
        MainWindow.jaccard_value_copy = self.jaccard_value.text


class SecondWindow(Screen):
    # Second Window ids/widgets
    commonstringbox = ObjectProperty(None)
    calculate_button = ObjectProperty(None)
    commonstringlength = ObjectProperty(None)
    wc_text1 = ObjectProperty(None)
    wc_text2 = ObjectProperty(None)
    jaccard_value = ObjectProperty(None)

    def calculateButtonPressed(self):
        # Display the common string
        commonstring, length = getCommonString(MainWindow.text1, MainWindow.text2)
        self.commonstringbox.text = commonstring

        # Display information about the texts on the second window
        self.commonstringlength.text = length
        self.wc_text1.text = MainWindow.text1wordcount
        self.wc_text2.text = MainWindow.text2wordcount
        self.jaccard_value.text = MainWindow.jaccard_value_copy


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("gui.kv")


class PlagiarismDetectorApp(App):
    def build(self):
        return kv


if __name__ == '__main__':
    PlagiarismDetectorApp().run()
