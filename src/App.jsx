/* eslint-disable no-unused-vars */
import React, { useState } from "react";
import axios from 'axios';
import "./App.css";

export function App() {
  const [board, setBoard] = useState(Array(9).fill(null));
  const [status, setStatus] = useState('Next player: X');

  const handleClick = (index) => {
    const newBoard = board.slice();
    if (newBoard[index] || status !== 'Next player: X') return;
    newBoard[index] = 'X';
    setBoard(newBoard);
    evaluateBoard(newBoard);
  };

  const evaluateBoard = async (board) => {
    try {
      const response = await axios.post('http://localhost:5000/evaluate', { board });
      setStatus(response.data.status);
    } catch (error) {
      console.error("Houve um erro na avaliação do tabuleiro", error);
    }
  };

  const renderCell = (index) => {
    return (
      <button className="gameButton" onClick={() => handleClick(index)}>
        {board[index]}
      </button>
    );
  };

  return (
    <div className="container">
      <div className="title">Jogo da Velha</div>
      <div className="buttonContainer">
        {renderCell(0)}{renderCell(1)}{renderCell(2)}
        {renderCell(3)}{renderCell(4)}{renderCell(5)}
        {renderCell(6)}{renderCell(7)}{renderCell(8)}
      </div>
      <div className="gameInfo">{status}</div>
    </div>
  );
}
