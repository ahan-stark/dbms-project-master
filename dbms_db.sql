USE dbms;
CREATE TABLE rooms(room_no INT(4),room_cost INT(5));
CREATE TABLE book(booked_room INT,booking_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,cust_id VARCHAR(12) FOREIGN KEY REFERENCES customer(cust_id),cust_name VARCHAR(50),booked_date DATE PRIMARY KEY(cust_id));
CREATE TABLE food(food_id INT(5),food_name VARCHAR(50),food_timing VARCHAR(20),food_price int(5));
CREATE TABLE food_book(food_name VARCHAR(50),cust_id VARCHAR(12) FOREIGN KEY REFERENCES customer(cust_id),price INT(4),quantity INT(4),totalamt INT(5));
CREATE TABLE customer(cust_id VARCHAR(12) PRIMARY KEY NOT NULL,cust_name VARCHAR(50));