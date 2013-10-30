/*
$(document).ready(function(){
 $("#msgid").html("This is Hello World by JQuery");
});
*/


// On document load
$(document).ready(function() {
   //$("#atomspace").html("Greetings earthling 2.");

    var getatomsAPI = "http://localhost:5000/api/v1.0/atoms";

console.log( "frog" );

    $.getJSON( getatomsAPI, function( data ) {
        console.log( "frog 3");
    }
    );

    console.log( "frog 2" );

    /*


        , function( json ) {
      console.log( "JSON Data: "  );
        $("#atomspace").html("Greetings earthling 3.");
     });
    */

/*
    $.getJSON(getatomsAPI, function( data ) {
        $("#atomspace").html("Greetings earthling 3.");
      var items = [];
      $.each( data, function( key, val ) {
        items.push( "<li id='" + key + "'>" + val + "</li>" );
      });

      $( "<ul/>", {
        "class": "my-new-list",
        html: items.join( "" )
      }).appendTo( "body" );



    });
*/

});