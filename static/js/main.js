console.log(999999999)

function initialize() {
    console.log(888)
    var myLatlng = new google.maps.LatLng(35.728070, 51.494620);
    var mapOptions = {
      zoom: 15,
      center: myLatlng,
      mapTypeId: google.maps.MapTypeId.ROADMAP
    }
     
    var map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
     
    var contentString = '<div style="direction: rtl; text-align: right;font-family: Tahoma;">' +
                                '<h6>ایران کیل</h6>' +
                                //  '<h5>Iran Keil</h5>' +
                                 '</div>';
     
    var infowindow = new google.maps.InfoWindow({
      content: contentString
    });
     
    var marker = new google.maps.Marker({
      position: myLatlng,
      map: map,
      title: 'Iran keil'
    });
     
    infowindow.open(map, marker);
    google.maps.event.addListener(marker, 'click', function() {
      infowindow.open(map, marker);
    });
  }