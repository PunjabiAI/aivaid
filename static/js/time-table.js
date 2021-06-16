

// add more dv 

$(document).ready(function() {
    var max_fields      = 10; //maximum input boxes allowed
    var wrapper         = $(".TextBoxContainer"); //Fields wrapper
    var add_button      = $(".btnAdd"); //Add button ID
    
    var x = 1; //initlal text box count
    $(add_button).click(function(e){ //on add input button click
        e.preventDefault();
        if(x < max_fields){ //max input box allowed
            x++; //text box increment
            $(wrapper).append('<div id="rem1"><ul><li><span class="time-dropdown">Open</span></li><li>  <input id="sunday" class="time-dropdown" type="time" name="appt-time" value=""></li><li><input id="sunday" class="time-dropdown" type="time" name="appt-time" value="">	</li><li><a href="#" class="time-dropdown remove">remove</a></li></ul></div>'); //add input box
        }
    });
    
     $(wrapper).on("click",".remove", function(e){ //user click on remove text
        e.preventDefault();  $(this).closest('#rem1').remove(); x--;
    })
});


$(document).ready(function() {
    var max_fields      = 10; //maximum input boxes allowed
    var wrapper         = $(".TextBoxContainer2"); //Fields wrapper
    var add_button      = $(".btnAdd2"); //Add button ID
    
    var x = 1; //initlal text box count
    $(add_button).click(function(e){ //on add input button click
        e.preventDefault();
        if(x < max_fields){ //max input box allowed
            x++; //text box increment
            $(wrapper).append('<div id="rem2"><ul><li><span class="time-dropdown">Open</span></li><li> <input id="monday" class="time-dropdown" type="time" name="appt-time" value=""></li><li> <input id="monday" class="time-dropdown" type="time" name="appt-time" value=""></li><li><a href="#" class="time-dropdown remove">remove</a></li></ul></div>'); //add input box
        }
    });
    
     $(wrapper).on("click",".remove", function(e){ //user click on remove text
        e.preventDefault(); $(this).closest('#rem2').remove(); x--;
    })
});

 
$(document).ready(function() {
    var max_fields      = 10; //maximum input boxes allowed
    var wrapper         = $(".TextBoxContainer3"); //Fields wrapper
    var add_button      = $(".btnAdd3"); //Add button ID
    
    var x = 1; //initlal text box count
    $(add_button).click(function(e){ //on add input button click
        e.preventDefault();
        if(x < max_fields){ //max input box allowed
            x++; //text box increment
            $(wrapper).append('<div id="rem3"><ul><li><span class="time-dropdown">Open</span></li><li><input id="tuesday" class="time-dropdown" type="time" name="appt-time" value=""></li><li><input id="tuesday" class="time-dropdown" type="time" name="appt-time" value=""></li><li><a href="#" class="time-dropdown remove">remove</a></li></ul></div>'); //add input box
        }
    });
    
     $(wrapper).on("click",".remove", function(e){ //user click on remove text
        e.preventDefault();  $(this).closest('#rem3').remove(); x--;
    })
});

$(document).ready(function() {
    var max_fields      = 10; //maximum input boxes allowed
    var wrapper         = $(".TextBoxContainer4"); //Fields wrapper
    var add_button      = $(".btnAdd4"); //Add button ID
    
    var x = 1; //initlal text box count
    $(add_button).click(function(e){ //on add input button click
        e.preventDefault();
        if(x < max_fields){ //max input box allowed
            x++; //text box increment
            $(wrapper).append('<div id="rem4"><ul><li><span class="time-dropdown">Open</span></li><li><input id="Wednesday" class="time-dropdown" type="time" name="appt-time" value=""></li><li><input id="Wednesday" class="time-dropdown" type="time" name="appt-time" value=""></li><li><a href="#" class="time-dropdown remove">remove</a></li></ul></div>'); //add input box
        }
    });
    
     $(wrapper).on("click",".remove", function(e){ //user click on remove text
        e.preventDefault();  $(this).closest('#rem4').remove(); x--;
    })
});

$(document).ready(function() {
    var max_fields      = 10; //maximum input boxes allowed
    var wrapper         = $(".TextBoxContainer5"); //Fields wrapper
    var add_button      = $(".btnAdd5"); //Add button ID
    
    var x = 1; //initlal text box count
    $(add_button).click(function(e){ //on add input button click
        e.preventDefault();
        if(x < max_fields){ //max input box allowed
            x++; //text box increment
            $(wrapper).append('<div id="rem5"><ul><li><span class="time-dropdown">Open</span></li><li><input id="Thursday" class="time-dropdown" type="time" name="appt-time" value=""></li><li><input id="Thursday" class="time-dropdown" type="time" name="appt-time" value=""></li><li><a href="#" class="time-dropdown remove">remove</a></li></ul></div>'); //add input box
        }
    });
    
     $(wrapper).on("click",".remove", function(e){ //user click on remove text
        e.preventDefault();  $(this).closest('#rem5').remove(); x--;
    })
});

$(document).ready(function() {
    var max_fields      = 10; //maximum input boxes allowed
    var wrapper         = $(".TextBoxContainer6"); //Fields wrapper
    var add_button      = $(".btnAdd6"); //Add button ID
    
    var x = 1; //initlal text box count
    $(add_button).click(function(e){ //on add input button click
        e.preventDefault();
        if(x < max_fields){ //max input box allowed
            x++; //text box increment
            $(wrapper).append('<div id="rem6"><ul><li><span class="time-dropdown">Open</span></li><li><input id="Friday" class="time-dropdown" type="time" name="appt-time" value=""></li><li><input id="Friday" class="time-dropdown" type="time" name="appt-time" value=""></li><li><a href="#" class="time-dropdown remove">remove</a></li></ul></div>'); //add input box
        }
    });
    
     $(wrapper).on("click",".remove", function(e){ //user click on remove text
        e.preventDefault();  $(this).closest('#rem6').remove(); x--;
    })
});

$(document).ready(function() {
    var max_fields      = 10; //maximum input boxes allowed
    var wrapper         = $(".TextBoxContainer7"); //Fields wrapper
    var add_button      = $(".btnAdd7"); //Add button ID

    var x = 1; //initlal text box count
    $(add_button).click(function(e){ //on add input button click
        e.preventDefault();
        if(x < max_fields){ //max input box allowed
            x++; //text box increment
            $(wrapper).append('<div id="rem7"><ul><li><span class="time-dropdown">Open</span></li><li><input id="Saturday" class="time-dropdown" type="time" name="appt-time" value=""></li><li><input id="Saturday" class="time-dropdown" type="time" name="appt-time" value=""></li><li><a href="#" class="time-dropdown remove">remove</a></li></ul></div>'); //add input box
        }
    });

     $(wrapper).on("click",".remove", function(e){ //user click on remove text
        e.preventDefault();  $(this).closest('#rem7').remove(); x--;
    })
});


// add more dv