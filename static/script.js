$('.toggle').on('click', function() {
  $('.container').stop().addClass('active');
});

$('.close').on('click', function() {
  $('.container').stop().removeClass('active');
});

function checkEqual(){
  var p1 = document.getElementById("password").value;
  var p2 = document.getElementById("password2").value;

  if (p1 !== '' && p2 !== ''){
    if (p1 !== p2) {
      $(':input[type="submit"]').prop('disabled', true);
      $('#error').removeClass('invisible');
    } else {
      $(':input[type="submit"]').prop('disabled', false);
      $('#error').addClass('invisible');
    }
  }
}