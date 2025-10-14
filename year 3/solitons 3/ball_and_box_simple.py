import time as t
import tkinter as tk


class BallAndBox():
    __size = 0
    __window = None
    __resolution = 50
    __cells = []

    def __init__(self, resolution):
        self.__resolution = resolution
        

    def populate(self):
        self.__window = tk.Tk()
        self.__window.state("zoomed")
        winWidth = self.__window.winfo_screenwidth() - 150
        winHeight = self.__window.winfo_screenheight() - 200
        XCells = winWidth//self.__resolution
        YCells = winHeight//self.__resolution

        sizer = tk.PhotoImage(width = 1, height = 1)
        self.__cells = [[tk.Button(self.__window,
                                width = self.__resolution, 
                                height = self.__resolution, 
                                image = sizer,
                                compound = "c",
                                text = "",
                                activebackground = "red2",
                                bg = "white",
                                cursor = "plus"
                                ), index, 0] for index in range(XCells*YCells)]
        
        for cell in self.__cells:
            cell[0].config(command = lambda x = cell[1]: self.addBall(x))
            cell[0].grid(column = cell[1]%XCells, row = cell[1]//XCells)

        self.__size = XCells*YCells
        self.__window.bind("<Key>", self.start_sim)
        self.__window.mainloop()

    def start_sim(self, event):
        if event.keysym == "Return":
            self.sim_loop()

    def sim_loop(self):
        try:
            while True:
                self.evolve()
        except KeyboardInterrupt:
            pass

    def get_state(self):
        return self.__cells
    
    def __set_state(self, state):
        self.__cells = state

    def evolve(self):
        t.sleep(0.1)
        for i in range(self.__size):
            if self.__cells[i][2] == 1:
                updated_index = self.__get_next_cell(i)
                tempState = self.get_state()

                tempState[i][2] = 0
                tempState[updated_index][2] = 2 

                tempState[i][0]["bg"] = "white"
                tempState[updated_index][0]["bg"] = "red3"

                self.__set_state(tempState)

        self.__cells = [[cell[0], cell[1], 0] if cell[2] == 0 else [cell[0], cell[1], 1] for cell in self.__cells]
        self.__window.update()

    
    def __toggle_cell(self, cell):
        state = self.__cells[cell][2]

        if state == 1:
            self.__cells[cell][0]["bg"] = "white"
            self.__cells[cell][2] = 0
        else:
            self.__cells[cell][0]["bg"] = "red3"
            self.__cells[cell][2] = 1
    
    
    def __get_next_cell(self, index):
        for i in range(self.__size):
            if self.__cells[(i + index)%self.__size][2] == 0:
                return (i + index)%self.__size 
        return None
    
    def addBall(self, index):
        self.__toggle_cell(index)


# test = BallAndBox([0,0,0,0,1,1,1,0,0,0,1,0])
# run_simulation(test, 10)
# test = BallAndBox(4)
# test.set_state([1, 1, 0, 0])
# run_simulation(test, 5)


test = BallAndBox(50)
test.populate()