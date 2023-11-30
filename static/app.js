document.getElementById("card_entry_button").addEventListener("click", function () {
    let cardList = document.getElementById("card_entry_box").value;
    let cardArray = cardList.split("\n");

    // Clear the decklist
    document.getElementById("deck_card_list").innerHTML = "";

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

        // Query the Scryfall API for the official card name and update the decklist accordingly
        url = encodeURI(`https://api.scryfall.com/cards/search?q=${query}`);
        fetch(url)
            .then(function (response) {
                return response.json();
            }).then(function (json) {
                let listItem = document.createElement("li");
                listItem.appendChild(document.createTextNode(cardQuantity + " " + json.data[0].name));
                document.getElementById("deck_card_list").appendChild(listItem);
            });
    });
});

document.getElementById("generate_random_deck_button").addEventListener("click", function () {
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
});

document.getElementById("deck_list_button").addEventListener("click", function () {
    fetch("/load")
    .then(function (response) {
        return response.json();
    }).then(function (json) {
        document.getElementById("deck_list").textContent = JSON.stringify(json);
    });
});

document.getElementById("text_view_button").addEventListener("click", function () {

});

document.getElementById("image_view_button").addEventListener("click", function () {
    
});