const FRAME = 0.1;
const CAN_X = 640;
const CAN_Y = 480;
// This function gets called once at the start
function setup() {
  createCanvas(CAN_X, CAN_Y)
}

// This function gets called every frame
var fall = 0;
var x = 400;
var y = 200;
function draw() {
    background('#0000AA');
    if (y < 400){
		fall += 1
	} else {fall = 0}
	y += fall
    rect(x, y, 60, 60);
}

function keyPressed() {
	//console.log(keyCode);
	if (keyCode == 87){ //w
        if (y == 0){}
        else {y -= 250}}
    else if (keyCode == 65){ //a
        if (x == 0){}
        else {x -= 20}}
    //else if (keyCode == 83){ //s
        //if (y == 410){}
        //else {y += 10}}
    else if (keyCode == 68){ //d
        if (x == 570){}
        else {x += 20}}
}
