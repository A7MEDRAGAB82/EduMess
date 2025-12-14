import tkinter as tk
from tkinter import ttk, messagebox

from controller import SchoolController


class EduMessApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # ----- Window basic settings -----
        self.title("EduMess - School Management System")
        self.geometry("1200x700")
        self.configure(bg="#050710")  # خلفية غامقة

        # Controller
        self.controller = SchoolController()

        # ----- Main layout: sidebar + main content -----
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        self._build_sidebar()
        self._build_main_area()

    # ================== Sidebar ==================
    def _build_sidebar(self):
        sidebar = tk.Frame(self, bg="#02040A", width=220)
        sidebar.grid(row=0, column=0, sticky="nsw")
        sidebar.grid_propagate(False)

        logo_lbl = tk.Label(
            sidebar,
            text="Edu Mess",
            fg="white",
            bg="#02040A",
            font=("Segoe UI", 20, "bold")
        )
        logo_lbl.pack(pady=(20, 30))

        btn_cfg = {
            "font": ("Segoe UI", 11, "bold"),
            "fg": "white",
            "bg": "#0B1220",
            "activebackground": "#1A2A3A",
            "activeforeground": "white",
            "bd": 0,
            "relief": "flat",
            "anchor": "w",
            "padx": 20,
            "height": 2,
            "width": 18
        }

        tk.Button(sidebar, text="Dashboard",
                  command=self.show_dashboard, **btn_cfg).pack(pady=4)
        tk.Button(sidebar, text="Teachers",
                  command=self.show_teachers_tab, **btn_cfg).pack(pady=4)
        tk.Button(sidebar, text="Students",
                  command=self.show_students_tab, **btn_cfg).pack(pady=4)
        tk.Button(sidebar, text="Courses",
                  command=self.show_courses_tab, **btn_cfg).pack(pady=4)

        tk.Label(sidebar, bg="#02040A").pack(expand=True, fill="both")

        tk.Button(sidebar, text="Settings", **btn_cfg).pack(pady=4)
        tk.Button(sidebar, text="Logout",
                  fg="#FF4B4B", **btn_cfg).pack(pady=(4, 20))

    # ================== Main content (tabs) ==================
    def _build_main_area(self):
        container = tk.Frame(self, bg="#050710")
        container.grid(row=0, column=1, sticky="nsew")
        container.grid_propagate(True)

        self.tabs = ttk.Notebook(container)
        self.tabs.pack(expand=True, fill="both", padx=10, pady=10)

        # Dashboard tab (بسيط)
        self.dashboard_tab = tk.Frame(self.tabs, bg="#050710")
        self.tabs.add(self.dashboard_tab, text="Dashboard")
        self._build_dashboard_content(self.dashboard_tab)

        # Tabs أخرى
        self.teachers_tab = tk.Frame(self.tabs, bg="#050710")
        self.students_tab = tk.Frame(self.tabs, bg="#050710")
        self.courses_tab = tk.Frame(self.tabs, bg="#050710")

        self.tabs.add(self.teachers_tab, text="Teachers")
        self.tabs.add(self.students_tab, text="Students")
        self.tabs.add(self.courses_tab, text="Courses")

        # نبني واجهة الطلاب
        self._build_students_tab(self.students_tab)

    # ---------- Dashboard UI ----------
    def _build_dashboard_content(self, parent: tk.Frame):
        header = tk.Label(
            parent,
            text="Welcome back, Admin\nAll your school management tools in one place",
            bg="#050710",
            fg="white",
            font=("Segoe UI", 18, "bold"),
            justify="left"
        )
        header.pack(anchor="w", padx=20, pady=(20, 10))

        cards_frame = tk.Frame(parent, bg="#050710")
        cards_frame.pack(anchor="w", padx=20, pady=10)

        def create_card(master, title, value, subtitle):
            frame = tk.Frame(master, bg="#0B1220", width=220, height=90)
            frame.pack_propagate(False)
            tk.Label(frame, text=title, bg="#0B1220", fg="#A0AEC0",
                     font=("Segoe UI", 10, "bold")).pack(anchor="w", padx=10, pady=(8, 0))
            tk.Label(frame, text=value, bg="#0B1220", fg="white",
                     font=("Segoe UI", 16, "bold")).pack(anchor="w", padx=10)
            tk.Label(frame, text=subtitle, bg="#0B1220", fg="#4FD1C5",
                     font=("Segoe UI", 9)).pack(anchor="w", padx=10, pady=(0, 5))
            return frame

        card1 = create_card(cards_frame, "Total Teachers", "17", "View Details →")
        card2 = create_card(cards_frame, "Total Students", "5K", "View Details →")
        card3 = create_card(cards_frame, "Total Courses", "17", "View Details →")

        card1.grid(row=0, column=0, padx=5)
        card2.grid(row=0, column=1, padx=5)
        card3.grid(row=0, column=2, padx=5)

        graphs = tk.Frame(parent, bg="#050710")
        graphs.pack(expand=True, fill="both", padx=20, pady=20)
        tk.Label(graphs, text="[Graphs Area - optional for now]",
                 bg="#050710", fg="#A0AEC0",
                 font=("Segoe UI", 12, "italic")).pack()

    # ================== Students Management Tab ==================
    def _build_students_tab(self, parent: tk.Frame):
        parent.configure(bg="#050710")

        header = tk.Label(
            parent,
            text="Student Management Dashboard",
            bg="#050710",
            fg="white",
            font=("Segoe UI", 18, "bold"),
            anchor="w"
        )
        header.pack(fill="x", padx=20, pady=(20, 5))

        sub = tk.Label(
            parent,
            text="Manage student information, grades and grade levels",
            bg="#050710",
            fg="#A0AEC0",
            font=("Segoe UI", 11),
            anchor="w"
        )
        sub.pack(fill="x", padx=20, pady=(0, 10))

        # Top bar: Add button
        top_bar = tk.Frame(parent, bg="#050710")
        top_bar.pack(fill="x", padx=20, pady=(0, 10))

        add_btn = tk.Button(
            top_bar, text="Add New Student +",
            bg="#3182CE", fg="white",
            activebackground="#2B6CB0",
            activeforeground="white",
            font=("Segoe UI", 10, "bold"),
            bd=0, padx=12, pady=6,
            command=self._open_add_student_window
        )
        add_btn.pack(side="right")

        # Table
        table_frame = tk.Frame(parent, bg="#050710")
        table_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        columns = ("name", "id", "grade", "grade_level")
        self.students_table = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            height=12
        )

        self.students_table.heading("name", text="Name")
        self.students_table.heading("id", text="ID")
        self.students_table.heading("grade", text="Grade")
        self.students_table.heading("grade_level", text="Grade Level")

        for col in columns:
            self.students_table.column(col, anchor="center", width=150)

        self.students_table.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(table_frame, orient="vertical",
                                  command=self.students_table.yview)
        self.students_table.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # Double-click row → open update/delete window
        self.students_table.bind("<Double-1>", self._open_update_student_window)

        # تحميل الطلاب من الـDB (لو الاتصال شغال)
        self._load_students_from_db()

    def _load_students_from_db(self):
        """يجلب كل الطلاب من الكنترولر ويعرضهم في الجدول."""
        try:
            self.students_table.delete(*self.students_table.get_children())
            students = self.controller.get_all_students()
            for s in students:
                self.students_table.insert(
                    "",
                    "end",
                    values=(
                        s["name"],
                        s["student_id"],
                        "",  # Grade letter لو حبيتوا تضيفوها بعدين
                        s["grade_level"],
                    ),
                )
        except Exception as ex:
            print("Error loading students:", ex)

    # ---------- Add Student Window ----------
    def _open_add_student_window(self):
        win = tk.Toplevel(self)
        win.title("Add New Student")
        win.configure(bg="#111827")
        win.geometry("600x320")
        win.grab_set()

        title = tk.Label(
            win, text="Add New Student",
            bg="#111827", fg="white",
            font=("Segoe UI", 16, "bold")
        )
        title.pack(anchor="w", padx=30, pady=(20, 0))

        sub = tk.Label(
            win, text="Enter the details of the new student",
            bg="#111827", fg="#A0AEC0",
            font=("Segoe UI", 10)
        )
        sub.pack(anchor="w", padx=30, pady=(0, 10))

        form = tk.Frame(win, bg="#111827")
        form.pack(fill="x", padx=30, pady=10)

        # Name
        tk.Label(form, text="Name", bg="#111827", fg="white").grid(row=0, column=0, sticky="w")
        name_entry = tk.Entry(form, width=30)
        name_entry.grid(row=1, column=0, padx=(0, 20), pady=(0, 10))

        # Grade (letter)
        tk.Label(form, text="Grade", bg="#111827", fg="white").grid(row=0, column=1, sticky="w")
        grade_entry = tk.Entry(form, width=30)
        grade_entry.grid(row=1, column=1, pady=(0, 10))

        # Grade Level (numeric)
        tk.Label(form, text="Grade Level", bg="#111827", fg="white").grid(row=2, column=0, sticky="w")
        grade_level_entry = tk.Entry(form, width=30)
        grade_level_entry.grid(row=3, column=0, padx=(0, 20), pady=(0, 10))

        btn_frame = tk.Frame(win, bg="#111827")
        btn_frame.pack(fill="x", padx=30, pady=20)

        def on_add_click():
            name = name_entry.get().strip()
            grade_letter = grade_entry.get().strip()
            grade_level = grade_level_entry.get().strip()

            if not name or not grade_level:
                messagebox.showerror("Error", "Name and Grade Level are required.")
                return

            try:
                student_id = self.controller.add_student(name, grade_level)
                self.students_table.insert(
                    "",
                    "end",
                    values=(name, student_id, grade_letter, grade_level),
                )
                messagebox.showinfo("Success", "Student Added Successfully!")
                win.destroy()
            except Exception as ex:
                messagebox.showerror("Error", f"Failed to add student: {ex}")

        add_btn = tk.Button(
            btn_frame, text="Add New Student",
            bg="#3182CE", fg="white",
            font=("Segoe UI", 10, "bold"),
            bd=0, padx=20, pady=6,
            command=on_add_click
        )
        add_btn.pack(side="left")

        cancel_btn = tk.Button(
            btn_frame, text="Cancel",
            bg="#111827", fg="white",
            bd=1, relief="solid",
            padx=20, pady=6,
            command=win.destroy
        )
        cancel_btn.pack(side="left", padx=10)

    # ---------- Update/Delete Student Window ----------
    def _open_update_student_window(self, event):
        selected = self.students_table.selection()
        if not selected:
            return

        item_id = selected[0]
        row = self.students_table.item(item_id, "values")
        name, student_id, grade_letter, grade_level = row

        win = tk.Toplevel(self)
        win.title("Update Student Information")
        win.configure(bg="#111827")
        win.geometry("600x320")
        win.grab_set()

        tk.Label(
            win, text="Update Student Information",
            bg="#111827", fg="white",
            font=("Segoe UI", 16, "bold")
        ).pack(anchor="w", padx=30, pady=(20, 0))

        tk.Label(
            win, text="Enter the details you want to update",
            bg="#111827", fg="#A0AEC0",
            font=("Segoe UI", 10)
        ).pack(anchor="w", padx=30, pady=(0, 10))

        form = tk.Frame(win, bg="#111827")
        form.pack(fill="x", padx=30, pady=10)

        # Name
        tk.Label(form, text="Name", bg="#111827", fg="white").grid(row=0, column=0, sticky="w")
        name_entry = tk.Entry(form, width=30)
        name_entry.insert(0, name)
        name_entry.grid(row=1, column=0, padx=(0, 20), pady=(0, 10))

        # ID (read-only)
        tk.Label(form, text="ID", bg="#111827", fg="white").grid(row=0, column=1, sticky="w")
        id_entry = tk.Entry(form, width=30)
        id_entry.insert(0, student_id)
        id_entry.configure(state="readonly")
        id_entry.grid(row=1, column=1, pady=(0, 10))

        # Grade
        tk.Label(form, text="Grade", bg="#111827", fg="white").grid(row=2, column=0, sticky="w")
        grade_entry = tk.Entry(form, width=30)
        grade_entry.insert(0, grade_letter)
        grade_entry.grid(row=3, column=0, padx=(0, 20), pady=(0, 10))

        # Grade Level
        tk.Label(form, text="Grade Level", bg="#111827", fg="white").grid(row=2, column=1, sticky="w")
        grade_level_entry = tk.Entry(form, width=30)
        grade_level_entry.insert(0, grade_level)
        grade_level_entry.grid(row=3, column=1, pady=(0, 10))

        btn_frame = tk.Frame(win, bg="#111827")
        btn_frame.pack(fill="x", padx=30, pady=20)

        def on_update():
            new_name = name_entry.get().strip()
            new_grade_level = grade_level_entry.get().strip()

            try:
                self.controller.update_student(
                    int(student_id),
                    new_name=new_name or None,
                    new_grade=new_grade_level or None,
                )
                self.students_table.item(
                    item_id,
                    values=(new_name or name,
                            student_id,
                            grade_entry.get().strip(),
                            new_grade_level or grade_level),
                )
                messagebox.showinfo("Success", "Updated Successfully!")
                win.destroy()
            except Exception as ex:
                messagebox.showerror("Error", f"Failed to update student: {ex}")

        def on_delete():
            if not messagebox.askyesno("Delete", f"Are you sure you want to delete student {name}?"):
                return
            try:
                self.controller.delete_student(int(student_id))
                self.students_table.delete(item_id)
                messagebox.showinfo("Success", "Deleted Successfully!")
                win.destroy()
            except Exception as ex:
                messagebox.showerror("Error", f"Failed to delete student: {ex}")

        update_btn = tk.Button(
            btn_frame, text="Update",
            bg="#3182CE", fg="white",
            font=("Segoe UI", 10, "bold"),
            bd=0, padx=20, pady=6,
            command=on_update
        )
        update_btn.pack(side="left")

        delete_btn = tk.Button(
            btn_frame, text="Delete",
            bg="#E53E3E", fg="white",
            font=("Segoe UI", 10, "bold"),
            bd=0, padx=20, pady=6,
            command=on_delete
        )
        delete_btn.pack(side="left", padx=10)

        cancel_btn = tk.Button(
            btn_frame, text="Cancel",
            bg="#111827", fg="white",
            bd=1, relief="solid",
            padx=20, pady=6,
            command=win.destroy
        )
        cancel_btn.pack(side="left", padx=10)

    # ---------- Sidebar handlers ----------
    def show_dashboard(self):
        self.tabs.select(self.dashboard_tab)

    def show_teachers_tab(self):
        self.tabs.select(self.teachers_tab)

    def show_students_tab(self):
        self.tabs.select(self.students_tab)

    def show_courses_tab(self):
        self.tabs.select(self.courses_tab)


if __name__ == "__main__":
    app = EduMessApp()
    app.mainloop()
