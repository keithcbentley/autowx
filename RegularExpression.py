import typing
import wx
from autowx import *


class UI:
    def __init__(self):
        self.frame = AutoFrame(parent=None, title='Regular Expression', size=(600, 400))
        self.main_panel = AutoPanel(parent=self.frame, orient=wx.VERTICAL)
        self.main_panel.SetBackgroundColour(wx.Colour(255, 255, 0))

        self.sb1 = AutoStaticBox(parent=self.main_panel, label='Input', proportion=2, flag=wx.EXPAND)
        self.input_text = AutoTextCtrl(parent=self.sb1, proportion=1, flag=wx.EXPAND)
        self.input_control_panel = AutoPanel(parent=self.sb1, orient=wx.VERTICAL, flag=wx.LEFT | wx.RIGHT, border=5)
        self.file_button = AutoButton(parent=self.input_control_panel, label="Load File", flag=wx.BOTTOM, border=5)
        self.splitline_checkbox = AutoCheckBox(parent=self.input_control_panel, label="Split Lines")

        self.sb2 = AutoStaticBox(parent=self.main_panel, label='Regular Expression', proportion=1, flag=wx.EXPAND)
        self.re_text = AutoTextCtrl(parent=self.sb2, proportion=1, flag=wx.EXPAND)
        self.re_execute_panel = AutoPanel(parent=self.sb2, orient=wx.VERTICAL, flag=wx.LEFT | wx.RIGHT, border=5)
        self.execute_button = AutoButton(parent=self.re_execute_panel, label="Execute", flag=wx.BOTTOM, border=5)
        self.ignore_case_checkbox = AutoCheckBox(parent=self.re_execute_panel, label='Ignore Case')
        self.verbose_checkbox = AutoCheckBox(parent=self.re_execute_panel, label='Verbose')
        self.multiline_checkbox = AutoCheckBox(parent=self.re_execute_panel, label='Multiline')
        self.dotall_checkbox = AutoCheckBox(parent=self.re_execute_panel, label='Dotall')

        self.re_function_panel = AutoPanel(parent=self.sb2, orient=wx.VERTICAL, flag=wx.ALL, border=5)
        self.match_radiobutton = AutoRadioButton(parent=self.re_function_panel, label='Match')
        self.fullmatch_radiobutton = AutoRadioButton(parent=self.re_function_panel, label='FullMatch')
        self.search_radiobutton = AutoRadioButton(parent=self.re_function_panel, label='Search')
        self.finditer_radiobutton = AutoRadioButton(parent=self.re_function_panel, label='FindIter')

        self.sb3 = AutoStaticBox(parent=self.main_panel, label='Output', proportion=3, flag=wx.EXPAND)
        self.output_text = AutoTextCtrl(parent=self.sb3, proportion=1, flag=wx.EXPAND)
        self.output_option_panel = AutoPanel(parent=self.sb3, orient=wx.VERTICAL, flag=wx.LEFT | wx.RIGHT, border=5)
        self.output_hide_match_none_checkbox = AutoCheckBox(parent=self.output_option_panel, label='Hide Match None')
        self.output_hide_capture_groups_checkbox = AutoCheckBox(parent=self.output_option_panel,
                                                                label='Hide Capture Groups')
        self.output_hide_match_information_checkbox = AutoCheckBox(parent=self.output_option_panel,
                                                                   label='Hide Match Information')
        self.output_show_input_checkbox = AutoCheckBox(parent=self.output_option_panel, label='Show Input')


def main():
    app = wx.App()
    ui = UI()
    ui.frame.Show()
    app.MainLoop()


main()
