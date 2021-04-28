!(function($) {
  "use strict";
    $(".related-carousel").owlCarousel({
        autoplay: true,
        dots: true,
        loop: true,
        responsive: {
          0: {
            items: 1
          },
          768: {
            items: 2
          },
          900: {
            items: 3
          }
        }
      });
    $(".portfolio-info").on("click", function() {
        window.location = $('#portfolio-info').attr('link')
    })
})(jQuery);