document.getElementById("deck_card_list").hidden = false;
document.getElementById("deck_image_list").hidden = true;

document.getElementById("card_entry_button").addEventListener("click", function () {
    let cardList = document.getElementById("card_entry_box").value;
    let cardArray = cardList.split("\n");

    document.getElementById("deck_card_list").innerHTML = "";
    document.getElementById("deck_image_list").innerHTML = "";

    // Loop through the list of cards inside the textArea
    cardArray.forEach(function(card) {
        cardLine = card.split(" ");
        let cardQuantity = 0;
        let cardName = "";

        // Check if the line begins with a quantity, otherwise assume a quantity of 1
        if (parseInt(cardLine[0])) {
            cardQuantity = parseInt(cardLine[0]);
            cardName = cardLine.slice(1).join(" ");
        } else {
            cardQuantity = 1;
            cardName = card;
        }

        // Replace spaces in query with '+'
        query = cardName.replace(/ /g, "+");

        // Query the Scryfall API for the official card name and update the decklist accordingly
        url = `https://api.scryfall.com/cards/named?fuzzy=${query}`;
        // url = encodeURI(url);
        fetch(url)
        .then(response => {
            if(!response.ok) {
                alert("Error: Card not found: \"" + cardName + "\"");
                throw Error(response.status);
            }
            //alert(response.status);
            return response.json();
        })
        .then(function (json) {
            // Create a new list item for each card
            let listItem = document.createElement("li");
            listItem.textContent = `${cardQuantity} ${json.name}`;
            document.getElementById("deck_card_list").appendChild(listItem);

            // Create a new image for each card
            let image = document.createElement("img");
            if (json.layout != "normal") {
                image.src = json.card_faces[0].image_uris.normal;
            } else {
                image.src = json.image_uris.normal;
            }
            image.alt = json.name;
            image.title = json.name;
            image.style = "width: 189px; margin: 5px;";
            document.getElementById("deck_image_list").appendChild(image);
        });
    });
});

document.getElementById("generate_random_deck_button").addEventListener("click", function () {
    // only fetches white and black cards for now
    let card_entry_box = document.getElementById("card_entry_box")
    card_entry_box.value = "";
    card_entry_box.placeholder = "fetching...";
    
    fetch("/random")
    .then(function (response) {
        return response.text();
    }).then(function (body) {
        document.getElementById("card_entry_box").value = body;
    });
});

document.getElementById("deck_save_button").addEventListener("click", function () {
    let body = JSON.stringify({'name': document.getElementById("deck_name_entry").value, 'deck_list': document.getElementById("card_entry_box").value});
    console.log(body);
    fetch("/save", {body, method: "POST", headers: {"Content-Type": "application/json"}})
    .then(function (response) {
        return response;
    }).then(function (response) {
        if (response.status === 400) {
            alert("Deck name already exists!");
        }
    });
});

document.getElementById("deck_load_button").addEventListener("click", function () {
    let name = document.getElementById("deck_name_entry").value;
    fetch(`/load?name=${name}`)
    .then(function (response) {
        return response.json();
    }).then(function (json) {
        console.log(json);
        document.getElementById("card_entry_box").value = json[0].deck_list;
    });
});

document.getElementById("text_view_button").addEventListener("click", function () {
    document.getElementById("deck_card_list").hidden = false;
    document.getElementById("deck_image_list").hidden = true;
});

document.getElementById("image_view_button").addEventListener("click", function () {
    document.getElementById("deck_card_list").hidden = true;
    document.getElementById("deck_image_list").hidden = false;
});

document.getElementById("login_button").addEventListener("click", function () {
    let username = document.getElementById("username_entry").value;
    let password = document.getElementById("password_entry").value;

    fetch("/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: `username=${encodeURIComponent(username)}&password=${encodeURIComponent(password)}`
    })
    .then(function (response) {
        return response;
    }).then(function (response) {
        if (response.status === 200) {
            document.getElementById("login_button").style.backgroundColor = "green";
            //alert("Login successful as " + response.username);
        } else {
            console.log(response);
            document.getElementById("login_button").style.backgroundColor = "red";
            alert("Invalid username or password");
        }
    });
});
