

Function.prototype.method = function(name, fn) {
	this.prototype[name] = fn
	return this
}

Function.method("inherits", function(Parent) {
	this.prototype = new Parent()
	return this
})

/* inheritance */
var Car = function() {
	this.i = 10
}

Car.method("drive", function() {
	document.writeln("Driving my car.")
})

var Ford = function() {
	this.name = "Ford"
}
	.inherits(Car)
	.method("hello", function() {
		document.writeln(this.i)
	})

var f = new Ford()
f.hello()
f.drive()


/* other */

Object.method("pop", function() {
	var r = this[this.length]
	this.length--

	return r
})

var add = function() {
	var total = 0
	arguments.pop()
	
	while(arguments.length > 0) {
		total += arguments.pop()
	}
	
	return total
}

document.write("<p> Add: " + add(1,2,3,4,5) + "</p>")

var sum = function() {
	var total = 0;

	for(var i=0; i<arguments.length; i++) {
		total += arguments[i]
	}
	
	return total
}

var arr = [1,2,3,4,5]

document.write("<p> Sum: " + sum.apply(null, arr) + "</p>")

var Person = function(name, age) {
	this.name = name
	this.age = age
}

Person.method("toString",  function() {
	return this.name + " is " + this.age + " years old."
})

var n = new Person("Nils", 20)
var k = new Person("Kari", 30)

document.writeln(n.toString() + "<br/>")

var e = function() {
	throw {
		what: "Something happend.",
		code: 22
	}
}

try {
	e()
} catch(ex) {
	document.writeln("Exception: " + ex.what)
}
