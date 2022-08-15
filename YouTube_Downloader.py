import os
import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from pytube import YouTube, Stream
from PIL import ImageTk, Image
from pytube import YouTube, Stream
import os


def message():
    return messagebox.showinfo('Wait!!', 'Your Video Is Downloading')


def get_resolutions(url):
    yt = YouTube(str(url))
    streams = set()
    for stream in yt.streams.filter(type="video"):
        streams.add(stream.resolution)
    return streams


path = str(os.getcwd())


# funcitons
def Reset():
    Instructions.config(text="copy paste your link")
    Instructions.update()


def Download(path):
    inp = str(inputtxt.get(1.0, "end-1c"))
    yt1 = YouTube(inp)
    yt1.streams.get_highest_resolution().download(path)
    PopUp(path)


def Download_Quality(x, path):
    str(x)
    inp = str(inputtxt.get(1.0, "end-1c"))
    yt1 = YouTube(inp)
    yt1.streams.filter(res=x).first().download(path)
    PopUp(path)


def directory():
    # get a directory path by user
    filepath1 = filedialog.askdirectory(initialdir=path,
                                        title="Select Path")
    path1 = str(filepath1)

    return filepath1


def mp3():
    filepath = filedialog.askdirectory(initialdir=path,
                                       title="Select Path")
    urlMP3 = inputtxt.get(1.0, "end-1c")
    yt = YouTube(str(urlMP3))
    message()
    x = yt.streams.filter(only_audio=True).first().download(filepath)
    base, ext = os.path.splitext(x)
    new_file = base + '.mp3'
    os.rename(x, new_file)

    # return urlMP3


def _360p():
    filepath = filedialog.askdirectory(initialdir=path,
                                       title="Select Path")
    urlMP3 = inputtxt.get(1.0, "end-1c")
    yt = YouTube(str(urlMP3))
    message()
    x = yt.streams.filter(progressive=True, file_extension='mp4', res="360p").order_by(
        'resolution').desc().first().download(filepath)


def _480p():
    filepath = filedialog.askdirectory(initialdir=path,
                                       title="Select Path")
    urlMP3 = inputtxt.get(1.0, "end-1c")
    yt = YouTube(str(urlMP3))
    message()
    x = yt.streams.filter(progressive=True, file_extension='mp4', res="480p").order_by(
        'resolution').desc().first().download(filepath)


def _240p():
    filepath = filedialog.askdirectory(initialdir=path,
                                       title="Select Path")
    urlMP3 = inputtxt.get(1.0, "end-1c")
    yt = YouTube(str(urlMP3))
    message()
    x = x = yt.streams.filter(res="240p").first().download(filepath)


def _144p():
    filepath = filedialog.askdirectory(initialdir=path,
                                       title="Select Path")
    urlMP3 = inputtxt.get(1.0, "end-1c")
    yt = YouTube(str(urlMP3))
    message()
    x = yt.streams.filter(res="360p").first().download(filepath)


def PopUp(path):
    Instructions.config(
        text="Your Download is starting ...................!!!")
    Instructions.update()
    # xINPUT = DownloadYT()
    pop = Toplevel(frame)
    pop.geometry("300x300")
    pop.title("Progress report")
    pop['background'] = "#E62D27"
    photo_pop = PhotoImage(file="1.png")
    pop.iconphoto(False, photo)

    Progress_Report1 = Label(
        pop, text="your Download is started ...........", font=('Helvetica 15'))
    Progress_Report1.pack()
    Progress_Report1.config(bg="#FFFFFF")

    Progress_Report = Label(
        pop, text="Progress Report -: ", font=('Helvetica 15'))
    Progress_Report.pack()
    Progress_Report.config(text="this is progress report")
    Progress_Report.config(bg="#FFFFFF")

    URL = inputtxt.get(1.0, "end-1c")
    yt = YouTube(str(URL))
    filesize1 = yt.streams.get_highest_resolution()
    filesize1.title
    files = filesize1.filesize
    Progress_Report2 = Label(pop, text="\nYour link is  -: \n" + URL +
                             "\n your video is Downloaded😀🤩\n"+"\nVideo Tittle -: \n" + filesize1.title
                             #  + "\nVideo Resolution -: " +
                             #  filesize1.resolution
                             + "\nyour file size is " +
                             str(round(files/1000000, 2))+"mb" + "\n\nyour file is at -: " + str(path), font=('Helvetica 15'))
    Progress_Report2.pack()
    Progress_Report.place(relx=0.5, rely=0.5, anchor=CENTER)
    # Progress_Report2.config(text="this is progress report")
    Progress_Report2.config(bg="#FFFFFF")


# Tkinter window
frame = Tk()
frame.title("YouTube Video Downloader")
frame.geometry('600x700')
# frame.resizable(false, false)

# Tkinter tittle logo

photo = PhotoImage(file="1.png")
frame.iconphoto(False, photo)

# tkinter background color
frame['background'] = "#E62D27"


# Tkinter  youtube button image on window
x = Image.open("1.png")
resize_image = x.resize((50, 50))
imgLogo = ImageTk.PhotoImage(resize_image)
l = Label(bg="#E62D27", image=imgLogo)
l.pack()
l.place(relx=0.3, rely=0.5, anchor=CENTER)

# Tkinter youtube GIF
youtubeGIF = Image.open("youtube.gif")
resize_youtubeGIF = youtubeGIF.resize((500, 300))
imgYoutube = ImageTk.PhotoImage(resize_youtubeGIF)
youtubeGIF_Label = Label(bg="#E62D27", image=imgYoutube)
youtubeGIF_Label.pack()
youtubeGIF_Label.place(relx=0.5, rely=0.25, anchor=CENTER)


# Tkinter Input Feild


inputtxt = Text(frame,
                height=3,
                width=60)
inputtxt.pack()
inputtxt.place(relx=0.5, rely=0.5, anchor=CENTER)


# Tkinter Downlaod button
imgDownload_button = PhotoImage(file="4.png")
Download_Button = Button(frame, text='Download', bg="#E62D27",
                         image=imgDownload_button, command=lambda: [message(), Download(path)])
Download_Button.pack()
Download_Button.place(relx=0.5, rely=0.7, x=-20)


# Reset

ResetIMAGE = Image.open("reset.png")
ResetIMAGE_RESIZE = ResetIMAGE.resize((50, 50))
ResetIMAGE_RESIZE_BUTTON = ImageTk.PhotoImage(ResetIMAGE_RESIZE)
Reset_BUTTON = Button(frame, text='Reset Button', bg="#ffffff",   image=ResetIMAGE_RESIZE_BUTTON,
                      command=Reset)
Reset_BUTTON .pack()
Reset_BUTTON .place(relx=0.4, rely=0.7, x=-25)

# Path selection B
PathImage = Image.open("5.png")
PathImageResized = PathImage.resize((50, 50))
imgReset_button = ImageTk.PhotoImage(PathImageResized)
path_Button = Button(frame, text='Select Directory', image=imgReset_button, bg="#ffffff",
                     command=lambda: [directory(), message(), Download(path)])
path_Button.pack()
path_Button.place(relx=0.6, rely=0.7, x=-17)


# mp3 button
MP3IMAGE = Image.open("mp3.png")
MP3IMAGE_RESIZE = MP3IMAGE.resize((50, 50))
MP3IMAGE_RESIZE_BUTTON = ImageTk.PhotoImage(MP3IMAGE_RESIZE)
mp3_Button = Button(frame, text='Select Directory', image=MP3IMAGE_RESIZE_BUTTON, bg="#ffffff",
                    command=lambda: [mp3(), PopUp(path)])
mp3_Button.pack()
mp3_Button.place(relx=0.5, rely=0.8, x=-20)


IMAGE360 = Image.open("360.jpg")
IMAGE360_RESIZE = IMAGE360.resize((50, 50))
IMAGE360_RESIZE_BUTTON = ImageTk.PhotoImage(IMAGE360_RESIZE)
p360_Button = Button(frame, text='Select Directory',   image=IMAGE360_RESIZE_BUTTON,
                     bg="#E62D27",
                     command=lambda: [_360p(), PopUp(path)])
p360_Button.pack()
p360_Button.place(relx=0.4, rely=0.8, x=-25)


IMAGE240 = Image.open("240.png")
IMAGE240_RESIZE = IMAGE240.resize((50, 50))
IMAGE240_RESIZE_BUTTON = ImageTk.PhotoImage(IMAGE240_RESIZE)
p240_Button = Button(frame, text='Select Directory', image=IMAGE240_RESIZE_BUTTON, bg="#ffffff",
                     command=lambda: [_240p(), PopUp(path)])
p240_Button.pack()
p240_Button.place(relx=0.6, rely=0.8, x=-17)


IMAGE144 = Image.open("144.png")
IMAGE144_RESIZE = IMAGE144.resize((50, 50))
IMAGE144_RESIZE_BUTTON = ImageTk.PhotoImage(IMAGE144_RESIZE)
p144_Button = Button(frame, text='Select Directory', image=IMAGE144_RESIZE_BUTTON, bg="#ffffff",
                     command=lambda: [_144p(), PopUp(path)])
p144_Button.pack()
p144_Button.place(relx=0.5, rely=0.9, x=-18)


# tkinter label for Instructions
Instructions = Label(frame, bg="#E62D27", text="copy paste your link")
Instructions.pack()
Instructions.place(relx=0.5, y=415, anchor=CENTER)
Instructions.config(font=("Comic Sans", 20))
Instructions.config(fg="#ffe6e6")


# tkinter mainloop
mainloop()
