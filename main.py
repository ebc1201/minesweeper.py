from tkinter import *
from cell import Cell
import settings
import utilities


root = Tk()
# Override window settings
root.configure(bg="black")
root.geometry(f"{settings.width}x{settings.height}")
root.title("Minesweeper")
root.resizable(False, False)

top_frame = Frame(
    root, bg="black", width=settings.width, height=utilities.height_prct(25)
)
top_frame.place(x=0, y=0)

left_frame = Frame(
    bg="black", width=utilities.width_prct(25), height=utilities.height_prct(25)
)
left_frame.place(x=0, y=utilities.height_prct(25))

center_frame = Frame(
    root, bg="black", width=utilities.width_prct(75), height=utilities.width_prct(75)
)
center_frame.place(x=utilities.width_prct(25), y=utilities.height_prct(25))

for x in range(settings.grid_size):
    for y in range(settings.grid_size):
        c = Cell()
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(column=x, row=y)


# Run window
root.mainloop()
