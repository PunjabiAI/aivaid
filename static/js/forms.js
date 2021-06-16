$(function() {
$('form').on('keydown', '.new_password', function(e) {
if (e.which === 32 &&  e.target.selectionStart === 0) {return false;}
});
});
jQuery('document').ready(function($) {
$('.forgotbtn02').click(function() {
   var empty = false;
    $('.new_password').each(function() {
    if ($(this).val() === '') { empty = true;}
    });
     if (empty || ($('#password01').val() !== $('#password02').val())){
    alert("Fill all fields correctly");
    $('#message').html('Password not matched').css('color', 'red');
    return false;
  }
  else
  { $('#message').html('Password matched').css('color', 'green');return true;
   return true;
  }
});
});
/* ================================ */
jQuery('document').ready(function($) {
$('.forgotbtn01').click(function() {
   var empty = false;
    $('.input').each(function() {
    if ($(this).val() === '') {empty = true;}
    });
    if(empty){alert("Please enter your email");return false;}
    else{return true;}
});
});
/* ================================ */
$(document).ready(function()
{$('.step01').click(function()
{if($('.tcCheck').is(':checked'))
{return true;}
else{alert("Please accept terms and conditions to proceed");return false;}
})
})
/* ================================ */
$(function() {
  $('.form-group').on('keydown', '.required', function(e) {
    if (e.which === 32 &&  e.target.selectionStart === 0) {
      return false;} });
});
jQuery('document').ready(function($) {
    $('#step02').click(function() {
     var selectedVal = ($('.selectVal :selected').val());
     var value;
        var empty = false;
        $('.required').each(function() {
            if ($(this).val() === '') {empty = true;}
        });
        if(empty || (selectedVal == '-1'))
        { alert("All fields are required");return false;}
        else
        {return true;}
    });
   });

/* ===================================== */
$(function() {
$("#statelist").change(function() {
var $dropdown = $(this);
$.getJSON("../static/data.json", function(data) {
var key = $dropdown.val();
var vals = [];
switch(key) {
case 'AndamanNicobar':
    vals = data.AndamanNicobar.split(",");
    break;
case 'AndhraPradesh':
    vals = data.AndhraPradesh.split(",");
    break;
case 'ArunachalPradesh':
     vals = data.ArunachalPradesh.split(",");
     break;
case 'Assam':
     vals = data.Assam.split(",");
     break;
case 'Bihar':
     vals = data.Bihar.split(",");
     break;
case 'Chandigarh':
     vals = data.Chandigarh.split(",");
     break;
case 'Chhattisgarh':
     vals = data.Chhattisgarh.split(",");
     break;
case 'DadraNagarHaveli':
     vals = data.DadraNagarHaveli.split(",");
     break;
case 'DamanDiu':
     vals = data.DamanDiu.split(",");
     break;
case 'Delhi':
     vals = data.Delhi.split(",");
     break;
case 'Goa':
     vals = data.Goa.split(",");
     break;
case 'Gujarat':
     vals = data.Gujarat.split(",");
     break;
case 'Haryana':
     vals = data.Haryana.split(",");
     break;
case 'HimachalPradesh':
     vals = data.HimachalPradesh.split(",");
     break;
case 'JammuKashmir':
     vals = data.JammuKashmir.split(",");
     break;
case 'Jharkhand':
     vals = data.Jharkhand.split(",");
     break;
case 'Karnataka':
     vals = data.Karnataka.split(",");
     break;
case 'Kerala':
     vals = data.Kerala.split(",");
     break;
case 'Lakshadweep':
     vals = data.Lakshadweep.split(",");
     break;
case 'MadhyaPradesh':
     vals = data.MadhyaPradesh.split(",");
     break;
case 'Maharashtra':
     vals = data.Maharashtra.split(",");
     break;
case 'Manipur':
     vals = data.Manipur.split(",");
     break;
case 'Meghalaya':
     vals = data.Meghalaya.split(",");
     break;
case 'Mizoram':
     vals = data.Mizoram.split(",");
     break;
case 'Nagaland':
     vals = data.Nagaland.split(",");
     break;
case 'Orissa':
     vals = data.Orissa.split(",");
     break;
case 'Pondicherry':
     vals = data.Pondicherry.split(",");
     break;
 case 'Punjab':
     vals = data.Punjab.split(",");
     break;
case 'Rajasthan':
     vals = data.Rajasthan.split(",");
     break;
case 'Sikkim':
     vals = data.Sikkim.split(",");
     break;
case 'TamilNadu':
     vals = data.TamilNadu.split(",");
     break;
case 'Tripura':
     vals = data.Tripura.split(",");
     break;
case 'UttarPradesh':
     vals = data.UttarPradesh.split(",");
     break;
case 'Uttaranchal':
     vals = data.Uttaranchal.split(",");
     break;
case 'WestBengal':
     vals = data.WestBengal.split(",");
     break;
case 'select':
    vals = ['Please choose from above'];
}
var $jsontwo = $("#citylist");
$jsontwo.empty();
$.each(vals, function(index, value) {
$jsontwo.append("<option>" + value + "</option>");
});
});
});
});
/* ================================ */
function changeSrc() {
if (document.getElementById("male").checked) {
document.getElementById("picture").src = "/static/images/male.png";
} else if (document.getElementById("female").checked) {
document.getElementById("picture").src = "/static/images/female.png";
}
}
/* ================================ */
var bmi_value,w_val;
function healthCal(){
   w_val = document.getElementById("weight").value;
   var val1 = document.getElementById("foot_value").value;
   var val2 = document.getElementById("inch_value").value;
   var final_val = ((val1 * 0.3048) + (val2 * 0.0254)).toFixed(2);
   document.getElementById("height").value = final_val;
   bmi_value = (w_val / (final_val* final_val)).toFixed(0);
   if ((w_val > 150 || w_val < 30) || (final_val > 3 || final_val < 0.1))
   {
     document.getElementById("bmi_result").value= "Please recheck your inputs";
     return false;
   }
   if(bmi_value < 18.5)
   {
     document.getElementById("bmi_result").value="You are Underweight" ;
     document.getElementById("bmi_value").value = bmi_value;
   }
   else if (bmi_value >= 18.5 && bmi_value <= 24.9)
   {
     document.getElementById("bmi_result").value="You are Normal";
     document.getElementById("bmi_value").value = bmi_value;
   }
   else if(bmi_value >= 25 && bmi_value <= 29)
   {
     document.getElementById("bmi_result").value="You are Overweight";
     document.getElementById("bmi_value").value = bmi_value;
   }
   else if(bmi_value > 30.5)
   {
     document.getElementById("bmi_result").value="You are Obese";
     document.getElementById("bmi_value").value = bmi_value;
   }
 }
 /* ================================ */
jQuery(document).ready(function($){
$('path').on('click',function(){
   $(this).css('fill',' #2bbbad');
   if($(this).attr('data-name'))
    {
     var test = ($(this).attr('data-name'));
     $("#locations").append(test ,",");
     $(this).attr('data-name', "");
    }
  });
});
/* =================================== */
$(document).ready(function()
{
  $(".locbtn").click(function(){
    if($("#locations").val() === '')
    {alert("Select Location");return false;}
    else{return true;}
  })
})
/* =================================== */
$(".btnrotate").click(function(){$(".rotateImg").toggleClass("showImg hideImg");return false;})
/* =================================== */
var checkboxes1 = $(".symptomList li input[type='checkbox']");
checkboxes1.on('change', function() {
    $('#your-symptoms').val(
        checkboxes1.filter(':checked').map(function(item) {
            return this.value;
        }).get().join(', ')
     );
});
/* =================================== */
$('.symBtn').click(function()
{
if($('#your-symptoms').val() === '')
{alert("Select symptoms");return false;}
else
{return true;}
})
/* =================================== */
jQuery('document').ready(function($) {
$('.reportbtn').click(function() {
var empty = false;
$('.getreport').each(function() {
if ($(this).val() === '') {empty = true;}
});
if(empty){alert("Enter your email");return false;}
else{return true;}
});
});
/* =================================== */
var dateToday = new Date();var dates = $(".select-date").datepicker({
    minDate: dateToday,
    onSelect: function(selectedDate)
 {       var option = this.id == "from" ? "minDate" : "maxDate",
            instance = $(this).data("datepicker"),
            date = $.datepicker.parseDate(instance.settings.dateFormat || $.datepicker._defaults.dateFormat, selectedDate, instance.settings);
        dates.not(this).datepicker("option", option, date);
    }
});
/* =================================== */
$( function() {$( ".select-dob" ).datepicker();} );