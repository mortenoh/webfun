
var instanceOf = function(object, constructor) {
  while(object != null) {
    if(object == constructor.prototype) {
      return true;
    }

    object = object.__proto__;
  }

  return false;
}

var Person = function(name, age) {
  this.name = name || "undefined";
  this.age = age || 0;
}

Person.prototype.increaseAge = function() {
  this.age++;
}

var Student = function(name, age, courses) {
  this.base = Person;
  this.base(name, age);
  this.courses = courses || [];
}

Student.prototype.addCourse = function(course) {
  this.courses[this.courses.length] = course;
}

Student.prototype.__proto__ = new Person;

$(document).ready(function() {
  var s1 = new Student("Morten Hansen", 29, ["inf1000", "inf1010"]);
  s1.addCourse("inf5110");

  var p1 = new Person("Test", 20);

  console.log(s1.courses);
  console.log("s1 instanceof Student: " + instanceOf(s1, Student));
  console.log("s1 instanceof Person: " + instanceOf(s1, Person));
  console.log("p1 instanceof Student: " + instanceOf(p1, Student));
  console.log("p1 instanceof Person: " + instanceOf(p1, Person));
});
