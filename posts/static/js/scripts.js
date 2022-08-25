////////////////////////////
// JavaScript for Posts Page
////////////////////////////

$(function () {
  // Executed when js-menu-icon js clicked
  $(".js-menu-icon").click(function () {
    // $(this) : Self element, namely div.js-menu-icon
    // next() : Next to div.js-menu-icon, namely div.menu
    // toggle() : Switch show and hide
    $(this).next().toggle();
  });
});

////////////////////////////
// LIKES
////////////////////////////

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
const csrftoken = getCookie("csrftoken");

$(function () {
  // Global valuable
  var is_liked = false;

  // Clicked like icon
  $(".js-like").click(function () {
    var post_id = $(this).data("like");
    var heart_icon_obj = $(this).find("img");
    var heart_icon_url = heart_icon_obj.attr("src");
    var like_count_obj = $(this).parent().find(".js-like-count");
    var like_count = Number(like_count_obj.html());

    if (heart_icon_url == "/static/img/icon-heart-twitterblue.svg") {
      // It has not been liked
      // Increase the count of likes
      $.ajax({
        url: "/tweetLikeAdd/" + post_id + "/",
        method: "POST",
        data: { post_id: post_id },
        headers: { "X-CSRFToken": csrftoken },
        mode: "same-origin",
      })
        // Successful
        .done((data) => {
          // Increase
          var new_like_count = like_count + 1;
          like_count_obj.html(new_like_count);
          // Change the icon to fill
          heart_icon_obj.attr("src", "/static/img/heart-fill.png");
        })
        // Failure
        .fail((data) => {
          alert("Error");
          console.log(data);
        });
    } else {
      // It has been liked
      // Decrease the count of likes
      $.ajax({
        url: "/tweetLikeSubtract/" + post_id + "/",
        method: "POST",
        data: { post_id: post_id },
        headers: { "X-CSRFToken": csrftoken },
        mode: "same-origin",
      })
        // Successful
        .done((data) => {
          // Decrease
          var new_like_count = like_count - 1;
          like_count_obj.html(new_like_count);
          // Change the button to unfill
          heart_icon_obj.attr("src", "/static/img/icon-heart-twitterblue.svg");
        })
        // Failure
        .fail((data) => {
          alert("Error");
          console.log(data);
        });
    }
  });
});

let cancel = () => {
  return location.assign("/");
};
