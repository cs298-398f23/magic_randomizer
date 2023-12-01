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

document.getElementById("deck_entry_button").addEventListener("click", function () {
    let body = document.getElementById("deck_entry_box").value;
    fetch("/save", {body, method: "POST"})
    .then(function (response) {
        return response;
    }).then(function (response) {
        if (response.status === 200) {
            document.getElementById("deck_entry_button").style.backgroundColor = "green";
        } else {
            console.log(response);
            document.getElementById("deck_entry_button").style.backgroundColor = "red";
        }
    });
});

document.getElementById("deck_load_button").addEventListener("click", function () {
    fetch("/load")
    .then(function (response) {
        return response.json();
    }).then(function (json) {
        document.getElementById("decks").textContent = JSON.stringify(json);
    });
});

document.getElementById("random_button").addEventListener("click", function () {
    fetch("/random?colors=W,B")
    .then(function (response) {
        return response.text();
    }).then(function (body) {
        document.getElementById("random").textContent = body;
    });
});
