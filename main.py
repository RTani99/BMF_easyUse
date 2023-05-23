import tkinter as tk
from tkinter import filedialog
import shutil
import os

layer = 0
entry = [None] * 50
entry_counter = 0
max_layer = 0
dir_flag = False

def copy_rename_file():
    global max_layer
    global dir_flag
    global layer
    # ファイルを選択
    selected_file = filedialog.askopenfilename()
    if selected_file:
        # コピー先のディレクトリを選択
        destination_directory = filedialog.askdirectory()
        new_dir = destination_directory + '/test'
        if not dir_flag:
            dir_flag = True
            os.mkdir(new_dir)
        if destination_directory:
            # 新しいファイル名を入力
            max_layer += int(entry[0].get())

            # ファイルをコピーして名前を変更
            for layer in range(max_layer + 1):            
                if (layer / 1000 >= 1):
                    new_file_name = '1_' + str(layer+1) + '.png'
                    layer += 1
                elif (layer / 100 >= 1):
                    new_file_name = '1_0' + str(layer+1) +'.png'
                    layer += 1
                elif(layer / 10 >= 1):
                    new_file_name = '1_00' + str(layer+1) + '.png'
                    layer += 1
                else:
                    new_file_name = '1_000' + str(layer+1) + '.png'
                    layer += 1
                new_file_path = new_dir + '/' + new_file_name
                shutil.copy2(selected_file, new_file_path)
            status_label.configure(text="ファイルをコピーして名前を変更しました。")
        else:
            status_label.configure(text="コピー先のディレクトリを選択してください。")
    else:
        status_label.configure(text="ファイルを選択してください。")
    layer += max_layer

def add_image():
    global entry_counter
    entry_counter += 1
    entry[entry_counter] = tk.Entry(window)
    entry[entry_counter].pack()

# GUIウィンドウを作成
window = tk.Tk()
window.title("ファイルコピー＆名前変更アプリ")

# ラベルを作成
label = tk.Label(window, text="Layer数")
label.pack()

# テキスト入力フィールドを作成
entry[0] = tk.Entry(window)
entry[0].pack()

# ボタンを作成
button = tk.Button(window, text="画像を選択する", command=copy_rename_file)
button.pack()

add_button = tk.Button(window, text="画像を追加する", command=add_image())
add_button.pack()

# ステータスラベルを作成
status_label = tk.Label(window, text="")
status_label.pack()

# GUIループを開始
window.mainloop()