import typing
import wx


# Choicebook Listbook Notebook Simplebook Toolbook Treebook
# CheckListBox initial
# Choice initial
# CollapsiblePane
# ComboBox initial
# Dialog
# FilePickerCtrl
# Gauge initial
# GenericDirCtrl
# HeaderCtrl
# HScrolledWindow
# Listbox initial
# ListCtrl
# ListView
# MDIChildFrame
# MDIClientWindow
# MDIParentFrame
# Menu
# MenuBar
# MiniFrame
# MultiChoiceDialog
# NumberEntryDialog
# PasswordEntryDialog
# PopupWindow
# PopupTransientWindow
# RadioBox
# ScrolledCanvas
# ScrolledWindow
# ScrollBar
# SingleChoiceDialog
# Slider
# SpinButton
# SpinCtrl
# SpinCtrlDouble
# SplitterWindow
# StaticBitmap
# StaticLine
# StaticText
# StatusBar
# TipWindow
# ToggleButton
# ToolBar
# ToolTip
# TreeCtrl
# VListBox
# VScrolledWindow


def dump(header, obj):
    print(header)
    print(obj)
    print('self:')
    for key, val in obj.__dict__.items():
        if key == '__doc__':
            pass
        else:
            print('  ', key, '--->>>', val, 'type: ', type(val))
    # If obj is a type, call mro on it directly.
    if type(obj) == type:
        mro = obj.mro(type)
    elif isinstance(obj, type):
        mro = obj.mro()
    else:
        mro = obj.__class__.mro()
    for clazz in mro:
        print('  c: ', clazz)
        for key, val in clazz.__dict__.items():
            if key == '__doc__':
                pass
            else:
                print('    ', key, '--->>>', val, 'type: ', type(val))


def extract_kws(kwargs, *args):
    extracted = {}
    for keyword in args:
        if keyword in kwargs:
            extracted[keyword] = kwargs[keyword]
            del kwargs[keyword]
    return extracted


def extract_add_args(kwargs):
    add_args = extract_kws(kwargs, 'proportion', 'flag', 'border')
    return add_args


def common_autoinit(self, args, kwargs):
    add_args = extract_add_args(kwargs)
    t = type(self)
    super(t, self).__init__(*args, **kwargs)
    parent = kwargs['parent']
    if parent:
        if parent.GetSizer():
            parent.GetSizer().Add(self, **add_args)


class AutoFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        common_autoinit(self, args, kwargs)


class AutoPanel(wx.Panel):
    def __init__(self, *args, **kwargs):
        sizer_args = extract_kws(kwargs, 'orient')
        add_args = extract_add_args(kwargs)
        super().__init__(*args, **kwargs)
        self.SetSizer(wx.BoxSizer(**sizer_args))
        parent = kwargs['parent']
        if parent.GetSizer():
            parent.GetSizer().Add(self, **add_args)


class AutoStaticBox(wx.StaticBox):
    def __init__(self, *args, **kwargs):
        add_args = extract_add_args(kwargs)
        super().__init__(*args, **kwargs)
        self.sizer = wx.StaticBoxSizer(box=self)
        parent = kwargs['parent']
        if parent.GetSizer():
            parent.GetSizer().Add(self.sizer, **add_args)

    def GetSizer(self):
        return self.sizer


class AutoButton(wx.Button):
    def __init__(self, *args, **kwargs):
        common_autoinit(self, args, kwargs)


class AutoRadioButton(wx.RadioButton):
    def __init__(self, *args, **kwargs):
        common_autoinit(self, args, kwargs)


class AutoCheckBox(wx.CheckBox):
    def __init__(self, *args, **kwargs):
        common_autoinit(self, args, kwargs)


class AutoTextCtrl(wx.TextCtrl):
    def __init__(self, *args, **kwargs):
        common_autoinit(self, args, kwargs)


class AutoChecklistBox(wx.CheckListBox):
    def __init__(self, *args, **kwargs):
        common_autoinit(self, args, kwargs)


class AutoChoice(wx.Choice):
    def __init__(self, *args, **kwargs):
        common_autoinit(self, args, kwargs)


class AutoComboBox(wx.ComboBox):
    def __init__(self, *args, **kwargs):
        common_autoinit(self, args, kwargs)


class AutoGauge(wx.Gauge):
    def __init__(self, *args, **kwargs):
        common_autoinit(self, args, kwargs)


class AutoListBox(wx.ListBox):
    def __init__(self, *args, **kwargs):
        common_autoinit(self, args, kwargs)


class AutoScrollBar(wx.ScrollBar):
    def __init__(self, *args, **kwargs):
        common_autoinit(self, args, kwargs)


class UI:
    def __init__(self):
        self.frame: AutoFrame = AutoFrame(parent=None, title='Regular Expression', size=(600, 400))
        self.main_panel: AutoPanel = AutoPanel(parent=self.frame, orient=wx.VERTICAL)
        self.main_panel.SetBackgroundColour(wx.Colour(255, 255, 0))
        self.button = AutoButton(parent=self.main_panel, label='AutoButton')
        self.radio_button1 = AutoRadioButton(parent=self.main_panel, label='AutoRadioButton1', style=wx.RB_GROUP)
        self.radio_button2 = AutoRadioButton(parent=self.main_panel, label='AutoRadioButton2')
        self.checkbox = AutoCheckBox(parent=self.main_panel, label='AutoCheckBox')
        self.textctrl = AutoTextCtrl(parent=self.main_panel)
        choices = ['choice1', 'choice2', 'choice3']
        self.checklistbox = AutoChecklistBox(parent=self.main_panel, choices=choices)
        self.choice = AutoChoice(parent=self.main_panel, choices=choices)
        self.combobox = AutoComboBox(parent=self.main_panel, choices=choices)
        self.gauge = AutoGauge(parent=self.main_panel)
        self.gauge.Value = 25
        self.listbox = AutoListBox(parent=self.main_panel, choices=choices)
        self.scrollbar = AutoScrollBar(parent=self.main_panel)

if __name__ == '__main__':
    def main():
        app = wx.App()
        ui = UI()
        ui.frame.Show()
        app.MainLoop()


    main()
