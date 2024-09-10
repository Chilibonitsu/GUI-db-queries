import re
import tkinter as tk
from tkinter import *
from tkinter import ttk, RIGHT, BOTTOM, VERTICAL, W, CENTER, END, LEFT, NW
from tkinter import messagebox
from connect import get_connection

def sales_out():
    global root

    root.destroy()
    root = tk.Tk()

    theme()

    parameters_of_window()

    cur.execute("select * from discount;")

    sales = cur.fetchall()

    # print(sales)

    tree = ttk.Treeview(root)
    tree['columns'] = ("ID", "SALE")
    tree.column("#0", width=0)
    tree.column("ID", anchor=W, width=160)
    tree.column("SALE", anchor=CENTER, width=160)

    tree.heading("#0", text="", anchor=W)
    tree.heading("ID", text="ID", anchor=W)
    tree.heading("SALE", text="SALE", anchor=CENTER)

    for k in sales:
        tree.insert(parent='', index=END, text="", values=k)
    # tree.grid_location(100,100)
    tree.grid(row=1, column=0, padx=100)

    ttk.Button(text="Назад", command=back).grid(column=0, row=0, pady=15)

    fsale = tk.Entry(text="Enter name", font=("Comic Sans MS", 12))
    lname = tk.Label(text="Ввод", bg="#228B22", font=("Comic Sans MS", 12))

    # sale = fsale.get()

    ent = tk.Button(text="Добавить скидку", bg="#228B22", command=lambda: sales_add(fsale))

    # sales_add(sale)

    ent.grid(row=4, pady=5)
    fsale.grid(row=3, pady=0)
    lname.grid(row=2, pady=5)


# print(cur.fetchall())

def sales_add(fsale):
    try:
        sale = fsale.get()

        query_string = 'INSERT INTO discount (disc) VALUES (%s);'
        params = (sale,)
        cur.execute(query_string, params)
        conn.commit()
        # print(sale)
        # print("asdasdasd")
        sales_out()
    except(Exception):
        print("err inserting sale")
        conn.commit()


def manufacturers_out():
    global root

    root.destroy()
    root = tk.Tk()

    theme()

    parameters_of_window()

    frm = ttk.Frame(root, padding=10)
    frm.grid()

    cur.execute("select * from manufacturers;")
    manufacturers = cur.fetchall()
 
    tree = ttk.Treeview(root)
    tree['columns'] = ("ID", "TYPE", "COUNTRY", "YEAR")
    tree.column("#0", width=0)
    tree.column("ID", anchor=W, width=160)
    tree.column("TYPE", anchor=CENTER, width=160)
    tree.column("COUNTRY", anchor=CENTER, width=160)
    tree.column("YEAR", anchor=NW, width=160)

    tree.heading("#0", text="", anchor=W)
    tree.heading("ID", text="ID", anchor=W)
    tree.heading("TYPE", text="Manufacturer", anchor=CENTER)
    tree.heading("COUNTRY", text="Country", anchor=CENTER)
    tree.heading("YEAR", text="Year", anchor=NW)

    for k in manufacturers:
        tree.insert(parent='', index=END, text="", values=k)
    # tree.grid_location(100,100)
    # tree.move('4','0', '0')
    tree.grid(row=2, column=0, padx=50, pady=50)

    ttk.Button(frm, text="Назад", command=back).grid(column=2, row=0)


def types_out():
    global root

    root.destroy()
    root = tk.Tk()

    theme()

    parameters_of_window()

    frm = ttk.Frame(root, padding=10)
    frm.grid()

    cur.execute("select * from types_of_wear;")
    types = cur.fetchall()
 
    tree = ttk.Treeview(root)

    tree['columns'] = ("ID", "TYPE")
    tree.column("#0", width=0)
    tree.column("ID", anchor=W, width=160)
    tree.column("TYPE", anchor=CENTER, width=160)

    tree.heading("#0", text="", anchor=W)
    tree.heading("ID", text="ID", anchor=W)
    tree.heading("TYPE", text="Type Of Wear", anchor=CENTER)

    for k in types:
        tree.insert(parent='', index=END, text="", values=k)

    tree.grid(row=2, column=0, padx=50, pady=50)

    ttk.Button(frm, text="Назад", command=back).grid(column=2, row=0)


def forms_out():
    global root

    root.destroy()
    root = tk.Tk()

    theme()

    parameters_of_window()

    frm = ttk.Frame(root, padding=10)
    frm.grid()

    cur.execute("""select form_of_wear.id_form, form_of_wear.name_of_form, types_of_wear.type_of_wear, types_of_wear.id_type_of_wear
                from form_of_wear
                join types_of_wear
                on types_of_wear.id_type_of_wear = form_of_wear.form_code;
                """)

    types = cur.fetchall()

    tree = ttk.Treeview(root)

    tree['columns'] = ("ID", "FORM", "TYPE", "ID_TYPE")
    tree.column("#0", width=0)
    tree.column("ID", anchor=W, width=160)
    tree.column("FORM", anchor=CENTER, width=160)
    tree.column("TYPE", anchor=CENTER, width=160)
    tree.column("ID_TYPE", anchor=CENTER, width=160)

    tree.heading("#0", text="", anchor=W)
    tree.heading("ID", text="ID_FORM", anchor=W)
    tree.heading("FORM", text="Form Of Wear", anchor=CENTER)
    tree.heading("TYPE", text="Type Of Wear", anchor=CENTER)
    tree.heading("ID_TYPE", text="ID_TYPE", anchor=CENTER)

    for k in types:
        tree.insert(parent='', index=END, text="", values=k)

    tree.grid(row=2, column=0, padx=50, pady=50)

    ttk.Button(frm, text="Назад", command=back).grid(column=2, row=0)


def customers_out():
    global root
    root.destroy()
    root = tk.Tk()

    theme()

    parameters_of_window()

    frm = ttk.Frame(root, padding=10)
    frm.grid()

    cur.execute("""select customers.id_man, customers.name_of_man, discount.disc, customers.discount
                    from customers, discount
                    WHERE customers.discount = discount.id_disc;
                    """)

    types = cur.fetchall()
   
    tree = ttk.Treeview(root)

    tree['columns'] = ("ID", "FIO", "SALE", "SALE_CODE")
    tree.column("#0", width=0)
    tree.column("ID", anchor=W, width=160)
    tree.column("FIO", anchor=CENTER, width=160)
    tree.column("SALE", anchor=CENTER, width=160)
    tree.column("SALE_CODE", anchor=CENTER, width=160)

    tree.heading("#0", text="", anchor=W)
    tree.heading("ID", text="ID_CUSTOMER", anchor=W)
    tree.heading("FIO", text="FIO", anchor=CENTER)
    tree.heading("SALE", text="SALE", anchor=CENTER)
    tree.heading("SALE_CODE", text="SALE_CODE", anchor=CENTER)

    for k in types:
        tree.insert(parent='', index=END, text="", values=k)

    tree.grid(row=2, column=0, padx=50, pady=50)

    ttk.Button(frm, text="Назад", command=back).grid(column=2, row=0)


def goods_out():
    global root
    root.destroy()
    root = tk.Tk()

    theme()
    parameters_of_window()

    frm = ttk.Frame(root, padding=10)
    frm.grid()

    cur.execute("""Select goods.id_good, goods.name_of_wear, goods.cost_of_wear, manufacturers.country, t.type_of_wear, f.name_of_form
                    From ((goods 
                    INNER join manufacturers on goods.country = manufacturers.id_man)
                    INNER join form_of_wear f on f.id_form = goods.form_of_wear)
                    INNER join types_of_wear t on t.id_type_of_wear = f.form_code;
                        """)

    types = cur.fetchall()
  
    tree = ttk.Treeview(root)

    tree['columns'] = ("ID_GOOD", "WEAR NAME", "COST", "COUNTRY", "TYPE", "FORM")
    tree.column("#0", width=0)
    tree.column("ID_GOOD", anchor=W, width=80)
    tree.column("WEAR NAME", anchor=W, width=220)
    tree.column("COST", anchor=W, width=160)
    tree.column("COUNTRY", anchor=W, width=160)
    tree.column("TYPE", anchor=W, width=160)
    tree.column("FORM", anchor=W, width=160)

    tree.heading("#0", text="", anchor=W)
    tree.heading("ID_GOOD", text="ID_GOOD", anchor=W)
    tree.heading("WEAR NAME", text="WEAR NAME", anchor=W)
    tree.heading("COST", text="COST", anchor=W)
    tree.heading("COUNTRY", text="COUNTRY", anchor=W)
    tree.heading("TYPE", text="TYPE", anchor=W)
    tree.heading("FORM", text="FORM", anchor=W)

    for k in types:
        tree.insert(parent='', index=END, text="", values=k)

    tree.grid(row=1, column=0, padx=50, pady=50)

    ttk.Button(frm, text="Назад", command=back).grid(column=2, row=0)


def out_orders():
    global root
    root.destroy()
    root = tk.Tk()

    theme()

    parameters_of_window()

    cur.execute("""
                    Select orders.id_order, customers.name_of_man, goods.cost_of_wear, discount.disc, goods.name_of_wear, manufacturers.name_of_man, manufacturers.country, form_of_wear.name_of_form, types_of_wear.type_of_wear
                    From (((((orders 
                    Inner join customers on customers.id_man = orders.name_of_customer)
                    Inner join discount on customers.discount = discount.id_disc)
                    Inner join goods on orders.name_of_good = goods.id_good)
                    Inner join manufacturers on goods.country = manufacturers.id_man)
                    Inner join form_of_wear on goods.form_of_wear = form_of_wear.id_form)
                    Inner join types_of_wear on form_of_wear.form_code= types_of_wear.id_type_of_wear;
        


                        """)

    types = cur.fetchall()
  
    tree = ttk.Treeview(root)

    tree['columns'] = ("ID_ORDER", "CUSTOMER NAME", "COST", "SALE", "GOOD NAME", "MANUFACTURER", "COUNTRY", "FORM")
    tree.column("#0", width=0)
    tree.column("ID_ORDER", anchor=W, width=80)
    tree.column("CUSTOMER NAME", anchor=W, width=220)
    tree.column("COST", anchor=W, width=80)
    tree.column("SALE", anchor=W, width=40)
    tree.column("GOOD NAME", anchor=W, width=260)
    tree.column("MANUFACTURER", anchor=W, width=140)
    tree.column("COUNTRY", anchor=W, width=100)
    tree.column("FORM", anchor=W, width=220)
    #tree.column("TYPE", anchor=W, width=160)

    tree.heading("#0", text="", anchor=W)
    tree.heading("ID_ORDER", text="ID_ORDER", anchor=W)
    tree.heading("CUSTOMER NAME", text="CUSTOMER NAME", anchor=W)
    tree.heading("COST", text="COST", anchor=W)
    tree.heading("SALE", text="SALE", anchor=W)
    tree.heading("GOOD NAME", text="GOOD NAME", anchor=W)
    tree.heading("MANUFACTURER", text="MANUFACTURER", anchor=W)
    tree.heading("COUNTRY", text="COUNTRY", anchor=W)
    tree.heading("FORM", text="FORM", anchor=W)
    #tree.heading("TYPE", text="TYPE", anchor=W)

    for k in types:
        tree.insert(parent='', index=END, text="", values=k)

    tree.grid(row=1, column=1, pady=20, padx=15,  columnspan=17)

    ttk.Button(text="Назад", command=back).grid(column=2, row=5, padx=40, pady=10)


    hard_query()


def hard_query():
    fcust = tk.Entry(width=20)
    fcost = tk.Entry()
    fsale = tk.Entry()
    fgood = tk.Entry()
    fman = tk.Entry()
    fcountry = tk.Entry()
    ftype = tk.Entry()
    lcust = tk.Label(text="Покупатель", font=("Dubai Light", 12))
    lcost = tk.Label(text="Цена", font=("Dubai Light", 12))
    lsale = tk.Label(text="Скидка", font=("Dubai Light", 12))
    lgood = tk.Label(text="Товар", font=("Dubai Light", 12))
    lman = tk.Label(text="Производитель", font=("Dubai Light", 12))
    lcountry = tk.Label(text="Страна", font=("Dubai Light", 12))
    lftype= tk.Label(text="Вид одежды", font=("Dubai Light", 12))
    # lname = tk.Label(text="Ввод", bg="#228B22", font=("Comic Sans MS", 12))

    # sale = fsale.get()

    # ent = tk.Button(text="Добавить скидку", bg="#228B22", command=lambda:sales_add(fsale))

    # sales_add(sale)


    lcust.grid(row=2, column=2)
    lcost.grid(row=2, column=3)
    lsale.grid(row=2, column=4)
    lgood.grid(row=2, column=5)
    lman .grid(row=2, column=6)
    lcountry.grid(row=2, column=7)
    lftype.grid(row=2, column=8)


    fcust.grid(row=3, column=2)
    fcost.grid(row=3, column=3)
    fsale.grid(row=3, column=4)
    fgood.grid(row=3, column=5)
    fman.grid(row=3, column=6)
    fcountry.grid(row=3, column=7)
    ftype.grid(row=3, column=8)

    ent = ttk.Button(text="Запрос",  command=lambda: que(fcust, fcost, fsale, fgood, fman, fcountry, ftype)).grid(row=4,column=2, pady=20)

    ent.grid(row=4, pady=40)
    # fsale.grid(row=3, pady=0)
    # lname.grid(row=2, pady=5)


def que(fcust, fcost, fsale, fgood, fman, fcountry, ftype):

    cust = fcust.get()
    cost = fcost.get()
    sale = fsale.get()
    good = fgood.get()
    man = fman.get()
    country = fcountry.get()
    type = ftype.get()

    query = []
    params = []

    if cust:
        query.append('customers.name_of_man = %s')
        params.append(cust)
   

    if cost:
        if is_numeric(cost):
            query.append('goods.cost_of_wear = %s')
            params.append(float(cost))
        else:
            var = is_valid_condition(cost) #возвращает кортеж с условием и значением
            if var:
                query.append(f'goods.cost_of_wear {var[0]} %s')
                params.append(var[1])
            else:
                messagebox.showerror("Ошибка", "Неверный формат данных")
               
                return

    if sale:
        if is_numeric(sale):
            query.append('discount.disc = %s')
            params.append(float(sale))
        else:
            var = is_valid_condition(sale)
            if var:
                query.append(f'discount.disc {var[0]} %s')
                params.append(var[1])
            else:
                messagebox.showerror("Ошибка", "Цена и скидка должны быть числами, перед числом может быть знак сравнения. Пример: >50, <50, >=50")
                return
     

    if good:
        query.append('goods.name_of_wear = %s')
        params.append(good)
  

    if man:
        query.append('manufacturers.name_of_man = %s')
        params.append(man)
    

    if country:
        query.append('manufacturers.country = %s')
        params.append(country)
   

    if type:
        query.append('form_of_wear.name_of_form = %s')
        params.append(type)
  

    if query:
        query_string = ' AND '.join(query)
    else:
        query_string = '1=1'  # Заглушка, если нет условий

    print(query_string)

    que_out(query_string, params)

def is_numeric(value):
    try:
        float(value)  # Проверка, можно ли преобразовать в число
        return True
    except ValueError:
        return False
    
def is_valid_condition(value):
    # Регулярное выражение для проверки оператора и числа
    pattern = r'^\s*(>=|<=|>|<|=|!=)\s*(\d+)\s*$'
    match = re.match(pattern, value)
    
    if match:
        operator, number = match.groups()
        number = float(number)
        # Проверка, что число в диапазоне от 1 до 100
        
        return operator, number
    return False


def que_out(query, params):
    global root
    root.destroy()
    root = tk.Tk()

    theme()

    parameters_of_window()

 

    query_string = f'''
        Select orders.id_order, customers.name_of_man, goods.cost_of_wear, discount.disc, goods.name_of_wear, manufacturers.name_of_man, manufacturers.country, form_of_wear.name_of_form, types_of_wear.type_of_wear
        From ((((((orders 
        Inner join customers on customers.id_man = orders.name_of_customer)
        Inner join discount on customers.discount = discount.id_disc)
        Inner join goods on orders.name_of_good = goods.id_good)
        Inner join manufacturers on goods.country = manufacturers.id_man)
        Inner join form_of_wear on goods.form_of_wear = form_of_wear.id_form)
        Inner join types_of_wear on form_of_wear.form_code= types_of_wear.id_type_of_wear)
        WHERE {query}
    '''
    cur.execute(query_string, params)
    types = cur.fetchall()
   
    tree = ttk.Treeview(root)

    tree['columns'] = ("ID_ORDER", "CUSTOMER NAME", "COST", "SALE", "GOOD NAME", "MANUFACTURER", "COUNTRY", "FORM")
    tree.column("#0", width=0)
    tree.column("ID_ORDER", anchor=W, width=80)
    tree.column("CUSTOMER NAME", anchor=W, width=220)
    tree.column("COST", anchor=W, width=80)
    tree.column("SALE", anchor=W, width=40)
    tree.column("GOOD NAME", anchor=W, width=260)
    tree.column("MANUFACTURER", anchor=W, width=140)
    tree.column("COUNTRY", anchor=W, width=100)
    tree.column("FORM", anchor=W, width=220)
    #tree.column("TYPE", anchor=W, width=160)

    tree.heading("#0", text="", anchor=W)
    tree.heading("ID_ORDER", text="ID_ORDER", anchor=W)
    tree.heading("CUSTOMER NAME", text="CUSTOMER NAME", anchor=W)
    tree.heading("COST", text="COST", anchor=W)
    tree.heading("SALE", text="SALE", anchor=W)
    tree.heading("GOOD NAME", text="GOOD NAME", anchor=W)
    tree.heading("MANUFACTURER", text="MANUFACTURER", anchor=W)
    tree.heading("COUNTRY", text="COUNTRY", anchor=W)
    tree.heading("FORM", text="FORM", anchor=W)

    for k in types:
        tree.insert(parent='', index=END, text="", values=k)

    tree.grid(row=1, column=1, pady=20, padx=15,  columnspan=17)

    ttk.Button(text="Назад", command=back).grid(column=2, row=5, padx=40, pady=10)

    hard_query()


def back():
    root.destroy()
    interface()


def theme():
    root.tk.call("source", "azure.tcl")
    root.tk.call("set_theme", "dark")


def parameters_of_window():
    root.geometry('1400x600+250+200')


def gif(root):
    frameCnt = 12
    frames = [PhotoImage(file='STRd.gif', format='gif -index %i' % (i)) for i in range(frameCnt)]

    def update(ind):
        frame = frames[ind]
        ind += 1
        if ind == frameCnt:
            ind = 0
        root.label.configure(image=frame)
        root.after(100, update, ind)
        label = Label(root)
        label = Label(root, bg="white")
        label.place(x=300, y=300)
        label.after(0, update, 0)


def interface():
    global root, canvas

    root = tk.Tk()

    root.tk.call("source", "azure.tcl")
    root.tk.call("set_theme", "dark")

    parameters_of_window()

    frm = ttk.Frame(root, padding=150)

    # gif(root)

    frm.grid()
    # ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
    ttk.Button(frm, text="Вывод таблиц скидок", command=sales_out).grid(column=1, row=0)
    ttk.Button(frm, text="Вывод производителей", command=manufacturers_out).grid(column=2, row=0)
    ttk.Button(frm, text="Вывод всех типов одежды", command=types_out).grid(column=3, row=0)
    ttk.Button(frm, text="Вывод одежды и их тип", command=forms_out).grid(column=4, row=0)
    ttk.Button(frm, text="Вывод покупателей", command=customers_out).grid(column=5, row=0)
    ttk.Button(frm, text="Вывод товаров", command=goods_out).grid(column=6, row=0)
    ttk.Button(frm, text="Вывод заказов", command=out_orders).grid(column=7, row=0)

    root.mainloop()


conn, cur = get_connection()

conn.set_client_encoding('UTF8')
cur = conn.cursor()

interface()

conn.close()
