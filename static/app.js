document.getElementById("card_entry_button").addEventListener("click", function () {
    let query = document.getElementById("card_entry_box").value;
    url = `https://api.scryfall.com/cards/search?q=${query}`;
    url = encodeURI(url)
    fetch(url)
        .then(function (response) {
            return response.json();
        }).then(function (json) {
            document.getElementById("card_image").src = json.data[0].image_uris.normal;
        });
});