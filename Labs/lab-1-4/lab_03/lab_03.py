import sys
import unittest
import csv


# Клас для студента
class Student:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Ім'я: {self.name}, Телефон: {self.phone}, Email: {self.email}, Адреса: {self.address}"

    def update_info(self, phone=None, email=None, address=None):
        """Метод для оновлення інформації про студента."""
        if phone:
            self.phone = phone
        if email:
            self.email = email
        if address:
            self.address = address


# Клас для списку студентів
class StudentList:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        """Метод для додавання нового студента."""
        self.students.append(student)
        self.sort_students()

    def remove_student(self, name):
        """Метод для видалення студента за ім'ям."""
        self.students = [student for student in self.students if student.name != name]

    def edit_student(self, name, phone=None, email=None, address=None):
        """Метод для редагування інформації про студента."""
        for student in self.students:
            if student.name == name:
                student.update_info(phone, email, address)
                break

    def sort_students(self):
        """Метод для сортування студентів за іменем."""
        self.students.sort(key=lambda x: x.name)

    def __str__(self):
        return "\n".join(str(student) for student in self.students)


# Клас для роботи з файлами
class FileManager:
    @staticmethod
    def load_from_csv(file_name):
        """Метод для завантаження студентів з CSV файлу."""
        student_list = StudentList()
        try:
            with open(file_name, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    student = Student(row["name"], row["phone"], row["email"], row["address"])
                    student_list.add_student(student)
            print(f"Дані завантажено з файлу '{file_name}'.")
        except FileNotFoundError:
            print(f"Помилка: файл '{file_name}' не знайдено.")
        except Exception as e:
            print(f"Помилка при завантаженні файлу: {e}")
        return student_list

    @staticmethod
    def save_to_csv(file_name, student_list):
        """Метод для збереження списку студентів у CSV файл."""
        try:
            with open(file_name, "w", newline='', encoding='utf-8') as csvfile:
                fieldnames = ["name", "phone", "email", "address"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for student in student_list.students:
                    writer.writerow({
                        "name": student.name,
                        "phone": student.phone,
                        "email": student.email,
                        "address": student.address
                    })
            print(f"Дані збережено у файл '{file_name}'.")
        except Exception as e:
            print(f"Помилка при збереженні файлу: {e}")


# Основна програма
def print_menu():
    print("\nТелефонний довідник студентів:")
    print("1. Додати нового студента")
    print("2. Змінити дані про студента")
    print("3. Видалити запис про студента")
    print("4. Роздрукувати довідник")
    print("5. Вийти з програми")


def main():
    student_list = StudentList()

    if len(sys.argv) > 1:
        csv_file = sys.argv[1]
        student_list = FileManager.load_from_csv(csv_file)

    while True:
        print_menu()
        choice = input("Виберіть опцію (1-5): ")
        if choice == "1":
            name = input("Введіть ім'я студента: ")
            phone = input("Введіть номер телефону: ")
            email = input("Введіть email студента: ")
            address = input("Введіть адресу студента: ")
            student = Student(name, phone, email, address)
            student_list.add_student(student)
        elif choice == "2":
            name = input("Введіть ім'я студента, якого хочете змінити: ")
            phone = input("Введіть новий номер телефону: ")
            email = input("Введіть новий email: ")
            address = input("Введіть нову адресу: ")
            student_list.edit_student(name, phone, email, address)
        elif choice == "3":
            name = input("Введіть ім'я студента, якого хочете видалити: ")
            student_list.remove_student(name)
        elif choice == "4":
            print(student_list)
        elif choice == "5":
            FileManager.save_to_csv("students.csv", student_list)
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


# Юніт тести
class TestStudentDirectory(unittest.TestCase):

    def setUp(self):
        self.student_list = StudentList()

    def test_add_student(self):
        student = Student("Іван", "123", "a@b.com", "Kyiv")
        self.student_list.add_student(student)
        self.assertEqual(len(self.student_list.students), 1)

    def test_remove_student(self):
        student = Student("Іван", "123", "a@b.com", "Kyiv")
        self.student_list.add_student(student)
        self.student_list.remove_student("Іван")
        self.assertEqual(len(self.student_list.students), 0)

    def test_sort_students(self):
        student1 = Student("Петро", "123", "a@b.com", "Kyiv")
        student2 = Student("Анна", "456", "c@d.com", "Lviv")
        self.student_list.add_student(student1)
        self.student_list.add_student(student2)
        self.student_list.sort_students()
        self.assertEqual(self.student_list.students[0].name, "Анна")


if __name__ == "__main__":
    # Якщо потрібно виконати тести:
    unittest.main()
    # Якщо потрібно запустити основну програму:
    # main()
