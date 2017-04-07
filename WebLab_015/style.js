function shapes()
{
    var x = document.getElementById("canvas");
    var canvas = x.getContext("2d");
    canvas.strokeStyle = "green";

    canvas.beginPath();
    canvas.moveTo(50, 50);
    canvas.lineTo(140, 100);
    canvas.lineTo(170, 10);
    canvas.lineTo(200, 100);
    canvas.lineTo(290, 50);
    canvas.lineTo(240, 140);
    canvas.lineTo(350, 160);
    canvas.lineTo(240, 200);
    canvas.lineTo(300, 270);
    canvas.lineTo(200, 230);
    canvas.lineTo(170, 310);
    canvas.lineTo(140, 230);
    canvas.lineTo(50, 270);
    canvas.lineTo(110, 200);
    canvas.lineTo(10, 160);
    canvas.lineTo(110, 140);
    canvas.closePath();
    canvas.stroke();

    var g = canvas.createLinearGradient(10, 10, 300, 200);
    g.addColorStop(0, "red");
    g.addColorStop(.5, "white");
    g.addColorStop(1, "blue");

    canvas.fillStyle = g;
    canvas.fill();
}
window.addEventListener("load", shapes, false);