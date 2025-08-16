import csv
from fpdf import FPDF
import os

# PDF class with header and footer
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "ABC School - Report Card", ln=True, align='C')  # Fixed en-dash
        self.set_font("Arial", "I", 12)
        self.cell(0, 10, "Academic Year: 2024-2025", ln=True, align='C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align='C')

# Read CSV file
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        name = row["Name"]
        maths = int(row["Maths"])
        science = int(row["Science"])
        english = int(row["English"])
        total = maths + science + english
        average = round(total / 3, 2)
        result = "Pass" if average >= 40 else "Fail"

        # Show progress in terminal
        print("---------")
        print(f"Name    : {name}")
        print(f"Maths   : {maths}")
        print(f"Science : {science}")
        print(f"English : {english}")
        print(f"Total   : {total}")
        print(f"Average : {average}")
        print(f"Result  : {result}")
        print("Report saved as:", f"{name}_report.pdf")
        print("---------\n")

        # Create PDF
        pdf = PDF()
        pdf.add_page()

        # Student Name
        pdf.set_font("Arial", "B", 14)
        pdf.cell(0, 10, f"Student Name: {name}", ln=True)
        pdf.ln(5)

        # Table header
        pdf.set_font("Arial", "B", 12)
        pdf.cell(60, 10, "Subject", 1)
        pdf.cell(60, 10, "Marks", 1)
        pdf.ln()

        # Table data
        pdf.set_font("Arial", "", 12)
        pdf.cell(60, 10, "Maths", 1)
        pdf.cell(60, 10, str(maths), 1)
        pdf.ln()

        pdf.cell(60, 10, "Science", 1)
        pdf.cell(60, 10, str(science), 1)
        pdf.ln()

        pdf.cell(60, 10, "English", 1)
        pdf.cell(60, 10, str(english), 1)
        pdf.ln()

        pdf.cell(60, 10, "Total", 1)
        pdf.cell(60, 10, str(total), 1)
        pdf.ln()

        pdf.cell(60, 10, "Average", 1)
        pdf.cell(60, 10, str(average), 1)
        pdf.ln()

        pdf.cell(60, 10, "Result", 1)
        pdf.cell(60, 10, result, 1)

        # Check if PDF file is locked or open
        filename = f"{name}_report.pdf"
        try:
            pdf.output(filename)
        except PermissionError:
            filename = f"{name}_report_new.pdf"
            pdf.output(filename)
            print(f"⚠️ Couldn't overwrite old file, so saved as: {filename}")

print("✅ All student reports generated successfully!")
