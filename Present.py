import re
import customtkinter as ctk
from tkinter import messagebox

import os

import jdatetime
today0 = jdatetime.date.today()
today1 = today0.strftime("%Y-%m-%d")



os.system("title Present")



app = ctk.CTk()
app.geometry("362x590")

app.title("Present")
app.resizable(False , True)



frame = ctk.CTkFrame(app , corner_radius = 0)
frame.pack()



label = ctk.CTkLabel(frame , text = "حضور و غیاب" , font = ("B nazanin" , 22) , anchor = "center")
label.grid(row = 0 , column = 0 , pady = 5 , padx = 5 , columnspan = 20 , sticky = "ew")



def c():
     index.delete(0 , "end")
     flname.delete(0 , "end")
     status.set("وضعیت دانش آموز را مشخص کنید")
     clas2.delete(0 , "end")
     lesson.set("درس را انتخاب کنید")
     teacher.delete(0 , "end")

bc = ctk.CTkButton(frame , text = "پاکسازی" , font = ("B nazanin" , 15) , width = 8 , anchor = "e" , command = c)
bc.grid(row = 0 , column = 1 , pady = 5 , padx = 5 , sticky = "e")



def changecolor(mode):     
     if mode == "سیستم":
          ctk.set_appearance_mode("System")
     elif mode == "روشن":
          app.configure(fg_color = "#ececec")
          frame.configure(fg_color = "#ececec")
          ctk.set_appearance_mode("Light")
     elif mode == "تیره":
          app.configure(fg_color = "#1F1F1F")
          frame.configure(fg_color = "#1F1F1F")
          ctk.set_appearance_mode("Dark")
     elif mode == "مشکی":
          app.configure(fg_color="#000000")
          frame.configure(fg_color = "#000000")
          ctk.set_appearance_mode("Dark")

menu_color = ctk.CTkSegmentedButton(frame , values = ["مشکی" , "روشن" , "تیره"] , command = changecolor , font  = ("B nazanin" , 20))
menu_color.set("سیستم")
menu_color.grid(row = 1 , column = 0 , pady = 5 , padx = 5 , columnspan = 3 , sticky = "ew")


index = ctk.CTkEntry(frame , placeholder_text = "شماره دانش آموز در لیست" , font = ("B nazanin" , 21) , justify = "right" , height = 37)
index.grid(row = 2 , column = 0 , pady = 5 , padx = 5 , columnspan = 5 , sticky = "ew")


flname = ctk.CTkEntry(frame , placeholder_text = "نام و نام خانوادگی دانش آموز" , font = ("B nazanin" , 21) , justify = "right" , height = 37)
flname.grid(row = 3 , column = 0 , pady = 5 , padx = 5 , columnspan = 5 , sticky = "ew")


status = ctk.CTkComboBox(frame , state="readonly" , values = ["وضعیت دانش آموز را مشخص کنید" , "حاضر" , "غیبت موجه" , "غیبت غیر موجه" , "تاخیر زیاد(بیشتر از سی دقیقه)" , "تاخیر کم(کمتر از سی دقیقه)"] , font = ("B nazanin" , 21) , dropdown_font = ("B nazanin" , 16) , justify = "right" , dropdown_hover_color = "#9CA3AF" , height = 37)
status.set("وضعیت دانش آموز را مشخص کنید")
status.grid(row = 5 , column = 0 , pady = 5 , padx = 5 , columnspan = 5 , sticky = "ew")


clas2 = ctk.CTkEntry(frame , placeholder_text = "شماره کلاس دانش آموز" , font = ("B nazanin" , 21) , justify = "right" , height = 37)
clas2.grid(row = 6 , column = 0 , pady = 5 , padx = 5 , columnspan = 5 , sticky = "ew")


lesson = ctk.CTkComboBox(frame , font = ("B nazanin" , 21) , justify = "right" , height = 37 ,
values = ["درس را انتخاب کنید","ریاضی","علوم","مطالعات اجتماعی","ادبیات","انشا(نگارش)","املا","زبان انگلیسی","زبان عربی","قرآن","پیام های آسمان","کار و فناوری","تفکر و سبک زندگی","هنر","تربیت بدنی","آمادگی دفاعی"] , dropdown_font = ("B nazanin" , 17) , dropdown_hover_color = "#9CA3AF")
lesson.grid(row = 7 , column = 0 , pady = 5 , padx = 5 , columnspan = 5 , sticky="ew")


teacher = ctk.CTkEntry(frame , placeholder_text = "نام و نام خانوادگی معلم" , font = ("B nazanin" , 21) , justify = "right" , height = 37)
teacher.grid(row = 9 , column = 0 , pady = 5 , padx = 5 , columnspan = 5 , sticky = "ew")



def clear():
     index.delete(0 , "end")
     flname.delete(0 , "end")
     status.set("وضعیت دانش آموز را مشخص کنید")



def add_student(): 


     idx = index.get().strip()
     fl_name = flname.get().strip()
     clas2_student = clas2.get().strip()
     lesson_bell = lesson.get().strip()
     flname_teacher = teacher.get().strip()
     status_student = status.get().strip()



     if not idx or not fl_name or not clas2_student or not lesson_bell or not status_student or not flname_teacher:
          messagebox.showwarning("خطا" , "تمام ورودی هارا پر کنید")


     elif not idx.isdigit():
          messagebox.showwarning("خطا" , "شماره دانش آموز باید عدد باشد")


     elif re.search(r'\d' , fl_name):
          messagebox.showwarning("خطا" , "در نام و نام خانوادگی دانش آموز نباید عدد به کار برود")


     elif status_student == "وضعیت دانش آموز را مشخص کنید":
          messagebox.showwarning("خطا" , "وضعیت دانش آموز را مشخص کنید")


     elif not clas2_student.isdigit():
          messagebox.showwarning("خطا" , "شماره کلاس دانش آموز باید عدد باشد")


     elif lesson_bell == "درس را انتخاب کنید":
          messagebox.showwarning("خطا" , "درس را انتخاب کنید")


     elif re.search(r'\d' , flname_teacher):
          messagebox.showwarning("خطا" , "در نام و نام خانوادگی معلم نباید عدد به کار برود")


     else:

          with open(f"{today1}_{clas2_student}.txt" , "a" , encoding = "utf-8") as f:
               f.write(f"{idx}.{fl_name} --> {status_student} -درس-> {lesson_bell} -نام و نام خانوادگی معلم-> {flname_teacher}\n")

          with open(f"name.txt" , "a" , encoding = "utf-8") as fii:
               fii.write(f"{fl_name}\n")

               f.close()


               messagebox.showinfo("فرایند صحیح" , "دانش آموز اضافه با موفقیت اضافه شد")
               clear()

add = ctk.CTkButton(frame , text = "اضافه کردن" , font = ("B nazanin" , 20) , command = add_student , width = 170 , height = 37)
add.grid(row = 10 , column = 1 , padx = 5 , pady = 5 , columnspan = 1 , sticky = "ew")



def remove_student():


     idx = index.get().strip()
     fl_name = flname.get().strip()
     clas2_student = clas2.get().strip()
     lesson_bell = lesson.get().strip()
     flname_teacher = teacher.get().strip()
     status_student = status.get().strip()


     if not idx or not fl_name or not clas2_student or not lesson_bell or not status_student or not flname_teacher:
          messagebox.showwarning("خطا" , "تمام ورودی هارا پر کنید")


     elif not idx.isdigit():
          messagebox.showwarning("خطا" , "شماره دانش آموز باید عدد باشد")


     elif re.search(r'\d' , fl_name):
          messagebox.showwarning("خطا" , "در نام و نام خانوادگی دانش آموز نباید عدد به کار برود")


     elif status_student == "وضعیت دانش آموز را مشخص کنید":
          messagebox.showwarning("خطا" , "وضعیت دانش آموز را مشخص کنید")


     elif not clas2_student.isdigit():
          messagebox.showwarning("خطا" , "شماره کلاس دانش آموز باید عدد باشد")


     elif lesson_bell == "درس را انتخاب کنید":
          messagebox.showwarning("خطا" , "درس را انتخاب کنید")


     elif re.search(r'\d' , flname_teacher):
          messagebox.showwarning("خطا" , "در نام و نام خانوادگی معلم نباید عدد به کار برود")


     elif not os.path.exists(f"{today1}_{clas2_student}.txt"):
          messagebox.showwarning("خطا", "فایلی با این تاریخ و کلاس وجود ندارد!لطفا اطلاعات را مجدد وارد کنید")


     else:
          with open(f"{today1}_{clas2_student}.txt" , "r", encoding = "utf-8") as f:
               lines = f.readlines()

          students = (f"{idx}.{fl_name} --> {status_student} -درس-> {lesson_bell} -نام و نام خانوادگی معلم-> {flname_teacher}\n")

          if students in lines:
               lines.remove(students)
               with open(f"{today1}_{clas2_student}.txt", "w", encoding="utf-8") as f:
                    f.writelines(lines)
               messagebox.showinfo("فرایند صحیح", "دانش آموز با موفقیت حذف شد")
               clear()

          else:
               messagebox.showwarning("خطا", "این دانش آموز وجود ندارد.")
               clear()

remove = ctk.CTkButton(frame , text = "حذف کردن" , font = ("B nazanin" , 20) , command = remove_student , width = 170 , height = 37)
remove.grid(row = 10 , column = 0 , padx = 5 , pady = 5 , columnspan = 1 , sticky = "ew")



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

absentd = ctk.CTkButton(frame , text = "🕣فایل غایب ها و تاخیر ها" , font = ("B nazanin" , 18) , command = absentd , height = 37)
absentd.grid(row = 11 , column = 0 , pady = 5 , padx = 5 , columnspan = 1 , sticky="ew")



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

present = ctk.CTkButton(frame , text = "🕖فایل حاضران" , font = ("B nazanin" , 19) , command = present , height = 37)
present.grid(row = 11 , column = 1 , pady = 5 , padx = 5 , columnspan = 1 , sticky="ew")



def readf():

     namef = ctk.CTkInputDialog(text = ":اسم فایل را وارد کنید" , title = "خواندن فایل" , font = ("B nazanin" , 17))
     name_file = namef.get_input().strip()

     if os.path.exists(name_file):

          with open(name_file , "r" , encoding = "utf-8") as rf:
               cf = rf.read()

          rw = ctk.CTkToplevel(app)
          rw.geometry("700x600")
          rw.title("خواندن فایل")
          rw.resizable(True , True)

          r = ctk.CTkScrollableFrame(rw , width = 700 , height = 600)

          read_label = ctk.CTkLabel(rw , text = cf , font = ("B nazanin" , 15) , justify = "right")
          read_label.grid(row = 0 , column = 0 , pady = 5 , padx = 5)

          close_button = ctk.CTkButton(rw , text = "بستن" , font = ("B nazanin" , 20) , fg_color = "#CE0000" , hover_color = "#990000" , anchor = "center" , command = rw.destroy)
          close_button.grid(row = 1 , column = 0 , pady = 5 , padx = 5 , sticky = "s")
          rw.grid_rowconfigure(0, weight=1)
          rw.grid_columnconfigure(0, weight=1)

     else:
          messagebox.showwarning("خطا" , "!فایل پیدا نشد")

read = ctk.CTkButton(frame , text = "خواندن فایل" , font = ("B nazanin" , 20) , command = readf , height = 37)
read.grid(row = 12 , column = 0 , pady = 5 , padx = 5 , columnspan = 5 , sticky="ew")



def show_about():
     window = ctk.CTkToplevel(app)
     window.geometry("600x500")
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

     about_label = ctk.CTkLabel(window , text = texta , font = ("B nazanin" , 18) , justify = "right")
     about_label.grid(row = 0 , column = 0 , pady = 5 , padx = 5 , columnspan = 15 , sticky = "ew")

     close_button = ctk.CTkButton(window , text = "بستن" , font = ("B nazanin" , 20) , hover_color = "#990000" , command = window.destroy , fg_color = "#CE0000" , anchor = "center")
     close_button.grid(row = 1 , column = 0 , pady = 5 , padx = 5 , columnspan = 100 , sticky = "ew")

about_button = ctk.CTkButton(frame , text = "توضیحات برنامه" , font = ("B nazanin" , 20) , fg_color = "#1B9300" , hover_color = "#115C00" , command = show_about , height = 37)
about_button.grid(row = 13 , column = 1 , pady = 5 , padx = 5 , columnspan = 1 , sticky = "ew")



def out():
     app.quit()
out = ctk.CTkButton(frame , text = "خروج" , font = ("B nazanin" , 21) , fg_color = "#CE0000", hover_color = "#990000" , command = out , height = 37)
out.grid(row = 13 , column = 0 , pady = 5 , padx = 5 , columnspan = 1 , sticky = "ew")



label1 = ctk.CTkLabel(frame , text = "©تمامی حقوق مادی و معنوی این برنامه متعلق به سید شایان سیدی است 1404" , font = ("B nazanin" , 12) , anchor = "center")
label1.grid(row = 14 , column = 0 , pady = 0 , padx = 1 , columnspan = 3 , sticky = "ew")






app.mainloop()
