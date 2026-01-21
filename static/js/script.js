// Some script to add the scrolling system when about or features button is clicked
document.getElementById("about-button").addEventListener("click", scroll_about);
function scroll_about(){
    document.getElementById("about").scrollIntoView(
        {behavior:"smooth",
        block:"start"}
    );
}
document.getElementById("features-button").addEventListener("click", scroll_feature);
function scroll_feature(){
    document.getElementById("features").scrollIntoView(
        {behavior: "smooth",
        block: "start"
        }
    );
}