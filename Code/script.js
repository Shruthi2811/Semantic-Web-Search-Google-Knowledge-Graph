$("#search-button").click(function(){
	var keyword = $("#search-input").val();
    $("#label").empty();
    $("#result_space").empty();
    changeStyle();
	get_result(keyword);
});

var get_result = function(keyword) {
	$.ajax({
        type: "GET",
        contentType : 'application/json; charset=utf-8',
        dataType : 'json',
        url: "/search/"+keyword,
        success :function(result) {
            display_result(result);
        },
        error : function (status) {
            console.log("No result fetched");
        }
    });
}

var changeStyle = function() {
    $( "#label" ).append( "<h3>Semantic Search</h3>" );
    $( "h3" ).addClass("top-left");
    $("form").addClass("move-top");
}

var display_result = function(result) {
    for (var element in result) {
        $("#result_space").append("<strong>Categorized: "+result[element].type+"</strong> <br>");
        if (typeof result[element].image != "undefined")
            $("#result_space").append("<img src=\""+result[element].image+"\"</a></br>");

        $("#result_space").append("<a href=\""+result[element].url+"\">"+result[element].name+"</a> </br>");
        $("#result_space").append("ID:  "+result[element].id+"</br>");
        $("#result_space").append(result[element].description+"<br>");
        if (typeof result[element].article != "undefined")
            $("#result_space").append("<p>"+result[element].article+"</p></br>");
        $("#result_space").append("<hr>"); 
    }
}