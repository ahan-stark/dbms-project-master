CREATE DATABASE dbms;
USE dbms;

CREATE TABLE `customer` (
  `cust_id` varchar(12) NOT NULL,
  `cust_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`cust_id`)
);

CREATE TABLE `rooms` (
  `room_no` int DEFAULT NULL,
  `room_cost` int DEFAULT NULL
);

CREATE TABLE `food` (
  `food_id` int DEFAULT NULL,
  `food_name` varchar(50) DEFAULT NULL,
  `food_timing` varchar(20) DEFAULT NULL,
  `food_price` int DEFAULT NULL
);

CREATE TABLE `book` (
  `booked_room` int DEFAULT NULL,
  `booking_id` int NOT NULL AUTO_INCREMENT,
  `cust_id` varchar(12) DEFAULT NULL,
  `cust_name` varchar(50) DEFAULT NULL,
  `booked_date` date DEFAULT NULL,
  `room_cost` int DEFAULT NULL,
  PRIMARY KEY (`booking_id`)
);

CREATE TABLE `food_book` (
  `food_name` varchar(50) DEFAULT NULL,
  `cust_id` varchar(12) DEFAULT NULL,
  `price` int DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  `totalamt` int DEFAULT NULL
);

