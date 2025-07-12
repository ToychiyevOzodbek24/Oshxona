from views import register, login, logout
from ucer_views import *

def auth_menu():
    print("""
    1. Register
    2. Login
    3. Exit
    """)
    choice = input("Choice: ")
    if choice == "1":
        if register():
            print("Successfully registered")
        else:
            print("Something went wrong")
    elif choice == "2":
        result = login()
        if result == "admin":
            print("Welcome my owner")
            return admin_menu()
        elif result == "user":
            return user_menu()
        else:
            return login()
    elif choice == "3":
        print("Good bye")
        return None
    else:
        print("Invalid choice")
    return auth_menu()


def admin_menu():
    print("""
    1. Add Food  
    2. Delete Food  
    3. View Menu  
    4. View Orders  
    5. View Order History  
    6. View Users  
    7. Exit
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
        print("Good bye")
        return logout()
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
        view_menu()
    elif choice == "2":
        place_order()
    elif choice == "3":
        my_orders()
    elif choice == "4":
        cancel_order()
    elif choice == "5":
        print("Good bye")
        return logout()
    else:
        print("Invalid choice")
        return user_menu()

    return user_menu()


if __name__ == '__main__':
    logout()
    auth_menu()






