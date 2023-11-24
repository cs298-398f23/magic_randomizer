document.getElementById("card_entry_button").addEventListener("click", function () {
    url = "https://api.scryfall.com/cards/search?q=Rhystic%20Study";
    fetch(url)
        .then(function (response) {
            return response.json();
        }).then(function (json) {
            document.getElementById("card_image").src = json.data[0].image_uris.normal;
        });
});