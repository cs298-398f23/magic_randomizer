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
            query = cardLine.slice(1).join(" ");
        } else {
            cardQuantity = 1;
            query = card;
        }

        // Replace spaces in query with '+'
        query = cardName.replace(/ /g, "+");

        // Query the Scryfall API for the official card name and update the decklist accordingly
        url = `https://api.scryfall.com/cards/search?q=${query}`;
        url = encodeURI(url);
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


            });
    });

    if (document.getElementById("deck_card_list").innerHTML === "") {
        document.getElementById("deck_card_list").innerHTML = "No Cards Loaded";
    }
    if (document.getElementById("deck_image_list").innerHTML === "") {
        document.getElementById("deck_image_list").innerHTML = "No Images Loaded";
    }
});

document.getElementById("generate_random_deck_button").addEventListener("click", function () {
    // only fetches white and black cards for now
    let card_entry_box = document.getElementById("card_entry_box")
    card_entry_box.value = "";
    card_entry_box.placeholder = "fetching...";
    
    fetch("/random?colors=W,B")
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
