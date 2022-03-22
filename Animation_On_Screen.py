from tkinter import *
import random
from PIL import Image, ImageTk
from screeninfo import get_monitors
i = 0
form_width = 200
form_heigth = 90
def move_me():
    screen_w = root.winfo_screenwidth()  # width of the screen
    screen_h = root.winfo_screenheight()  # height of the screen
    x, y = str(random.randrange(800)), str(random.randrange(800))
    loc = "300x300+" + x + '+' + y
    root.geometry(loc)
    root.after(500, move_me)  # <-- auto call to move_me again every 1/2 second

def move_up_down():
    screen_w = root.winfo_screenwidth()  # width of the screen
    screen_h = root.winfo_screenheight()  # height of the screen
    global form_width
    global form_heigth
    form_width = 200
    form_heigth = 100
    pos_x = screen_w - form_width
    global i
    i = i + 1

    x, y = str(pos_x), str(i)
    loc = str(form_width) + "x" + str(form_heigth) + "+" + x + '+' + y
    # loc = "300x300+" + x + '+' + y
    root.geometry(loc)
    root.after(500, move_up_down)  # <-- auto call to move_me again every 1/2 second


def delete_background(image_to_transform, threshold):
    output_image = image_to_transform
    # Vertically Up->Down (forward)
    for x in range(output_image.width):
        for y in range(output_image.height):
            # for the given pixel at w,h, lets check its value against the threshold
            if output_image.getpixel((x, y)) == (0,0,0,255) :  # 1,2,3 - RGB, 4- intensywnosc od 0 do 255
                break
            else:
                output_image.putpixel((x, y), (0, 0, 10, 255))
    # Vertically Down->Up (backward)
    for x in range(output_image.width):
        for y in range(output_image.height-1, 1, -1):
            # for the given pixel at w,h, lets check its value against the threshold
            if output_image.getpixel((x, y)) == (0,0,0,255) :  # 1,2,3 - RGB, 4- intensywnosc od 0 do 255
                break
            else:
                output_image.putpixel((x, y), (0, 0, 10, 255))
    # Horizontally Left->Right
    for y in range(output_image.height):
        for x in range(output_image.width):
            # for the given pixel at w,h, lets check its value against the threshold
            if output_image.getpixel((x, y)) == (0,0,0,255) :  # 1,2,3 - RGB, 4- intensywnosc od 0 do 255
                break
            else:
                output_image.putpixel((x, y), (0, 0, 10, 255))

    return output_image

def from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    r, g, b = rgb
    return f'#{r:02x}{g:02x}{b:02x}'


for m in get_monitors():
    print(str(m))

root = Tk()
root.title("Lukasz Morawski")
root.geometry("300x300+100+100")
image = Image.open("bus1.png")

resize_image = image.resize((form_width, form_heigth))
ph = ImageTk.PhotoImage(resize_image)
photo = PhotoImage(file="bus1.PNG")
label = Label(root, image=ph, bg=from_rgb((0,0,10)))
im1 = delete_background(image, 0)
im1 = im1.save("bus1.png")
label.place(x=10, y=10)
root.configure(bg=from_rgb((0,0,10)))
root.wm_attributes("-transparentcolor", from_rgb((0,0,10)) )
move_up_down()      # <-- call to move_me
root.overrideredirect(True)
root.mainloop()