var canvas = document.getElementById('canvas');
var context = canvas.getContext('2d');
var socket = io.connect('http://' + document.domain + ':' + location.port);
var socket = io();
// чё нажал клиент
socket.on('regular_msg', function (data) {
    // подписываемся на данные, которые мы регулярно получаем от сервера
    context.clearRect(0, 0, 1280, 1024);
    context.width = 1280;
    context.height = 1024;
    context.fillStyle = 'green';
    for (var key in data) {
        let player = data[key];
        context.beginPath();
        context.arc(player.x, player.y, 10, 0, 2 * Math.PI);
        context.fill();
    }
});
// тест
socket.on('hi', function (data) {

});