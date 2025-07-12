
def auth_menu():
    print("""
    1. Register
    2. Login
    3. Exit
    """)
    choice = input("Choice: ")
    if choice == "1":
        pass
    elif choice == "2":
        pass
    elif choice == "3":
        print("Good bye")
        return None
    else:
        print("Invalid choice")
    return auth_menu()


def admin_menu():
    print("""
    1. Ovqat qo‘shis
    2. Ovqat o‘chirish
    3. Menyuni ko‘rish
    4. Buyurtmalarni ko‘rish
    5. Buyurtmalar tarixini ko‘rish
    6. Foydalanuvchilarni ko‘rish
    7. Chiqish
    """)
    choice = input("Choice: ")
    if choice == "1":
        pass
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "4":
        pass
    elif choice == "5":
        pass
    elif choice == "6":
        pass
    elif choice == "7":
        pass
        return auth_menu()
    else:
        print("Invalid choice")
    return admin_menu()


def user_menu():
    print("""
    1. Menyuni ko‘rish
    2. Buyurtma berish
    3. Mening buyurtmalarim
    4. Buyurtmani bekor qilish
    5. Chiqish
    """)

    choice = input("Choice: ")
    if choice == "1":
        pass
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "4":
        pass
    elif choice == "5":
        print("Good bye")
        return None
    else:
        pass
        return auth_menu()

    return user_menu()


if __name__ == '__main__':
    auth_menu()






