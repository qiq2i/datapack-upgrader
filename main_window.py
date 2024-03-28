import tkinter as tk
from tkinter import ttk
import pyperclip  # 需要额外安装pyperclip库，可通过pip install pyperclip命令安装
from nbt_to_components import transfer  # 导入transfer函数

root = tk.Tk()#创建主窗口

#设置窗口属性
root.title("物品NBT格式转components格式 "+"0.1")#标题
root.geometry("900x500")#大小

#创建控件
label = tk.Label(root, text="物品NBT格式转components格式")
label.grid(row=0, column=1)#grid()布局

# 创建并放置两个输入框
label_Item_id = tk.Label(root, text="物品ID：")
label_Item_id.grid(row=1, column=0)

Item_id = tk.Text(root,width=60,height=1,wrap='word')
Item_id.grid(row=1, column=1)
Item_id.insert(tk.END, "stone")

label_Item_id_tip1 = tk.Text(root, wrap='word',width=30,height=10)
label_Item_id_tip1.grid(row=2, column=2)
label_Item_id_tip1.insert(tk.END, "物品为成书written_book和书与笔writable_book时，必须写物品id。这是由于这两个物品的NBT有相同的部分，而转化为components时要进行区分。\n\n物品NBT例子：\n{Damage:50}")
label_Item_id_tip1.configure(cursor="arrow")  # 隐藏光标
label_Item_id_tip1.config(highlightthickness=0)  # 隐藏高亮边框
label_Item_id_tip1.config(selectbackground=root.cget("bg"))  # 设置选中文本背景色与窗口背景色一致

label_Item_nbt = tk.Label(root, text="物品NBT：")
label_Item_nbt.grid(row=2, column=0)

Item_nbt = tk.Text(root,width=60,height=10)
Item_nbt.grid(row=2, column=1)

# 输出
label_Item_id = tk.Label(root, text="物品components：")
label_Item_id.grid(row=4, column=0)
Item_components = tk.Text(root,width=60,height=10)
Item_components.grid(row=4, column=1)
Item_components.insert(tk.END, "[]")
# 点击转化
def transfer_bottom():
    try:
        id = Item_id.get('1.0', 'end')
    except Exception:
        id = "air"
    try:
        nbt = Item_nbt.get('1.0', 'end')
    except Exception:
        nbt = "{}"
    try:
        components = transfer(id,nbt)
    except Exception:
        components = "[]"
    Item_components.delete('1.0', 'end')  # 删除现有内容
    Item_components.insert(tk.END, components)  # 插入新内容

# 创建一个按钮，点击后获取两个输入框的内容
get_inputs_button = ttk.Button(root, text="NBT转components", command=transfer_bottom)
get_inputs_button.grid(row=3, column=1)

# 复制按钮
def copy_string_to_clipboard():
    # 需要复制的字符串
    target_string = Item_components.get('1.0', 'end')

    # 将字符串复制到剪贴板
    pyperclip.copy(target_string)

copy_button = ttk.Button(root, text="复制组件components", command=copy_string_to_clipboard)
copy_button.grid(row=5, column=1)

# 清除按钮
def clear():
    # 需要复制的字符串
    Item_nbt.delete('1.0', 'end')

clear_button = ttk.Button(root, text="清空物品nbt内容", command=clear)
clear_button.grid(row=4, column=2)

def open_url(url):
    import webbrowser
    webbrowser.open_new(url)

# 创建一个Label，其中包含网址文本，并绑定点击事件
link_label_1 = tk.Label(root, text="点击进入:B站 https://space.bilibili.com/355336076")
link_label_1.bind("<Button-1>", lambda event: open_url("https://space.bilibili.com/355336076"))
link_label_1.grid(row=5, column=2)

link_label_2 = tk.Label(root, text="https://github.com/qiq2i/datapack-upgrader")
link_label_2.bind("<Button-1>", lambda event: open_url("https://github.com/qiq2i/datapack-upgrader"))
link_label_2.grid(row=6, column=2)

name = tk.Label(root, text="小棋孜")
name.grid(row=7, column=2)

'''
# 图标
root.iconphoto(True, tk.PhotoImage(file='title.png'))
# 创建一个图片对象
image = tk.PhotoImage(file="title.png")
# 创建一个标签，并将其设置为显示图片
label_png = tk.Label(root, image=image)
label_png.grid(row=4, column=2)
'''
# 主循环，处理事件和保持窗口打开
root.mainloop()