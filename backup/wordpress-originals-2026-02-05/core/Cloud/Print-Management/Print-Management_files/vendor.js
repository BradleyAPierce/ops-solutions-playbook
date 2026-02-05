var dc = $(document);



function fullheight() {

    var e = $(window).height();

    $(window).width(),

        $(".fullheight").css("height", e)

}



function setbg() {

    $(".setbg,.slides").each(function() {

        var e = $(this).find(".bg-img").attr("src");

        $(this).css("background-image", "url(" + e + ")"), $(this).find("img.bg-img").hide();

    });

}



wh = $(window).height(),

    ww = $(window).width(),



    dc.on("click", ".goto", function(e) {

        e.preventDefault();

        var n = this.hash,

            i = $(n);

        $("html, body").stop().animate({

            scrollTop: i.offset().top

        });

    });





function heroSlider() {

    var hpslide = $(".heroslides");

    hpslide.owlCarousel({

        loop: false,

        nav: false,

        margin: 0,

        items: 1,

        dots: false,

        mouseDrag: false,
        touchDrag: false,

        autoHeight: false

    });

}



$(".hpslidernav #prev").click(function() {

    hpslide.trigger('prev.owl.carousel');

});

$(".hpslidernav #next").click(function() {

    hpslide.trigger('next.owl.carousel');

});



$(function() {

    $('.dropdown').hover(function() {

            $(this).addClass('open');

        },

        function() {

            $(this).removeClass('open');

        });

});





$('.panel-collapse').on('show.bs.collapse', function() {

    $(this).siblings('.panel-heading').addClass('active');

});



$('.panel-collapse').on('hide.bs.collapse', function() {

    $(this).siblings('.panel-heading').removeClass('active');

});





$(window).on("load", function() {

    fullheight();

    setbg();

    heroSlider();

});



$(window).on('load resize', function() {



});





/* Class change on scroll and click ======================== */

// $(document).ready(function() {

//     $('.scrollMenu a').bind('click', function(e) {

//         e.preventDefault();

//         var target = $(this).attr("href");

//         var scMenu = $('.scrollMenu').outerHeight();

//         $('html, body').stop().animate({

//             scrollTop: $(target).offset().top - scMenu

//         }, 600, function() {

//             location.hash = target;

//         });

//         return false;

//     });

// });

$(window).scroll(function() {

    var scrollDistance = $(window).scrollTop();

    $('.scroll-section').each(function(i) {

        if ($(this).position().top <= scrollDistance) {

            $('.scrollMenu li.active').removeClass('active');

            $('.scrollMenu li a').eq(i).parent('li').addClass('active');

        }

    });

}).scroll();


$(document).ready(function() {
    $('.btn-top-sidebar a').click(function(e) {
        $('.btn-top-sidebar a').parents('.scrollMenu').toggleClass('show-sc');
    });
});





// Mobile Menu //////////////////////////////////////////////////////////////////////////////

$('#toggle').sidr({

    renaming: false,

    side: 'right',

    source: '#menu',

});



$('#sidr li').each(function() {

    var item = $(this);

    if (item.find('ul').length > 0) {

        item.find('a').first().append('<span class="sub-toggle"><i class="fa fa-angle-down"></i></span>');

    }

});



$('#sidr li.dropdown > a').click(function(e) {

    e.preventDefault();

    var item = $(this).children('span'),

        txt;

    item.toggleClass('is-open');

    txt = item.hasClass('is-open') ? '<i class="fa fa-angle-up"></i>' : '<i class="fa fa-angle-down"></i>';

    item.html(txt);

    $(this).closest('li').toggleClass('sub-menu-open');

});



// hide any open popovers when the anywhere else in the body is clicked

$('body').on('click', function(e) {

    $('#sidr').each(function() {

        if (!$(this).is(e.target) && $(this).has(e.target).length === 0 && $('body').has(e.target).length === 0) {

            $.sidr('close', 'sidr');

            //							$('.navbar-nav li').removeClass('sub-menu-open');

            //							$('.sub-toggle').removeClass('is-open');

        }

    });

});



$('a.navbar-toggle').click(function() {

    //alert('hi');

    $('.navbar-nav li').removeClass('sub-menu-open');

});



//$(function(){

//    $('.sidr .dropdown').click(function() {

//        $(this).addClass('open');

//    },

//    function() {

//        $(this).removeClass('open');

//    });

//});




$('.dropdown-menu.subnav ul.list li a').click(function() {
    $('body').removeClass('sidr-open');
    setTimeout(function() {
        $('#sidr').addClass('hide');
    }, 300);
});





$(document).ready(function() {
    $('#nav-tabs-wrapper li').click(function(e) {
        $('#nav-tabs-wrapper li').removeClass('active');
        var $this = $(this);
        if (!$this.hasClass('active')) {
            $this.addClass('active');
        }
    });
});

// $('.jump_nav_scroll_sidebar a').on('click', function(event) {
//     var scrlhh = $('.navbar').outerHeight();
//     var target = $(this.getAttribute('href'));
//     if (target.length) {
//         event.preventDefault();
//         $('html, body').stop().animate({
//             scrollTop: target.offset().top - scrlhh
//         }, 1000);
//     }
// });


/* MatchHeight ====================== */
$(document).ready(function() {
  $(window).on("load resize",function(){
    $('.scaning-same').matchHeight();
    $('.footer-menu-section .small-gutters .menu-parts.boxes-height').matchHeight();
    $('.it-service .offers-boxes').matchHeight();
  })
})

/* Copyright Year auto-update */
$(document).ready(function(){
	var dteNow = new Date();
	var intYear = dteNow.getFullYear();

	$('#copyright').each(function() {
		var text = $(this).text();
		$(this).text(text.replace('CurrentCopyrightYear', intYear)); 
	});
})