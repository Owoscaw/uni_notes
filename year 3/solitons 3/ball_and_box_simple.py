import time as t
import tkinter as tk

class BallAndBox():
    __state = []
    __size = 0
    __window = None
    __resolution = 50
    __cells = []

    def __init__(self, resolution):
        self.__resolution = resolution
        

    def populate(self):
        self.__window = tk.Tk()
        self.__window.state("zoomed")
        winWidth = self.__window.winfo_screenwidth()
        winHeight = self.__window.winfo_screenheight() - 200
        XCells = winWidth//self.__resolution
        YCells = winHeight//self.__resolution

        sizer = tk.PhotoImage(width = 1, height = 1)
        self.__cells = [[tk.Button(self.__window,
                                width = self.__resolution, 
                                height = self.__resolution, 
                                image = sizer,
                                compound = "c",
                                text = "X",
                                activebackground = "red2",
                                cursor = "plus"
                                ), index] for index in range(XCells*YCells)]
        
        for cell in self.__cells:
            cell[0].config(command = lambda x = cell[1]: self.addBall(x))
            cell[0].grid(column = cell[1]%XCells, row = cell[1]//XCells)
            
            self.__state.append(0)

        self.__size = XCells*YCells
        self.__set_state([0]*self.__size)
        self.__window.mainloop()

    def get_state(self):
        return self.__state
    
    def __set_state(self, state):
        self.__state = state

    def evolve(self):
        for i in range(self.__size):
            if self.__state[i] == 1:
                updated_index = self.__get_next_cell(i)
                tempState = self.get_state()
                tempState[i] = 0
                tempState[updated_index] = 2 
                self.__set_state(tempState)
                self.__toggleCell(i)
                self.__toggleCell(updated_index)

        self.__state = [0 if box == 0 else 1 for box in self.__state]
                
    
    def __toggleCell(self, cell):
        state = self.__cells[cell][1]

        if state == 1:
            self.__cells[cell][0]["bg"] = "white"
            self.__cells[cell][1] = 0
        else:
            self.__cells[cell][0]["bg"] = "red3"
            self.__cells[cell][1] = 1



    
    def __get_next_cell(self, index):
        for i in range(self.__size):
            if self.__state[(i + index)%self.__size] == 0:
                return (i + index)%self.__size 
        return None
    
    def addBall(self, index):
        print(f"{index} clicked")
        self.__toggleCell(index)


# test = BallAndBox([0,0,0,0,1,1,1,0,0,0,1,0])
# run_simulation(test, 10)
# test = BallAndBox(4)
# test.set_state([1, 1, 0, 0])
# run_simulation(test, 5)


test = BallAndBox(50)
test.populate()