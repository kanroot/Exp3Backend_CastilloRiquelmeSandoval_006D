(function($){
  $(function(){
    $('.sidenav').sidenav();
    $('.materialboxed').materialbox();
    $('.parallax').parallax();
    $('select').formSelect();
    // for HTML5 "required" attribute
    $("select[required]").css({
      display: "inline",
      height: 0,
      padding: 0,
      width: 0
    });
    $('.carousel').carousel({dist: 0,padding: 0,fullWidth: true,indicator: false,duration: 100,});
    rememberColorMode();
    carouselAutoPlay();

  }); // end of document ready
})(jQuery); // end of jQuery name space

function carouselAutoPlay() {
  $('.carousel').carousel('next');
  setTimeout(carouselAutoPlay, 2500);
}

function rememberColorMode() {

  const ClassMemory = [
    ["html" , "ColorMode"] ,
    ["html" , "TextSize"]
  ] ;

  for ( let [ Tag , MemoryName ] of ClassMemory ) {

    let TagNotAlive = !(document.querySelector( Tag )) ;

    let MemoryValue = window.localStorage.getItem( MemoryName ) ;

    if ( MemoryValue || TagNotAlive ) {
      document.querySelector( Tag ).classList.add( MemoryValue );
    }
  }

}