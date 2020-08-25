import tkinter as tk
import tkinter.font as tkFont
from main import get_htmltext
from tkinter.filedialog import askdirectory
from tkinter import messagebox
# from lib.fbCrawler import start_crawl 

class Application(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.grid()
        self.CreateFrame()
        self.folderPath = ''

    def getFolderPath(self):
        self.folderPath = askdirectory()
        self.entry2.insert(tk.END, self.folderPath)

    def primary(self):
        get_htmltext(self.entry.get(), self.entry2.get())
        messagebox.showinfo("訊息","檔案產生完畢!")

    def CreateFrame(self):
        titleStyle = tkFont.Font(family="Lucida Grande", size=30)
        labelStyle = tkFont.Font(family="Lucida Grande", size=15)

        self.label = tk.Label(self, font=titleStyle)
        self.label["text"] = "乖寶-留言抓取"
        self.label.grid(row=1, column=0, sticky=tk.N+tk.W, padx=180, pady=20)

        self.label2 = tk.Label(self, font=labelStyle)
        self.label2["text"] = "貼文網址"
        self.label2.grid(row=2, column=0, sticky=tk.N+tk.W, padx=80, pady=20)

        self.entry = tk.Entry(self, width=50)
        self.entry.place(width=200, height=200)
        self.entry.grid(row=2, column=0, sticky=tk.E, padx=80)

        self.entry2 = tk.Entry(self, width=50)
        self.entry2.grid(row=3, column=0, sticky=tk.E, padx=80)

        self.button = tk.Button(self, width=10, command=self.getFolderPath)
        self.button["text"] = "檔案產生路徑"
        self.button.grid(row=3, column=0, sticky=tk.N+tk.W, padx=80, pady=20)

        self.button2 = tk.Button(self, width=30, command=self.primary)
        self.button2["text"] = "開始抓取"
        self.button2.grid(row=4, column=0, sticky=tk.N+tk.W, padx=180, pady=20)

root = tk.Tk()
root.geometry('600x400')
app = Application(root)
root.mainloop()
