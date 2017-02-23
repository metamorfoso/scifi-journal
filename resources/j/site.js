// Keep track of scroll top value just after latest scrolling
var lastScrollTop = 0;
// Get the elements that will need their class updated
var currentPanel = $('#current-panel');
var logoPanel = $('#large-logo-panel');

// Function for making the logo panel appear as if it's scrolling
// at half speed -- only in mobile view
var transformMobileLogoPanel = function (yDelta) {
  // Only proceed if viewport is mobile-sized
  if(Modernizr.mq('(max-width: 1081px)')) {
    logoPanel.css({
      '-webkit-transform' : 'translateY(' + yDelta + 'px)',
      '-moz-transform'    : 'translateY(' + yDelta + 'px)',
      '-ms-transform'     : 'translateY(' + yDelta + 'px)',
      '-o-transform'      : 'translateY(' + yDelta + 'px)',
      'transform'         : 'translateY(' + yDelta + 'px)'
    });
  }
}

// Function for making the current issue panel move downards when the user
// scrolls the page down -- only in non-mobile
var transformCurrentPanel = function (yDelta) {
  // Only proceed if viewport is NOT mobile-sized
  if(Modernizr.mq('(min-width: 1081px)')) {
    currentPanel.css({
      'transform'         : 'translateY(' + yDelta + 'px)',
      '-webkit-transform' : 'translateY(' + yDelta + 'px)',
      '-moz-transform'    : 'translateY(' + yDelta + 'px)',
      '-ms-transform'     : 'translateY(' + yDelta + 'px)',
      '-o-transform'      : 'translateY(' + yDelta + 'px)'
    });
  }
}

// Track scrolling and trigger desired behaviour at appropriate points
$(window).scroll(function () {
    // Compare current scrollTop value to last known one to work out scrolling direction
    var scrollTop = $(this).scrollTop();
    var logoYDelta = scrollTop / 2  // how much to move logo panel by (in mobile view)
    var currentPanelYDelta = scrollTop / 2  // how much to move current issue panel (in non-mobile view)
    // Fix logo panel in place when scrollTop hits 220 (non-mobile)
    if (scrollTop >= 220 && Modernizr.mq('(min-width: 1081px)')) {
      logoPanel.addClass('fix');
    } else {
      logoPanel.removeClass('fix');
    }

    // Fix current panel in place when scrollTop hits 550 (non-mobile)
    if (scrollTop >= 550 && Modernizr.mq('(min-width: 1081px)')) {
      currentPanel.addClass('fix');
    } else {
      currentPanel.removeClass('fix');
    }

    // Transform current panel until user has scrolled downward 190px (mobile)
    if (scrollTop <= 190) {
      transformCurrentPanel(currentPanelYDelta);
    }

    // Transform logo panel (mobile) on every scrolling action
    transformMobileLogoPanel(logoYDelta);

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
