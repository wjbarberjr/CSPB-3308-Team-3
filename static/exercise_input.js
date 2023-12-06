$(function(){
    var $select = $("reps");
    for (i = 1; i <= 25; i++){
        $select.append($('<option></option>').val(i).html(i))
    }
});

$(function(){
    var $select = $("sets");
    for (i = 1; i <= 10; i++){
        $select.append($('<option></option>').val(i).html(i))
    }
});