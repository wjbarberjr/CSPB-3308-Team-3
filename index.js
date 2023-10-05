const table = document.getElementById('output');
let total = 0;

function cal_out() {
    const calories = Number(document.getElementById("calories").value);
    total += calories;

    const new_row = document.createElement('tr');

    const calories_consumed = document.createElement('td')
    calories_consumed.innerText = total;
    new_row.appendChild(calories_consumed);

    const calories_entered = document.createElement('td')
    calories_entered.innerHTML = calories;
    new_row.appendChild(calories_entered)

    table.appendChild(new_row);
}

function clear_table() {
    document.querySelectorAll('#output > tr:not(:first-child)').forEach(child => child.remove());
    total = 0;
}