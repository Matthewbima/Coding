// Gaming Server Bot Project
console.log("Welcome to the Gaming Server Bot! Let's manage our game stats and server information!");

// Introducing a player and game information
var serverName = 'Valorant Legends Server';
var serverAge = 2;
console.log(`Server Name: ${serverName}, Age: ${serverAge} years`);

// Player introduction using variables and string interpolation
var playerName = 'Phoenix';
var friendName = 'Jett';
var hobby = 'playing Valorant';
console.log(`Hello, I'm ${playerName}, and my best friend ${friendName} and I love ${hobby} together!`);

// Server greetings and functions with parameters
function welcomeMessage() {
    return "Welcome to the most epic game server!";
}
const farewellMessage = () => "Thanks for gaming with us!";

console.log(welcomeMessage());
console.log(farewellMessage());

// Mathematical operations (adding, subtracting, etc.) for player stats
const increaseScore = (score, points) => console.log(`Increasing score by ${points}, new score: ${score + points}`);
const decreaseScore = (score, points) => console.log(`Decreasing score by ${points}, new score: ${score - points}`);
const multiplyScore = (score, multiplier) => console.log(`Multiplying score by ${multiplier}, new score: ${score * multiplier}`);
const divideScore = (score, divider) => console.log(`Dividing score by ${divider}, new score: ${score / divider}`);

increaseScore(50, 20);
decreaseScore(70, 10);
multiplyScore(60, 2);
divideScore(120, 4);

// Using the file system to check for a game log file
const fs = require('fs');
fs.readFile('./gameLog.txt', 'utf8', (err, data) => {
    if (err) {
        console.log("Error reading game log:", err);
    } else {
        console.log("Game Log:", data);
    }
});

// Checking the server's memory status
const os = require('os');
const totalMemory = os.totalmem();
const freeMemory = os.freemem();
console.log(`Server Free Memory: ${freeMemory} bytes`);
console.log(`Server Total Memory: ${(totalMemory / 1048576).toFixed(2)} Megabytes`);

// Displaying server file path information
const path = require('path');
const serverFilePath = path.parse(__filename);
console.log("Current Server File Path Information:", serverFilePath);
