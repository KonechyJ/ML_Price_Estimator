window.addEventListener('load', function()
{
    const window_width = document.body.clientWidth
    const hamburger = document.getElementById('hamburger')
    const nav = document.querySelector('.side-nav')
    // Change CSS class when window resizes.
    if (window_width < 1000)
    {
        if (nav.className == "side-nav hide")
        {
            nav.className = "side-nav";
        } else {
            nav.className = "side-nav hide";
        }
    }
    // Click event for hamburger icon, change CSS class.
    hamburger.addEventListener('click', function()
    {
        if (nav.className == "side-nav hide")
        {
            nav.className = "side-nav";
        } else {
            nav.className = "side-nav hide";
        }
    })
});


