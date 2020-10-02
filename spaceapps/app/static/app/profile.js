//{{ request.user.id|json_script:"user_id" }} Should be added to the Html
// TODO: have to see how to handle the is_followed
const user_id = JSON.parse(document.getElementById('user_id').textContent);
var followers_count;
var is_followed;
document.addEventListener('DOMContentLoaded', function () {
    user_clicked = parseInt(follow_btn.dataset.user_id)
    load_profile(user_clicked)


});

function load_profile(user_clicked) {
    fetch(`/profile/${user_clicked}`)
        .then(response => response.json())
        .then(user => {
            // Have to see with Ali whether we will create the element here or not
            followers_count = user.followers_count

            if (user_id === user.id) {
                // create the follow button and add event listener
                // follow_btn.addEventListener('click', () => follow())
            } else {
                // edit
            }

        })
}

function updateFollowStats() {

    document.querySelector("#followers_count").innerHTML = followers_count;
    document.querySelector('#follow-btn').innerHTML = is_followed ? "unfollow" : "follow";
    document.querySelector('#follow-btn').style.backgroundColor = is_followed ? "red" : "blue";

}

function follow() {
    fetch('/follow/', {
        method: 'POST',
        body: JSON.stringify({
            user: user_clicked,
        })
    })
        .then(response => response.json())
        .then(result => {
            // Print result
            console.log(result);
            followers_count = result.followers_count
            is_followed = result.is_followed
            updateFollowStats();
        });

}
