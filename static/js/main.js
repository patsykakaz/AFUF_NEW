
$(document).ready(function(){
    footerPush();
});

$(window).load(function(){
    $('.navbar.navbar-default').css('opacity',1);
    // $('#i18n').css('top',$('#logo').outerHeight()/2);
    if($(window).width()>991){
        $('.navCat').css('font-size',18);
        navCat();
    }
});

$(window).resize(function(){
    if($(window).width()>991){
        $('.navCat').css('font-size',18);
        navCat();
    }
});

function footerPush(){
    if($('footer').offset().top + $('footer').outerHeight() < $(window).height()){
        // 80 = 80px for the default footer.margin-top
        $('footer').css('margin-top', 80+$(window).height()-($('footer').offset().top+$('footer').outerHeight()));
    }
}


function navCat(){
    $("#all_navCat").removeClass('hide');
    if($('#all_navCat').outerHeight() > $('.navCat').outerHeight() +2){
        Fsize = parseFloat($('.navCat').css('font-size'))-0.05;
        console.log($('.navCat').outerHeight());
        console.log(Fsize);
        $('.navCat').css('font-size',Fsize);
        $('.navCat').attr('rel',Fsize);
        if(Fsize>0){
            setTimeout(navCat(),10);
        }
    }
}