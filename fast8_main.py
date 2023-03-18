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


def run_command_with_stdout(exec_command):
    process = subprocess.Popen(exec_command, stdout=subprocess.PIPE)
    result = process.communicate()

    return result[0].decode().split('\n')


def create_button(app_form, button_text, button_column, button_row, button_width, button_command):
    button = ttk.Button(app_form)
    button['width'] = button_width
    button['text'] = button_text
    button['command'] = button_command
    button.grid(column=button_column, row=button_row)


def start_adb_service():
    result = run_command_with_stdout(f'adb devices')
    print(result)
    success = False
    for i in result:
        if i.find('daemon started successfully') != -1:
            success = True

    if success:
        print('ADB started')


def download_list_packages():
    result = run_command_with_stdout(f'adb shell pm list packages')
    for i in result:
        print(i)


def create_package_list(app_form, root):
    listbox = ttk.Treeview(app_form, show="headings", columns=("#1", "#2", "#3"), height=15)
    listbox.column("#1", width=300)
    listbox.column("#2", width=400)
    listbox.column("#3", width=80)
    listbox.grid(column=2, row=3, rowspan=15)
    listbox.heading("#1", text="Пакет")
    listbox.heading("#2", text="Наименование")
    listbox.heading("#3", text="Бесполезный")
    ysb = ttk.Scrollbar(root, command=listbox.yview)
    listbox.configure(yscroll=ysb.set)

    #for item in bases_list:
    #    listbox.insert(parent=item['parent'], index=bases_list.index(item), values=item['name'])


root = tkinter.Tk()
root.title("FAST8 android ADB manager ")
form = ttk.Frame(root, padding=5)
form.grid()

label_frame1 = ttk.LabelFrame(root, text='Команды')
label_frame1.grid(column=1, row=1)

label_frame2 = ttk.LabelFrame(root, text='Пакеты')
label_frame2.grid(column=1, row=2)

create_button(label_frame1, "Скачать и установить ADВ", 1, 1, 40, download_tools)
create_button(label_frame1, "Запустить службу ADВ", 2, 1, 30, start_adb_service)
create_button(label_frame1, "Получить с устройства список установленных пакетов", 3, 1, 50, download_list_packages)

create_package_list(label_frame2, root)

root.mainloop()
