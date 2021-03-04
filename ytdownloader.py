import tkinter as tk
from pytube import YouTube

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Youtube Video Downloader')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='Enter Youtube Video link:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)

def download ():
    
    x1 = YouTube(entry1.get())

    label3 = tk.Label(root, text= 'Downloading ' + x1.title )
    canvas1.create_window(200, 210, window=label3)
    stream = x1.streams.first()
    stream.download()
    print("Download Complete")
    label4 = tk.Label(root, text= 'Download Complete ',fg='Green')
    canvas1.create_window(200, 230, window=label4)
    label5 = tk.Label(root, text= 'File Path: Desktop ',fg='yellow')
    canvas1.create_window(200, 250, window=label5)
    
button1 = tk.Button(text='Download', command=download, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)


root.mainloop()


