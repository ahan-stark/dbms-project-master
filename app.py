from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

cnx = mysql.connector.connect(
    user="root", password="1234", host="localhost", database="dbms"
)
cursor = cnx.cursor()
app = Flask(__name__)


@app.route("/rooms", methods=["POST"])
def save_rooms():
    room_id = request.form.get("room_id")
    cost_room = request.form.get("cost_room")
    query = "INSERT INTO rooms VALUES({}, {})".format(room_id, cost_room)
    cursor.execute(query)
    cnx.commit()
    return redirect(url_for("get_rooms"))


@app.route("/rooms/insert")
def get_rooms():
    return render_template("index.html")


@app.route("/rooms/display")
def dis_rooms():
    rooms = []
    query = "SELECT room_no,room_cost FROM rooms "
    cursor.execute(query)
    for (room_no, room_cost) in cursor:
        room = {"num": room_no, "cost": room_cost}
        rooms.append(room)
    print(rooms)
    return render_template("dis_room.html", disprooms=rooms)


@app.route("/book/<num>/<cost>/<chosendate>", methods=["GET", "POST"])
def book(num, cost, chosendate):
    # logic to insert booking details to booking table
    # query = "insert into book values({})".format(num)
    # cursor.execute(query)
    # cnx.commit()
    return render_template("add_name.html", id=num, cost=cost, date=chosendate)


@app.route("/add_name", methods=["POST"])
def booking():
    # logic to insert booking details to booking table
    room_id = request.form.get('room_id')
    cust_id = request.form.get('cust_id')
    cust_name = request.form.get('cust_name')
    book_date = request.form.get('add_date')
    room_cost = request.form.get('room_cost')

    query = "INSERT INTO book (booked_room,cust_id,cust_name,booked_date,room_cost) VALUES({},'{}','{}','{}',{})".format(
        room_id, cust_id, cust_name, book_date, room_cost)
    cursor.execute(query)
    cnx.commit()
    return render_template("success.html")


@app.route("/sort")
def sort_rooms():
    rooms = []
    query = "SELECT room_no,room_cost FROM rooms ORDER BY room_cost;"
    cursor.execute(query)
    for (room_no, room_cost) in cursor:
        room = {"num": room_no, "cost": room_cost}
        rooms.append(room)
    return render_template("dis_room.html", disprooms=rooms)


@app.route('/')
def start_page():
    return render_template("welcome.html")


@app.route('/inpdate')
def inpdate():
    return render_template("input-date.html")


@app.route('/getdate', methods=["POST"])
def get_date():
    particulardate = request.form.get('chosendate')
    query = "SELECT *  FROM rooms WHERE room_no NOT IN (SELECT booked_room FROM book WHERE booked_date='{}');".format(
        particulardate)
    cursor.execute(query)
    dis = []
    for (booked_room, cust_name) in cursor:
        room = {"num": booked_room, "cost": cust_name}
        dis.append(room)
    return render_template("book-rooms.html", disprooms=dis, chosendate=particulardate)


@app.route("/takefood")
def dis_food():
    return render_template("ins_food.html")


@app.route("/ins_food", methods=['POST'])
def ins_food():
    food_id = request.form.get('food_id')
    food_name = request.form.get('food_name')
    food_time = request.form.get('food_time')
    food_price = request.form.get('food_price')
    query = "INSERT INTO food VALUES ({},'{}','{}',{})".format(
        food_id, food_name, food_time, food_price)
    cursor.execute(query)
    cnx.commit()
    return render_template("success.html")


@app.route("/food_menu", methods=['GET'])
def food_menu():
    menu = []
    query = "SELECT food_id,food_name,food_timing,food_price FROM food"
    cursor.execute(query)
    for(food_id, food_name, food_timing, food_price) in cursor:
        food = {"id": food_id, "name": food_name,
                "timing": food_timing, "price": food_price}
        menu.append(food)
    print(menu)
    return render_template("dis_food.html", foodmenu=menu)


@app.route("/book_food/<name>/<cost>", methods=["GET", "POST"])
def book_food(name, cost):
    return render_template("book_food.html", food_name=name, food_cost=cost)


@app.route("/foodbook_details", methods=["POST"])
def bookfood_details():
    food_name = request.form.get("food_name")
    customer_id = request.form.get("customer_id")
    food_price = request.form.get("food_price")
    quantity = request.form.get("quantity")
    total_amount = request.form.get("total_amount")
    query = "INSERT INTO food_book VALUES ('{}','{}',{},{},{})".format(
        food_name, customer_id, food_price, quantity, total_amount)
    cursor.execute(query)
    cnx.commit()
    return render_template("success.html")


@app.route("/getcustid_finalprice")
def check_finalprice():
    return render_template("cust_id-forfinalbilling.html")


@app.route("/calculate_fianlamt", methods=["POST"])
def cal_finalamt():
    price_food = []
    cust_id = request.form.get("cust_id")
    query = "select food_name,totalamt from food_book where cust_id ='{}'".format(
        cust_id)
    cursor.execute(query)
    for(food_name, totalamt) in cursor:
        a = {"name": food_name, "amt": totalamt}
        price_food.append(a)
    price_room = []
    query1 = "select booked_room,cust_name,booked_date,room_cost from book where cust_id ='{}'".format(
        cust_id)
    cursor.execute(query1)
    for(booked_room, cust_name, booked_date, room_cost) in cursor:
        b = {"room_id": booked_room, "name": cust_name,
             "date": booked_date, "cost": room_cost}
        price_room.append(b)
    return render_template("final-amount.html", totalbilling_food=price_food, totalbilling_room=price_room)


@app.route('/about')
def about():
    return render_template('about.html')
