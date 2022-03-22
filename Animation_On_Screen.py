from tkinter import *
import csv
from PIL import Image, ImageTk
# from screeninfo import get_monitors
# import random




i = 0
form_width = 200
form_height = 90
lastClickX = 0 # used for dragging form
lastClickY = 0 # used for dragging form
pos_x = 0
pos_from_file = 0
move = 0

def read_Setting():
    global pos_from_file
    try:
        txt_file = open('ustawienia.txt')
        pos_from_file = txt_file.read()
    except IOError:
        pos_from_file = open('ustawienia.txt', 'w+') #create file
        pos_from_file = 0
    finally:
        txt_file.close()
        # print('USTAWIENIA: ', pos_from_file)
read_Setting()

def move_up_down():
    global move
    global lastClickX
    screen_w = root.winfo_screenwidth()  # width of the screen
    screen_h = root.winfo_screenheight()  # height of the screen
    global form_width
    global form_height

    global i
    form_width = 200
    form_height = 100
    if pos_from_file == 0:
        pos_x = screen_w - form_width
    else:
        pos_x = pos_from_file

    #pos_x = str(lastClickX)
    #if lastClickX != 0:
    #    pos_x = str(lastClickX)
    #if move == 0:
        i = i + 1

        x, y = str(pos_x), str(i)
        loc = str(form_width) + "x" + str(form_height) + "+" + x + '+' + y
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


#for m in get_monitors():
#    print(str(m))

# def get_monitor_from_coord(x, y):
#     monitors = get_monitors()
#
#     for m in reversed(monitors):
#         if m.x <= x <= m.width + m.x and m.y <= y <= m.height + m.y:
#             return m
#     return monitors[0]


def SaveLastClickPos(event):
    global move
    move = 0
    global lastClickX, lastClickY
    lastClickX = event.x
    lastClickY = event.y


def Dragging(event):
    global move
    move = 1
    x, y = event.x - lastClickX + root.winfo_x(), event.y - lastClickY + root.winfo_y()
    root.geometry("+%s+%s" % (x , y))

def Finish_Dragging(event):
    global move
    move = 0
    # Get the screen which contains top
    # current_screen = get_monitor_from_coord(root.winfo_x(), root.winfo_y())
    # print(current_screen.width, current_screen.height, root.winfo_x(), root.winfo_y())
def Terminate_Program(event):
    quit()



root = Tk()
root.title("Lukasz Morawski")
root.geometry("300x300+100+100")
image = Image.open("bus1.png")

resize_image = image.resize((form_width, form_height))
ph = ImageTk.PhotoImage(resize_image)
photo = PhotoImage(file="bus1.PNG")
label = Label(root, image=ph, bg=from_rgb((0,0,10)))
im1 = delete_background(image, 0)
im1 = im1.save("bus1.png")
label.place(x=10, y=10)

# root.bind('<Button-1>', SaveLastClickPos) # left click
# root.bind("<ButtonRelease-1>", Finish_Dragging)
# root.bind('<B1-Motion>', Dragging) # moving
root.bind('<Button-3>', Terminate_Program) # right click
root.configure(bg=from_rgb((0,0,10)))
root.wm_attributes("-transparentcolor", from_rgb((0,0,10)) )

move_up_down()      # <-- call to move_me
root.overrideredirect(True)

root.mainloop()