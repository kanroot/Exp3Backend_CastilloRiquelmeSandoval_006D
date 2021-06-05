var free=0;
var silver=19.99; 
var gold=54.99;

var dict ={
    "free": free,
    "silver": silver,
    "gold": gold
}
function DropdownCambio(dropdown){
    
   var dolar=document.getElementById("valordolar");
   dolar.innerHTML=dict[dropdown.value]+" USD";
  

   let url="https://mindicador.cl/api/dolar";
  (function($) {
      $.get(url,function(respuesta)
          {            
             var x=Math.round(respuesta["serie"][0]["valor"]*dict[dropdown.value]);
             $("#valorclp").text(x+" CLP");
          }, "json")
  })(jQuery);
} 
 
