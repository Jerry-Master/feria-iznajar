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

function checkUser(change=true){
  $.post("/check/", {
    'user': document.getElementById("user").value
  }, function(data, status){
    if (change){
      if (data === 'True'){
        $(':input[type="submit"]').prop('disabled', true);
        $('#error-user').removeClass('invisible');
      } else {
        $(':input[type="submit"]').prop('disabled', false);
        $('#error-user').addClass('invisible');
      }
    } else {
      if (data === 'False'){
        $(':input[type="submit"]').prop('disabled', true);
        $('#error-user').removeClass('invisible');
      } else {
        $(':input[type="submit"]').prop('disabled', false);
        $('#error-user').addClass('invisible');
      }
    }
  });
}

function checkLog(){
  $.post("/checkLog/", {
    'username': document.getElementById("user").value,
    'password': document.getElementById("password").value
  }, function(data, status){
    console.log(document.getElementById("user").value);
    if (data === 'True'){
      if (document.getElementById("user").value === 'admin'){
        $.get('/admin/', function(data, status){
          document.write(data);
        });
      } else {
        $('#error-log').addClass('invisible');
        $.post('/money/', {
          'username': document.getElementById("user").value
        }, function(data, status){
          window.location = data;
        });
      }
    } else {
      $('#error-log').removeClass('invisible');
    }
  });
}