import subprocess
import tkinter
from tkinter import ttk
import urllib.request
import zipfile


def download_tools():
    destination = 'platform_tools.zip'
    url = 'https://dl.google.com/android/repository/platform-tools-latest-windows.zip'
    urllib.request.urlretrieve(url, destination)

    zfile = zipfile.ZipFile(file='platform_tools.zip')
    zfile.extractall('platform-tools')


def run_command(exec_command):
    process = subprocess.Popen(exec_command)
    process.wait()


def create_button(app_form, button_text, button_column, button_row, button_width, button_command):
    button = ttk.Button(app_form)
    button['width'] = button_width
    button['text'] = button_text
    button['command'] = button_command
    button.grid(column=button_column, row=button_row)


def start_adb_service():
    run_command(f'adb start-server')


root = tkinter.Tk()
root.title("FAST8 android ADB manager ")
form = ttk.Frame(root, padding=5)
form.grid()

create_button(form, "Скачать и установить ABD", 1, 1, 30, download_tools)
create_button(form, "Запустить службу ABD", 1, 2, 30, start_adb_service)

root.mainloop()
