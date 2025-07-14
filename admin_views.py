from file_manager import read, writerows, append
from utils import get_next_id
import threading
import time

def add_food():
    name = input("Taom nomi: ")
    price = input("Narxi: ")
    food = [str(get_next_id("menu")), name, price, "5"]
    append("menu", food)
    print("Ovqat qo'shildi.")

def delete_food():
    menu = read("menu")
    food_id = input("O'chirmoqchi bo'lgan taom ID: ")
    
    new_menu = []
    for row in menu:
        if row[0] != food_id:
            new_menu.append(row)
    writerows("menu", new_menu)
    print("Taom o'chirildi.")

def view_menu():
    menu = read("menu")
    for row in menu:
        print(f"{row[0]}. {row[1]} - {row[2]} so'm")

def view_orders():
    orders = read("orders")
    for row in orders:
        if row[3] == "pending":
            print(f"{row[0]}. {row[1]} - {row[2]} x{row[4]} ({row[5]})")

def view_order_histore():
    orders = read("orders")
    for row in orders:
        if row[3] in ["ready", "cancelled"]:
            print(f"{row[0]}. {row[1]} - {row[2]} x{row[4]} - {row[3]} ({row[5]})")

def show_all_users():
    users = read("users")
    for user in users:
        print(f"{user[0]}. {user[1]} - {user[2]}")

def process_orders():
    orders = read("orders")
    pending = []
    for order in orders:
        if order[3] == "pending":
            pending.append(order)

    def prepare(order):
        time.sleep(5 * int(order[4]))
        for row in orders:
            if row[0] == order[0]:
                row[3] = "ready"
        writerows("orders", orders)
        print(f"{order[2]} x{order[4]} tayyor bo'ldi")

    threads = []
    for order in pending:
        t = threading.Thread(target=prepare, args=(order,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("Barcha buyurtmalar tayyor.")
