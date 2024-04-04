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
