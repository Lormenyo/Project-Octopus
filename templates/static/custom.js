function addPost(){
    report = $('#post').val();
    $('.new-comment').html('<div class="w3-container w3-card w3-white w3-round w3-margin"><br><img src="https://www.w3schools.com/w3images/avatar2.png" alt="Avatar" class="w3-left w3-circle w3-margin-right" style="width:60px"><span class="w3-right w3-opacity">1 min</span><h4>Akwasi Amponsah</h4><br><hr class="w3-clear"><p>' + report + '</p><div class="w3-row-padding" style="margin:0 -16px"><div class="w3-half"><img src="https://img.izismile.com/img/img5/20120730/640/overloaded_truck_causes_bridge_collapse_in_china_640_05.jpg" class="w3-margin-bottom"></div><div class="w3-half"><img src="https://amp.businessinsider.com/images/503d0bc56bb3f7e43c00000a-750-563.jpg" style="width:100%" alt="Nature" ></div></div>');
    $('#post').val("");
}