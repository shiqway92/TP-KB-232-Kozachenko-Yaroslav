students = []  # Список для збереження студентів


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
            print(f"Ім'я: {student['name']}, Телефон: {student['phone']}, Email: {student['email']}, Адреса: {student['address']}")


def add_student():
    name = input("Введіть ім'я студента: ")
    phone = input("Введіть номер телефону: ")
    email = input("Введіть email студента: ")
    address = input("Введіть адресу студента: ")

    # Додаємо нового студента до списку
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
    # Сортуємо список студентів за ім'ям
    students.sort(key=lambda x: x["name"])


def main():
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
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
