$(window).scroll(function(){
    $('.navbar').toggleClass('scrolled', $(this).scrollTop() > 200);
    $('.nav-link').toggleClass('scrolled', $(this).scrollTop() > 200);
    });
    
    /*----------index.html backToTopBtn javascript code----------*/
    mybutton=document.getElementById("back-to-top");
    window.onscroll = function(){scrollFunction()};
    function topFunction(){
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
    } 
    