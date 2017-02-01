$(document).ready(function () {

    $('#map_title').css('padding-top', ($('#GMAP_overlay').height() - $('#map_title').height())/2.5).css('padding-bottom', ($('#GMAP_overlay').height() - $('#map_title').height())/1.5);
    ToggleAssociates();
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
    // if($(window).scrollTop()+$(window).height()-200 > $('#cat_sponsors').offset().top){
    //     $('#cat_sponsors').css('opacity',1);
    // }
});

function ToggleAssociates(){
    $('#associate_layer').height($('#associate_layer .col-md-4').outerHeight());
    console.log($('#associate_layer .col-md-4').outerHeight());
    $("#cat_associates").click(function(){
        $('#associate_layer').height('auto');
    });
}

function SizeSponsors(){
    widthToApply = ($('#carousel2').width()-25*$('#carousel2 .item').first().children('#carousel2 .sponsor').length )/$('#carousel2 .item').first().children('.sponsor').length;
    // 25(px) = padding + min_margin between each $('.sponsor')

    $('.sponsor').each(function(){
        // $(this).outerWidth(widthToApply);
        $(this).outerWidth(widthToApply).css('max-height', widthToApply);
        // $(this).children('img').css('margin-top',(widthToApply-$(this).children('img').height())/2);
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





