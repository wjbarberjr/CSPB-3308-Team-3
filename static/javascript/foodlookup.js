$(document).ready(function() {
    $("#foodName").on("input", function() {
        var query = $(this).val();
        
        if(query.length >= 3) {
            var baseURL = "https://coding.csel.io/user/wihi1131/proxy/3308";
            $.get(baseURL + "/search_food", {query: query}, function(data) {
                var suggestions = JSON.parse(data);

                var suggestionList = $("#suggestions");
                suggestionList.empty();

                suggestions.forEach(function(food) {
                    suggestionList.append("<li>" + food + "</li>");
                });
            });
        }
    });

    $("#suggestions").on("click", "li", function() {
        $("#foodName").val($(this).text());
        $("#suggestions").empty();
    });
    
    $("#food-form").submit(function(event) {
        event.preventDefault();

        var formData = {
            name: $("#newFoodName").val(),
            portion_size: $("#portionSize").val(),
            calories: $("#calories").val(),
            total_fat: $("#totalFat").val(),
            saturated_fat: $("#saturatedFat").val(),
            trans_fat: $("#transFat").val(),
            cholesterol: $("#cholesterol").val(),
            sodium: $("#sodium").val(),
            total_carbohydrates: $("#totalCarbohydrates").val(),
            dietary_fiber: $("#dietaryFiber").val(),
            sugars: $("#sugars").val(),
            protein: $("#protein").val(),
            vitamin_d: $("#vitaminD").val(),
            calcium: $("#calcium").val(),
            iron: $("#iron").val(),
            potassium: $("#potassium").val()
    };

        $.post("/add_food", formData, function(response) {
            alert(response.message);
        });
    });
});