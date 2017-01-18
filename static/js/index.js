$(document).ready(function () {
    $('#CHU').addClass('scrolloff');        
    // set the mouse events to none when doc is ready
    
    $('#overlay').on("mouseup",function(){  
    // lock it when mouse up
        $('#CHU').addClass('scrolloff'); 
        //somehow the mouseup event doesn't get call...
    });
    $('#overlay').on("mousedown",function(){
    // when mouse down, set the mouse events free
        $('#CHU').removeClass('scrolloff');
    });

    $("#map").mouseleave(function () {      
    // becuase the mouse up doesn't work... 
        $('#CHU').addClass('scrolloff');
        // set the pointer events to none when mouse leaves the map area
        // or you can do it on some other event
    });

    SizeSponsors();
    SponsorOpacitize();
});

$(window).resize(function(){
    SizeSponsors();
});


function SizeSponsors(){
    widthToApply = ($('#sponsors_layer .row').width() -25*$('.sponsor').length ) / $('.sponsor').length;
    $('.sponsor').each(function(){
        $(this).outerWidth(widthToApply);
    });
}

function SponsorOpacitize(){
    $('.sponsor').mouseover(function(){
        $('.sponsor').addClass('opacitize');
        $(this).removeClass('opacitize');
    });
    $('.sponsor').mouseout(function(){
        $('.sponsor').removeClass('opacitize');
    });
}





