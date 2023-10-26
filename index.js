const full_table = document.getElementById('output_table');
let total_cals = 0;
let total_fat = 0;
let total_protein = 0;
let total_carbs = 0;


function add_to_table() {
    /* get calories value and add to total_cals  */ 
    const calories = Number(document.getElementById("calories").value);
    total_cals += calories;

    /* get fat value and add to total_fats  */
    const fats = Number(document.getElementById("fat").value);
    total_fat += fats;

    /* get protein value and add to total_protein  */
    const proteins = Number(document.getElementById("protein").value);
    total_protein += proteins;

    /* get carbs value and add to total_carbs  */
    const carbs = Number(document.getElementById("carbs").value);
    total_carbs += carbs;

     



    /* create a new row of curr inputs that will be added to the output_table */
    const curr_row = document.createElement('tr');

    /** create column for food input */
    const food = document.getElementById("food_input").value;
    const food_input = document.createElement('td')
    food_input.innerText = food
    curr_row.appendChild(food_input)

    /* create column values for cals and macros */
    /* curr calories  */
    const calories_consumed = document.createElement('td')
    calories_consumed.innerText = calories;
    curr_row.appendChild(calories_consumed);

    /* curr fats  */
    const fats_consumed = document.createElement('td')
    fats_consumed.innerText = fats;
    curr_row.appendChild(fats_consumed);

    /* curr proteinss  */
    const proteins_consumed = document.createElement('td')
    proteins_consumed.innerText = proteins;
    curr_row.appendChild(proteins_consumed);

    /* curr carbs  */
    const carbs_consumed = document.createElement('td')
    carbs_consumed.innerText = carbs;
    curr_row.appendChild(carbs_consumed);

    

    full_table.appendChild(curr_row);
}

/* update running total row of output_table 
const total_row = document.getElementById("total_row");
total_row.cells[1].innerText = total_cals;
total_row.cells[2].innerText = total_fats;
total_row.cells[3].innerText = total_protein;
total_row.cells[4].innerText = total_carbs;*/

function clear_table() {
    document.querySelectorAll('#output_table > tr:not(:first-child)').forEach(child => child.remove());
    total = 0;
}