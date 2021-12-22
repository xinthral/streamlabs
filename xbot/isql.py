"""
Interactive SQL Window
TKinter GUI allowing interaction between user and database
"""
import tkinter as tk
from xsql import Database

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("800x600")
        self.pack()
        self.create_window_menu()
        self.create_framework()

    def create_window_menu(self):
        """ Builds menubar for main window """
        self.main_menu = tk.Menu(self)

        # File Menu
        self.file_menu = tk.Menu(self.main_menu, tearoff=0)
        self.file_menu.add_command(label='New', command=None)
        self.file_menu.add_command(label='Open', command=None)
        self.file_menu.add_command(label='Save', command=None)
        self.file_menu.add_command(label='Save As..', command=None)
        self.file_menu.add_command(label='Close', command=None)
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Exit', command=root.quit)
        self.main_menu.add_cascade(label='File', menu=self.file_menu)

        # Edit Menu
        self.edit_menu = tk.Menu(self.main_menu, tearoff=0)
        self.edit_menu.add_command(label='Cut', command=None)
        self.edit_menu.add_command(label='Copy', command=None)
        self.edit_menu.add_command(label='Paste', command=None)
        self.edit_menu.add_command(label='Delete', command=None)
        self.edit_menu.add_command(label='Select All', command=None)
        self.main_menu.add_cascade(label='Edit', menu=self.edit_menu)

        # Help Menu
        self.help_menu = tk.Menu(self.main_menu, tearoff=0)
        self.help_menu.add_command(label='About', command=None)
        self.main_menu.add_cascade(label='Help', menu=self.help_menu)

        self.master.config(menu=self.main_menu)

    def create_framework(self):
        """ Build main window frame layout """
        self.options_frame = OptionsFrame(self.master)
        self.display_frame = DisplayFrame(self.master)
        self.readout_frame = ReadoutFrame(self.master)
        self.options_frame.pack(side=tk.RIGHT, fill=tk.Y)
        self.display_frame.pack()#fill=tk.BOTH)
        self.readout_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.style_framework()

    def style_framework(self):
        """ Apply style to the framework """
        self.display_frame.config(bg='red')
        self.options_frame.config(bg='white')
        self.readout_frame.config(bg='blue')

class OptionsFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        # self.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.create_widgets()

    def create_button_home(self):
        """ Create Button """
        self.go_home = tk.Button(self, fg='green')
        self.go_home['text'] = 'Go Home'
        self.go_home['command'] = self.pressed_home_button
        self.go_home.pack()

    def create_button_quit(self):
        """ Create Button """
        self.quit = tk.Button(self, text='Exit', fg='red', command=self.master.destroy)
        self.quit.pack()

    def create_widgets(self):
        """ Build All Widgets """
        self.create_button_home()
        self.create_button_quit()

    def pressed_home_button(self):
        """ Execution of button event """
        print('Home Button Pressed!')

class DisplayFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        # self.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.create_widgets()

    def create_button_home(self):
        """ Create Button """
        self.go_home = tk.Button(self, fg='green')
        self.go_home['text'] = 'Go Home'
        self.go_home['command'] = self.pressed_home_button
        self.go_home.pack()

    def create_button_quit(self):
        """ Create Button """
        self.quit = tk.Button(self, text='Exit', fg='red', command=self.master.destroy)
        self.quit.pack()

    def create_widgets(self):
        """ Build All Widgets """
        self.create_button_home()
        self.create_button_quit()

    def pressed_home_button(self):
        """ Execution of button event """
        print('Home Button Pressed!')

class ReadoutFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        # self.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.create_widgets()

    def create_scrollbar(self):
        """ Create vertical scrollbar """
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def create_textbox(self):
        """ Create Textbox area """
        self.output_box = tk.Text(self.master, bg='black', fg='green',
            heigth=10, width=50, insertontime=20,
            yscrollcommand=self.scrollbar.set,
        )
        self.output_box.pack(expand=True)

    def create_widgets(self):
        """ Build All Widgets """
        self.create_scrollbar()
        self.create_textbox()

    def pressed_button_submit(self):
        """ Execution of button event """
        print('Home Button Pressed!')

if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
