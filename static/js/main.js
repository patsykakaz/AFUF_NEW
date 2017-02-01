
$(document).ready(function(){
    FooterPush();
    $("#all_navCat").removeClass('hide');
        // $("#all_navCat").css('opacity',1);
});

$(window).load(function(){
    $('.navbar.navbar-default').css('opacity',1);
    // $('#i18n').css('top',$('#logo').outerHeight()/2);
    if($(window).width()>991){
        // $('.navCat').css('font-size',26);
        // NavCat();
    }
});

$(window).resize(function(){

});

function FooterPush(){
    if($('footer').offset().top + $('footer').outerHeight() < $(window).height()){
        // 80 = 80px for the default footer.margin-top
        $('footer').css('margin-top', 80+$(window).height()-($('footer').offset().top+$('footer').outerHeight()));
    }
}


// function NavCat(){
//     $("#all_navCat").removeClass('hide');
//     console.log("#all : "+$('#all_navCat').outerHeight());
//     console.log("first a : "+$('.navCat a').outerHeight());
//     if($('#all_navCat').outerHeight() > $('.navCat a').outerHeight()+2){
//         console.log('size down !')
//         Fsize = parseFloat($('.navCat a').css('font-size'))-0.05;
//         // console.log($('.navCat a').outerHeight());
//         console.log(Fsize);
//         $('.navCat a').css('font-size',Fsize);
//         $('.navCat a').attr('rel',Fsize);
//         if(Fsize>0){
//             setTimeout(NavCat(),5);
//         }
//     }else{
//         console.log('no size down ...')
//         $("#all_navCat").css('opacity',1);
//     }
// }
function NavCat(){
    $("#all_navCat").removeClass('hide');
    if($('#all_navCat').outerHeight() > $('.navCat').outerHeight() +2){
        Fsize = parseFloat($('.navCat').css('font-size'))-0.05;
        console.log($('.navCat').outerHeight());
        console.log(Fsize);
        $('.navCat').css('font-size',Fsize);
        $('.navCat').attr('rel',Fsize);
        if(Fsize>0){
            setTimeout(NavCat(),5);
        }
    }else{
        $("#all_navCat").css('opacity',1);
    }
}






