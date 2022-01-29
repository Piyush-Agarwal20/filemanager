import os

def CreateFolderifnot(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(files,folder):
    CreateFolderifnot(folder)
    for file in files:
      os.replace(file,f"{folder}/{file}")


files=os.listdir()

imgsEx=[".img",".jpeg",".jpg",".png"]
progEx=[".py",".pug",".html",".c",".css",".java"]
docEx=[".docx",".txt","doc",".pdf",".xlsx"]
mediaEx=[".mp3",".mp4",".flv",".wav"]

images=[file for file in files if os.path.splitext(file)[1].lower() in imgsEx ]
progs=[file for file in files if os.path.splitext(file)[1].lower() in progEx]
docs=[file for file in files if os.path.splitext(file)[1].lower() in docEx]
medias=[file for file in files if os.path.splitext(file)[1].lower() in mediaEx]

move(medias,"media")
move(images,"images")
move(docs,"docs")