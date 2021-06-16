// var ulLength = $('ul li').length;
// $('.no').text(ulLength);
// var time = 50;
// var closure_func = function(closureArg, closuretime) {
//     setTimeout(function(timeout_arg) {

//         var current_height = $(".chat-w").prop("scrollHeight");
//         $(".chat-w").delay(1600).animate({
//             scrollTop: current_height
//         }, 2000, function() {
//             $("li:nth-child(" + timeout_arg + ")").show("drop", {
//                 direction: "down",
//                 easing: 'easeInOutExpo'
//             }, 2000);
//         });
//     }, (closuretime), closureArg);
// }
// for (i = 1; i <= ulLength; i++) {
//     closure_func(i, time);
//     //time = time + 50;
// }











// $('li').each(function(i) {
  
    
  
  
//    $(this).delay( i*(2000) ).show("drop", {direction: "down",easing: 'easeInOutExpo'}, 1500);
//   var current_height = $(".chat-w").prop("scrollHeight");
//         $(".chat-w").animate({
//             scrollTop: current_height
//         }, 1000);
// });

// $(".car").delay(15000).animate({left: -200}, 1000, function() {
//       $(".car").delay(500).animate({left: -400}, 1000);
//     });




var current_height = $(".chat-w").prop("scrollHeight");
$("li:nth-child(1)").show("drop", {direction: "down",easing: 'easeInOutExpo'}, 1000, function() {
$("li:nth-child(2)").delay(1000).show("drop", {direction: "down",easing: 'easeInOutCirc'}, 1000, function() {
$("li:nth-child(3)").delay(1000).show("drop", {direction: "down",easing: 'easeInOutCirc'}, 1000, function() {
$("li:nth-child(4)").delay(1000).show("drop", {direction: "down",easing: 'easeInOutCirc'}, 1000, function() {
$("li:nth-child(5)").delay(1000).show("drop", {direction: "down",easing: 'easeInOutCirc'}, 1000, function() {
$(".chat-w").animate({scrollTop: current_height}, 1000, function() {
$("li:nth-child(6)").delay(500).show("drop", {direction: "down",easing: 'easeInOutCirc'}, 1000, function() {
$(".chat-w").animate({scrollTop: current_height}, 1000, function() {
$("li:nth-child(7)").delay(500).show("drop", {direction: "down",easing: 'easeInOutCirc'}, 1000, function() {
$(".chat-w").animate({scrollTop: current_height}, 1000, function() {
$("li:nth-child(8)").delay(500).show("drop", {direction: "down",easing: 'easeInOutCirc'}, 1000, function() {
$(".chat-w").animate({scrollTop: current_height}, 1000, function() {
$("li:nth-child(9)").delay(500).show("drop", {direction: "down",easing: 'easeInOutCirc'}, 1000, function() {
$(".car").delay(1000).animate({left: -220}, 1000, function() {
$(".car").delay(1000).animate({left: -440}, 1000, function() {

});
});
}); 
});
}); 
});
}); 
});
});
});
});
});
});
});
});