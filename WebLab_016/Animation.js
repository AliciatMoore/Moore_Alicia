/*function mouse()
{
    var x = document.getElementById("canvas");
    canvas = x.getContext("2d");
    
    window.addEventListener("mousemove", icon, false);
}

function icon(e) {
    canvas.clearRect(0, 0, 600, 600);
    var xPos = e.clientX;
    var yPos = e.clientY;
    canvas.fillRect(xPos-50, yPos-50, 100, 100);
}

window.addEventListener("load", mouse, false);*/

function mouse()
{
    var x = document.getElementById("canvas");
    canvas = x.getContext("2d");

    window.addEventListener("mousemove", icon, false);
}

function icon(e) {
    canvas.clearRect(0, 0, 600, 600);
    var xPos = e.clientX;
    var yPos = e.clientY;

    var pic = new Image();
    pic.src = "https://www.royalcanin.com/~/media/Royal-Canin/Product-Categories/dog-puppy-landing-hero.ashx";

    canvas.drawImage(pic, xPos-100/*starting x*/, yPos-100, 200/*width*/, 200/*height*/);
}

window.addEventListener("load", mouse, false);