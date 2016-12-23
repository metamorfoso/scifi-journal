// Keep track of scroll top value just after latest scrolling
var lastScrollTop = 0;
// Get the elements that will need their class updated
var currentPanel = $('#current-panel');
var logoPanel = $('#logo-panel');

$(window).scroll(function () {
    // Compare current scroll top value to last known one to work out scrolling direction
    var scrollTop = $(this).scrollTop();
    if (scrollTop > lastScrollTop) {
        // downscroll
        currentPanel.removeClass('scrolling-up').addClass('scrolling-down');
    } else {
        // upscroll
        currentPanel.removeClass('scrolling-down').addClass('scrolling-up');
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