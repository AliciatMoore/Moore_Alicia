function drag() {
    bunny = document.getElementById("bunny");
    leftbox = document.getElementById("leftBox");

    bunny.addEventListener("dragstart", startDrag, false);
    bunny.addEventListener("dragend", endDrag, false);

    leftbox.addEventListener("dragenter", dragEnter, false);
    leftbox.addEventListener("dragleave", dragLeave, false);
    leftbox.addEventListener("dragover", function(e){e.preventDefault()}, false);
    leftbox.addEventListener("drop", drop, false);
}

function startDrag(e){
    var pic ='<img id = "bunny" src = "https://s-media-cache-ak0.pinimg.com/originals/06/b3/aa/06b3aa090d6e2e75191ce3f19d7ad38c.jpg">';
    e.dataTransfer.setData('picture', pic);
}

function dragEnter(e){
    e.preventDefault();
    leftbox.style.background = "pink";
    leftbox.style.border = "3px solid yellow";
}

function dragLeave(e){
    e.preventDefault();
    leftbox.style.background = "white";
    leftbox.style.border = "3px solid purple";
}

function drop(e){
    e.preventDefault();
    leftBox.innerHTML = e.dataTransfer.getData('Picture');
}

function endDrag(e){
    pic = e.target;
    pic.style.visibility = "hidden";
}
window.addEventListener("load", drag, false);
