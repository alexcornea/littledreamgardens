function myFunction() {
  var x = document.getElementById("myTopnav");
  if (x.className === "topnav-LGD") {
    x.className += " responsive";
  } else {
    x.className = "topnav-LGD";
  }
};

    $(document).ready(function(){
        // Show hide popover
        $(".drop1").click(function(){
            $(this).find(".dropdown1").slideToggle("fast");
        });
    });
    $(document).on("click", function(event){
        var $trigger = $(".drop1");
        if($trigger !== event.target && !$trigger.has(event.target).length){
            $(".dropdown1").slideUp("fast");
        }
    });


    $(document).ready(function(){
        // Show hide popover
        $(".drop2").click(function(){
            $(this).find(".dropdown2").slideToggle("fast");
        });
    });
    $(document).on("click", function(event){
        var $trigger = $(".drop2");
        if($trigger !== event.target && !$trigger.has(event.target).length){
            $(".dropdown2").slideUp("fast");
        }
    });


    $(document).ready(function(){
        // Show hide popover
        $(".drop3").click(function(){
            $(this).find(".dropdown3").slideToggle("fast");
        });
    });
    $(document).on("click", function(event){
        var $trigger = $(".drop3");
        if($trigger !== event.target && !$trigger.has(event.target).length){
            $(".dropdown3").slideUp("fast");
        }
    });


    $(document).ready(function(){
        // Show hide popover
        $(".drop4").click(function(){
            $(this).find(".dropdown4").slideToggle("fast");
        });
    });
    $(document).on("click", function(event){
        var $trigger = $(".drop4");
        if($trigger !== event.target && !$trigger.has(event.target).length){
            $(".dropdown4").slideUp("fast");
        }
    });

    //Get the button
  var mybutton = document.getElementById("#back-to-top");

    // When the user scrolls down 20px from the top of the document, show the button
  window.onscroll = function() {scrollFunction()};

  function scrollFunction() {
    if (document.body.scrollTop > 450 || document.documentElement.scrollTop > 450) {
      back_to_top.style.display = "block";
    } else {
      back_to_top.style.display = "none";
    }
  }

    // When the user clicks on the button, scroll to the top of the document
  function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
    }