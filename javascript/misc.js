
var empty = {}

var txt = {
	one: "Hello",
	"two": "there"
}

var d = {
	name: "Morten",
	age: 29
}

var dd = d
var $ = d

dd.name = "Nils"

document.write("$.name = " + $.name + "<br/>")
document.write("<br/>" + txt.one + " " + txt["two"])
document.write("<br/>" + d.name)

document.write("<h2>Reflection</h2>")
document.write("<p>")
document.write("typeof dd = " + typeof dd + "<br/>")
document.write("typeof 10 = " + typeof 10 + "<br/>")
document.write("typeof 20.5 = " + typeof 20.5 + "<br/>")
document.write("typeof d.name = " + typeof d.name + "<br/>")
document.write("typeof notdefined = " + typeof adf + "<br/>")
document.write("d.hasOwnProperty('name') = " + d.hasOwnProperty("name") + "<br/>")
document.write("</p>")
