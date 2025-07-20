import tkinter as tk
from tkinter import messagebox

class MedicalRecordApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Medical Record App")
        
        self.label_patient_id = tk.Label(master, text="Patient ID:")
        self.label_patient_id.grid(row=0, column=0)
        self.entry_patient_id = tk.Entry(master)
        self.entry_patient_id.grid(row=0, column=1)

        self.label_name = tk.Label(master, text="Name:")
        self.label_name.grid(row=1, column=0)
        self.entry_name = tk.Entry(master)
        self.entry_name.grid(row=1, column=1)

        self.label_age = tk.Label(master, text="Age:")
        self.label_age.grid(row=2, column=0)
        self.entry_age = tk.Entry(master)
        self.entry_age.grid(row=2, column=1)

        self.label_diagnosis = tk.Label(master, text="Diagnosis:")
        self.label_diagnosis.grid(row=3, column=0)
        self.entry_diagnosis = tk.Entry(master)
        self.entry_diagnosis.grid(row=3, column=1)

        self.button_add_record = tk.Button(master, text="Add Record", command=self.add_record)
        self.button_add_record.grid(row=4, column=0, columnspan=2)

        self.button_display_records = tk.Button(master, text="Display All Records", command=self.display_records)
        self.button_display_records.grid(row=5, column=0, columnspan=2)

        self.medical_store = MedicalRecordStore()

    def add_record(self):
        patient_id = self.entry_patient_id.get()
        name = self.entry_name.get()
        age = self.entry_age.get()
        diagnosis = self.entry_diagnosis.get()

        if not (patient_id and name and age and diagnosis):
            messagebox.showerror("Error", "All fields are required!")
            return

        self.medical_store.add_record(patient_id, name, age, diagnosis)
        messagebox.showinfo("Success", "Record added successfully!")
        self.entry_patient_id.delete(0, tk.END)
        self.entry_name.delete(0, tk.END)
        self.entry_age.delete(0, tk.END)
        self.entry_diagnosis.delete(0, tk.END)

    def display_records(self):
        records = self.medical_store.get_all_records()
        if not records:
            messagebox.showinfo("Info", "No records found.")
        else:
            display_text = ""
            for record in records:
                display_text += f"Patient ID: {record['patient_id']}\n"
                display_text += f"Name: {record['name']}\n"
                display_text += f"Age: {record['age']}\n"
                display_text += f"Diagnosis: {record['diagnosis']}\n\n"
            messagebox.showinfo("Medical Records", display_text)

class MedicalRecordStore:
    def __init__(self):
        self.records = []

    def add_record(self, patient_id, name, age, diagnosis):
        self.records.append({
            'patient_id': patient_id,
            'name': name,
            'age': age,
            'diagnosis': diagnosis
        })

    def get_all_records(self):
        return self.records

def main():
    root = tk.Tk()
    app = MedicalRecordApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
