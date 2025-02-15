import React, { useState } from "react";
import "./Board.css";

const ROWS = 6;
const COLS = 7;

const Board = () => {
  const [grid, setGrid] = useState(Array(ROWS).fill().map(() => Array(COLS).fill(null)));
  const [winner, setWinner] = useState(null);
  const [winningPositions, setWinningPositions] = useState([]);

  const handleClick = async (colIndex) => {
    const newGrid = grid.map(row => [...row]);
    console.log(newGrid);
    try {
      const response = await fetch(`http://localhost:8000/play?player_col=${colIndex}`);
      const data = await response.json();
      console.log(data);
      if (data.player_last_move) {
        const [row, col] = [data.player_last_move.row, data.player_last_move.col];
        newGrid[row][col] = "red";
      }

      if (data.ai_last_move) {
        const [row, col] = [data.ai_last_move.row, data.ai_last_move.col];
        newGrid[row][col] = "yellow";
      }

      setGrid(newGrid);

      if (data.winner) {
        setWinner(data.winner === 1 ? "red" : "yellow");
        setWinningPositions(data.winning_positions || []);
      }

    } catch (error) {
      console.error("Error playing move:", error);
    }
  };

  const resetGame = async () => {
    try {
      const response = await fetch(`http://localhost:8000/reset`);
      setGrid(Array(ROWS).fill().map(() => Array(COLS).fill(null)));
      setWinner(null);
      setWinningPositions([]);
    } catch (error) {
      console.error("Error resetting game:", error);
    }
  };

  const isWinningPosition = (row, col) => {
    return winningPositions.some(pos => pos.row === row && pos.col === col);
  };

  return (
    <div className="container">
      <h1 className="title">Connect 4</h1>
      <div className="board">
        {grid.map((row, rowIndex) => (
          row.map((cell, colIndex) => (
            <div 
              key={`${rowIndex}-${colIndex}`} 
              className={`cell ${isWinningPosition(rowIndex, colIndex) ? `winning-cell ${winner}-winning-cell` : ''}`} 
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