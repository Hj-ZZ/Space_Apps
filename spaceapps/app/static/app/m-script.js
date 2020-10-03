//Post Stuff

const realFileBtn = document.getElementById("real-file");
const customBtn = document.getElementById("custom-button");
const customTxt = document.getElementById("custom-text");
customBtn.addEventListener("click", function() {
  realFileBtn.click();
});
realFileBtn.addEventListener("change", function() {
  if (realFileBtn.value) {
    customTxt.innerHTML = realFileBtn.value.match(
      /[\/\\]([\w\d\s\.\-\(\)]+)$/
    )[1];
  } else {
    customTxt.innerHTML = "No file chosen, yet.";
  }
});

document.addEventListener('DOMContentLoaded',  function(){


  console.log("hello")
  //Posts
  fetch('/getPosts/all')
  .then(response => response.json())
  .then(posts => {
    const container = document.createElement("div");

      posts.forEach(post => {
          container.className = "container-posts"

          const post_item = document.createElement("div");

          post_item.className = "post-item";
          post_item.innerHTML = `
                                    <div class = "user-post">
                                    <img class = "user-image" src="${post.owner.image}"></img>
                                    <a href = "profile/${post.owner.id}"class = "post-owner" data-id = "${post.owner.id}">${post.owner.username}</a>
                                    </div>
                                    <video class = "post-video" src = ${post.video} type="video/mp4" controls="controls"></video>
                                    <div class = "interraction">

                                    <div class = "like-button" data-id = "${post.id}" data-isLiked = "true">
                                         <i class="fas fa-heart fa-lg"></i>  ${post.like_count}


                                    </div>
                                    <a class="btn-explore" href="${post.url_article}"target="_blank">explore</a>
                                    <div>`

          container.appendChild(post_item);
      })
      document.querySelector(".main-posts").appendChild(container)
      document.querySelectorAll('.like-button').forEach(div =>
          div.addEventListener('click', function(div) {

              like(div);

          })
      );
  })






  //Articles

  fetch('/getArticles')
  .then(response => response.json())
  .then(articles => {
      articles.forEach(article => {
          const articleItem = document.createElement("div");
          articleItem.className = "article-item";
          articleItem.innerHTML = `<h2>${article.title}</h2>
                                  <img src = ${article.image} alt = "No Image D:" />`


          document.querySelector(".nasa-app").appendChild(articleItem);
      })
  })


function like(e){
    var likeButton = e.currentTarget;

    var post_id = likeButton.dataset.id;

    var isLiked = likeButton.dataset.isLiked === 'true'

    fetch(`/like/${post_id}`, {
        method: 'PUT',
    }).then(response => response.json())
    .then(result => {
        console.log(result);
        likeButton.innerHTML = `<i class="fas fa-heart fa-lg"></i> ${result.like_count}`;
        console.log(likeButton)
        likeButton.querySelector('i').style.color = result.is_liked ? "green":"gray";
        console.log(result.is_liked)

    })
}


});
