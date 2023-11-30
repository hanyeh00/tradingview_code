import datetime
import socket
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import PySimpleGUI as sg
import time

sg.theme('DarkBlue4')
layout = [[sg.Text('Demonstration of Tradingview')],
          [sg.MLine(key='-ML1-' + sg.WRITE_ONLY_KEY, size=(40, 8))],
          [sg.Button('Exit')]]
# chrome....
sr = Service(r"C:\Program Files (x86)\chromedriver.exe")
chrome_options = Options()
chrome_options.add_argument('--headless')
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])

driver = webdriver.Chrome(service=sr)

url = "http://tradingview.com/"

driver.get(url)
time.sleep(15)
window = sg.Window('Window Title', layout, finalize=True)
# name1, name4 = "close-button-ggQH9Zyp","main-text-ggQH9Zyp"
# name3="message-PQUvhamm"
name1, name4 = "button-JoOdB0AC apply-common-tooltip overlayButton-ucBqatk5", "message-PQUvhamm"


def create_server(text):
    host = '127.0.0.1'
    port = 5001
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.bind(('', port))
    soc.listen()
    conn, address = soc.accept()
    conn.sendall((text).encode())
    conn.close()
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    window['-ML1-' + sg.WRITE_ONLY_KEY].print("operation complete", text, st, text_color='Black')


search = {"buy", "sell", "exit"}
global word,z


z=0

def popup():
    try:
        # t0 = pc()
        # click_on_button()
        txt = driver.find_elements(By.CLASS_NAME, name4)

        word = txt[0].text
        global z
        if word != z:
            msg = [create_server(word) for value in search if (value in word)]
            z=word


        else:

            pass



    except Exception:
        pass



while True:
    event, values = window.read(timeout=100)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    else:
        popup()


window.close()
