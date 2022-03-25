let finalplace = document.getElementById("finalamt");
let food_amt = document.getElementsByClassName("food-amt");
let room_cost = document.getElementsByClassName("room-cost");
let food_sum = 0;
let room_sum = 0;
for (let i = 0; i < food_amt.length; i++) {
  food_sum = food_sum + parseInt(food_amt[i].value);
}
for (let i = 0; i < room_cost.length; i++) {
  room_sum = room_sum + parseInt(room_cost[i].value);
}
let finalamt = food_sum + room_sum;
finalplace.value = finalamt;
