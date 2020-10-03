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



  //Posts
  fetch('/getPosts/all')
  .then(response => response.json())
  .then(posts => {

      posts.forEach(post => {

          const post_item = document.createElement("div");
          post_item.className = "post-item";
          post_item.innerHTML = `
                                    <a href = "profile/${post.owner.id}"class = "post-owner" data-id = "${post.owner.id}">${post.owner.username}</a>
                                    <h2 class = "post-description">${post.description}</h2>
                                    <video class = "post-video" src = ${post.video} type="video/mp4" controls="controls"></video>
                                    <div class = "like-button" data-id = "${post.id}" data-isLiked = "true">
                                        ${post.like_count} like(s)
                                    </div>

          `
          document.querySelector(".main-posts").appendChild(post_item);
      })

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

  //Categories
  /*
  fetch('/getCategories')
  .then(response => response.json())
  .then(categories => {
      categories.forEach(category => {

          const categoryItem = document.createElement("div");
          categoryItem.className = "category-item";
          categoryItem.innerHTML = category.name;

          document.querySelector(".categories-container").appendChild(categoryItem);
      })
  })
  */

  function like(e){
      var likeButton = e.currentTarget;

      var post_id = likeButton.dataset.id;

      var isLiked = likeButton.dataset.isLiked === 'true'

      fetch(`/like/${post_id}`, {
          method: 'PUT',
      }).then(response => response.json())
      .then(result => {
          console.log(result);
          likeButton.innerHTML = `${result.like_count} like(s)`;

      })
  }


});
