// Keep track of scroll top value just after latest scrolling
var lastScrollTop = 0;
// Get the elements that will need their class updated
var currentPanel = $('#current-panel');
var logoPanel = $('#large-logo-panel');

// Function for making the logo panel appear as if it's scrolling
// at half speed when in mobile view
var transformLogoPanel = function (yDelta) {
  // Only proceed if viewport is mobile-sized
  if(Modernizr.mq('(max-width: 1080px)')) {
    logoPanel.css({
      '-webkit-transform' : 'translateY(' + yDelta + 'px)',
      '-moz-transform'    : 'translateY(' + yDelta + 'px)',
      '-ms-transform'     : 'translateY(' + yDelta + 'px)',
      '-o-transform'      : 'translateY(' + yDelta + 'px)',
      'transform'         : 'translateY(' + yDelta + 'px)'
    });
  }
}

var transformCurrentPanel = function (yDelta) {
  currentPanel.css({
    'transform' : 'translateY(' + yDelta + 'px)'
  });
}

$(window).scroll(function () {
    // Compare current scroll top value to last known one to work out scrolling direction
    var scrollTop = $(this).scrollTop();
    var logoYDelta = scrollTop / 2  // destination for logo panel in mobile view
    var currentPanelYDelta = scrollTop / 2
    if (scrollTop != lastScrollTop) {
        transformLogoPanel(logoYDelta);
    }

    // When scrolltop hits 185, logo panel needs to be fixed in place
    if (scrollTop >= 185) {
        logoPanel.addClass('fix');
    } else {
        logoPanel.removeClass('fix');
    }

    // Transform current panel until user has scrolled 190 px down
    if (scrollTop <= 190) {
      transformCurrentPanel(currentPanelYDelta);
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
