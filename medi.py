class MedicalRecordStore:
    def __init__(self):
        self.records = {}

    def add_record(self, patient_id, name, age, diagnosis):
        self.records[patient_id] = {
            'name': name,
            'age': age,
            'diagnosis': diagnosis
        }

    def get_record(self, patient_id):
        return self.records.get(patient_id)

    def delete_record(self, patient_id):
        if patient_id in self.records:
            del self.records[patient_id]
            print(f"Record with patient ID {patient_id} deleted successfully.")
        else:
            print(f"Record with patient ID {patient_id} not found.")

    def display_records(self):
        if not self.records:
            print("No records found.")
        else:
            print("Medical Records:")
            for patient_id, record in self.records.items():
                print(f"Patient ID: {patient_id}")
                print(f"Name: {record['name']}")
                print(f"Age: {record['age']}")
                print(f"Diagnosis: {record['diagnosis']}")
                print()


def main():
    medical_store = MedicalRecordStore()

    while True:
        print("\nMedical Record Store Menu:")
        print("1. Add Record")
        print("2. Get Record")
        print("3. Delete Record")
        print("4. Display All Records")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            patient_id = input("Enter Patient ID: ")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            diagnosis = input("Enter Diagnosis: ")
            medical_store.add_record(patient_id, name, age, diagnosis)
            print("Record added successfully.")

        elif choice == '2':
            patient_id = input("Enter Patient ID to retrieve record: ")
            record = medical_store.get_record(patient_id)
            if record:
                print("Record found:")
                print(f"Patient ID: {patient_id}")
                print(f"Name: {record['name']}")
                print(f"Age: {record['age']}")
                print(f"Diagnosis: {record['diagnosis']}")
            else:
                print(f"No record found for patient ID {patient_id}.")

        elif choice == '3':
            patient_id = input("Enter Patient ID to delete record: ")
            medical_store.delete_record(patient_id)

        elif choice == '4':
            medical_store.display_records()

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
