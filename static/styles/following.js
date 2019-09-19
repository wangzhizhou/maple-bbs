function Follow(obj,data,url){
  if(obj.hasClass('active')) {
    $.ajax ({
      type : "DELETE",
      url : url,
      data:data,
      contentType: 'application/json;charset=UTF-8',
      success: function(response) {
        if (response.status === '200')
        {
          obj.text('关注').removeClass('active');
        } else
        {alert('fail');}}});
  }else {
    $.ajax ({
      type : "POST",
      url : url,
      data:data,
      contentType: 'application/json;charset=UTF-8',
      success: function(response) {
        if (response.status === '200')
        {
          obj.text('取消关注').addClass('active');
        } else
        {alert('fail');}
      }});
  }
}
$(document).ready(function(){
  $('button.topic-following').click(function(){
    var _$this = $(this);
    var url = "/following/topics";
    var data = JSON.stringify({
      topicId:_$this.attr("data-id"),
    });
    Follow(_$this,data,url);
  });
  $('button.tag-following').click(function(){
    var _$this = $(this);
    var url = "/following/tags";
    var data = JSON.stringify({
      tagId:_$this.attr("data-id"),
    });
    Follow(_$this,data,url);
  });
  $('button.user-following').click(function(){
    var _$this = $(this);
    var url = "/following/users";
    var data = JSON.stringify({
      userId:_$this.attr("data-id"),
    });
    Follow(_$this,data,url);
  });
  $('button.collect-following').click(function(){
    var _$this = $(this);
    var url = "/following/collects";
    var data = JSON.stringify({
      collectId:_$this.attr("data-id"),
    });
    Follow(_$this,data,url);
  });
});
function DoCollect(collect_url) {
  $(document).ready(function(){
    $('button#edit-collect').click(function() {
      var data = JSON.stringify({
        name:$('#name').val(),
        description:$('#description').val(),
        is_hidden:$("input[name='is_hidden']:checked").val()
      });
      $.ajax ({
        type : "PUT",
        url : collect_url,
        data:data,
        contentType: 'application/json;charset=UTF-8',
        success: function(response) {
          if (response.status === '200')
          {
            window.location.href = collect_url;
          }
        }
      });
    });
    $('button#delete-collect').click(function() {
      $.ajax ({
        type : "DELETE",
        url : collect_url,
        data:JSON.stringify(),
        contentType: 'application/json;charset=UTF-8',
        success: function(response) {
          if (response.status === '200')
          {
            window.location.href = collect_url;
          }
        }
      });
    });
    $('#delete-from-collect').click(function() {
      var _$this = $(this);
      var topicId = _$this.attr('data-id');
      var data = JSON.stringify({
        topicId:topicId
      });
      $.ajax ({
        type : "DELETE",
        url : '/topic/' + topicId + '/collect',
        data:data,
        contentType: 'application/json;charset=UTF-8',
        success: function(response) {
          if (response.status === '200')
          {
            _$this.parent().remove();
          }
        }
      });
    });
  });
}
