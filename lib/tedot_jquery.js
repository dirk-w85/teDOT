$(document).ready(function(){

  $("#btn-hide").click(function(){
    $("pre").toggle();
  });


  $("#btn-update").click(function(){
    $.get("https://api.chucknorris.io/jokes/random", function(data, status){
      alert("Data: " + data.value + "\nStatus: " + status);
      $('#updated-text').text()
    });
  });

});