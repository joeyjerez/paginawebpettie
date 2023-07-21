$("#switchClarinete").click(function(){
    $("#body").css({"background-color" : "#FF0000"});
})


//Clientes semanales accion de mostrar y ocultar
$("#clientesSemanales").hide();

$("#patitas").click(function(){
    $("#clientesSemanales").show();
});

$("#patitasOcultar").click(function(){
    $("#clientesSemanales").hide();
});
//Fin clientes accion mostrar ocultar
