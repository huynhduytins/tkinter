import csv
from tkinter import *
from tkinter import messagebox


class InfoEmployee:

    def __init__(self, em_code, name, marital_status, num_children, edu_level, base_salary, personal_leave=0,
                 non_accept_leave=0, OT=0, work_result='None', real_salary=0):
        self.em_code = em_code
        self.name = name
        self.marital_status = marital_status
        self.num_children = num_children
        self.edu_level = edu_level
        self.base_salary = base_salary
        self.personal_leave = personal_leave
        self.non_accept_leave = non_accept_leave
        self.OT = OT
        self.work_result = work_result
        self.real_salary = real_salary


class App:

    def __init__(self, master, s, ms=0):
        self.master = master
        self.s = s
        self.ms = ms
        self.master.title("employee information")
        self.master.geometry('550x600')
        self.listEmployee = []

    def readFile(self):
        with open('DsNhanVien.csv', mode='r') as md:
            for r in md:
                r = r.split(',')
                self.listEmployee.append(
                    InfoEmployee(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10]))

    def max_id(self):
        d = 0
        with open('DsNhanVien.csv', mode='r') as f1:
            for x in csv.reader(f1):
                d+=1
        return d+1


    def listToString(s):
        str1 = " "
        return (str1.join(s))

    def ID(self):
        return len(self.listEmployee) + 1

    def remove(self, em_code):
        f1 = open("DsNhanVien.csv", "r")
        with open("new.csv", "w", encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            for x in csv.reader(f1):
                if int(x[0]) != int(em_code):
                    writer.writerow(x)
        f1.close()
        f1 = open("new.csv", "r")
        with open("DsNhanVien.csv", "w", encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            for x in csv.reader(f1):
                writer.writerow(x)
        f1.close()
        self.master.destroy()

    def screen(self):

        label = {}

        l = ["ID", "T??n", "T??nh tr???ng h??n nh??n", "S??? ng?????i con", "Tr??nh ????? v??n h??a", "L????ng c??n b???n",
             "S??? ng??y ngh??? c?? ph??p", "S??? ng??y ngh??? kh??ng ph??p", "S??? ng??y l??m th??m", "K???t qu??? c??ng vi???c",
             "L????ng th???c t???"]

        self.heading = Label(self.master, text="Personal Details", bg="light green", font=("Courier New", 10, 'bold'))
        self.heading.grid(row=0, column=1)
        Label(self.master, text="").grid(row=1, column=1)
        for i in range(2, len(l) + 2):
            Label(self.master, text="").grid(row=i * 2 + 1, column=0)
            label[i] = Label(self.master, text=l[i - 2])
            label[i].grid(row=i * 2, column=0)

        self.entry = {}
        for i in range(2, len(l) + 2):
            Label(self.master, text="").grid(row=i * 2 + 1, column=1, padx='100')
            self.entry[l[i - 2]] = Entry(self.master, justify='center')
            self.entry[l[i - 2]].grid(row=i * 2, column=1, padx='100')

        if self.s == "SAVE":
            d = self.max_id()
            self.entry["ID"].insert(0, str(d))
            self.entry["ID"].config(state="disable")

        if self.s == 'DELETE':
            self.display(self.ms)
            self.submit = Button(self.master, text="DELETE", fg="Black", font=("Courier New", 10, 'bold'),
                                 command=self.delete)
            self.submit.grid(row=28, column=1)

        elif self.s == 'MODIFY':
            self.display(self.ms)
            self.submit = Button(self.master, text="SAVE", fg="Black", font=("Courier New", 10, 'bold'),
                                 command=self.save)
            self.submit.grid(row=28, column=1)

        else:
            self.submit = Button(self.master, text="ADD", fg="Black", font=("Courier New", 10, 'bold'),
                                 command=self.save)
            self.submit.grid(row=28, column=1)

    def delete(self):
        rep = messagebox.askquestion('Delete', 'Delete this employee. Are you sure?')
        if rep == 'yes':
            self.remove(self.ms.em_code)
        else:
            pass

    def save(self):

        if self.entry["T??n"].get() == "":
            self.message("T??n", "Kh??ng ???????c ph??p ????? tr???ng")

        elif self.entry["T??nh tr???ng h??n nh??n"].get() == "":
            self.message("T??nh tr???ng h??n nh??n", "Kh??ng ???????c ph??p ????? tr???ng")
        elif self.entry["T??nh tr???ng h??n nh??n"].get() not in ["M", "S"]:
            self.message("T??nh tr???ng h??n nh??n", "Phai nhap tinh trang gia dinh tuong ung voi:\n"
                                                "                M = married\n"
                                                "                S = Single\n")

        elif self.entry["S??? ng?????i con"].get() == "":
            self.message("S??? ng?????i con", "Kh??ng ???????c ph??p ????? tr???ng")
        elif int(self.entry["S??? ng?????i con"].get()) > 20:
            self.message("S??? ng?????i con", "S??? ng?????i con kh??ng ???????c v?????t qu?? 20")

        elif self.entry["Tr??nh ????? v??n h??a"].get() == "":
            self.message("Tr??nh d??? v??n h??a", "Kh??ng ???????c ph??p ????? tr???ng")
        elif self.entry["Tr??nh ????? v??n h??a"].get() not in ['C1', 'C2', 'C3', 'DH', 'CH']:
            self.message("Tr??nh ????? v??n h??a", "Ph???i nh???p tr??nh ????? v??n h??a t????ng ???ng v???i:\n"
                                             "            C1 = c???p 1\n"
                                             "            C2 = c???p 2\n"
                                             "            C3 = c???p 3\n"
                                             "            DH = ?????i h???c\n"
                                             "            CH = cao h???c\n")

        elif self.entry["L????ng c??n b???n"].get() == "":
            self.message("L????ng c??n b???n", "Kh??ng ???????c ph??p ????? tr???ng")
        elif int(self.entry["L????ng c??n b???n"].get()) > 1000000:
            self.message("L????ng c??n b???n", "L????ng c??n b???n kh??ng l???n h??n 1000000")

        elif self.entry["S??? ng??y ngh??? c?? ph??p"].get() == "":
            self.message("S??? ng??y ngh??? c?? ph??p", "Kh??ng ???????c ph??p ????? tr???ng")
        elif int(self.entry["S??? ng??y ngh??? c?? ph??p"].get()) > 28:
            self.message("S??? ng??y ngh??? c?? ph??p", "S??? ng??y ngh??? c?? ph??p kh??ng l???n h??n 28 ng??y")

        elif self.entry["S??? ng??y ngh??? kh??ng ph??p"].get() == "":
            self.message("S??? ng??y ngh??? kh??ng ph??p", "Kh??ng ???????c ph??p ????? tr???ng")
        elif int(self.entry["S??? ng??y ngh??? kh??ng ph??p"].get()) > 28:
            self.message("S??? ng??y ngh??? kh??ng ph??p", "S??? ng??y ngh??? kh??ng ph??p kh??ng l???n h??n 28 ng??y")

        elif self.entry["S??? ng??y l??m th??m"].get() == "":
            self.message("S??? ng??y l??m th??m", "Kh??ng ???????c ph??p ????? tr???ng")
        elif int(self.entry["S??? ng??y l??m th??m"].get()) > 28:
            self.message("S??? ng??y l??m th??m", "S??? ng??y l??m th??m kh??ng l???n h??n 28 ng??y")

        elif self.entry["K???t qu??? c??ng vi???c"].get() == "":
            self.message("K???t qu??? c??ng vi???c", "Kh??ng ???????c ph??p ????? tr???ng")
        elif self.entry["K???t qu??? c??ng vi???c"].get() not in ['T', 'TB', 'K']:
            self.message("K???t qu??? c??ng vi???c", "K???t qu??? l??m vi???c t????ng ???ng v???i:\n"
                                              "           T = t???t\n"
                                              "          TB = ?????t\n"
                                              "           K = k??m\n")
        else:
            real_salary = int(self.entry["L????ng c??n b???n"].get()) + (
                int(self.entry["L????ng c??n b???n"].get()) * 0.05 if int(self.entry["S??? ng?????i con"].get()) > 2 else 0) + \
                          (int(self.entry["L????ng c??n b???n"].get()) * 0.1 if self.entry[
                                                                               "Tr??nh ????? v??n h??a"].get() == 'CH' else 0) + \
                          int(self.entry["L????ng c??n b???n"].get()) * 0.04 * int(
                self.entry["S??? ng??y l??m th??m"].get()) - int(self.entry["L????ng c??n b???n"].get()) * 0.05 * int(
                self.entry["S??? ng??y l??m th??m"].get())

            self.entry["L????ng th???c t???"].delete(0, END)
            self.entry["L????ng th???c t???"].insert(0, real_salary)

            if self.s == "SAVE":
                with open("DsNhanVien.csv", "a", encoding='UTF8', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(
                        [self.entry["ID"].get(), self.entry["T??n"].get(), self.entry["T??nh tr???ng h??n nh??n"].get(),
                         self.entry["S??? ng?????i con"].get(), self.entry["Tr??nh ????? v??n h??a"].get(),
                         self.entry["L????ng c??n b???n"].get(), self.entry["S??? ng??y ngh??? c?? ph??p"].get(),
                         self.entry["S??? ng??y ngh??? kh??ng ph??p"].get(),
                         self.entry["S??? ng??y l??m th??m"].get(), self.entry["K???t qu??? c??ng vi???c"].get(), real_salary])
                self.heading.config(text="successful")
                self.submit['state'] = DISABLED

            elif self.s == 'MODIFY':
                f1 = open("DsNhanVien.csv", "r")
                with open("new.csv", "w", encoding='UTF8', newline='') as f:
                    writer = csv.writer(f)
                    for x in csv.reader(f1):
                        if int(x[0]) == int(self.ms.em_code):
                            writer.writerow(
                                [self.entry["ID"].get(), self.entry["T??n"].get(),
                                 self.entry["T??nh tr???ng h??n nh??n"].get(),
                                 self.entry["S??? ng?????i con"].get(), self.entry["Tr??nh ????? v??n h??a"].get(),
                                 self.entry["L????ng c??n b???n"].get(), self.entry["S??? ng??y ngh??? c?? ph??p"].get(),
                                 self.entry["S??? ng??y ngh??? kh??ng ph??p"].get(),
                                 self.entry["S??? ng??y l??m th??m"].get(), self.entry["K???t qu??? c??ng vi???c"].get(),
                                 real_salary])
                            continue
                        writer.writerow(x)
                f1.close()
                f1 = open("new.csv", "r")
                with open("DsNhanVien.csv", "w", encoding='UTF8', newline='') as f:
                    writer = csv.writer(f)
                    for x in csv.reader(f1):
                        writer.writerow(x)
                f1.close()
                self.heading.config(text="successful")
                self.submit['state'] = DISABLED

    def display(self, emp):
        self.entry["ID"].insert(0, emp.em_code)

        self.entry["T??n"].insert(0, emp.name)

        self.entry["T??nh tr???ng h??n nh??n"].insert(0, emp.marital_status)

        self.entry["S??? ng?????i con"].insert(0, emp.num_children)

        self.entry["Tr??nh ????? v??n h??a"].insert(0, emp.edu_level)

        self.entry["L????ng c??n b???n"].insert(0, emp.base_salary)

        self.entry["S??? ng??y ngh??? c?? ph??p"].insert(0, emp.personal_leave)

        self.entry["S??? ng??y ngh??? kh??ng ph??p"].insert(0, emp.non_accept_leave)

        self.entry["S??? ng??y l??m th??m"].insert(0, emp.OT)

        self.entry["K???t qu??? c??ng vi???c"].insert(0, emp.work_result)

        self.entry["L????ng th???c t???"].insert(0, emp.real_salary)
        if self.s == "DELETE":
            self.entry["ID"].config(state="disable")
            self.entry["T??n"].config(state="disable")
            self.entry["T??nh tr???ng h??n nh??n"].config(state="disable")
            self.entry["S??? ng?????i con"].config(state="disable")
            self.entry["Tr??nh ????? v??n h??a"].config(state="disable")
            self.entry["L????ng c??n b???n"].config(state="disable")
            self.entry["S??? ng??y ngh??? c?? ph??p"].config(state="disable")
            self.entry["S??? ng??y ngh??? kh??ng ph??p"].config(state="disable")
            self.entry["S??? ng??y l??m th??m"].config(state="disable")
            self.entry["K???t qu??? c??ng vi???c"].config(state="disable")
            self.entry["L????ng th???c t???"].config(state="disable")

    def message(self, text1, text2):
        messagebox.showinfo(text1, text2)


def displayDele(emp, s):
    root = Tk()
    e = App(root, s, emp)
    e.screen()
    root.mainloop()


def display(s):
    root = Tk()
    e = App(root, s)
    e.screen()
    root.mainloop()
