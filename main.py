from PIL import Image
import tkinter as tk
from tkinter import filedialog


# tk.Frame.__init__(self, gui)
# super().__init__(self, gui)
# These do different things. Look into that.


class App(tk.Frame):

    def __init__(self, gui):
        tk.Frame.__init__(self, gui)
        gui.resizable(width=False, height=False)
        gui.geometry('500x220')

        self.pack()

        self.button_state = tk.DISABLED

        self.input_button = tk.Button(self)
        self.input_button['text'] = 'file to inject'
        self.input_button['command'] = self.get_input_location
        self.input_button['width'] = 25
        self.input_button['height'] = 15
        self.input_button.pack(side=tk.LEFT)

        self.target_button = tk.Button(self)
        self.target_button['text'] = 'target file'
        self.target_button['command'] = self.get_target_location
        self.target_button['width'] = 25
        self.target_button['height'] = 15
        self.target_button.pack(side=tk.RIGHT)

        self.inject_button = tk.Button(self)
        self.inject_button['text'] = 'inject'
        self.inject_button['state'] = self.button_state
        self.inject_button['command'] = self.inject
        self.inject_button['height'] = 15
        self.inject_button.pack()

        self.input_location = ''
        self.target_location = ''

        self.input_image = None
        self.target_image = None

    def ready(self):
        if self.input_location and self.target_location:
            self.inject_button['state'] = tk.NORMAL

    def inject(self):
        self.target_image.convert('RGBA')
        self.target_image.putalpha(self.input_image.split()[0])
        self.target_image.save(self.get_save_location())

    def set_input_button_image(self):
        self.input_image = Image.open(self.input_location)
        # self.input_image = tk.PhotoImage(self.input_image)  # To prevent garbage collection of image
        # self.input_button['image'] = self.input_image
        self.ready()
        pass

    def set_target_button_image(self):
        self.target_image = Image.open(self.target_location)
        # self.target_image = tk.PhotoImage(file=self.target_location)  # To prevent garbage collection of image
        # self.target_button['image'] = self.target_image
        self.ready()

    def get_input_location(self):
        self.input_location = filedialog.askopenfilename(title='Select file to inject')
        self.set_input_button_image()

    def get_target_location(self):
        self.target_location = filedialog.askopenfilename(title='Select the target file')
        self.set_target_button_image()

    @staticmethod
    def get_save_location():
        return filedialog.asksaveasfilename(title='Save file with modified alpha',
                                            defaultextension='png')

root = tk.Tk()
app = App(root)
app.mainloop()
