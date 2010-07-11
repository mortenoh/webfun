
var click1 = function() {
	var div = document.querySelectorAll("div")
	
	for(id in div) {
		if(typeof div[id] === 'object') {
			document.body.removeChild(div[id])
		}
	}
}

var add = function() {
	var xhr = new XMLHttpRequest()

	xhr.onreadystatechange = function() {
		if(xhr.readyState == 4) {
			var d = document.createElement("div")
			d.innerText = xhr.responseText
			d.style.backgroundColor = "red"
			d.style.color = "white"

			document.body.appendChild(d)
		}
	}

	xhr.open("GET", "ajax.txt", false)
	xhr.send(null)	
}
