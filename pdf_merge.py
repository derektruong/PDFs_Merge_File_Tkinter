from tkinter import *
from tkinter import filedialog
import MakeCenter
import PyPDF2
import os


def Replace(string):
    return string.replace('/', '\\\\')


def main():
    def Chon_Path_file():
        nonlocal str_Path_file
        folder_name = filedialog.askdirectory()
        folder_name = Replace(folder_name)
        str_Path_file.set(folder_name)

    def Chon_New_Path_file():
        nonlocal str_New_Path_file
        folder_name = filedialog.askdirectory()
        folder_name = Replace(folder_name)  # show an "Open" dialog box and return the path to the selected file
        str_New_Path_file.set(folder_name)

    def tiepAct():
        str_Path_file.set("")
        str_New_Path_file.set("")
        str_New_File.set("")
        strKQ.set("")

    def NoiAct():
        try:
            merge = PyPDF2.PdfFileMerger()
            Path_name = str(str_Path_file.get())
            New_Path_name = str(str_New_Path_file.get())
            New_File_name = str(str_New_File.get())
            for file in os.listdir(Path_name):
                filename = os.fsdecode(file)
                if filename.endswith("pdf"):
                    merge.append(PyPDF2.PdfFileReader(f"{Path_name}\\{filename}"))
            New_Path_name = New_Path_name + '\\\\'
            with open(f"{New_Path_name}{New_File_name}.pdf", 'wb') as file_temp:
                merge.write(file_temp)
        except FileNotFoundError as err:
            strKQ.set(f"Lỗi {err} thử lại!")
        except FileExistsError as err:
            strKQ.set(f"Lỗi {err} thử lại!")
        else:
            strKQ.set('Đã xong! Đóng để xem file vừa nối hoặc tiếp tục!')

    root = Tk()
    # Các biến entry
    str_Path_file = StringVar()
    str_New_Path_file = StringVar()
    str_New_File = StringVar()
    strKQ = StringVar()

    root.title("Nối file pdf đơn giản - Minh Đức")
    root.minsize(height=400, width=900)
    root.resizable(height=False, width=False)
    MakeCenter.MakeCenter(root)
    Label(root, text="NỐI FILE PDFs", fg="yellow", justify=CENTER, font=("Segoe U", 20)).place(x=450, y=25, anchor="center")
    Label(root, text="Đường dẫn chứa file pdf cần nối:", font=("Helvetica", 14)).place(x=40, y=70)
    Entry(root, width=40, textvariable=str_Path_file, bd=0.5, font=("Helvetica", 14)).place(x=330, y=70)

    Label(root, text="Đường dẫn xuất file pdf đã nối:", font=("Helvetica", 14)).place(x=40, y=115)
    Entry(root, width=40, textvariable=str_New_Path_file, font=("Helvetica", 14)).place(x=330, y=115)

    Label(root, text="Tên file muốn xuất:", font=("Helvetica", 14)).place(x=40, y=160)
    Entry(root, width=40, textvariable=str_New_File, font=("Helvetica", 14)).place(x=330, y=160)

    # Button Choose file
    frameButton_Chon1 = Frame()
    Button(frameButton_Chon1, text="Chọn", fg='lawn green',borderwidth=0,relief='groove', command=Chon_Path_file).pack(side=BOTTOM)
    frameButton_Chon1.place(x=780, y=70)
    frameButton_Chon2 = Frame()
    Button(frameButton_Chon2, text="Chọn", fg='deep sky blue',borderwidth=0,relief='groove', command=Chon_New_Path_file).pack(side=BOTTOM)
    frameButton_Chon2.place(x=780, y=115)

    # Button Solve
    frameButton = Frame()
    Button(frameButton, text="Nối", fg='cyan',borderwidth=0.5, command=NoiAct, font=("Arial", 12)).pack(side=LEFT)
    Button(frameButton, text="Tiếp", fg='pink',borderwidth=0.5, command=tiepAct, font=("Arial", 12)).pack(side=LEFT)
    Button(frameButton, text="Thoát", fg='red',borderwidth=0.5, command=root.quit, font=("Arial", 12)).pack(side=LEFT)
    frameButton.place(x=400, y=200)

    Label(root, text="Kết quả:", fg="orange", font=("Helvetica", 18)).place(x=170, y=250)
    Entry(root, width=50, textvariable=strKQ, bd=0.2, font=("Helvetica", 16)).place(x=270, y=252)
    root.mainloop()


if __name__ == '__main__':
    main()
