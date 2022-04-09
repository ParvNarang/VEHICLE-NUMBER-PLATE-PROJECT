from tqdm import tqdm
import time
import PySimpleGUI as sg
def a():

    g1 = r'/Users/parvnarang/Desktop/x.gif'
    gifs = [g1]
    layout = [[sg.Image(background_color='white', key='-IMAGE-', right_click_menu=['UNUSED', 'Exit'])],[sg.Text('              ... LOADING ...  ',key='smptex')],]
    window = sg.Window('LOADING',layout, finalize=True,size=(300,300))
    image =  window['-IMAGE-']
    event, values = window.read(timeout=100)
    image.update_animation(g1, 100)

    for i in tqdm(range(40)):
        time.sleep(0.01)
        pass

a()