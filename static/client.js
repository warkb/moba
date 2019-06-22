var canvas = document.getElementById('canvas');
var context = new LibCanvas.Context2D(canvas);
var socket = io.connect('http://' + document.domain + ':' + location.port);
var socket = io();
var full_widts = 1280;
var full_height = 1024;

socket.on('regular_msg', function (data) {
    // подписываемся на данные, которые мы регулярно получаем от сервера
    context.clearRect(0, 0, 1280, 1024);
    LibCanvas.extract();
    context.size = new LibCanvas.Size(full_widts, full_height);
    // TODO: че там с частичной перересовкой?
    context.clearAll();
    for (var key in data) {
        // рисуем кружочек
        let player = data[key];
        // context.beginPath();
        // context.arc(player.x, player.y, 10, 0, 2 * Math.PI);
        // context.fill();
        let newShape = new Circle(player.x, player.y, 50);
        context.fill(newShape, 'green');
    }
});
// отсылаем данные о клике правой клавишей на сервер
var mouse = new LibCanvas.Mouse(canvas);
mouse.events.add(
    {
        contextmenu: function (event, mouse) {
            event.preventDefault();
            let x = (event.layerX / canvas.clientWidth) * full_widts;
            let y = (event.layerY / canvas.clientHeight) * full_height;
            socket.emit('new_dest_point', {x: x, y: y});
        }
    }
);
