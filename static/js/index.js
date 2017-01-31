$(document).ready(function () {

    $('#map_title').css('padding-top', ($('#GMAP_overlay').height() - $('#map_title').height())/2.5).css('padding-bottom', ($('#GMAP_overlay').height() - $('#map_title').height())/1.5);
    SizeSponsors();
    SponsorOpacitize();

    $('#GMAP_overlay').click(function(){
        $('#GMAP_overlay').css('pointer-events','none');
        $('#GMAP_overlay h3').css('opacity',0);
    });
    $('#map').mouseout(function(){
        $('#GMAP_overlay').css('pointer-events','visible');
        $('#GMAP_overlay h3').css('opacity',1);
    });

});

$(window).resize(function(){
    SizeSponsors();
});

$(window).scroll(function(){
    if($(window).scrollTop()+$(window).height()-200 > $('#cat_sponsors').offset().top){
        $('#cat_sponsors').css('opacity',1);
    }
});

function SizeSponsors(){
    widthToApply = ($('#carousel2').width()-25*$('#carousel2 .item').first().children('#carousel2 .sponsor').length )/$('#carousel2 .item').first().children('.sponsor').length;
    // 25(px) = padding + min_margin between each $('.sponsor')

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





