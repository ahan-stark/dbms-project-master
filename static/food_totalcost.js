let food_cost=document.getElementById("food-cost");
let food_quantity=document.getElementById("food-quantity");
let btn=document.getElementById("check-total");
let total_cost=document.getElementById("total");
btn.addEventListener("click", function (){
    let total=food_cost.value*food_quantity.value;
    total_cost.value=total;
});

