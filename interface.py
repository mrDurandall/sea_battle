import tkinter

from common.const import SEA_COLOR_MAIN, SHIP_COLOR, SEA_COLOR_BLOCKED


def button_color_black(event):
    event.widget['background'] = SHIP_COLOR


def button_color_sea(event):
    event.widget['background'] = SEA_COLOR_MAIN


def set_ship(event):
    adjacent_blocks = []
    for x in range(event.widget.x - 1, event.widget.x + 2):
        for y in range(event.widget.y - 1, event.widget.y + 2):
            if 0 <= x <= 9 and 0 <= y <= 9:
                adjacent_blocks.append(buttons[x][y])
    for button in adjacent_blocks:
        button.unbind('<Motion>')
        button.unbind('<Leave>')
        button.unbind('<ButtonRelease-1>')
        button['background'] = SEA_COLOR_BLOCKED
    event.widget['background'] = SHIP_COLOR




window = tkinter.Tk()
window.title('Test')
window.geometry('1000x500')
buttons = []

for x in range(10):
    buttons.append([])
    for y in range(10):
        buttons[x].append(tkinter.Button(window,
                                         height=2,
                                         width=5,
                                         text=f'{x}-{y}',
                                         background=SEA_COLOR_MAIN
                                         ))
        cur_button = buttons[x][y]
        cur_button.grid(column=x, row=y)
        cur_button.bind('<Motion>', button_color_black)
        cur_button.bind('<Leave>', button_color_sea)
        cur_button.bind('<ButtonRelease-1>', set_ship)
        cur_button.x, cur_button.y = x, y
        print(cur_button.x)

window.mainloop()

