about_button = document.getElementById("about-button").addEventListener("click", scroll);
function scroll(){
    document.getElementById("about").scrollIntoView(
        {behavior:"smooth",
        block:"start"}
    );
}
console.log("Hello");