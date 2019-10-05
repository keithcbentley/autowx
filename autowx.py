import typing
import wx


# Choicebook initial
# Listbook initial
# Notebook initial
# Simplebook initial
# Toolbook
# Treebook initial
# CheckListBox initial
# Choice initial
# CollapsiblePane
# ComboBox initial
# Dialog
# FilePickerCtrl
# Gauge initial
# GenericDirCtrl
# HeaderCtrl
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
# ScrollBar initial
# SingleChoiceDialog
# Slider initial
# SpinButton initial
# SpinCtrl initial
# SpinCtrlDouble initial
# SplitterWindow
# StaticBitmap initial
# StaticLine initial
# StaticText initial
# StatusBar
# TipWindow
# ToggleButton initial
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
    add_args = extract_kws(kwargs, 'proportion', 'flag', 'border', 'userData', 'pos', 'span')
    return add_args


def extract_sizer_args(kwargs):
    sizer_args = extract_kws(kwargs, 'sizer', 'orient', 'sizerClass', 'rows', 'cols', 'vgap', 'hgap', 'gap')
    return sizer_args


def common_autoinit(self, args, kwargs):
    add_args = extract_add_args(kwargs)
    t = type(self)
    super(t, self).__init__(*args, **kwargs)
    parent = kwargs.get('parent')
    if parent:
        if parent.GetSizer():
            parent.GetSizer().Add(self, **add_args)


class AutoFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        common_autoinit(self, args, kwargs)


class AutoPanel(wx.Panel):
    def __init__(self, *args, **kwargs):
        sizer_args = extract_sizer_args(kwargs)
        add_args = extract_add_args(kwargs)
        super().__init__(*args, **kwargs)
        sizer = sizer_args.get('sizer')
        sizerClass = sizer_args.get('sizerClass')
        if sizer:
            self.SetSizer(sizer)
        elif sizerClass:
            extract_kws(sizer_args, 'sizerClass')
            self.SetSizer(sizerClass(**sizer_args))
        else:
            self.SetSizer(wx.BoxSizer(**sizer_args))
        parent = kwargs.get('parent')
        if parent.GetSizer():
            parent.GetSizer().Add(self, **add_args)


class AutoStaticBox(wx.StaticBox):
    def __init__(self, *args, **kwargs):
        sizer_args = extract_sizer_args(kwargs)
        add_args = extract_add_args(kwargs)
        super().__init__(*args, **kwargs)
        sizer_args['box'] = self
        self.sizer = wx.StaticBoxSizer(**sizer_args)
        parent = kwargs.get('parent')
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


class AutoSlider(wx.Slider):
    def __init__(self, *args, **kwargs):
        common_autoinit(self, args, kwargs)


class AutoSpinButton(wx.SpinButton):
    def __init__(self, *args, **kwargs):
        common_autoinit(self, args, kwargs)


class AutoSpinCtrl(wx.SpinCtrl):
    def __init__(self, *args, **kwargs):
        common_autoinit(self, args, kwargs)


class AutoSpinCtrlDouble(wx.SpinCtrlDouble):
    def __init__(self, *args, **kwargs):
        common_autoinit(self, args, kwargs)


class AutoStaticBitmap(wx.StaticBitmap):
    def __init__(self, *args, **kwargs):
        common_autoinit(self, args, kwargs)


class AutoStaticLine(wx.StaticLine):
    def __init__(self, *args, **kwargs):
        common_autoinit(self, args, kwargs)


class AutoStaticText(wx.StaticText):
    def __init__(self, *args, **kwargs):
        common_autoinit(self, args, kwargs)


class AutoToggleButton(wx.ToggleButton):
    def __init__(self, *args, **kwargs):
        common_autoinit(self, args, kwargs)


class AutoNotebook(wx.Notebook):
    def __init__(self, *args, **kwargs):
        common_autoinit(self, args, kwargs)


class AutoListbook(wx.Listbook):
    def __init__(self, *args, **kwargs):
        common_autoinit(self, args, kwargs)


class AutoChoicebook(wx.Choicebook):
    def __init__(self, *args, **kwargs):
        common_autoinit(self, args, kwargs)


class AutoSimplebook(wx.Simplebook):
    def __init__(self, *args, **kwargs):
        common_autoinit(self, args, kwargs)


class AutoToolbook(wx.Toolbook):
    def __init__(self, *args, **kwargs):
        common_autoinit(self, args, kwargs)


class AutoTreebook(wx.Treebook):
    def __init__(self, *args, **kwargs):
        common_autoinit(self, args, kwargs)


class AutoMenuBar(wx.MenuBar):
    def __init__(self, *args, **kwargs):
        frame_args = extract_kws(kwargs, 'frame')
        super().__init__(*args, **kwargs)
        frame = frame_args.get('frame')
        if frame:
            frame.SetMenuBar(self)


class AutoMenu(wx.Menu):
    def __init__(self, *args, **kwargs):
        append_args = extract_kws(kwargs, 'menuBar', 'title')
        super().__init__(*args, **kwargs)
        menuBar = append_args.get('menuBar')
        if menuBar:
            extract_kws(append_args, 'menuBar')
            append_args['menu'] = self
            menuBar.Append(**append_args)


class AutoMenuItem(wx.MenuItem):
    def __init__(self, *args, **kwargs):
        menu_args = extract_kws(kwargs, 'menu')
        super().__init__(*args, **kwargs)
        menu = menu_args.get('menu')
        if menu:
            menu.Append(self)


class UI:
    def __init__(self):
        self.frame: AutoFrame = AutoFrame(parent=None, title='Autocontrol Sampler', size=(600, 400))
        self.main_panel: AutoPanel = AutoPanel(parent=self.frame,
                                               sizerClass=wx.FlexGridSizer, cols=3,
                                               rows=0, gap=(10, 10))
        self.main_panel.SetBackgroundColour(wx.Colour(255, 255, 0))
        self.button = AutoButton(parent=self.main_panel, label='Refresh')
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
        self.slider = AutoSlider(parent=self.main_panel)
        self.spinbutton = AutoSpinButton(parent=self.main_panel)
        self.spinctrl = AutoSpinCtrl(parent=self.main_panel)
        self.spinctrldouble = AutoSpinCtrlDouble(parent=self.main_panel, inc=.1)
        self.staticbitmap = AutoStaticBitmap(parent=self.main_panel, bitmap=wx.Bitmap(100, 100), size=(100, 100))
        self.staticline = AutoStaticLine(parent=self.main_panel, size=(100, 5), flag=wx.ALL, border=5)
        self.statictext = AutoStaticText(parent=self.main_panel, label='StaticText', flag=wx.ALL, border=5)
        self.togglebutton = AutoToggleButton(parent=self.main_panel, label='ToggleButton')
        self.panel2 = AutoPanel(parent=self.main_panel, sizerClass=wx.GridBagSizer)
        self.panel2.SetBackgroundColour(wx.Colour(200, 255, 200))
        self.button = AutoButton(parent=self.panel2, label='AutoButton', pos=(0, 0))
        self.button = AutoButton(parent=self.panel2, label='AutoButton', pos=(1, 1))
        self.button = AutoButton(parent=self.panel2, label='AutoButton', pos=(2, 2))
        self.panel3 = AutoStaticBox(parent=self.main_panel, label='AutoStaticBox', flag=wx.TOP, border=-3,
                                    orient=wx.VERTICAL)
        self.button = AutoButton(parent=self.panel3, label='AutoButton')
        self.button = AutoButton(parent=self.panel3, label='AutoButton')
        self.button = AutoButton(parent=self.panel3, label='AutoButton')

        self.notebook = AutoNotebook(parent=self.main_panel)
        self.page1_panel = AutoPanel(parent=self.notebook, sizerClass=wx.GridBagSizer)
        self.page1_panel.SetBackgroundColour(wx.Colour(200, 255, 200))
        self.button = AutoButton(parent=self.page1_panel, label='AutoButton1', pos=(0, 0))
        self.button = AutoButton(parent=self.page1_panel, label='AutoButton1', pos=(1, 1))
        self.button = AutoButton(parent=self.page1_panel, label='AutoButton1', pos=(2, 2))
        self.notebook.AddPage(page=self.page1_panel, text='Page1')

        self.page2_panel = AutoPanel(parent=self.notebook, sizerClass=wx.GridBagSizer)
        self.page2_panel.SetBackgroundColour(wx.Colour(200, 255, 200))
        self.button = AutoButton(parent=self.page2_panel, label='AutoButton2', pos=(0, 0))
        self.button = AutoButton(parent=self.page2_panel, label='AutoButton2', pos=(1, 1))
        self.button = AutoButton(parent=self.page2_panel, label='AutoButton2', pos=(2, 2))
        self.notebook.AddPage(page=self.page2_panel, text='Page2')

        self.listbook = AutoListbook(parent=self.main_panel)
        self.page1_panel = AutoPanel(parent=self.listbook, sizerClass=wx.GridBagSizer)
        self.page1_panel.SetBackgroundColour(wx.Colour(200, 255, 200))
        self.button = AutoButton(parent=self.page1_panel, label='AutoButton L1', pos=(0, 0))
        self.button = AutoButton(parent=self.page1_panel, label='AutoButton L1', pos=(1, 1))
        self.button = AutoButton(parent=self.page1_panel, label='AutoButton L1', pos=(2, 2))
        self.listbook.AddPage(page=self.page1_panel, text='Page1')

        self.page2_panel = AutoPanel(parent=self.listbook, sizerClass=wx.GridBagSizer)
        self.page2_panel.SetBackgroundColour(wx.Colour(200, 255, 200))
        self.button = AutoButton(parent=self.page2_panel, label='AutoButton L2', pos=(0, 0))
        self.button = AutoButton(parent=self.page2_panel, label='AutoButton L2', pos=(1, 1))
        self.button = AutoButton(parent=self.page2_panel, label='AutoButton L2', pos=(2, 2))
        self.listbook.AddPage(page=self.page2_panel, text='Page2')

        self.choicebook = AutoChoicebook(parent=self.main_panel)
        self.page1_panel = AutoPanel(parent=self.choicebook, sizerClass=wx.GridBagSizer)
        self.page1_panel.SetBackgroundColour(wx.Colour(200, 255, 200))
        self.button = AutoButton(parent=self.page1_panel, label='AutoButton C1', pos=(0, 0))
        self.button = AutoButton(parent=self.page1_panel, label='AutoButton C1', pos=(1, 1))
        self.button = AutoButton(parent=self.page1_panel, label='AutoButton C1', pos=(2, 2))
        self.choicebook.AddPage(page=self.page1_panel, text='Page1')

        self.page2_panel = AutoPanel(parent=self.choicebook, sizerClass=wx.GridBagSizer)
        self.page2_panel.SetBackgroundColour(wx.Colour(200, 255, 200))
        self.button = AutoButton(parent=self.page2_panel, label='AutoButton C2', pos=(0, 0))
        self.button = AutoButton(parent=self.page2_panel, label='AutoButton C2', pos=(1, 1))
        self.button = AutoButton(parent=self.page2_panel, label='AutoButton C2', pos=(2, 2))
        self.choicebook.AddPage(page=self.page2_panel, text='Page2')

        self.simplebook = AutoSimplebook(parent=self.main_panel)
        self.page1_panel = AutoPanel(parent=self.simplebook, sizerClass=wx.GridBagSizer)
        self.page1_panel.SetBackgroundColour(wx.Colour(200, 255, 200))
        self.button = AutoButton(parent=self.page1_panel, label='AutoButton S1', pos=(0, 0))
        self.button = AutoButton(parent=self.page1_panel, label='AutoButton S1', pos=(1, 1))
        self.button = AutoButton(parent=self.page1_panel, label='AutoButton S1', pos=(2, 2))
        self.simplebook.AddPage(page=self.page1_panel, text='Page1')

        self.page2_panel = AutoPanel(parent=self.simplebook, sizerClass=wx.GridBagSizer)
        self.page2_panel.SetBackgroundColour(wx.Colour(200, 255, 200))
        self.button = AutoButton(parent=self.page2_panel, label='AutoButton S2', pos=(0, 0))
        self.button = AutoButton(parent=self.page2_panel, label='AutoButton S2', pos=(1, 1))
        self.button = AutoButton(parent=self.page2_panel, label='AutoButton S2', pos=(2, 2))
        self.simplebook.AddPage(page=self.page2_panel, text='Page2')
        self.simplebook.SetSelection(1)

        self.treebook = AutoTreebook(parent=self.main_panel)
        self.page1_panel = AutoPanel(parent=self.treebook, sizerClass=wx.GridBagSizer)
        self.page1_panel.SetBackgroundColour(wx.Colour(200, 255, 200))
        self.button = AutoButton(parent=self.page1_panel, label='AutoButton T1', pos=(0, 0))
        self.button = AutoButton(parent=self.page1_panel, label='AutoButton T1', pos=(1, 1))
        self.button = AutoButton(parent=self.page1_panel, label='AutoButton T1', pos=(2, 2))
        self.treebook.AddPage(page=self.page1_panel, text='Page1')

        self.page2_panel = AutoPanel(parent=self.treebook, sizerClass=wx.GridBagSizer)
        self.page2_panel.SetBackgroundColour(wx.Colour(200, 255, 200))
        self.button = AutoButton(parent=self.page2_panel, label='AutoButton T2', pos=(0, 0))
        self.button = AutoButton(parent=self.page2_panel, label='AutoButton T2', pos=(1, 1))
        self.button = AutoButton(parent=self.page2_panel, label='AutoButton T2', pos=(2, 2))
        self.treebook.AddPage(page=self.page2_panel, text='Page2')

        self.menubar = AutoMenuBar(frame=self.frame)
        self.menu1 = AutoMenu(menuBar=self.menubar, title='Menu1')
        self.menuitem1_1 = AutoMenuItem(id=wx.ID_ANY, text='Menu Item 1 1', menu=self.menu1)
        self.menuitem1_2 = AutoMenuItem(id=wx.ID_ANY, text='Menu Item 1 2', menu=self.menu1)

        self.menu2 = AutoMenu(menuBar=self.menubar, title='Menu2')
        self.menuitem2_1 = AutoMenuItem(id=wx.ID_ANY, text='Menu Item 2 1', menu=self.menu2)
        self.menuitem2_2 = AutoMenuItem(id=wx.ID_ANY, text='Menu Item 2 2', menu=self.menu2)


if __name__ == '__main__':
    def refresh_main_panel(ui: UI):
        ui.main_panel.Refresh()


    def main():
        app = wx.App()
        ui = UI()
        ui.button.Bind(wx.EVT_BUTTON, lambda event: refresh_main_panel(ui))
        ui.frame.Show()
        app.MainLoop()


    main()
