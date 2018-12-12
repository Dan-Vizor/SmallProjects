let t=0
const TIME_INTERVAL = 0.1;
const RADIUS = 150
const LIGHT_GREY = 150
const WHITE = 255

// This function gets called once at the start
function setup() {
  createCanvas(1200, 900)

}

// This function gets called every frame
function draw() {
 //background('white');
  if (mouseIsPressed){
    fill(color('red'));
  } else{
    fill(WHITE);
  }
  //triangle(35, 65, 58, 10, 105, 65);

  let radius = RADIUS * sin(t)
  ellipse(mouseX, mouseY, radius)
  
  t += TIME_INTERVAL;
}