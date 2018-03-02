//Request the server asynchronously to add the opportunity to the favorites list for the user.
// Since the this project assumes one user, no user id is being sent to the server
function addToFav(id){
    $.ajax({
      type: "POST",
      url: '/editFav',
      data: {"id":id,"type":"add"},
      success: added(id),
      dataType: 'text'
    });
}

//Request the server asynchronously to remove opportunity from favorites list
function removeFromFav(id){
    $.ajax({
      type: "POST",
      url: '/editFav',
      data: {"id":id,"type":"remove"},
      success: removed(),
      dataType: 'text'
    });
}

//remove the grayscaling effect on the favorites icon for that opportunity
function added(id){
        $('#'+id).removeClass('grayscale');
}

//reload the page after 0.2 seconds to reflect the change
function removed(){
    setTimeout(function(){
      location.reload(true);
    },200);
}