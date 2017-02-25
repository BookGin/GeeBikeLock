(function ($) {

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = $.trim(cookies[i]);
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) == (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
function csrfSafeMethod(method) {
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
  'beforeSend': function(xhr, settings) {
    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
      xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
  }
});

})(jQuery);
$("#received_message_button").click(function(){
    $.ajax({
        type: 'GET',
        dataType: 'text',
        async: false,
        url: '/message/',
        success: function(data) {
            alert(data);
            $("#received_message_panel").html(data)
        },
        error: function(xhr, ajaxOptions, thrownError) {
            alert(thrownError);
        },
    });

});
$("#send_message_button").click(function(){
    var message_json = {};
    message_json['content'] = $("#message_box").val();
    message_json['receiver'] = $("#receiver_box").val();
    $.ajax({
        type: 'POST',
        dataType: 'json',
        async: false,
        url: '/message/',

        data:message_json,
        success: function(data) {
            $("#message_box").val("");
        },
        error: function(xhr, ajaxOptions, thrownError) {
            alert(thrownError);
        },
    });

});
