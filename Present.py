import customtkinter as ctk
from tkinter import messagebox
import os
import jdatetime
today0 = jdatetime.date.today()
today1 = today0.strftime("%Y-%m-%d")


os.system("title Present")


app = ctk.CTk()
app.geometry("400x660")
app.title("Present")

frame = ctk.CTkFrame(app , corner_radius = 0)
frame.pack(fill = "both" , expand = True)


label = ctk.CTkLabel(frame , text = "حضور و غیاب" , font = ("B nazanin" , 19))
label.pack(pady = 0)

def changecolor(color):
     if color == "روشن":
          ctk.set_appearance_mode("Light")
     elif color == "تیره":
          ctk.set_appearance_mode("Dark")
     elif color == "سیستم":
          ctk.set_appearance_mode("System")

menu_color = ctk.CTkOptionMenu(frame , values = ["سیستم" , "روشن" , "تیره"] , command = changecolor , font = ("B nazanin" , 15))
menu_color.pack(pady = 8)


index = ctk.CTkEntry(frame , placeholder_text = "شماره دانش آموز در لیست" , font = ("B nazanin" , 15) , justify = "right")
index.pack(pady = 4)

fname = ctk.CTkEntry(frame , placeholder_text = "نام دانش آموز" , font = ("B nazanin" , 15) , justify = "right")
fname.pack(pady = 4)

lname = ctk.CTkEntry(frame , placeholder_text = "نام خانوادگی دانش آموز" , font = ("B nazanin" , 15) , justify = "right")
lname.pack(pady = 4)

status = ctk.CTkOptionMenu(frame , values = ["حاضر" , "غیبت موجه" , "غیبت غیر موجه" , "تاخیر زیاد(بیشتر از سی دقیقه)" , "تاخیر کم(کمتر از سی دقیقه)"] , font = ("B nazanin" , 15))
status.pack(pady = 5)

clas2 = ctk.CTkEntry(frame , placeholder_text = "شماره کلاس دانش آموز" , font = ("B nazanin" , 15) , justify = "right")
clas2.pack(pady = 4)

lesson = ctk.CTkEntry(frame , placeholder_text = "درس" , font = ("B nazanin" , 15) , justify = "right")
lesson.pack(pady = 4)

lessono = ctk.CTkOptionMenu(frame , values = ["ریاضی","علوم","مطالعات اجتماعی","ادبیات","انشا(نگارش)","املا","زبان انگلیسی","زبان عربی","قرآن","پیام های آسمان","کار و فناوری","تفکر و سبک زندگی","هنر","ترتیب بدنی","آمادگی دفاعی"] , font = ("B nazanin" , 14))
lessono.pack(pady = 4)

def auti_lesson(choice):

     lesson.delete(0 , "end")
     lesson.insert(0 , choice)

lessono.configure(command = auti_lesson)

teacher = ctk.CTkEntry(frame , placeholder_text = "اسم و فامیل معلم" , font = ("B nazanin" , 15) , justify = "right")
teacher.pack(pady = 4)

def add_student():

     idx = index.get().strip()
     first_name = fname.get().strip()
     last_name = lname.get().strip()
     clas2_student = clas2.get().strip()
     lesson_bell = lesson.get().strip()
     flname_teacher = teacher.get().strip()
     status_student = status.get().strip()

     if not idx or not first_name or not last_name or not clas2_student or not lesson_bell or not status_student or not flname_teacher:
          messagebox.showwarning("خطا" , "تمام ورودی هارا پر کنید")

     else:
          with open(f"{today1}_{clas2_student}.txt" , "a" , encoding = "utf-8") as f:
               f.write(f"{idx}.{flname_teacher} <--نام کوچک و خانوادگی معلم-- {lesson_bell} <--درس-- {status_student} <-- {first_name} {last_name}\n")
               f.close()
               messagebox.showinfo("فرایند صحیح" , "دانش آموز اضافه با موفقیت اضافه شد")

add = ctk.CTkButton(frame , text = "اضافه کردن" , font = ("B nazanin" , 17) , command = add_student)
add.pack(pady = 5)


def remove_student():

     idx = index.get().strip()
     first_name = fname.get().strip()
     last_name = lname.get().strip()
     clas2_student = clas2.get().strip()
     lesson_bell = lesson.get().strip()
     flname_teacher = teacher.get().strip()
     status_student = status.get().strip()

     if not idx or not first_name or not last_name or not clas2_student or not lesson_bell or not status_student or not flname_teacher:
          messagebox.showwarning("خطا" , "تمام ورودی هارا پر کنید")

     elif not os.path.exists(f"{today1}_{clas2_student}.txt"):
          messagebox.showwarning("خطا", "فایلی با این تاریخ و کلاس وجود ندارد!لطفا اطلاعات را مجدد وارد کنید")

     else:
          with open(f"{today1}_{clas2_student}.txt" , "r", encoding = "utf-8") as f:
               lines = f.readlines()

          students = (f"{idx}.{flname_teacher} <--نام کوچک و خانوادگی معلم-- {lesson_bell} <--درس-- {status_student} <-- {first_name} {last_name}\n")
        
          if students in lines:
               lines.remove(students)
               with open(f"{today1}_{clas2_student}.txt", "w", encoding="utf-8") as f:
                    f.writelines(lines)
               messagebox.showinfo("فرایند صحیح", "دانش آموز با موفقیت حذف شد")

          else:
               messagebox.showwarning("خطا", "این دانش آموز وجود ندارد.")

remove = ctk.CTkButton(frame , text = "حذف کردن" , font = ("B nazanin" , 17) , command = remove_student)
remove.pack(pady = 5)


def absentd():
     
     input_absent = ctk.CTkInputDialog(text = "شماره کلاس را وارد کنید" , title = "لیست غایب ها و تاخیری ها" , font = ("B nazanin" , 17))
     number_class = input_absent.get_input().strip()

     input_date = ctk.CTkInputDialog(text = "مثال : 01-08-1404 : تاریخ فایل را وارد کنید" , title = "لیست غایب ها و تاخیری ها" , font = ("B nazanin" , 17))
     date = input_date.get_input().strip()

     if os.path.exists(f"{date}_{number_class}.txt"):

          with open(f"{date}_{number_class}.txt" , "r" , encoding = "utf-8") as infile:
               absentd_students = [line.strip() for line in infile if "غیبت" in line or "تاخیر" in line]

          with open(f"not-present_{date}_{number_class}.txt" , "w" , encoding = "utf-8") as outfile:
               outfile.write("\n".join(absentd_students) + "\n")
          messagebox.showinfo("فرایند صحیح" , "فایل با موفقیت ایجاد شد")

     else:
          messagebox.showwarning("خطا" , "فایلی با این اسم و تاریخ وجود ندارد")

absentd = ctk.CTkButton(frame , text = "فایل غایب ها و تاخیر ها" , font = ("B nazanin" , 15) , command = absentd)
absentd.pack(pady = 5)


def present():
     
     input_present = ctk.CTkInputDialog(text = "شماره کلاس را وارد کنید" , title = "لیست حاضران" , font = ("B nazanin" , 17))
     number_class = input_present.get_input().strip()

     input_date = ctk.CTkInputDialog(text = "مثال : 01-08-1404 : تاریخ فایل را وارد کنید" , title = "لیست حاضران" , font = ("B nazanin" , 17))
     date = input_date.get_input().strip()

     if os.path.exists(f"{date}_{number_class}.txt"):

          with open(f"{date}_{number_class}.txt" , "r" , encoding = "utf-8") as infile:
               present_students = [line.strip() for line in infile if "حاضر" in line]

          with open(f"present_{date}_{number_class}.txt" , "w" , encoding = "utf-8") as outfile:
               outfile.write("\n".join(present_students) + "\n")
          messagebox.showinfo("فرایند صحیح" , "فایل با موفقیت ایجاد شد")

     else:
          messagebox.showwarning("خطا" , "فایلی با این اسم و تاریخ وجود ندارد")

present = ctk.CTkButton(frame , text = "فایل حاضران" , font = ("B nazanin" , 15) , command = present)
present.pack(pady = 5)


def readf():

     namef = ctk.CTkInputDialog(text = ":اسم فایل را وارد کنید" , title = "خواندن فایل" , font = ("B nazanin" , 17))
     name_file = namef.get_input().strip()

     if os.path.exists(name_file):

          with open(name_file , "r" , encoding = "utf-8") as rf:
               cf = rf.read()

          rw = ctk.CTkToplevel(app)
          rw.geometry("850x700")
          rw.title("خواندن فایل")

          read_label = ctk.CTkLabel(rw , text = cf , font = ("B nazanin" , 15) , justify = "left")
          read_label.pack(pady = 7)

          close_button = ctk.CTkButton(rw , text = "بستن" , font = ("B nazanin" , 20) , command = rw.destroy)
          close_button.pack(pady = 1)

     else:
          messagebox.showwarning("خطا" , "!فایل پیدا نشد")

read = ctk.CTkButton(frame , text = "خواندن فایل" , font = ("B nazanin" , 15) , command = readf)
read.pack(pady = 5)


def show_about():
     window = ctk.CTkToplevel(app)
     window.geometry("600x450")
     window.title("توضیحات برنامه")

     texta = """
سازنده برنامه : سید شایان سیدی
نام برنامه : حاضر
زبان برنامه نویسی : پایتون
کار برنامه : کمک به معلمان با حضور و غیاب سیستمی که راحت تر و دقیق تر انجام می شود
با پر کردن ورودی ها و زدن دکمه "اضافه کردن" یک فایل با تاریخ روز و شماره کلاس ایجاد می شود
و اسم دانش آموز به آن فایل اضافه می شود
اگر هم ورودی هارا پر کنید و دکمه "حذف کردن" را بزنید و از قبل دانش آموزی با اطلاعاتی که وارد کردید
وجود داشته باشد آن دانش از آن فایل حذف می شود
با زدن دکمه "فایل غایب ها و تاخیر ها" هم و نوشتن تاریخ و شماره کلاس هم میتونید در یک فایل جدید 
لیست کسانی که غایب بودند و یا تاخیر داشته اند در کلاس را ببینید
با زدن دکمه "فایل حاضران" هم و نوشتن تاریخ و شماره کلاس هم میتونید در یک فایل جدید 
لیست کسانی که حاضر بودند در کلاس را ببینید
با استفاده از گزینه "خواندن فایل" و نوشتن اسم فایل هم میتونید محتوای داخل فایل
رو به زیبایی ببینید
شما میتوانید به همین گونه دانش آموزان را حضور و غیاب کنید
     """

     about_label = ctk.CTkLabel(window , text = texta , font = ("B nazanin" , 15) , justify = "right")
     about_label.pack(pady=10)

     close_button = ctk.CTkButton(window , text = "بستن" , font = ("B nazanin" , 20) , command = window.destroy)
     close_button.pack(pady = 1)

about_button = ctk.CTkButton(frame , text = "توضیحات برنامه" , font=("B nazanin" , 18) , command = show_about)
about_button.pack(pady = 5)


def out():
     app.quit()
out = ctk.CTkButton(frame , text = "خروج" , font = ("B nazanin" , 17) , command = out)
out.pack(pady = 5)



app.mainloop()