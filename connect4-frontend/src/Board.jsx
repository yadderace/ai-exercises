import React, { useState } from "react";
import "./Board.css";

const ROWS = 6;
const COLS = 7;

const Board = () => {
  const [grid, setGrid] = useState(Array(ROWS).fill().map(() => Array(COLS).fill(null)));
  const [currentPlayer, setCurrentPlayer] = useState("red");

  const handleClick = (colIndex) => {
    const newGrid = grid.map(row => [...row]);
    
    for (let row = ROWS - 1; row >= 0; row--) {
      if (!newGrid[row][colIndex]) {
        newGrid[row][colIndex] = currentPlayer;
        setGrid(newGrid);
        setCurrentPlayer(currentPlayer === "red" ? "yellow" : "red");
        break;
      }
    }
  };

  return (
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
  );
};

export default Board;
