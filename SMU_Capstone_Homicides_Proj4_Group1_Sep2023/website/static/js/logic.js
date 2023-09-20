$(document).ready(function() {
    console.log("Page Loaded");

    $("#filter").click(function() {
        // alert("button clicked!");
        make_predictions();
    });
});


// call Flask API endpoint
function make_predictions() {
    var sex = $("#sex").val();
    var age = $("#age").val();
    var race = $("#race").val();
    var year = $("#year").val();
    var month = $("#month").val();
    var weekday = $("#weekday").val();
    var season = $("#season").val();
    var city = $("#city").val();
    var state = $("#state").val();
    var population = $("#population").val();


    // check if inputs are valid
    
    // create the payload
    var payload = {
        "sex": sex,
        "age": age,
        "race": race,
        "year": year,
        "month": month,
        "weekday": weekday,
        "season": season,
        "city": city,
        "state": state,
        "population": population,
    }    
    console.log(payload)
    
   
    
    // Perform a POST request to the query URL
    $.ajax({
        type: "POST",
        url: "/makePredictions",
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({ "data": payload }),
        success: function(response) { 
            // print it
            console.log(response);
            
            if (response["arrest"] > 0.5) {
                $("#output").text(`Arrest made with probability ${response["arrest"].toFixed(2)}`)
            }
            else {
                $("#output").text(`No arrest made with probability ${response["no_arrest"].toFixed(2)}`)
            }    
         
        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            alert("Status: " + textStatus);
            alert("Error: " + errorThrown);
        }
    });

}
