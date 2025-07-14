from file_manager import read, writerows, append
from utils import get_next_id
from datetime import datetime


def view_menu():
    menu = read("menu")
    for row in menu:
        print(f"{row[0]}. {row[1]} - {row[2]} so‘m")


def place_order():
    view_menu()

    name = None

    reader = read(filename="users")
    for row in reader:
        if row[-2] == "True":
            name = row[2]
            break
    food_id = input("Taom ID: ")
    amount = input("Nechta buyurtma: ")

    menu = read("menu")
    food = next((x for x in menu if x[0] == food_id), None)
    if not food:
        print("Taom topilmadi.")
        return

    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    order = [str(get_next_id("orders")), name, food[1], "pending", amount, time_now]
    append("orders", order)
    print("Buyurtma qabul qilindi.")


def my_orders():
    name = None

    reader = read(filename="users")
    for row in reader:
        if row[-2] == "True":
            name = row[2]
            break
    orders = read("orders")
    for row in orders:
        if row[1] == name:
            print(f"{row[0]}. {row[2]} - {row[3]} x{row[4]} ({row[5]})")


def cancel_order():
    name = None

    reader = read(filename="users")
    for row in reader:
        if row[-2] == "True":
            name = row[2]
            break

    canceled = read(filename="orders")
    for row in canceled:
        if row[3] == "pending":
            print(f"{row[0]}. {row[2]} - {row[3]} x{row[4]} ({row[5]})")

    order_id = input("Buyurtma ID: ")
    orders = read("orders")
    for row in orders:
        if row[0] == order_id and row[1] == name and row[3] == "pending":
            row[3] = "cancelled"
            writerows("orders", orders)
            print("Buyurtma bekor qilindi.")
            return
    print("Bekor qilib bo‘lmadi.")


def today_orders():
    name = None

    reader = read(filename="users")
    for row in reader:
        if row[-2] == "True":
            name = row[2]
            break

    today = datetime.now().strftime("%Y-%m-%d")
    orders = read("orders")
    found = False
    for row in orders:
        if row[1] == name and row[5].startswith(today):
            print(f"{row[0]}. {row[2]} - {row[3]} x{row[4]} ({row[5]})")
            found = True
    if not found:
        print("Bugungi buyurtmalaringiz yo‘q.")
