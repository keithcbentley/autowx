import typing
import wx

# Choicebook Listbook Notebook Simplebook Toolbook Treebook
# CheckListBox
# Choice
# CollapsiblePane
# ComboBox
# Dialog
# FilePickerCtrl
# Gauge
# GenericDirCtrl
# HeaderCtrl
# HScrolledWindow
# Listbox
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


class AutoFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class AutoPanel(wx.Panel):
    def __init__(self, *args, **kwargs):
        sizer_args = extract_kws(kwargs, 'orient')
        add_args = extract_kws(kwargs, 'proportion', 'flag', 'border')
        super().__init__(*args, **kwargs)
        self.SetSizer(wx.BoxSizer(**sizer_args))
        parent = kwargs['parent']
        if parent.GetSizer():
            parent.GetSizer().Add(self, **add_args)


class AutoStaticBox(wx.StaticBox):
    def __init__(self, *args, **kwargs):
        add_args = extract_kws(kwargs, 'proportion', 'flag', 'border')
        super().__init__(*args, **kwargs)
        self.sizer = wx.StaticBoxSizer(box=self)
        parent = kwargs['parent']
        if parent.GetSizer():
            parent.GetSizer().Add(self.sizer, **add_args)

    def GetSizer(self):
        return self.sizer


class AutoTextCtrl(wx.TextCtrl):
    def __init__(self, *args, **kwargs):
        add_args = extract_kws(kwargs, 'proportion', 'flag', 'border')
        super().__init__(*args, **kwargs)
        parent = kwargs['parent']
        if parent.GetSizer():
            parent.GetSizer().Add(self, **add_args)


class AutoButton(wx.Button):
    def __init__(self, *args, **kwargs):
        add_args = extract_kws(kwargs, 'proportion', 'flag', 'border')
        super().__init__(*args, **kwargs)
        parent = kwargs['parent']
        if parent.GetSizer():
            parent.GetSizer().Add(self, **add_args)


class AutoRadioButton(wx.RadioButton):
    def __init__(self, *args, **kwargs):
        add_args = extract_kws(kwargs, 'proportion', 'flag', 'border')
        super().__init__(*args, **kwargs)
        parent = kwargs['parent']
        if parent.GetSizer():
            parent.GetSizer().Add(self, **add_args)


class AutoCheckBox(wx.CheckBox):
    def __init__(self, *args, **kwargs):
        add_args = extract_kws(kwargs, 'proportion', 'flag', 'border')
        super().__init__(*args, **kwargs)
        parent = kwargs['parent']
        if parent.GetSizer():
            parent.GetSizer().Add(self, **add_args)

