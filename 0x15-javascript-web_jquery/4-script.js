$(document).ready(function() {
    $("#toggle_header").click(function() {
      var currentClass = $("header").attr("class");
      var newClass = (currentClass === "red") ? "green" : "red";
      $("header").removeClass(currentClass).addClass(newClass);
    });
  });
  