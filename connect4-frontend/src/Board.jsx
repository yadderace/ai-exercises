import React, { useState } from "react";
import "./Board.css";

const ROWS = 6;
const COLS = 7;

const checkWinner = (grid) => {
  // Check horizontal, vertical, and diagonal win conditions
  for (let row = 0; row < ROWS; row++) {
    for (let col = 0; col < COLS; col++) {
      const player = grid[row][col];
      if (!player) continue;
      
      // Check horizontal
      if (col + 3 < COLS && player === grid[row][col + 1] && player === grid[row][col + 2] && player === grid[row][col + 3]) {
        return player;
      }
      
      // Check vertical
      if (row + 3 < ROWS && player === grid[row + 1][col] && player === grid[row + 2][col] && player === grid[row + 3][col]) {
        return player;
      }
      
      // Check diagonal (bottom-left to top-right)
      if (row - 3 >= 0 && col + 3 < COLS && player === grid[row - 1][col + 1] && player === grid[row - 2][col + 2] && player === grid[row - 3][col + 3]) {
        return player;
      }
      
      // Check diagonal (top-left to bottom-right)
      if (row + 3 < ROWS && col + 3 < COLS && player === grid[row + 1][col + 1] && player === grid[row + 2][col + 2] && player === grid[row + 3][col + 3]) {
        return player;
      }
    }
  }
  return null;
};

const Board = () => {
  const [grid, setGrid] = useState(Array(ROWS).fill().map(() => Array(COLS).fill(null)));
  const [currentPlayer, setCurrentPlayer] = useState("red");
  const [winner, setWinner] = useState(null);

  const handleClick = (colIndex) => {
    if (winner) return; // Stop game if there's a winner
    
    const newGrid = grid.map(row => [...row]);
    
    for (let row = ROWS - 1; row >= 0; row--) {
      if (!newGrid[row][colIndex]) {
        newGrid[row][colIndex] = currentPlayer;
        setGrid(newGrid);
        const gameWinner = checkWinner(newGrid);
        if (gameWinner) {
          setWinner(gameWinner);
        } else {
          setCurrentPlayer(currentPlayer === "red" ? "yellow" : "red");
        }
        break;
      }
    }
  };

  const resetGame = () => {
    setGrid(Array(ROWS).fill().map(() => Array(COLS).fill(null)));
    setCurrentPlayer("red");
    setWinner(null);
  };

  return (
    <div className="container">
      <h1 className="title">Connect 4</h1>
      <div className="board">
        {grid.map((row, rowIndex) => (
          row.map((cell, colIndex) => (
            <div 
              key={`${rowIndex}-${colIndex}`} 
              className="cell" 
              onClick={() => handleClick(colIndex)}
            >
              <div className={`piece ${cell || "empty"}`}></div>
            </div>
          ))
        ))}
      </div>
      {winner && <h2 className="winner">{winner.toUpperCase()} Wins!</h2>}
      <button className="reset-button" onClick={resetGame}>Reset Game</button>
    </div>
  );
};

export default Board;