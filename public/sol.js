'use strict';
const SVG_NS = 'http://www.w3.org/2000/svg';

var svgSolarSystem = 0
var svgRect = 0
var planets = [];

function loadPlanets() {
function httpGet(theUrl) {
    var xmlHttp = new XMLHttpRequest();
      xmlHttp.open( "GET", theUrl, false);
      xmlHttp.send( null );
      return xmlHttp.responseText;
  }

planets = JSON.parse(httpGet('/planets'));
  console.log(planets);

/*planets =  [
  {name: 'Mercuary', radius: 9, orbitDistance: 75, colour: 'orange', frequency : 10 },
  {name: 'Venus', radius: 17, orbitDistance: 110, colour: 'purple', frequency : 4 },
  {name: 'Mars', radius: 12, orbitDistance: 220, colour: 'brown', frequency : 1.7 },
  {name: 'Jupiter', radius: 28, orbitDistance: 290, colour: 'tan', frequency : 1.3 },
  {name: 'Neptune', radius: 20, orbitDistance: 365, colour: 'navy', frequency : 1.2 },
  {name: 'Uranus', radius: 20, orbitDistance: 430, colour: 'blue', frequency : 1.1 },
  {name: 'Polto', radius: 6, orbitDistance: 480, colour: 'gray', frequency : 0.9 },
  {name: 'Earth', radius: 18, orbitDistance: 160, colour: 'green', frequency : 2.5},
  {name: 'ghost', radius: 12, orbitDistance: 330, colour: 'black', frequency : 30}
 ]*/

  svgSolarSystem = document.getElementById('svgSolarSystem');
  svgRect = svgSolarSystem.getBoundingClientRect();

  const sunOrigin = {
    x : svgRect.width / 2,
    y : svgRect.height / 2
  }

for(var starNo = 0; starNo < 2800; starNo ++) {
  var rx = Math.random() * svgRect.width
  var ry = Math.random() * svgRect.height
  const star = document.createElementNS(SVG_NS, 'circle');
  star.setAttribute('cx', rx);
  star.setAttribute('cy', ry);
  star.setAttribute('r', 1);
  star.setAttribute('fill', 'white');
  svgSolarSystem.appendChild(star);
}

  const sunElement = document.createElementNS(SVG_NS, 'circle');
  sunElement.setAttribute('cx', svgRect.width / 2);
  sunElement.setAttribute('cy', svgRect.height / 2);
  sunElement.setAttribute('r', 45);
  sunElement.setAttribute('fill', 'gold');
  svgSolarSystem.appendChild(sunElement);

  planets.forEach(planet => {
    //if (svgRect.height > sunOrigin.y + planet.orbitDistance) {
    planet.element = document.createElementNS(SVG_NS, 'circle');
    planet.element.setAttribute('id', planet.name);
    planet.element.setAttribute('name', planet.name);
    planet.element.setAttribute('r', planet.radius);
    planet.element.setAttribute('fill', planet.colour);
    planet.element.setAttribute('cx', sunOrigin.x + planet.orbitDistance);
    planet.element.setAttribute('cy', sunOrigin.y);
    svgSolarSystem.appendChild(planet.element);
  //}
});

  const animationSpeed = 0.008;
  const animateFrame = function() {
    planets.forEach(planet => {
      const angle = animationSpeed * 2 * Math.PI * planet.frequency * new Date().getTime() / 1000;
      const xPosition = planet.orbitDistance * Math.sin(angle);
      const yPosition = planet.orbitDistance * Math.cos(angle);
      planet.element.setAttribute('cx', svgRect.width / 2 + xPosition);
      planet.element.setAttribute('cy', svgRect.height / 2 + yPosition);

    })
  }
  setInterval(animateFrame, 10);
};

var clickNewPlanet = function() {
    var newPlanetN = document.getElementById('newN').value;
    var newPlanetO = document.getElementById('newO').value;
    var newPlanetC = document.getElementById('newC').value;
    var newPlanetR = document.getElementById('newR').value;
    var newPlanetOF = document.getElementById('newOF').value;
    var newPlanet = {name: newPlanetN, radius: newPlanetR, orbitDistance: newPlanetO, colour: newPlanetC, frequency: newPlanetOF}
    var body = JSON.stringify(newPlanet)

     var xhr = new XMLHttpRequest();
  xhr.open('PUT', '/planet', true);
  xhr.setRequestHeader('Content-Type', 'application/json; charset=UTF-8');
  xhr.send(body);
  xhr.onloadend = function () {
    console.log('new planet loaded')
    console.log(body)

    newPlanet.element = document.createElementNS(SVG_NS, 'circle');
    newPlanet.element.setAttribute('id', newPlanetN);
    newPlanet.element.setAttribute('name', newPlanetN);
    newPlanet.element.setAttribute('r', newPlanetR);
    newPlanet.element.setAttribute('fill', newPlanetC);
    newPlanet.element.setAttribute('cx', svgRect.width / 2 + newPlanetO);
    newPlanet.element.setAttribute('cy', svgRect.height / 2);
    svgSolarSystem.appendChild(newPlanet.element);
    planets.push(newPlanet);
    console.log('planet made named:', newPlanetN);
  }};

var clickupdatePlanet = function() {
  delPlanet()
  clickNewPlanet()
}

  var testName = function() {
    var ifFound = false
    var findPlanetN = document.getElementById('findN').value;
    planets.forEach(planet => {
     if (planet.name === findPlanetN) {
      var testNameOutput = document.getElementById('testNameOutput')
      testNameOutput.innerText = 'planet found named ' + planet.name
      console.log('planet found named:', findPlanetN)
      ifFound = true
    }})
    if (ifFound === false) {
      var testNameOutput = document.getElementById('testNameOutput')
      testNameOutput.innerText = 'cannot find planet named ' + findPlanetN
      console.log('cannot find planet named: ' + findPlanetN)
    }
  }
  var deathStar = function() {
    console.log('Death Star WIP')
  }

var delPlanet = function() {
  var ifFound = false
  var xhr = new XMLHttpRequest();
    var newPlanetN = document.getElementById('newN').value;
          xhr.open('DELETE', '/planet/' + newPlanetN, true);
          xhr.send();
    planets.forEach(planet => {
     if (planet.name === newPlanetN) {
      console.log(newPlanetN)
      console.log(document.getElementById(newPlanetN))
      svgSolarSystem.removeChild(svgSolarSystem.getElementById(newPlanetN));
      console.log('planet found and deleted named:', newPlanetN)
      ifFound = true
    }})
    if (ifFound === false) { console.log('error cannot find planet named:', newPlanetN) }
  }
