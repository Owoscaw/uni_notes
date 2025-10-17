import tkinter as tk

class R3simulation():
    __window = None

    def __init__(self):
        self.__window = tk.Tk()
        pass

    def run(self):

        self.__window.state("zoomed")
        self.__window.mainloop()



test = R3simulation()
test.run()
