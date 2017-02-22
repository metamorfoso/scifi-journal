// Keep track of scroll top value just after latest scrolling
var lastScrollTop = 0;
// Get the elements that will need their class updated
var currentPanel = $('#current-panel');
var logoPanel = $('#large-logo-panel');

// Function for making the logo panel appear as if it's scrolling
// at half speed when in mobile view
var transformLogoPanel = function (destination) {
  // logoPanel.css('transform', 'translateY(' + dest + 'px)');
  logoPanel.css({
    '-webkit-transform' : 'translateY(' + destination + 'px)',
    '-moz-transform'    : 'translateY(' + destination + 'px)',
    '-ms-transform'     : 'translateY(' + destination + 'px)',
    '-o-transform'      : 'translateY(' + destination + 'px)',
    'transform'         : 'translateY(' + destination + 'px)'
  });
}

$(window).scroll(function () {
    // Compare current scroll top value to last known one to work out scrolling direction
    var scrollTop = $(this).scrollTop();
    var destination = scrollTop / 2  // destination for logo panel in mobile view
    if (scrollTop > lastScrollTop) {
        // downscroll
        currentPanel.removeClass('scrolling-up').addClass('scrolling-down');
        logoPanel.removeClass('scrolling-up').addClass('scrolling-down');
        transformLogoPanel(destination);
    } else {
        // upscroll
        currentPanel.removeClass('scrolling-down').addClass('scrolling-up');
        logoPanel.removeClass('scrolling-down').addClass('scrolling-up');
        transformLogoPanel(destination);
    }
    // When scrolltop hits 215, logo panel needs to be fixed in place
    if (scrollTop >= 215) {
        logoPanel.addClass('fix')
    } else {
        logoPanel.removeClass('fix')
    }
    // Update last known scroll top value
    lastScrollTop = scrollTop;
});

// handle mobile menu clicks
var menuButton = document.getElementById('menuButton');
var mobileMenu = document.getElementById('mobileMenu');
var navBlock = document.getElementById('nav-block');
menuButton.addEventListener('click', function (e) {
  menuButton.classList.toggle('is-active');
  mobileMenu.classList.toggle('display');
  navBlock.classList.toggle('invert-colours');
  e.preventDefault();
});
