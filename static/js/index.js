$(document).ready(function () {

    $('#map_title').css('padding-top', ($('#GMAP_overlay').height() - $('#map_title').height())/2.5).css('padding-bottom', ($('#GMAP_overlay').height() - $('#map_title').height())/1.5);
    ToggleAssociates($('#associate_layer .col-md-4').outerHeight());
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

$(window).load(function(){
    Liner();
});

$(window).resize(function(){
    // $("#cat_associates").fadeIn();
    ToggleAssociates($('#associate_layer .col-md-4').outerHeight());
    SizeSponsors();
    // if($(window).width()>991){
        // $('.navCat').css('font-size',14);
        // NavCat();
        Liner();
    // }
});

$(window).scroll(function(){
    // if($(window).scrollTop()+$(window).height()-200 > $('#cat_sponsors').offset().top){
    //     $('#cat_sponsors').css('opacity',1);
    // }
});

function Liner(){
    $('.level_title').each(function(){
        h2 = $(this).children('h2');
        liner = $(this).children('.liner');
        liner.width($(this).width() - h2.outerWidth() - 28);
        // console.log(h2.width());
    });
}

function ToggleAssociates(heightToApply){
    // heightToApply = $('#associate_layer .col-md-4').outerHeight();
    if(!$('#associate_layer').attr('unfold')){
        $('#associate_layer').height(heightToApply);
    }else{
        $('#associate_layer').height(heightToApply);
        H = heightToApply*(Math.ceil($('.associate').length/3));
        $('#associate_layer').height(H);
    }
   // console.log(heightToApply);
    $("#cat_associates").click(function(){
        H = heightToApply*(Math.ceil($('.associate').length/3));
        $('#associate_layer').height(H).attr('unfold','True');
        $("#cat_associates").fadeOut();
    });
}

function SizeSponsors(){
    widthToApply = ($('#carousel2').width()-25*$('#carousel2 .item').first().children('#carousel2 .sponsor').length )/$('#carousel2 .item').first().children('.sponsor').length;
    // 25(px) = padding + min_margin between each $('.sponsor')

    $('.sponsor').each(function(){
        // if($(window).width() > 768){
            $(this).outerWidth(widthToApply).css('max-height', widthToApply);
        // }else{
            // $(this).outerWidth(widthToApply*2).css('max-height', widthToApply*2);
        // }
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





