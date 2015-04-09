$(document).ready( function(){
    Draggable.create(".wheel1", {
        type: "rotation",
        throwProps: true,
        trigger: ".wheel"
    })
    TweenLite.set(".wheel1", {
        transformOrigin: "bottom right"
    })
});

function allowDrop(ev) {
    ev.preventDefault();
}

function drag(ev) {
    ev.dataTransfer.setData("link", "www.google.com");
}

function drop(ev) {
    ev.preventDefault();
    var data = ev.dataTransfer.getData("text");
    ev.target.appendChild(document.getElementById(data).cloneNode(true));
}