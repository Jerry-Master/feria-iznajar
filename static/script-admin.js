
function add(username){
    $.post('/add/', {'username': username, 'quantity': document.getElementById("add").value}, function(data, status){
      window.location = data;
    });
  }
  
  function remove(username){
    $.post('/remove/', {'username': username, 'quantity': document.getElementById("remove").value}, function(data, status){
      window.location = data;
    });
  }
  
  async function getBookings() {
    $.get('/admin-data/', function(data, status){
      const sampleBookings = data['body'];
  
      const dummyLoader = () => {
        return new Promise((resolve, reject) => {
           resolve(sampleBookings);
        });
      };
    
      dummyLoader().then(bookings => {
        document.querySelector("#booking-table")
                .innerHTML = bookings.map(({ username, money}) => `
                    <tr>
                    <td>${username}</td>
                    <td>${money}</td>
                    <td><button onclick='add("${username}")'> give </button></td>
                    <td><input id='add'></td>
                    <td><button onclick='remove("${username}")'> subtract </button></td>
                    <td><input id='remove'></td>
                    </tr>
                `)
                .join('');
      });
    });
  }
  
  getBookings();