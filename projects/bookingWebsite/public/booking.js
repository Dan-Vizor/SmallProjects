'use strict';

function enterChild() {
	const weeks = ['010717', '080717'] //dates will be tables on db
	var date = document.getElementById('date').value;
	if (weeks.some(function(i) {if(i === date){return(true)}})) {
	    console.log("Good date");	
	}
	else {
		alert("error could not find week");
		return(null);
	}
	var kidFName = document.getElementById('kidFName').value;
	var kidLName = document.getElementById('kidLName').value;
	var kidName = kidFName + " " + kidLName
	
	//check that not on db
	//send to db
	
	document.getElementById("out").innerText = kidName + " was added to week " + date
}

function removeChild() {
	var kidFName = document.getElementById('kidFName').value;
	var kidLName = document.getElementById('kidLName').value;
	var kidName = kidFName + " " + kidLName
	var date = document.getElementById('date').value;
	
	//remove from db
}
