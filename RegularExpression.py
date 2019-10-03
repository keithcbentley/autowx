import typing
from autowx import *
import re


class ViewModel:
    def __init__(self):
        self.frame = AutoFrame(parent=None, title='Regular Expression', size=(600, 400))
        self.main_panel = AutoPanel(parent=self.frame, orient=wx.VERTICAL)
        self.main_panel.SetBackgroundColour(wx.Colour(255, 255, 0))

        self.sb1 = AutoStaticBox(parent=self.main_panel, label='Input', proportion=2, flag=wx.EXPAND)
        self.input_text = AutoTextCtrl(parent=self.sb1, style=wx.TE_MULTILINE, proportion=1, flag=wx.EXPAND)
        self.input_control_panel = AutoPanel(parent=self.sb1, orient=wx.VERTICAL, flag=wx.LEFT | wx.RIGHT, border=5)
        self.input_file_button = AutoButton(parent=self.input_control_panel, label="Load File", flag=wx.BOTTOM,
                                            border=5)
        self.input_splitline_checkbox = AutoCheckBox(parent=self.input_control_panel, label="Split Lines")

        self.sb2 = AutoStaticBox(parent=self.main_panel, label='Regular Expression', proportion=1, flag=wx.EXPAND)
        self.re_text = AutoTextCtrl(parent=self.sb2, style=wx.TE_MULTILINE, proportion=1, flag=wx.EXPAND)
        self.re_execute_panel = AutoPanel(parent=self.sb2, orient=wx.VERTICAL, flag=wx.LEFT | wx.RIGHT, border=5)
        self.re_execute_button = AutoButton(parent=self.re_execute_panel, label="Execute", flag=wx.BOTTOM, border=5)
        self.re_ignore_case_checkbox = AutoCheckBox(parent=self.re_execute_panel, label='Ignore Case')
        self.re_verbose_checkbox = AutoCheckBox(parent=self.re_execute_panel, label='Verbose')
        self.re_multiline_checkbox = AutoCheckBox(parent=self.re_execute_panel, label='Multiline')
        self.re_dotall_checkbox = AutoCheckBox(parent=self.re_execute_panel, label='Dotall')

        self.re_function_panel = AutoPanel(parent=self.sb2, orient=wx.VERTICAL, flag=wx.ALL, border=5)
        self.re_match_radiobutton = AutoRadioButton(parent=self.re_function_panel, label='Match', style=wx.RB_GROUP)
        self.re_fullmatch_radiobutton = AutoRadioButton(parent=self.re_function_panel, label='FullMatch')
        self.re_search_radiobutton = AutoRadioButton(parent=self.re_function_panel, label='Search')
        self.re_finditer_radiobutton = AutoRadioButton(parent=self.re_function_panel, label='FindIter')

        self.sb3 = AutoStaticBox(parent=self.main_panel, label='Output', proportion=3, flag=wx.EXPAND)
        self.output_text = AutoTextCtrl(parent=self.sb3, style=wx.TE_MULTILINE, proportion=1, flag=wx.EXPAND)
        self.output_option_panel = AutoPanel(parent=self.sb3, orient=wx.VERTICAL, flag=wx.LEFT | wx.RIGHT, border=5)
        self.output_hide_match_none_checkbox = AutoCheckBox(parent=self.output_option_panel, label='Hide Match None')
        self.output_hide_capture_groups_checkbox = AutoCheckBox(parent=self.output_option_panel,
                                                                label='Hide Capture Groups')
        self.output_hide_match_information_checkbox = AutoCheckBox(parent=self.output_option_panel,
                                                                   label='Hide Match Information')
        self.output_show_input_checkbox = AutoCheckBox(parent=self.output_option_panel, label='Show Input')

        self.re_match_radiobutton.Value = True

    def execute_button_set_command(self, command):
        self.re_execute_button.Bind(wx.EVT_BUTTON, lambda event: command(self))

    #    def file_button_set_command(self, command):
    #        self.input_file_button['command'] = lambda: command(self)

    def re_text_get(self) -> str:
        return self.re_text.Value

    def re_ignore_case_get(self) -> bool:
        return self.re_ignore_case_checkbox.Value

    def re_verbose_get(self) -> bool:
        return self.re_verbose_checkbox.Value

    def re_multiline_get(self) -> bool:
        return self.re_multiline_checkbox.Value

    def re_dotall_get(self) -> bool:
        return self.re_dotall_checkbox.Value

    def input_text_get(self) -> str:
        return self.input_text.Value

    def input_text_set(self, text) -> None:
        self.input_text.Value = text

    def splitlines_get(self) -> bool:
        return self.input_splitline_checkbox.Value

    def output_text_clear(self) -> None:
        self.output_text.Clear()

    def output_text_append(self, text):
        self.output_text.AppendText(text)

    def hide_match_none_get(self) -> bool:
        return self.output_hide_match_none_checkbox.Value

    def hide_capture_groups_get(self) -> bool:
        return self.output_hide_capture_groups_checkbox.Value

    def hide_match_information_get(self):
        return self.output_hide_match_information_checkbox.Value

    def show_input_get(self):
        return self.output_show_input_checkbox.Value

    def do_match_get(self) -> bool:
        return self.re_match_radiobutton.Value

    def do_fullmatch_get(self) -> bool:
        return self.re_fullmatch_radiobutton.Value

    def do_search_get(self) -> bool:
        return self.re_search_radiobutton.Value

    def do_finditer_get(self) -> bool:
        return self.re_finditer_radiobutton.Value


def none_to_empty(string):
    if string is None:
        return ''
    return string


def none_to_space_none(string):
    if string is None:
        return ' None'
    return ''


class ViewModelAdapter:
    c_match_start_string = ':::Match start\n'
    c_match_end_string = ':::Match end\n'
    c_group_format = '    group {0}: -->{1}<--{2}\n'
    c_span_format = '    span: {0}\n'
    c_numbered_start_string = '  :::Numbered groups start\n'
    c_numbered_end_string = '  :::Numbered groups end\n'
    c_named_start_string = '  :::Named groups start\n'
    c_named_end_string = '  :::Named groups end\n'

    def __init__(self, view_model: ViewModel):
        self.view_model = view_model
        self.output_string = None

    def regex_flags(self):
        flags = 0
        if self.view_model.re_ignore_case_get():
            flags |= re.IGNORECASE
        if self.view_model.re_verbose_get():
            flags |= re.VERBOSE
        if self.view_model.re_multiline_get():
            flags |= re.MULTILINE
        if self.view_model.re_dotall_get():
            flags |= re.DOTALL
        return flags

    def begin_output(self):
        self.view_model.output_text_clear()
        self.output_string = ''

    def append_output(self, string):
        self.output_string += string

    def end_output(self):
        self.view_model.output_text_append(self.output_string)

    @staticmethod
    def clean_input_string(input_string):
        if input_string[-1] == '\n':
            return '-->' + input_string[0:-1] + ' + \\n<--'
        return '-->' + input_string + '<--'

    def input_string_string(self, input_string):
        if self.view_model.show_input_get():
            return '  input string: ' + ViewModelAdapter.clean_input_string(input_string) + '\n'
        return ''

    def match_none_string(self, input_string):
        if self.view_model.hide_match_none_get():
            return ''
        string = ''
        string += self.match_start_string()
        string += self.input_string_string(input_string)
        string += '  None\n'
        string += self.match_end_string()
        return string

    def match_start_string(self):
        if self.view_model.hide_match_information_get():
            return ''
        return self.c_match_start_string

    def match_content_string(self, match):
        if self.view_model.hide_match_information_get():
            return ''
        string = ''
        string += self.c_group_format.format(0, none_to_empty(match[0]), none_to_space_none(match[0]))
        string += self.c_span_format.format(str(match.span(0)))
        return string

    def match_end_string(self):
        if self.view_model.hide_match_information_get():
            return ''
        return self.c_match_end_string

    def content_groups_string(self, match):
        if self.view_model.hide_capture_groups_get():
            return ''
        string = ''
        string += self.c_numbered_start_string
        for index, group in enumerate(match.groups()):
            string += self.c_group_format.format(index + 1, none_to_empty(group), none_to_space_none(group))
            string += self.c_span_format.format(str(match.span(index + 1)))
        string += self.c_numbered_end_string
        string += self.c_named_start_string
        named_groups = match.groupdict()
        if len(named_groups) == 0:
            string += '    None\n'
        else:
            for key, value in named_groups.items():
                string += self.c_group_format.format(key, none_to_empty(value), none_to_space_none(value))
                string += self.c_span_format.format(str(match.span(key)))
        string += self.c_named_end_string
        return string

    def match_to_string(self, match, input_string):
        if match is None:
            return self.match_none_string(input_string)
        string = ''
        string += self.match_start_string()
        string += self.input_string_string(input_string)
        string += self.match_content_string(match)
        string += self.content_groups_string(match)
        string += self.match_end_string()
        return string

    def output_match(self, match, input_string):
        match_as_string = self.match_to_string(match, input_string)
        self.append_output(match_as_string)


def re_execute_button_command(view_model):
    view_model_adapter = ViewModelAdapter(view_model)
    view_model_adapter.begin_output()

    regex = view_model.re_text_get()
    regex_flags = view_model_adapter.regex_flags()
    pattern = re.compile(regex, regex_flags)

    input_text = view_model.input_text_get()
    if view_model.splitlines_get():
        input_text_pieces = input_text.splitlines(keepends=True)
    else:
        input_text_pieces = [input_text]
    for text in input_text_pieces:
        if view_model.do_match_get():
            match = pattern.match(text)
            view_model_adapter.output_match(match, text)

        if view_model.do_fullmatch_get():
            match = pattern.fullmatch(text)
            view_model_adapter.output_match(match, text)

        if view_model.do_search_get():
            match = pattern.search(text)
            view_model_adapter.output_match(match, text)

        if view_model.do_finditer_get():
            for match in pattern.finditer(text):
                view_model_adapter.output_match(match, text)

    view_model_adapter.end_output()


# def file_button_command(view_model):
#    file_name = filedialog.askopenfilename()
#    if file_name:
#        file = open(file_name, 'r')
#        contents = file.read()
#        view_model.input_text_set(contents)


def main():
    app = wx.App()
    ui = ViewModel()
    ui.execute_button_set_command(re_execute_button_command)
    ui.frame.Show()
    app.MainLoop()


main()
