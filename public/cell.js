'use strict';
const SVG_NS = 'http://www.w3.org/2000/svg';

var svgCanvas = 0
var svgRect = 0

var loadPage = function() {
	svgCanvas = document.getElementById('svgCanvas');
	svgRect = svgCanvas.getBoundingClientRect();

for(var foodNo = 0; foodNo < 500; foodNo ++) {
  var rx = Math.random() * svgRect.width
  var ry = Math.random() * svgRect.height
  const food = document.createElementNS(SVG_NS, 'circle');
  food.setAttribute('cx', rx);
  food.setAttribute('cy', ry);
  food.setAttribute('r', 3);
  var r = Math.random()
  if (r < 0.5) {food.setAttribute('fill', 'red');}
	else {food.setAttribute('fill', 'green');}
  svgCanvas.appendChild(food);
}
}
var restart = function() {
	var x = svgRect.width
	var y = svgRect.height
	 const player = document.createElementNS(SVG_NS, 'circle');
	  player.setAttribute('cx', x);
	  player.setAttribute('cy', y);
	  player.setAttribute('r', 12);
	  player.setAttribute('fill', 'gold');
	  svgCanvas.appendChild(player);
}