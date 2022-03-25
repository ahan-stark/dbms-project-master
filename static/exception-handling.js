function validateForm() {
  let aadharno = document.forms["bookroom"]["cust_id"].value;
  let customer_name = document.forms["bookroom"]["cust_name"].value;
  let bookin_date = document.forms["bookroom"]["add_date"].value;
  if (aadharno == "") {
    alert("enter valid aadhar number!");
    return false;
  } else if (aadharno.length != 12) {
    alert("enter valid aadhar number!");
    return false;
  }
  if (customer_name == "") {
    alert("enter name!");
    return false;
  }
  if (bookin_date == "") {
    alert("choose the booking date!");
    return false;
  }
}

function validateinsrooms() {
  let roomid = document.forms["insert_rooms"]["room_id"].value;
  let roomcost = document.forms["insert_rooms"]["cost_room"].value;
  if (roomid == "") {
    alert("enter room id!");
    return false;
  }
  if (roomcost == "") {
    alert("enter room cost!");
    return false;
  }
}
function checkdate() {
  let entered_date = document.forms["check-date"]["chosendate"].value;
  if (entered_date == "") {
    alert("choose a date");
    return false;
  }
}
function insertfood() {
  let food_id = document.forms["insert-food"]["food_id"].value;
  if (food_id == "") {
    alert("enter food id");
    return false;
  }
  let food_name = document.forms["insert-food"]["food_name"].value;
  if (food_name == "") {
    alert("enter food name");
    return false;
  }
  let food_cost = document.forms["insert-food"]["food_price"].value;
  if (food_cost == "") {
    alert("enter food cost");
    return false;
  }
}
function checkid() {
  let aadharnumber = document.forms["aadhar-no"]["cust_id"].value;
  if (aadharnumber == "") {
    alert("enter valid aadhar number!");
    return false;
  } else if (aadharnumber.length != 12) {
    alert("enter valid aadhar number!");
    return false;
  }
}
