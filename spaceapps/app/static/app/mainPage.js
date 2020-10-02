document.addEventListener('DOMContentLoaded',  function(){
    
    //Posts
    fetch('/getPosts/all')
    .then(response => response.json())
    .then(posts => {
        
        posts.forEach(post => {
            
            const post_item = document.createElement("div");
            post_item.className = "post-item";
            post_item.innerHTML = ` <h3 class = "post-title">${post.owner.username}</h3>
                                    <h3 class = "post-description">${post.description}</h3> 
                                    <video class = "post-video" src = ${post.video} type="video/mp4" width = "400px" height = "400px" controls="controls"></video>
            `
            document.querySelector(".post-container").appendChild(post_item);
        })
    })

    //Articles
    fetch('/getArticles')
    .then(response => response.json())
    .then(articles => {
        articles.forEach(article => {
            const articleItem = document.createElement("div");
            articleItem.className = "article-item";
            articleItem.innerHTML = `<h3>${article.title}</h3>
                                    <img src = ${article.image} alt = "No Image D:" />`

            document.querySelector(".article-container").appendChild(articleItem);
        })
    })
    
    //Categories
    
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
    
});