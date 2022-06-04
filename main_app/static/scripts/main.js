$(".navbar-burger").click(function () {
    $(".navbar-burger").toggleClass("is-active");
    $(".navbar-menu").toggleClass("is-active");
  });
  
  $(".dropdown").click(function (event) {
    $(this).toggleClass("is-active");
  });