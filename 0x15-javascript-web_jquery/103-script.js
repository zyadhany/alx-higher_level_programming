$(document).ready(function() {
    $("#language_code").keypress(function(event) {
      if (event.which === 13) { // Enter key pressed
        getHelloTranslation();
      }
    });
  
    $("#btn_translate").click(getHelloTranslation);
  });
  
  function getHelloTranslation() {
    var langCode = $("#language_code").val();
    if (!langCode) {
      return; // No language code entered, do nothing
    }
  
    $.ajax({
      url: "https://www.fourtonfish.com/hellosalut/hello/" + langCode,
      success: function(data) {
        $("#hello").text(data.hello);
      },
      error: function() {
        $("#hello").text("Error: Could not fetch translation.");
      }
    });
  }
  