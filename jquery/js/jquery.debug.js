
jQuery.fn.debug = function() {
  return this.each(function(){
    alert(this);
  });
};

jQuery.log = function(message) {
	alert(message);
};

jQuery.fn.alertLength = function() {
	alert("You have selected " + this.length + " elements.");
};
