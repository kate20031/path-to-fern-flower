let playerCoins = 10;
let playerLives = 3;

function startGame() {
    document.getElementById("start-screen").style.display = "none";
    document.getElementById("game-screen").style.display = "block";
    encounterCharacter(); // Start character encounter when the game starts
}

function chooseHuman() {
    alert("You chose Human!");
    playerCoins -= 1;  // Choosing Human costs 1 coin
    playerLives -= 1;  // Costs 1 life

    document.getElementById("player-coins").innerText = playerCoins;
    document.getElementById("player-lives").innerText = playerLives;

    document.getElementById("player-choice").innerHTML = "You chose Human.";
    document.getElementById("dialogue").style.display = "none"; // Hide dialogue after choice
}

function chooseSpirit() {
    alert("You chose Spirit!");
    playerCoins += 2;  // Choosing Spirit gives 2 coins
    playerLives -= 1;  // Costs 1 life

    document.getElementById("player-coins").innerText = playerCoins;
    document.getElementById("player-lives").innerText = playerLives;

    document.getElementById("player-choice").innerHTML = "You chose Spirit.";
    document.getElementById("dialogue").style.display = "none"; // Hide dialogue after choice
}

function showCharacter() {
    const character = document.getElementById("character");
    character.style.display = "block"; // Show the character image
}

function encounterCharacter() {
    showCharacter(); // Show character on screen
    const dialogueBox = document.getElementById("dialogue");
    dialogueBox.style.display = "block"; // Show the dialogue box
    document.getElementById("character-dialogue").innerText = "Do you trust this being? Choose wisely!";
}
