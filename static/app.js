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
            for (let i = 0; i < cardQuantity; i++) {
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
            }
        });
    });
});

document.getElementById("generate_random_deck_button").addEventListener("click", function () {
    // only fetches white and black cards for now
    /* Old code below

    document.getElementById("card_entry_box").value = "fetching...";
    fetch("/random?colors=W,B")
    .then(function (response) {
        return response.text();
    }).then(function (body) {
        document.getElementById("card_entry_box").value = body;
    });
    */


    document.getElementById("card_entry_box").value = "fetching...";

    // Fetch the list of all card names from the Scryfall API
    // TODO: CACHE THIS LIST SOMEWHERE SO WE DONT HAVE TO CALL MULTIPLE TIMES FOR IT
    fetch("https://api.scryfall.com/catalog/card-names")
    .then(function (response) {
        return response.json();
    })
    .then(function (json) {
        let cardNames = json.data;
        let cardList = "";
        // Generate a random decklist of 40 cards
        // TODO: CHECK IF THE CARD IS ALREADY IN THE LIST AND UPDATE QUANTITY INSTEAD OF ADDING A NEW LINE
        for (let i = 0; i < 40; i++) {
            let randomIndex = Math.floor(Math.random() * cardNames.length);
            // Add a new line after each card except the last one to prevent an extra blank line
            if (i !== 40) {
                // Get another card if it's already in the list
                while (cardList.includes(cardNames[randomIndex])) {
                    randomIndex = Math.floor(Math.random() * cardNames.length);
                }
                cardList += "1 " + cardNames[randomIndex] + "\n";
            } else {
                //cardList += "1 " + cardNames[randomIndex];
            }
        }

        //TODO:Mana Curve possibly
        cardList += "4 Plains\n";
        cardList += "4 Island\n";
        cardList += "4 Swamp\n";
        cardList += "4 Mountain\n";
        cardList += "4 Forest";

        // Add the complete decklist to the textArea
        document.getElementById("card_entry_box").value = cardList;
    });

});

document.getElementById("deck_save_button").addEventListener("click", function () {
    let body = document.getElementById("card_entry_box").value;
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
        document.getElementById("deck_list").textContent = JSON.stringify(json);
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
