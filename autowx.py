import typing
import wx


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


def main():
    app = wx.App()
    frame = AutoFrame(parent=None, title='Regular Expression')

    main_panel = AutoPanel(parent=frame, orient=wx.VERTICAL)

    main_panel.SetBackgroundColour(wx.Colour(255, 255, 0))

    sb1 = AutoStaticBox(parent=main_panel, label='Input', proportion=2, flag=wx.EXPAND)
    input_text = AutoTextCtrl(parent=sb1, proportion=1, flag=wx.EXPAND)
    input_control_panel = AutoPanel(parent=sb1, orient=wx.VERTICAL, flag=wx.LEFT | wx.RIGHT, border=5)
    file_button = AutoButton(parent=input_control_panel, label="Load File", flag=wx.BOTTOM, border=5)
    splitline_checkbox = AutoCheckBox(parent=input_control_panel, label="Split Lines")

    sb2 = AutoStaticBox(parent=main_panel, label='Regular Expression', proportion=1, flag=wx.EXPAND)
    re_text = AutoTextCtrl(parent=sb2, proportion=1, flag=wx.EXPAND)
    re_execute_panel = AutoPanel(parent=sb2, orient=wx.VERTICAL, flag=wx.LEFT | wx.RIGHT, border=5)
    execute_button = AutoButton(parent=re_execute_panel, label="Execute", flag=wx.BOTTOM, border=5)
    ignore_case_checkbox = AutoCheckBox(parent=re_execute_panel, label='Ignore Case')
    verbose_checkbox = AutoCheckBox(parent=re_execute_panel, label='Verbose')
    multiline_checkbox = AutoCheckBox(parent=re_execute_panel, label='Multiline')
    dotall_checkbox = AutoCheckBox(parent=re_execute_panel, label='Dotall')

    re_function_panel = AutoPanel(parent=sb2, orient=wx.VERTICAL, flag=wx.ALL, border=5)
    match_radiobutton = AutoRadioButton(parent=re_function_panel, label='Match')
    fullmatch_radiobutton = AutoRadioButton(parent=re_function_panel, label='FullMatch')
    search_radiobutton = AutoRadioButton(parent=re_function_panel, label='Search')
    finditer_radiobutton = AutoRadioButton(parent=re_function_panel, label='FindIter')

    sb3 = AutoStaticBox(parent=main_panel, label='Output', proportion=3, flag=wx.EXPAND)
    output_text = AutoTextCtrl(parent=sb3, proportion=1, flag=wx.EXPAND)
    output_option_panel = AutoPanel(parent=sb3, orient=wx.VERTICAL, flag=wx.LEFT | wx.RIGHT, border=5)
    output_hide_match_none_checkbox = AutoCheckBox(parent=output_option_panel, label='Hide Match None')
    output_hide_capture_groups_checkbox = AutoCheckBox(parent=output_option_panel, label='Hide Capture Groups')
    output_hide_match_information_checkbox = AutoCheckBox(parent=output_option_panel, label='Hide Match Information')
    output_show_input_checkbox = AutoCheckBox(parent=output_option_panel, label='Show Input')

    frame.Show()

    app.MainLoop()


main()
