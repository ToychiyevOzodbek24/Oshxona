<<<<<<< HEAD
from views import register, login
from user_views import *
=======
from views import register, login, logout, show_all_users
from admin_views import *
>>>>>>> 108ff929a87863981becdd3b164dd06b8cc2949a


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
        add_food()
    elif choice == "2":
        delete_food()
    elif choice == "3":
        view_menu()
    elif choice == "4":
        view_orders()
    elif choice == "5":
        view_order_histore()
    elif choice == "6":
        show_all_users()
    elif choice == "7":
        print("Good bye")
        return logout()
    else:
        print("Invalid choice")
    return admin_menu()


def user_menu():
    print("""
    1. View Menu  
    2. Place Order  
    3. My Orders  
    4. Cancel Order  
    5. Exit

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
