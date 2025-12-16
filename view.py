

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from datetime import date, datetime


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
       tk.Button(sidebar, text="Logout", **btn_cfg).pack(pady=(4, 20))


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


       # Build all tabs
       self._build_students_tab(self.students_tab)
       self._build_teachers_tab(self.teachers_tab)
       self._build_courses_tab(self.courses_tab)


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






       # Grade Level (numeric)
       tk.Label(form, text="Grade Level", bg="#111827", fg="white").grid(row=2, column=0, sticky="w")
       grade_level_entry = tk.Entry(form, width=30)
       grade_level_entry.grid(row=3, column=0, padx=(0, 20), pady=(0, 10))


       btn_frame = tk.Frame(win, bg="#111827")
       btn_frame.pack(fill="x", padx=30, pady=20)


       def on_add_click():
           name = name_entry.get().strip()


           grade_level = grade_level_entry.get().strip()


           if not name or not grade_level:
               messagebox.showerror("Error", "Name and Grade Level are required.")
               return


           try:
               student_id = self.controller.add_student(name, grade_level)
               self.students_table.insert(
                   "",
                   "end",
                   values=(name, student_id,  grade_level),
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


   # ================== Helper Methods ==================
   def _get_all_courses(self):
       """Get all courses from database."""
       try:
           rows = self.controller.db.fetch_all("SELECT course_id, title FROM Courses ORDER BY course_id")
           return [{"course_id": r[0], "title": r[1]} for r in rows]
       except Exception as e:
           print(f"Error fetching courses: {e}")
           return []


   def _get_student_submissions(self, assignment_id: int):
       """Get all student submissions for an assignment."""
       try:
           rows = self.controller.db.fetch_all(
               """
               SELECT g.Student_ID, u.User_Name, g.Submission_Text, g.Score, g.Submission_Date
               FROM Grades g
                        JOIN Users u ON g.Student_ID = u.User_ID
               WHERE g.Assignment_ID = ?
               ORDER BY g.Student_ID
               """,
               (assignment_id,)
           )
           return [
               {
                   "student_id": r[0],
                   "name": r[1],
                   "submission_text": r[2] or "",
                   "score": r[3],
                   "submission_date": r[4]
               } for r in rows
           ]
       except Exception as e:
           print(f"Error fetching submissions: {e}")
           return []


   def _get_all_students_for_attendance(self, course_id: int):
       """Get all students for attendance marking (includes all students, not just those with existing records)."""
       try:
           # First try to get students who have attendance records
           rows = self.controller.db.fetch_all(
               """
               SELECT DISTINCT s.Student_ID, u.User_Name, s.Grade_Level
               FROM Students s
                        JOIN Users u ON s.Student_ID = u.User_ID
                        JOIN Attendance a ON a.Student_ID = s.Student_ID
               WHERE a.Course_ID = ?
               ORDER BY s.Student_ID
               """,
               (course_id,)
           )
           students_with_attendance = {r[0]: {"student_id": r[0], "name": r[1], "grade_level": r[2]} for r in rows}


           # If no students with attendance, get all students
           if not students_with_attendance:
               all_students = self.controller.get_all_students()
               return all_students


           return list(students_with_attendance.values())
       except Exception as e:
           # Fallback to all students if query fails
           print(f"Error fetching students for attendance: {e}")
           return self.controller.get_all_students()


   # ================== Teachers Tab ==================
   def _build_teachers_tab(self, parent: tk.Frame):
       parent.configure(bg="#050710")


       header = tk.Label(
           parent,
           text="Teacher Portal",
           bg="#050710",
           fg="white",
           font=("Segoe UI", 18, "bold"),
           anchor="w"
       )
       header.pack(fill="x", padx=20, pady=(20, 5))


       sub = tk.Label(
           parent,
           text="View students, grade assignments, and mark attendance",
           bg="#050710",
           fg="#A0AEC0",
           font=("Segoe UI", 11),
           anchor="w"
       )
       sub.pack(fill="x", padx=20, pady=(0, 20))


       # Create notebook for teacher sub-tabs
       teacher_notebook = ttk.Notebook(parent)
       teacher_notebook.pack(fill="both", expand=True, padx=20, pady=(0, 20))


       # Tab 1: View Students
       view_students_frame = tk.Frame(teacher_notebook, bg="#050710")
       teacher_notebook.add(view_students_frame, text="View Students")
       self._build_view_students_section(view_students_frame)


       # Tab 2: Grade Assignments
       grade_frame = tk.Frame(teacher_notebook, bg="#050710")
       teacher_notebook.add(grade_frame, text="Grade Assignments")
       self._build_grade_assignments_section(grade_frame)


       # Tab 3: Mark Attendance
       attendance_frame = tk.Frame(teacher_notebook, bg="#050710")
       teacher_notebook.add(attendance_frame, text="Mark Attendance")
       self._build_mark_attendance_section(attendance_frame)


   def _build_view_students_section(self, parent: tk.Frame):
       """Section for teachers to view all students."""
       parent.configure(bg="#050710")


       # Refresh button
       top_bar = tk.Frame(parent, bg="#050710")
       top_bar.pack(fill="x", padx=20, pady=(20, 10))


       refresh_btn = tk.Button(
           top_bar, text="Refresh",
           bg="#3182CE", fg="white",
           activebackground="#2B6CB0",
           activeforeground="white",
           font=("Segoe UI", 10, "bold"),
           bd=0, padx=12, pady=6,
           command=lambda: self._load_teacher_students_table()
       )
       refresh_btn.pack(side="right")


       # Table
       table_frame = tk.Frame(parent, bg="#050710")
       table_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))


       columns = ("name", "id", "grade_level", "enrollment_date")
       self.teacher_students_table = ttk.Treeview(
           table_frame,
           columns=columns,
           show="headings",
           height=15
       )


       self.teacher_students_table.heading("name", text="Name")
       self.teacher_students_table.heading("id", text="ID")
       self.teacher_students_table.heading("grade_level", text="Grade Level")
       self.teacher_students_table.heading("enrollment_date", text="Enrollment Date")


       for col in columns:
           self.teacher_students_table.column(col, anchor="center", width=200)


       self.teacher_students_table.pack(side="left", fill="both", expand=True)


       scrollbar = ttk.Scrollbar(table_frame, orient="vertical",
                                 command=self.teacher_students_table.yview)
       self.teacher_students_table.configure(yscroll=scrollbar.set)
       scrollbar.pack(side="right", fill="y")


       self._load_teacher_students_table()


   def _load_teacher_students_table(self):
       """Load students into teacher view table."""
       try:
           self.teacher_students_table.delete(*self.teacher_students_table.get_children())
           students = self.controller.get_all_students()
           for s in students:
               enrollment_date = s["enrollment_date"]
               if enrollment_date:
                   if isinstance(enrollment_date, str):
                       date_str = enrollment_date
                   else:
                       date_str = enrollment_date.strftime("%Y-%m-%d")
               else:
                   date_str = "N/A"


               self.teacher_students_table.insert(
                   "",
                   "end",
                   values=(
                       s["name"],
                       s["student_id"],
                       s["grade_level"],
                       date_str,
                   ),
               )
       except Exception as ex:
           messagebox.showerror("Error", f"Failed to load students: {ex}")


   def _build_grade_assignments_section(self, parent: tk.Frame):
       """Section for teachers to grade student assignments."""
       parent.configure(bg="#050710")


       # Course selection
       course_frame = tk.Frame(parent, bg="#050710")
       course_frame.pack(fill="x", padx=20, pady=(20, 10))


       tk.Label(
           course_frame, text="Select Course:",
           bg="#050710", fg="white",
           font=("Segoe UI", 11, "bold")
       ).pack(side="left", padx=(0, 10))


       self.grade_course_var = tk.StringVar()
       self.grade_course_combo = ttk.Combobox(
           course_frame, textvariable=self.grade_course_var,
           width=30, state="readonly"
       )
       self.grade_course_combo.pack(side="left", padx=(0, 10))
       self.grade_course_combo.bind("<<ComboboxSelected>>", self._on_grade_course_selected)


       # Assignment selection
       assignment_frame = tk.Frame(parent, bg="#050710")
       assignment_frame.pack(fill="x", padx=20, pady=(0, 10))


       tk.Label(
           assignment_frame, text="Select Assignment:",
           bg="#050710", fg="white",
           font=("Segoe UI", 11, "bold")
       ).pack(side="left", padx=(0, 10))


       self.grade_assignment_var = tk.StringVar()
       self.grade_assignment_combo = ttk.Combobox(
           assignment_frame, textvariable=self.grade_assignment_var,
           width=30, state="readonly"
       )
       self.grade_assignment_combo.pack(side="left", padx=(0, 10))
       self.grade_assignment_combo.bind("<<ComboboxSelected>>", self._on_grade_assignment_selected)


       refresh_btn = tk.Button(
           assignment_frame, text="Refresh",
           bg="#3182CE", fg="white",
           activebackground="#2B6CB0",
           activeforeground="white",
           font=("Segoe UI", 10, "bold"),
           bd=0, padx=12, pady=6,
           command=self._load_grade_courses
       )
       refresh_btn.pack(side="left", padx=(10, 0))


       # Submissions table
       table_frame = tk.Frame(parent, bg="#050710")
       table_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))


       columns = ("student_name", "student_id", "submission", "score", "submission_date")
       self.submissions_table = ttk.Treeview(
           table_frame,
           columns=columns,
           show="headings",
           height=10
       )


       self.submissions_table.heading("student_name", text="Student Name")
       self.submissions_table.heading("student_id", text="Student ID")
       self.submissions_table.heading("submission", text="Submission")
       self.submissions_table.heading("score", text="Score")
       self.submissions_table.heading("submission_date", text="Submission Date")


       self.submissions_table.column("student_name", anchor="center", width=150)
       self.submissions_table.column("student_id", anchor="center", width=100)
       self.submissions_table.column("submission", anchor="w", width=300)
       self.submissions_table.column("score", anchor="center", width=100)
       self.submissions_table.column("submission_date", anchor="center", width=150)


       self.submissions_table.pack(side="left", fill="both", expand=True)


       scrollbar = ttk.Scrollbar(table_frame, orient="vertical",
                                 command=self.submissions_table.yview)
       self.submissions_table.configure(yscroll=scrollbar.set)
       scrollbar.pack(side="right", fill="y")


       # Double-click to grade
       self.submissions_table.bind("<Double-1>", self._open_grade_submission_window)


       # Load courses initially
       self._load_grade_courses()


   def _load_grade_courses(self):
       """Load courses into grade course combo."""
       try:
           courses = self._get_all_courses()
           course_options = [f"{c['course_id']}: {c['title']}" for c in courses]
           self.grade_course_combo['values'] = course_options
           if course_options:
               self.grade_course_combo.current(0)
               self._on_grade_course_selected(None)
       except Exception as ex:
           print(f"Error loading courses: {ex}")


   def _on_grade_course_selected(self, event):
       """When course is selected, load assignments."""
       try:
           selection = self.grade_course_var.get()
           if not selection:
               return
           course_id = int(selection.split(":")[0])
           assignments = self.controller.get_course_assignments(course_id)
           assignment_options = [f"{a['assignment_id']}: {a['title']}" for a in assignments]
           self.grade_assignment_combo['values'] = assignment_options
           if assignment_options:
               self.grade_assignment_combo.current(0)
               self._on_grade_assignment_selected(None)
           else:
               self.grade_assignment_combo.set("")
               self.submissions_table.delete(*self.submissions_table.get_children())
       except Exception as ex:
           print(f"Error loading assignments: {ex}")


   def _on_grade_assignment_selected(self, event):
       """When assignment is selected, load submissions."""
       try:
           selection = self.grade_assignment_var.get()
           if not selection:
               return
           assignment_id = int(selection.split(":")[0])
           submissions = self._get_student_submissions(assignment_id)


           self.submissions_table.delete(*self.submissions_table.get_children())
           for sub in submissions:
               submission_text_raw = sub["submission_text"] or ""
               submission_text = submission_text_raw[:50] + "..." if len(
                   submission_text_raw) > 50 else submission_text_raw
               score = sub["score"] if sub["score"] is not None else "Not Graded"
               sub_date = sub["submission_date"]
               if sub_date:
                   if isinstance(sub_date, str):
                       date_str = sub_date
                   else:
                       date_str = sub_date.strftime("%Y-%m-%d")
               else:
                   date_str = "N/A"


               self.submissions_table.insert(
                   "",
                   "end",
                   values=(
                       sub["name"],
                       sub["student_id"],
                       submission_text,
                       score,
                       date_str
                   ),
                   tags=(sub["student_id"], str(assignment_id))
               )
       except Exception as ex:
           messagebox.showerror("Error", f"Failed to load submissions: {ex}")


   def _open_grade_submission_window(self, event):
       """Open window to grade a submission."""
       selected = self.submissions_table.selection()
       if not selected:
           return


       item_id = selected[0]
       row = self.submissions_table.item(item_id, "values")
       student_name, student_id, submission_text, score, sub_date = row
       tags = self.submissions_table.item(item_id, "tags")


       assignment_id = int(tags[1]) if len(tags) > 1 else None
       if not assignment_id:
           messagebox.showerror("Error", "Assignment ID not found")
           return


       # Get full submission text
       try:
           submissions = self._get_student_submissions(assignment_id)
           full_submission = next((s["submission_text"] for s in submissions if s["student_id"] == int(student_id)), submission_text)
       except:
           full_submission = submission_text


       win = tk.Toplevel(self)
       win.title("Grade Assignment")
       win.configure(bg="#111827")
       win.geometry("700x500")
       win.grab_set()


       tk.Label(
           win, text="Grade Assignment",
           bg="#111827", fg="white",
           font=("Segoe UI", 16, "bold")
       ).pack(anchor="w", padx=30, pady=(20, 0))


       tk.Label(
           win, text=f"Student: {student_name} (ID: {student_id})",
           bg="#111827", fg="#A0AEC0",
           font=("Segoe UI", 10)
       ).pack(anchor="w", padx=30, pady=(10, 20))


       # Submission text
       tk.Label(
           win, text="Submission:",
           bg="#111827", fg="white",
           font=("Segoe UI", 11, "bold")
       ).pack(anchor="w", padx=30, pady=(0, 5))


       submission_text_widget = scrolledtext.ScrolledText(
           win, width=70, height=10,
           bg="#0B1220", fg="white",
           insertbackground="white",
           wrap=tk.WORD
       )
       submission_text_widget.insert("1.0", full_submission)
       submission_text_widget.configure(state="disabled")
       submission_text_widget.pack(padx=30, pady=(0, 20), fill="both", expand=True)


       # Score input
       score_frame = tk.Frame(win, bg="#111827")
       score_frame.pack(fill="x", padx=30, pady=(0, 20))


       tk.Label(
           score_frame, text="Score:",
           bg="#111827", fg="white",
           font=("Segoe UI", 11, "bold")
       ).pack(side="left", padx=(0, 10))


       score_entry = tk.Entry(score_frame, width=20)
       if score != "Not Graded":
           score_entry.insert(0, str(score))
       score_entry.pack(side="left")


       btn_frame = tk.Frame(win, bg="#111827")
       btn_frame.pack(fill="x", padx=30, pady=20)


       def on_submit_grade():
           try:
               score_value = float(score_entry.get().strip())
               if score_value < 0 or score_value > 100:
                   messagebox.showerror("Error", "Score must be between 0 and 100")
                   return


               success = self.controller.submit_grade(int(student_id), assignment_id, score_value)
               if success:
                   messagebox.showinfo("Success", "Grade submitted successfully!")
                   self._on_grade_assignment_selected(None)  # Refresh table
                   win.destroy()
               else:
                   messagebox.showerror("Error", "Failed to submit grade")
           except ValueError:
               messagebox.showerror("Error", "Please enter a valid number")
           except Exception as ex:
               messagebox.showerror("Error", f"Failed to submit grade: {ex}")


       submit_btn = tk.Button(
           btn_frame, text="Submit Grade",
           bg="#3182CE", fg="white",
           font=("Segoe UI", 10, "bold"),
           bd=0, padx=20, pady=6,
           command=on_submit_grade
       )
       submit_btn.pack(side="left")


       cancel_btn = tk.Button(
           btn_frame, text="Cancel",
           bg="#111827", fg="white",
           bd=1, relief="solid",
           padx=20, pady=6,
           command=win.destroy
       )
       cancel_btn.pack(side="left", padx=10)


   def _build_mark_attendance_section(self, parent: tk.Frame):
       """Section for teachers to mark student attendance."""
       parent.configure(bg="#050710")


       # Course selection
       course_frame = tk.Frame(parent, bg="#050710")
       course_frame.pack(fill="x", padx=20, pady=(20, 10))


       tk.Label(
           course_frame, text="Select Course:",
           bg="#050710", fg="white",
           font=("Segoe UI", 11, "bold")
       ).pack(side="left", padx=(0, 10))


       self.attendance_course_var = tk.StringVar()
       self.attendance_course_combo = ttk.Combobox(
           course_frame, textvariable=self.attendance_course_var,
           width=30, state="readonly"
       )
       self.attendance_course_combo.pack(side="left", padx=(0, 10))
       self.attendance_course_combo.bind("<<ComboboxSelected>>", self._on_attendance_course_selected)


       # Date selection
       date_frame = tk.Frame(parent, bg="#050710")
       date_frame.pack(fill="x", padx=20, pady=(0, 10))


       tk.Label(
           date_frame, text="Date:",
           bg="#050710", fg="white",
           font=("Segoe UI", 11, "bold")
       ).pack(side="left", padx=(0, 10))


       self.attendance_date_entry = tk.Entry(date_frame, width=20)
       self.attendance_date_entry.insert(0, date.today().strftime("%Y-%m-%d"))
       self.attendance_date_entry.pack(side="left", padx=(0, 10))


       mark_btn = tk.Button(
           date_frame, text="Mark Attendance",
           bg="#3182CE", fg="white",
           activebackground="#2B6CB0",
           activeforeground="white",
           font=("Segoe UI", 10, "bold"),
           bd=0, padx=12, pady=6,
           command=self._open_mark_attendance_window
       )
       mark_btn.pack(side="left", padx=(10, 0))


       refresh_btn = tk.Button(
           date_frame, text="Refresh",
           bg="#3182CE", fg="white",
           activebackground="#2B6CB0",
           activeforeground="white",
           font=("Segoe UI", 10, "bold"),
           bd=0, padx=12, pady=6,
           command=self._load_attendance_courses
       )
       refresh_btn.pack(side="left", padx=(10, 0))


       # Students table
       view_btn = tk.Button(
           date_frame, text="View Attendance Records",
           bg="#4FD1C5", fg="white",
           activebackground="#38B2AC",
           activeforeground="white",
           font=("Segoe UI", 10, "bold"),
           bd=0, padx=12, pady=6,
           command=self._load_attendance_records
       )
       view_btn.pack(side="left", padx=(10, 0))


       table_frame = tk.Frame(parent, bg="#050710")
       table_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))


       columns = ("student_name", "student_id", "attendance_date", "status", "course")
       self.attendance_records_table = ttk.Treeview(
           table_frame,
           columns=columns,
           show="headings",
           height=12
       )


       self.attendance_records_table.heading("student_name", text="Student Name")
       self.attendance_records_table.heading("student_id", text="Student ID")
       self.attendance_records_table.heading("attendance_date", text="Date")
       self.attendance_records_table.heading("status", text="Status")
       self.attendance_records_table.heading("course", text="Course")


       self.attendance_records_table.column("student_name", anchor="center", width=180)
       self.attendance_records_table.column("student_id", anchor="center", width=100)
       self.attendance_records_table.column("attendance_date", anchor="center", width=120)
       self.attendance_records_table.column("status", anchor="center", width=100)
       self.attendance_records_table.column("course", anchor="center", width=150)


       self.attendance_records_table.pack(side="left", fill="both", expand=True)


       scrollbar = ttk.Scrollbar(table_frame, orient="vertical",
                                 command=self.attendance_records_table.yview)
       self.attendance_records_table.configure(yscroll=scrollbar.set)
       scrollbar.pack(side="right", fill="y")


       # Load courses initially (but don't trigger attendance records load yet)
       try:
           courses = self._get_all_courses()
           course_options = [f"{c['course_id']}: {c['title']}" for c in courses]
           self.attendance_course_combo['values'] = course_options
           if course_options:
               self.attendance_course_combo.current(0)
       except Exception as ex:
           print(f"Error loading courses: {ex}")


   def _load_attendance_courses(self):
       """Load courses into attendance course combo."""
       try:
           courses = self._get_all_courses()
           course_options = [f"{c['course_id']}: {c['title']}" for c in courses]
           self.attendance_course_combo['values'] = course_options
           if course_options:
               self.attendance_course_combo.current(0)
               # Only load attendance records if table exists
               if hasattr(self, 'attendance_records_table'):
                self._on_attendance_course_selected(None)
       except Exception as ex:
           print(f"Error loading courses: {ex}")


   def _on_attendance_course_selected(self, event):
       """When course is selected, load students."""
       self._load_attendance_records()


   def _get_attendance_records(self, course_id: int = None, attendance_date: str = None):
           """Get attendance records from database."""
           try:
               if course_id and attendance_date:
                   # Get records for specific course and date
                   rows = self.controller.db.fetch_all(
                       """
                       SELECT u.User_Name, a.Student_ID, a.Att_Date, a.Status, c.title
                       FROM Attendance a
                                JOIN Users u ON a.Student_ID = u.User_ID
                                JOIN Courses c ON a.Course_ID = c.course_id
                       WHERE a.Course_ID = ?
                         AND a.Att_Date = ?
                       ORDER BY a.Att_Date DESC, u.User_Name
                       """,
                       (course_id, attendance_date)
                   )
               elif course_id:
                   # Get all records for specific course
                   rows = self.controller.db.fetch_all(
                       """
                       SELECT u.User_Name, a.Student_ID, a.Att_Date, a.Status, c.title
                       FROM Attendance a
                                JOIN Users u ON a.Student_ID = u.User_ID
                                JOIN Courses c ON a.Course_ID = c.course_id
                       WHERE a.Course_ID = ?
                       ORDER BY a.Att_Date DESC, u.User_Name
                       """,
                       (course_id,)
                   )
               else:
                   # Get all attendance records
                   rows = self.controller.db.fetch_all(
                       """
                       SELECT u.User_Name, a.Student_ID, a.Att_Date, a.Status, c.title
                       FROM Attendance a
                                JOIN Users u ON a.Student_ID = u.User_ID
                                JOIN Courses c ON a.Course_ID = c.course_id
                       ORDER BY a.Att_Date DESC, u.User_Name
                       """
                   )


               return [
                   {
                       "student_name": r[0],
                       "student_id": r[1],
                       "attendance_date": r[2],
                       "status": r[3],
                       "course": r[4]
                   } for r in rows
               ]
           except Exception as e:
               print(f"Error fetching attendance records: {e}")
               return []




   def _load_attendance_records(self):
           try:
               # Check if table exists before using it
               if not hasattr(self, 'attendance_records_table'):
                   return
               self.attendance_records_table.delete(*self.attendance_records_table.get_children())


               selection = self.attendance_course_var.get()
               date_str = self.attendance_date_entry.get().strip()


               course_id = None
               if selection:
                   course_id = int(selection.split(":")[0])


               attendance_date = None
               if date_str:
                   try:
                       attendance_date = datetime.strptime(date_str, "%Y-%m-%d").date()
                       attendance_date = attendance_date.strftime("%Y-%m-%d")
                   except ValueError:
                       pass  # Invalid date format, will show all records


               records = self._get_attendance_records(course_id, attendance_date)


               for record in records:
                   att_date = record["attendance_date"]
                   if att_date:
                       if isinstance(att_date, str):
                           date_str = att_date
                       else:
                           date_str = att_date.strftime("%Y-%m-%d")
                   else:
                       date_str = "N/A"


                   self.attendance_records_table.insert(
                       "",
                       "end",
                       values=(
                           record["student_name"],
                           record["student_id"],
                           date_str,
                           record["status"],
                           record["course"]
                   ))
           except Exception as ex:
               messagebox.showerror("Error", f"Failed to load students: {ex}")


   def _open_mark_attendance_window(self):
       """Open window to mark attendance for all students."""
       selection = self.attendance_course_var.get()
       if not selection:
           messagebox.showerror("Error", "Please select a course first")
           return


       try:
           course_id = int(selection.split(":")[0])
           date_str = self.attendance_date_entry.get().strip()
           attendance_date = datetime.strptime(date_str, "%Y-%m-%d").date()
       except ValueError:
           messagebox.showerror("Error", "Please enter a valid date (YYYY-MM-DD)")
           return


       students = self._get_all_students_for_attendance(course_id)
       if not students:
           messagebox.showwarning("Warning", "No students found ")
           return


       win = tk.Toplevel(self)
       win.title("Mark Attendance")
       win.configure(bg="#111827")
       win.geometry("600x500")
       win.grab_set()


       tk.Label(
           win, text="Mark Attendance",
           bg="#111827", fg="white",
           font=("Segoe UI", 16, "bold")
       ).pack(anchor="w", padx=30, pady=(20, 0))


       tk.Label(
           win, text=f"Course: {selection} | Date: {date_str}",
           bg="#111827", fg="#A0AEC0",
           font=("Segoe UI", 10)
       ).pack(anchor="w", padx=30, pady=(10, 20))


       # Attendance frame with checkboxes
       attendance_frame = tk.Frame(win, bg="#111827")
       attendance_frame.pack(fill="both", expand=True, padx=30, pady=(0, 20))


       scrollbar_frame = tk.Frame(attendance_frame, bg="#111827")
       scrollbar_frame.pack(fill="both", expand=True)


       canvas = tk.Canvas(scrollbar_frame, bg="#0B1220", highlightthickness=0)
       scrollbar = ttk.Scrollbar(scrollbar_frame, orient="vertical", command=canvas.yview)
       scrollable_frame = tk.Frame(canvas, bg="#0B1220")


       scrollable_frame.bind(
           "<Configure>",
           lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
       )


       canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
       canvas.configure(yscrollcommand=scrollbar.set)


       attendance_vars = {}
       for student in students:
           frame = tk.Frame(scrollable_frame, bg="#0B1220")
           frame.pack(fill="x", padx=10, pady=5)


           var = tk.StringVar(value="Present")
           attendance_vars[student["student_id"]] = var


           tk.Label(
               frame, text=f"{student['name']} (ID: {student['student_id']})",
               bg="#0B1220", fg="white",
               font=("Segoe UI", 10),
               width=30, anchor="w"
           ).pack(side="left", padx=(0, 10))


           tk.Radiobutton(
               frame, text="Present", variable=var, value="Present",
               bg="#0B1220", fg="white", selectcolor="#0B1220",
               activebackground="#0B1220", activeforeground="white"
           ).pack(side="left", padx=(0, 10))


           tk.Radiobutton(
               frame, text="Absent", variable=var, value="Absent",
               bg="#0B1220", fg="white", selectcolor="#0B1220",
               activebackground="#0B1220", activeforeground="white"
           ).pack(side="left", padx=(0, 10))


           tk.Radiobutton(
               frame, text="Late", variable=var, value="Late",
               bg="#0B1220", fg="white", selectcolor="#0B1220",
               activebackground="#0B1220", activeforeground="white"
           ).pack(side="left")


       canvas.pack(side="left", fill="both", expand=True)
       scrollbar.pack(side="right", fill="y")


       btn_frame = tk.Frame(win, bg="#111827")
       btn_frame.pack(fill="x", padx=30, pady=20)


       def on_submit_attendance():
           try:
               success_count = 0
               for student_id, var in attendance_vars.items():
                   status = var.get()
                   if self.controller.mark_attendance(student_id, course_id, attendance_date, status):
                       success_count += 1


               messagebox.showinfo("Success", f"Attendance marked for {success_count} students!")
               self._load_attendance_records()
               win.destroy()
           except Exception as ex:
               messagebox.showerror("Error", f"Failed to mark attendance: {ex}")


       submit_btn = tk.Button(
           btn_frame, text="Submit Attendance",
           bg="#3182CE", fg="white",
           font=("Segoe UI", 10, "bold"),
           bd=0, padx=20, pady=6,
           command=on_submit_attendance
       )
       submit_btn.pack(side="left")


       cancel_btn = tk.Button(
           btn_frame, text="Cancel",
           bg="#111827", fg="white",
           bd=1, relief="solid",
           padx=20, pady=6,
           command=win.destroy
       )
       cancel_btn.pack(side="left", padx=10)


   # ================== Courses Tab ==================
   def _build_courses_tab(self, parent: tk.Frame):
       parent.configure(bg="#050710")


       header = tk.Label(
           parent,
           text="Courses & Assignments",
           bg="#050710",
           fg="white",
           font=("Segoe UI", 18, "bold"),
           anchor="w"
       )
       header.pack(fill="x", padx=20, pady=(20, 5))


       sub = tk.Label(
           parent,
           text="View courses, assignments, and submit your work",
           bg="#050710",
           fg="#A0AEC0",
           font=("Segoe UI", 11),
           anchor="w"
       )
       sub.pack(fill="x", padx=20, pady=(0, 20))


       # Create notebook for course sub-tabs
       course_notebook = ttk.Notebook(parent)
       course_notebook.pack(fill="both", expand=True, padx=20, pady=(0, 20))


       # Tab 1: View Courses
       view_courses_frame = tk.Frame(course_notebook, bg="#050710")
       course_notebook.add(view_courses_frame, text="View Courses")
       self._build_view_courses_section(view_courses_frame)


       # Tab 2: Submit Assignment (Student Portal)
       submit_frame = tk.Frame(course_notebook, bg="#050710")
       course_notebook.add(submit_frame, text="Submit Assignment")
       self._build_submit_assignment_section(submit_frame)


   def _build_view_courses_section(self, parent: tk.Frame):
       """Section to view all courses and their assignments."""
       parent.configure(bg="#050710")


       # Refresh button
       top_bar = tk.Frame(parent, bg="#050710")
       top_bar.pack(fill="x", padx=20, pady=(20, 10))


       refresh_btn = tk.Button(
           top_bar, text="Refresh",
           bg="#3182CE", fg="white",
           activebackground="#2B6CB0",
           activeforeground="white",
           font=("Segoe UI", 10, "bold"),
           bd=0, padx=12, pady=6,
           command=self._load_courses_table
       )
       refresh_btn.pack(side="right")


       # Courses table
       table_frame = tk.Frame(parent, bg="#050710")
       table_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))


       columns = ("course_id", "title")
       self.courses_table = ttk.Treeview(
           table_frame,
           columns=columns,
           show="headings",
           height=10
       )


       self.courses_table.heading("course_id", text="Course ID")
       self.courses_table.heading("title", text="Course Title")


       self.courses_table.column("course_id", anchor="center", width=150)
       self.courses_table.column("title", anchor="w", width=400)


       self.courses_table.pack(side="left", fill="both", expand=True)


       scrollbar = ttk.Scrollbar(table_frame, orient="vertical",
                                 command=self.courses_table.yview)
       self.courses_table.configure(yscroll=scrollbar.set)
       scrollbar.pack(side="right", fill="y")


       # Double-click to view assignments
       self.courses_table.bind("<Double-1>", self._open_view_assignments_window)


       self._load_courses_table()


   def _load_courses_table(self):
       """Load courses into table."""
       try:
           self.courses_table.delete(*self.courses_table.get_children())
           courses = self._get_all_courses()
           for c in courses:
               self.courses_table.insert(
                   "",
                   "end",
                   values=(c["course_id"], c["title"])
               )
       except Exception as ex:
           messagebox.showerror("Error", f"Failed to load courses: {ex}")


   def _open_view_assignments_window(self, event):
       """Open window to view assignments for a course."""
       selected = self.courses_table.selection()
       if not selected:
           return


       item_id = selected[0]
       row = self.courses_table.item(item_id, "values")
       course_id, course_title = row


       try:
           assignments = self.controller.get_course_assignments(int(course_id))
       except Exception as ex:
           messagebox.showerror("Error", f"Failed to load assignments: {ex}")
           return


       win = tk.Toplevel(self)
       win.title(f"Assignments - {course_title}")
       win.configure(bg="#111827")
       win.geometry("700x500")
       win.grab_set()


       tk.Label(
           win, text=f"Assignments for: {course_title}",
           bg="#111827", fg="white",
           font=("Segoe UI", 16, "bold")
       ).pack(anchor="w", padx=30, pady=(20, 10))


       # Assignments table
       table_frame = tk.Frame(win, bg="#111827")
       table_frame.pack(fill="both", expand=True, padx=30, pady=(0, 20))


       columns = ("assignment_id", "title", "due_date")
       assignments_table = ttk.Treeview(
           table_frame,
           columns=columns,
           show="headings",
           height=15
       )


       assignments_table.heading("assignment_id", text="Assignment ID")
       assignments_table.heading("title", text="Title")
       assignments_table.heading("due_date", text="Due Date")


       assignments_table.column("assignment_id", anchor="center", width=150)
       assignments_table.column("title", anchor="w", width=300)
       assignments_table.column("due_date", anchor="center", width=150)


       assignments_table.pack(side="left", fill="both", expand=True)


       scrollbar = ttk.Scrollbar(table_frame, orient="vertical",
                                 command=assignments_table.yview)
       assignments_table.configure(yscroll=scrollbar.set)
       scrollbar.pack(side="right", fill="y")


       for a in assignments:
           due_date = a["due_date"]
           if due_date:
               if isinstance(due_date, str):
                   date_str = due_date
               else:
                   date_str = due_date.strftime("%Y-%m-%d")
           else:
               date_str = "N/A"


           assignments_table.insert(
               "",
               "end",
               values=(a["assignment_id"], a["title"], date_str)
           )


       close_btn = tk.Button(
           win, text="Close",
           bg="#111827", fg="white",
           bd=1, relief="solid",
           padx=20, pady=6,
           command=win.destroy
       )
       close_btn.pack(pady=20)


   def _build_submit_assignment_section(self, parent: tk.Frame):
       """Section for students to submit assignments."""
       parent.configure(bg="#050710")


       # Student ID input
       student_frame = tk.Frame(parent, bg="#050710")
       student_frame.pack(fill="x", padx=20, pady=(20, 10))


       tk.Label(
           student_frame, text="Student ID:",
           bg="#050710", fg="white",
           font=("Segoe UI", 11, "bold")
       ).pack(side="left", padx=(0, 10))


       self.submit_student_id_entry = tk.Entry(student_frame, width=20)
       self.submit_student_id_entry.pack(side="left", padx=(0, 20))


       # Course selection
       course_frame = tk.Frame(parent, bg="#050710")
       course_frame.pack(fill="x", padx=20, pady=(0, 10))


       tk.Label(
           course_frame, text="Select Course:",
           bg="#050710", fg="white",
           font=("Segoe UI", 11, "bold")
       ).pack(side="left", padx=(0, 10))


       self.submit_course_var = tk.StringVar()
       self.submit_course_combo = ttk.Combobox(
           course_frame, textvariable=self.submit_course_var,
           width=30, state="readonly"
       )
       self.submit_course_combo.pack(side="left", padx=(0, 10))
       self.submit_course_combo.bind("<<ComboboxSelected>>", self._on_submit_course_selected)


       refresh_btn = tk.Button(
           course_frame, text="Refresh",
           bg="#3182CE", fg="white",
           activebackground="#2B6CB0",
           activeforeground="white",
           font=("Segoe UI", 10, "bold"),
           bd=0, padx=12, pady=6,
           command=self._load_submit_courses
       )
       refresh_btn.pack(side="left", padx=(10, 0))


       # Assignment selection
       assignment_frame = tk.Frame(parent, bg="#050710")
       assignment_frame.pack(fill="x", padx=20, pady=(0, 10))


       tk.Label(
           assignment_frame, text="Select Assignment:",
           bg="#050710", fg="white",
           font=("Segoe UI", 11, "bold")
       ).pack(side="left", padx=(0, 10))


       self.submit_assignment_var = tk.StringVar()
       self.submit_assignment_combo = ttk.Combobox(
           assignment_frame, textvariable=self.submit_assignment_var,
           width=30, state="readonly"
       )
       self.submit_assignment_combo.pack(side="left", padx=(0, 10))


       # Submission text area
       submission_frame = tk.Frame(parent, bg="#050710")
       submission_frame.pack(fill="both", expand=True, padx=20, pady=(0, 10))


       tk.Label(
           submission_frame, text="Submission Text:",
           bg="#050710", fg="white",
           font=("Segoe UI", 11, "bold")
       ).pack(anchor="w", pady=(0, 5))


       self.submission_text_widget = scrolledtext.ScrolledText(
           submission_frame, width=80, height=15,
           bg="#0B1220", fg="white",
           insertbackground="white",
           wrap=tk.WORD
       )
       self.submission_text_widget.pack(fill="both", expand=True)


       # Submit button
       submit_btn_frame = tk.Frame(parent, bg="#050710")
       submit_btn_frame.pack(fill="x", padx=20, pady=(0, 20))


       submit_btn = tk.Button(
           submit_btn_frame, text="Submit Assignment",
           bg="#3182CE", fg="white",
           activebackground="#2B6CB0",
           activeforeground="white",
           font=("Segoe UI", 12, "bold"),
           bd=0, padx=20, pady=10,
           command=self._submit_assignment
       )
       submit_btn.pack()


       # Load courses initially
       self._load_submit_courses()


   def _load_submit_courses(self):
       """Load courses into submit course combo."""
       try:
           courses = self._get_all_courses()
           course_options = [f"{c['course_id']}: {c['title']}" for c in courses]
           self.submit_course_combo['values'] = course_options
           if course_options:
               self.submit_course_combo.current(0)
               self._on_submit_course_selected(None)
       except Exception as ex:
           print(f"Error loading courses: {ex}")


   def _on_submit_course_selected(self, event):
       """When course is selected, load assignments."""
       try:
           selection = self.submit_course_var.get()
           if not selection:
               return
           course_id = int(selection.split(":")[0])
           assignments = self.controller.get_course_assignments(course_id)
           assignment_options = [f"{a['assignment_id']}: {a['title']}" for a in assignments]
           self.submit_assignment_combo['values'] = assignment_options
           if assignment_options:
               self.submit_assignment_combo.current(0)
       except Exception as ex:
           print(f"Error loading assignments: {ex}")


   def _submit_assignment(self):
       """Submit assignment for a student."""
       try:
           student_id_str = self.submit_student_id_entry.get().strip()
           if not student_id_str:
               messagebox.showerror("Error", "Please enter Student ID")
               return


           student_id = int(student_id_str)


           assignment_selection = self.submit_assignment_var.get()
           if not assignment_selection:
               messagebox.showerror("Error", "Please select an assignment")
               return


           assignment_id = int(assignment_selection.split(":")[0])


           submission_text = self.submission_text_widget.get("1.0", tk.END).strip()
           if not submission_text:
               messagebox.showerror("Error", "Please enter submission text")
               return


           success = self.controller.student_submit_assignment(student_id, assignment_id, submission_text)
           if success:
               messagebox.showinfo("Success", "Assignment submitted successfully!")
               self.submission_text_widget.delete("1.0", tk.END)
           else:
               messagebox.showerror("Error", "Failed to submit assignment")
       except ValueError:
           messagebox.showerror("Error", "Please enter a valid Student ID")
       except Exception as ex:
           messagebox.showerror("Error", f"Failed to submit assignment: {ex}")




if __name__ == "__main__":
   app = EduMessApp()
   app.mainloop()



