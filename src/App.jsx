/* eslint-disable no-unused-vars */
import React, { useState } from "react";
import axios from 'axios';
import "./App.css";

export function App() {
  const [board, setBoard] = useState(Array(9).fill(null));
  const [player, setPlayer] = useState(null);
  const [playerStatus, setPlayerStatus] = useState('Próximo Jogador é o X');
  const [status, setStatus] = useState('Tem jogo');

  const handleClick = async (index) => {
    const newBoard = board.slice();
    if (newBoard[index] || status !== 'Tem jogo') return;
  
    try {
      nextPlayer(newBoard)
        .then(function () {
          newBoard[index] = player;
          setBoard(newBoard);
          evaluateBoard(newBoard);
        })
        .catch (function (error) {
          console.error("CACETE!", error);
        });
      
    } catch (error) {
      console.error("Erro ao obter o próximo jogador", error);
    }
  };
  
  const nextPlayer = async (board) => {
    try {
      const response = await axios.post('http://localhost:5000/next-player', { board });
      const nextPlayer = response.data.player;
      setPlayer(nextPlayer);
    } catch (error) {
      console.error("Houve um erro na avaliação do próximo jogador", error);
    }
  };

  const evaluateBoard = async (board) => {
    try {
      const response = await axios.post('http://localhost:5000/evaluate', { board });
      const gameStatus = response.data.status;
      if (gameStatus === 'Tem jogo') {
        setPlayerStatus(`Próximo Jogador é o ${player}`);
      } else {
        setStatus(gameStatus);
      }
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
      <div className="gameInfo">{playerStatus}</div>
      <div className="gameInfo">{status}</div>
    </div>
  );
}
