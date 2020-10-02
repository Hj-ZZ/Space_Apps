
var followers_count;
var is_followed;
var user_id;
document.addEventListener('DOMContentLoaded', function () {
  alert("hello world")
  try {
      follow_btn = document.querySelector('.follow-btn');
      user_id = parseInt(follow_btn.dataset.user_id)
      follow_btn.addEventListener('click',()=>follow(user_id))

      // get data from the dataset
      is_followed = follow_btn.dataset.is_followed === "True"

      followers_count =  parseInt(follow_btn.dataset.followers_count)

      //creating and adding event listener to the follow btn
      updateFollowStats();


    } catch (error) {

    }
    // By default the index page is loaded

});


function updateFollowStats(){

    document.querySelector("#followers-cnt").innerText = followers_count;
    document.querySelector('#follow-btn').innerHTML = is_followed ? "unfollow":"follow";

}
function follow(user_id){

  fetch(`/follow/${user_id}`, {
          method: 'POST',
          body: JSON.stringify({
              user: user_id,
          })
      })
      .then(response => response.json())
      .then(result => {
          console.log(result);
          followers_count = result.followers_count
          is_followed = result.is_followed
          updateFollowStats();
    });

}
