# Automated-report-generation



#  Task 2 – Student Report Card Generator

###  Project Overview

This project focuses on automating the generation of **student report cards** using Python. Traditionally, teachers prepare report cards manually, which is time-consuming and prone to errors. This project solves that problem by reading student marks from a **CSV file** and generating **personalized PDF report cards** for each student. The script also displays the student’s performance details on the terminal so that the user can verify the output.

The generated reports include the student’s name, marks in different subjects, total score, average marks, and the final result (Pass/Fail). The PDFs are formatted with a proper title, table, and layout for easy readability.



### ⚙ Tools & Libraries Used

* **Python 3.12** → Core programming language.
* **CSV Module** → Reads student data from a CSV file (`students.csv`).
* **FPDF Library** → Creates well-formatted PDF report cards.
* **OS Module** → Handles file saving and prevents overwriting errors.
* **Text Editor / IDE** → Python IDLE and Jupyter Notebook were used for writing and testing code.

---

### 🛠 Implementation Details

1. **CSV Input File (`students.csv`)**

   * The CSV file stores student names and their marks in subjects (Maths, Science, English).
   * Example:

---
     Name,Maths,Science,English
     Ali,78,85,92
     Sara,56,61,74
     Rohan,40,35,50
     ```

2. **Python Script (`report_generator.py`)**

   * Reads each student’s marks from the CSV file.
   * Calculates:

     * **Total Marks**
     * **Average Marks**
     * **Result (Pass/Fail)**
   * Displays details in the terminal for verification.
   * Creates a **PDF Report Card** with a formatted table.

3. **PDF Report Card**
   Each student receives a PDF file named after them (e.g., `Ali_report.pdf`).

   * Contains:

     * School Title
     * Academic Year
     * Student Name
     * Marks in each subject
     * Total & Average
     * Pass/Fail Result

---

### Example Output

**Terminal Output**

```
---------
Name    : Ali
Maths   : 78
Science : 85
English : 92
Total   : 255
Average : 85.0
Result  : Pass
Report saved as: Ali_report.pdf
---------
```

**Sample PDF (Ali\_report.pdf)**

```
ABC School – Report Card
Academic Year: 2024–2025
Student Name: Ali

Subject   Marks
Maths     78
Science   85
English   92
Total     255
Average   85.0
Result    Pass
```

---

###  Applications

* **Schools & Colleges** → Automates student report generation.
* **Coaching Institutes** → Quick progress reports for multiple students.
* **Corporate Training** → Can be adapted for employee performance tracking.
* **Personal Use** → Parents can track child’s academic performance.

---

###  Project Outcome

* Automated **report card creation** from CSV data.
* Reduced manual work and improved **accuracy**.
* Created **well-formatted PDFs** using Python.
* Ensured scalability → Works for any number of students by just updating the CSV file.

This project demonstrates how Python can be used in **real-world education systems** to save time and reduce errors.

---


