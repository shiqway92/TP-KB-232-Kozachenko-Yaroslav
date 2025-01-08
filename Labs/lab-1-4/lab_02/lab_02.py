import csv
import sys
import unittest

students = []  # Список для збереження студентів


def load_students_from_csv(file_name):
    """Завантажує дані з CSV-файлу у список students."""
    try:
        with open(file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                students.append({
                    "name": row["name"],
                    "phone": row["phone"],
                    "email": row["email"],
                    "address": row["address"]
                })
        print(f"Дані завантажено з файлу '{file_name}'.")
    except FileNotFoundError:
        print(f"Помилка: файл '{file_name}' не знайдено.")
    except Exception as e:
        print(f"Помилка при завантаженні файлу: {e}")


def save_students_to_csv(file_name):
    """Зберігає список students у CSV-файл."""
    try:
        with open(file_name, "w", newline='', encoding='utf-8') as csvfile:
            fieldnames = ["name", "phone", "email", "address"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for student in students:
                writer.writerow(student)
        print(f"Дані збережено у файл '{file_name}'.")
    except Exception as e:
        print(f"Помилка при збереженні файлу: {e}")


def print_menu():
    print("\nТелефонний довідник студентів:")
    print("1. Додати нового студента")
    print("2. Змінити дані про студента")
    print("3. Видалити запис про студента")
    print("4. Роздрукувати довідник")
    print("5. Вийти з програми")


def print_students():
    if not students:
        print("Довідник порожній!")
    else:
        print("\nВідсортований довідник студентів:")
        for student in students:
            print(f"Ім'я: {student['name']}, Телефон: {student['phone']}, "
                  f"Email: {student['email']}, Адреса: {student['address']}")


def add_student():
    name = input("Введіть ім'я студента: ")
    phone = input("Введіть номер телефону: ")
    email = input("Введіть email студента: ")
    address = input("Введіть адресу студента: ")

    students.append({"name": name, "phone": phone, "email": email, "address": address})
    sort_students()
    print(f"Студента {name} додано!")


def edit_student():
    name = input("Введіть ім'я студента, якого хочете змінити: ")
    for student in students:
        if student["name"] == name:
            print(f"Поточні дані: {student}")
            student["phone"] = input("Введіть новий номер телефону: ")
            student["email"] = input("Введіть новий email: ")
            student["address"] = input("Введіть нову адресу: ")
            sort_students()
            print(f"Дані студента {name} оновлено!")
            return
    print(f"Студента з ім'ям '{name}' не знайдено.")


def delete_student():
    name = input("Введіть ім'я студента, якого хочете видалити: ")
    global students
    students = [student for student in students if student["name"] != name]
    print(f"Студента {name} видалено!")


def sort_students():
    students.sort(key=lambda x: x["name"])


def main():
    if len(sys.argv) > 1:
        csv_file = sys.argv[1]
        load_students_from_csv(csv_file)
    else:
        print("Увага: Ім'я файлу CSV не передано як аргумент командного рядка.")
    
    while True:
        print_menu()
        choice = input("Виберіть опцію (1-5): ")
        if choice == "1":
            add_student()
        elif choice == "2":
            edit_student()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            print_students()
        elif choice == "5":
            save_students_to_csv("students.csv")
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


# Юніт тести для перевірки функціональності
class TestStudentDirectory(unittest.TestCase):

    def setUp(self):
        global students
        students = []  # Скидаємо список перед кожним тестом

    def test_add_student(self):
        students.append({"name": "Іван", "phone": "123", "email": "a@b.com", "address": "Kyiv"})
        self.assertEqual(len(students), 1)

    def test_delete_student(self):
        students.append({"name": "Іван", "phone": "123", "email": "a@b.com", "address": "Kyiv"})
        students = [student for student in students if student["name"] != "Іван"]
        self.assertEqual(len(students), 0)

    def test_sort_students(self):
        students.append({"name": "Петро", "phone": "123", "email": "a@b.com", "address": "Kyiv"})
        students.append({"name": "Анна", "phone": "456", "email": "c@d.com", "address": "Lviv"})
        sort_students()
        self.assertEqual(students[0]['name'], "Анна")


if __name__ == "__main__":
    # Запуск юніт-тестів
    unittest.main(exit=False)
    # Запуск основної програми
    main()
