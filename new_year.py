from PIL import ImageTk, Image
import time
import tkinter


def key_pressed(event):
    global n
    if event.keysym == 'space':
        if n == 0:
            n += 1
            canvas.coords(sec, (350, 353, 305, 100))
            canvas.coords(minute, (350, 353, 329, 120))
            canvas.coords(hour, (350, 353, 310, 200))
            canvas.pack()
        elif n == 1:
            n += 1
            canvas.coords(sec, (350, 353, 315, 100))
            canvas.coords(minute, (350, 353, 333, 120))
            canvas.pack()
        elif n == 2:
            n += 1
            canvas.coords(sec, (350, 353, 325, 100))
            canvas.coords(hour, (350, 353, 324, 200))
            canvas.pack()
        elif n == 3:
            n += 1
            canvas.coords(sec, (350, 353, 335, 100))
            canvas.coords(minute, (350, 353, 343, 120))
            canvas.pack()
        elif n == 4:
            n += 1
            canvas.coords(sec, (350, 353, 345, 100))
            canvas.coords(hour, (350, 353, 343, 200))
            canvas.pack()
        elif n == 5:
            n += 1
            canvas.coords(sec, (350, 353, 350, 100))
            canvas.coords(minute, (350, 353, 350, 100))
            canvas.coords(hour, (350, 353, 350, 100))
            imagesprite1 = canvas.create_image(0, 100, image=image1, anchor='nw')  
            canvas.pack()


n = 0
master = tkinter.Tk()
master.title('Clock')
canvas = tkinter.Canvas(master, bg='white', height=700, width=700)
canvas.pack()

pilImage = Image.open("birds.jpg")
pilImage.thumbnail((700, 700), Image.ANTIALIAS)
image = ImageTk.PhotoImage(pilImage)
imagesprite = canvas.create_image(0, 0, image=image, anchor='nw')

pilImage1 = Image.open("2021.png")
pilImage1.thumbnail((700, 700), Image.ANTIALIAS)
image1 = ImageTk.PhotoImage(pilImage1)

canvas.create_oval((349, 349), (352, 352), fill='black')
minute = canvas.create_line((350, 353), (325, 130), fill='black', width=2)
sec = canvas.create_line((350, 353), (300, 100), fill='black', width=1)
hour = canvas.create_line((350, 353), (305, 200), fill='black', width=3)
master.bind("<KeyPress>", key_pressed)
canvas.pack()
master.mainloop()