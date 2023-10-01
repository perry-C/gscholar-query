import os
import webbrowser

import dearpygui.dearpygui as dpg
from screeninfo import get_monitors

from scrape_paper import scrape_paper

monitor_info = get_monitors()[0]

window_width = 1200
window_height = 800

x_pos = (monitor_info.width - window_width) // 2
y_pos = (monitor_info.height - window_height) // 2

dpg.create_context()
dpg.create_viewport(x_pos=x_pos, y_pos=y_pos, title='Custom Title',
                    width=window_width, height=window_height)


def quit(sender, app_data):
    if app_data == 256:
        dpg.stop_dearpygui()


def enter_value(sender, app_data):
    # The keypressed is enter
    if app_data == 257:
        dpg.set_value('text_2', 'Processing...')
        value = dpg.get_value('input_1')
        scrape_paper(value)
        dpg.set_value('text_2', 'Scraping finished!')
        webbrowser.open_new('file://' + os.path.realpath('data/data.html'))


with dpg.font_registry():
    main_font = dpg.add_font('assets/fonts/CascadiaCode.ttf', 24)

with dpg.handler_registry():
    dpg.add_key_press_handler(callback=quit)
    dpg.add_key_press_handler(callback=enter_value)


with dpg.window(width=window_width, height=window_height):
    dpg.add_text('Enter the paper you are looking for:',
                 tag='text_1')
    dpg.add_input_text(
        default_value='', tag='input_1')
    dpg.add_text(tag='text_2', wrap=window_width)
    dpg.add_listbox(items=[*range(10, 60, 10)],
                    label='Number of items to search for')
    dpg.bind_font(main_font)


dpg.setup_dearpygui()
dpg.show_font_manager()
dpg.show_viewport()

# below replaces, start_dearpygui()
while dpg.is_dearpygui_running():
    # insert here any code you would like to run in the render loop
    # you can manually stop by using stop_dearpygui()
    # print('this will run every frame')
    dpg.render_dearpygui_frame()


# dpg.destroy_context()
