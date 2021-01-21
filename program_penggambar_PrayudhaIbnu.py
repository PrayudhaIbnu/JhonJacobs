from tkinter import *
from PIL import Image, ImageDraw

class ImageGenerator():
    def __init__(self,parent, *kwargs):
        self.framekanvas = Frame(parent)
        self.frameTombol = Frame(parent)
        
        self.parent = parent
        self.sizex = 1024
        self.sizey = 768
        self.b1 = "tidakDiKlik"
        self.xold = None
        self.yold = None

        self.koordinat= []
        self.buatTempatMenggambar()
        self.menggambarDgPensil()
        self.tombol()

    def buatTempatMenggambar(self):
        self.tempatMenggambar=Canvas(self.framekanvas,width=self.sizex,height=self.sizey, bg='white')
        self.tempatMenggambar.grid(row = 0, column=0)

        self.framekanvas.pack()

    def tombol(self):
        Button(self.frameTombol, text='Hapus', command=self.hapus).pack(side=LEFT)
        Button(self.frameTombol, text='Simpan', command=self.simpan).pack()

        self.frameTombol.pack()

    def menggambarDgPensil(self):
        self.tempatMenggambar.bind("<Motion>", self.pembuatGaris)
        self.tempatMenggambar.bind("<ButtonPress-1>", self.jikaDilepas)
        self.tempatMenggambar.bind("<ButtonRelease-1>", self.jikaDiKlik)

        self.image=Image.new("RGB",(400,400),(255,255,255))
        self.draw=ImageDraw.Draw(self.image)

    def simpan(self):
        self.draw.line(self.koordinat,(0,128,0),width=3)
        filename = "temp.jpg"
        self.image.save(filename)

    def hapus(self):
        self.tempatMenggambar.delete("all")
        self.koordinat=[]

    def jikaDilepas(self,event):
        self.b1 = "diKlik"

    def jikaDiKlik(self,event):
        self.b1 = "tidakDiKlik"
        self.xold = None
        self.yold = None

    def pembuatGaris(self,event):
        if self.b1 == "diKlik":
            if self.xold is not None and self.yold is not None:
                garis = event.widget.create_line(self.xold,self.yold,event.x,event.y,smooth='true')
                self.koordinat.append((self.xold,self.yold))
        self.xold = event.x
        self.yold = event.y


if __name__ == "__main__":
    root=Tk()
    root.title('aplikasi menggambar')
    root.wm_geometry("%dx%d" % (430, 430))
    ImageGenerator(root)
    root.mainloop()