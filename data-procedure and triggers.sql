DELIMITER //
create procedure cust_ins(IN id VARCHAR(12), IN cus_name VARCHAR(50))
BEGIN
DECLARE foundcount INT;
SELECT count(*) INTO foundcount FROM dbms.customer WHERE cust_id=id;
IF foundcount=0 THEN 
INSERT INTO dbms.customer VALUES(id, cus_name);
END IF;
END 
// DELIMITER ;

CALL cust_ins('123456789123','Mohammed Thavaf')

DELIMITER //
create trigger cust_ins before insert on dbms.book
for each row 
BEGIN
call cust_ins(new.cust_id,new.cust_name);
END 
// DELIMITER ;
