const API_KEY = "8fff672777a24a39a1ee4de44e0dc49e";
const url = "https://newsapi.org/v2/everything?q=";
// 8fff672777a24a39a1ee4de44e0dc49e
window.addEventListener("load", () => fetchNews("India"));

function reload() {
    window.location.reload();
}

async function fetchNews(query) {
    const res = await fetch(`${url}${query}&apiKey=${API_KEY}`);
    const data = await res.json();
    bindData(data.articles);
}

function bindData(articles) {
    const cardsContainer = document.getElementById("cards-container");
    const newsCardTemplate = document.getElementById("template-news-card");

    cardsContainer.innerHTML = "";

    articles.forEach((article) => {
        if (!article.urlToImage) return;
        const cardClone = newsCardTemplate.content.cloneNode(true);
        fillDataInCard(cardClone, article);
        cardsContainer.appendChild(cardClone);
    });
}

function fillDataInCard(cardClone, article) {
    const newsImg = cardClone.querySelector("#news-img");
    const newsTitle = cardClone.querySelector("#news-title");
    const newsSource = cardClone.querySelector("#news-source");
    const newsDesc = cardClone.querySelector("#news-desc");

    newsImg.src = article.urlToImage;
    newsTitle.innerHTML = article.title;
    newsDesc.innerHTML = article.description;

    const date = new Date(article.publishedAt).toLocaleString("en-US", {
        timeZone: "Asia/Jakarta",
    });

    newsSource.innerHTML = `${article.source.name} · ${date}`;

    cardClone.firstElementChild.addEventListener("click", () => {
        window.open(article.url, "_blank");
    });
}

let curSelectedNav = null;
function onNavItemClick(id) {
    fetchNews(id);
    const navItem = document.getElementById(id);
    curSelectedNav?.classList.remove("active");
    curSelectedNav = navItem;
    curSelectedNav.classList.add("active");
}
function onNavItemClick1(topic) {
    // This code is for client-side highlighting before navigating.
    // Highlight the selected nav item
    const navItems = document.querySelectorAll('.nav-item');
    navItems.forEach(item => {
        item.classList.remove('active-nav-item'); // remove the class from all items
        if(item.id === 'nav-' + topic) {
            item.classList.add('active-nav-item'); // add the class to the one that was clicked
        }
    });

    // The following code is for server-side rendering.
    // Construct the URL for the new page.
    const topicUrls = {
        'auto': 'https://www.prnewswire.com/news-releases/automotive-transportation-latest-news/automotive-transportation-latest-news-list/?page=1&pagesize=100',
        'media': 'https://www.prnewswire.com/news-releases/entertainment-media-latest-news/entertainment-media-latest-news-list/?page=1&pagesize=100',
        'bt': 'https://www.prnewswire.com/news-releases/business-technology-latest-news/business-technology-latest-news-list/?page=1&pagesize=100',
        'finance': 'https://www.prnewswire.com/news-releases/financial-services-latest-news/financial-services-latest-news-list/?page=1&pagesize=100',
        'general': 'https://www.prnewswire.com/news-releases/general-business-latest-news/general-business-latest-news-list/?page=1&pagesize=100'
    };
    let scrapeUrl = topicUrls[topic];

    // Navigate to the new page, passing along the selected topic.
    window.location.href = `/scrape?topic=${topic}&url=${encodeURIComponent(scrapeUrl)}`;
}



const searchButton = document.getElementById("search-button");
const searchText = document.getElementById("search-text");

searchButton.addEventListener("click", () => {
    const query = searchText.value;
    if (!query) return;
    fetchNews(query);
    curSelectedNav?.classList.remove("active");
    curSelectedNav = null;
});
