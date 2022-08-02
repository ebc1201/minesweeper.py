from tkinter import *
import settings
import utilities

root = Tk()
# Override window settings
root.configure(bg="red")
root.geometry(f"{settings.width} x {settings.height}")
root.title("Minesweeper")
root.resizable(False, False)

top_frame = Frame(
    root, bg="red", width=settings.width, height=utilities.height_prct(25)
)
top_frame.place(x=0, y=0)

left_frame = Frame(
    bg="blue", width=utilities.width_prct(25), height=utilities.height_prct(25)
)
left_frame.place(x=0, y=utilities.height_prct(25))

center_frame = Frame(
    root, bg="green", width=utilities.width_prct(75), height=utilities.width_prct(75)
)
center_frame.place(x=utilities.width_prct(25), y=utilities.height_prct(25))


# Run window
root.mainloop()
