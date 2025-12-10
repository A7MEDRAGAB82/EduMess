"""
Controller layer that exposes simple functions for UI developers.
"""

from __future__ import annotations

from datetime import date
from typing import Any, Dict, List, Optional

from model import Database


class SchoolController:
    def __init__(self, db: Optional[Database] = None) -> None:
        self.db = db or Database()

    def add_student(self, name: str, grade: str) -> int:
        """
        Add a new student. 
        """
        # Step 1: Add user in Users table
        user_id = self.db.execute_scalar(
            """
            INSERT INTO Users (User_Name, Password, Role)
                OUTPUT inserted.User_ID
            VALUES (?, ?, 'Student')
            """,
            (name, name.lower().replace(" ", "") + "123"),
        )

        if not user_id:
            raise Exception("Failed to create user")

        # Step 2: Add student record
        from datetime import date


        student_id = self.db.execute_scalar(
            """
            INSERT INTO Students (Student_ID, Grade_Level, Enrollment_Date)
                OUTPUT inserted.Student_ID
            VALUES (?, ?, ?)
            """,
            (user_id, int(grade), date.today()),
        )

        return int(student_id)

    def delete_student(self, student_id: int) -> bool:
        """
        Delete a student by ID.
        Because of ON DELETE CASCADE in SQL Server,
        deleting the User will automatically delete the Student record.
        """
        try:

            self.db.execute_query(
                "DELETE FROM Users WHERE User_ID = ?",
                (student_id,)
            )
            print(f"User/Student {student_id} deleted successfully.")
            return True
        except Exception as e:
            print(f"Error deleting student: {e}")
            return False

    def update_student(self, student_id: int, new_name: str = None, new_grade: str = None) -> bool:
        """
        Update student details.
        Updates 'Users' table if name changes.
        Updates 'Students' table if grade changes.
        """
        try:

            if new_name:
                self.db.execute_query(
                    "UPDATE Users SET User_Name = ? WHERE User_ID = ?",
                    (new_name, student_id)
                )


            if new_grade:
                self.db.execute_query(
                    "UPDATE Students SET Grade_Level = ? WHERE Student_ID = ?",
                    (int(new_grade), student_id)
                )

            print(f"Student {student_id} updated successfully.")
            return True

        except Exception as e:
            print(f"Error updating student: {e}")
            return False

    def get_all_students(self) -> List[Dict[str, Any]]:
        """Fetch all students. No inputs. Returns list of dicts."""
        rows = self.db.fetch_all(
            """
            SELECT s.Student_ID, u.User_Name, s.Grade_Level, s.Enrollment_Date
            FROM Students s
            JOIN Users u ON s.Student_ID = u.User_ID
            ORDER BY s.Student_ID
            """
        )
        return [
            {
                "student_id": r[0], 
                "name": r[1], 
                "grade_level": r[2],
                "enrollment_date": r[3]
            } for r in rows
        ]

    def add_course(self, title: str) -> int:
        """Add a course. Input: name (str)."""
        course_id = self.db.execute_scalar(
            "INSERT INTO Courses (title) OUTPUT inserted.course_id VALUES (?)",
            (title,),
        )
        return int(course_id)

    def create_assignment(self, course_id: int, title: str, due_date: date) -> int:
        """Create assignment. Inputs: course_id (int), title (str), due_date (datetime.date)."""
        assignment_id = self.db.execute_scalar(
            """
            INSERT INTO Assignments (course_id, title, due_date)
            OUTPUT inserted.assignment_id
            VALUES (?, ?, ?)
            """,
            (course_id, title, due_date),
        )
        return int(assignment_id)

    def student_submit_assignment(self, student_id: int, assignment_id: int, submission_text: str) -> bool:
        """
        Student uploads an assignment answer.
        """
        try:
            self.db.execute_query(
                """
                INSERT INTO Grades (Student_ID, Assignment_ID, Submission_Date, Submission_Text, Score)
                VALUES (?, ?, GETDATE(), ?, NULL)
                """,
                (student_id, assignment_id, submission_text)
            )
            print(f"Student {student_id} submitted assignment successfully.")
            return True
        except Exception as e:
            print(f"Error submitting assignment: {e}")
            return False

    def mark_attendance(
        self, student_id: int, course_id: int, attendance_date: date, status: str
    ) -> bool:
        """Record attendance."""

        try:
            self.db.execute_query(
                """
                INSERT INTO Attendance (Student_ID, Course_ID, Att_Date, Status)
                VALUES (?, ?, ?, ?)
                """,
                (student_id, course_id, attendance_date, status),
            )
            return True
        except Exception as e:
            print(f"Error marking attendance: {e}")
            return False

    def submit_grade(self, student_id: int, assignment_id: int, score: float) -> bool:
        """
        Teacher action: Grade a student's submission.
        This UPDATES the existing record created by the student.
        """
        try:
            cursor = self.db.session.execute(
                """
                UPDATE Grades
                SET Score = ?
                WHERE Student_ID = ?
                  AND Assignment_ID = ?
                """,
                (score, student_id, assignment_id)
            )
            self.db.conn.commit()

            if cursor.rowcount == 0:
                print("Student hasn't submitted yet. Inserting grade directly...")
                self.db.execute_query(
                    """
                    INSERT INTO Grades (Student_ID, Assignment_ID, Score, Submission_Date)
                    VALUES (?, ?, ?, GETDATE())
                    """,
                    (student_id, assignment_id, score)
                )

            print(f"Grade {score} assigned to Student {student_id}.")
            return True
        except Exception as e:
            print(f"Error grading: {e}")
            return False

    def get_course_assignments(self, course_id: int) -> List[Dict[str, Any]]:
        """Get assignments for a course. Input: course_id (int)."""
        rows = self.db.fetch_all(
            """
            SELECT assignment_id, title, due_date
            FROM Assignments
            WHERE course_id = ?
            ORDER BY due_date
            """,
            (course_id,),
        )
        return [
            {"assignment_id": r[0], "title": r[1], "due_date": r[2]} for r in rows
        ]

    def get_students_in_course(self, course_id: int) -> List[Dict[str, Any]]:
        """Get students tied to a course."""
        rows = self.db.fetch_all(
            """
            SELECT DISTINCT s.Student_ID, u.User_Name, s.Grade_Level
            FROM Students s
            JOIN Users u ON s.Student_ID = u.User_ID 
            JOIN Attendance a ON a.Student_ID = s.Student_ID
            WHERE a.Course_ID = ?
            ORDER BY s.Student_ID
            """,
            (course_id,),
        )
        return [
            {"student_id": r[0], "name": r[1], "grade_level": r[2]} for r in rows
        ]


