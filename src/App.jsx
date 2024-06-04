import React, { useState } from 'react';
import './App.css';

function App() {
  const [board, setBoard] = useState(Array(9).fill(' '));
  const [status, setStatus] = useState('Tem jogo');
  const [currentPlayer, setCurrentPlayer] = useState('x');

  const handleClick = async (index) => {
    const newBoard = board.slice();
    if (newBoard[index] === ' ' && status === 'Tem jogo') {
      newBoard[index] = currentPlayer;  // Jogador atual faz uma jogada
      setBoard(newBoard);

      const response = await fetch('http://127.0.0.1:5000/evaluate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ board: newBoard }),
      });
      const result = await response.json();
      setStatus(result.status);

      if (result.status === 'Tem jogo') {
        // Alterna jogador
        setCurrentPlayer(currentPlayer === 'x' ? 'o' : 'x');
      }
    }
  };

  return (
    <div className="container">
      <h1 className="title">Jogo da Velha</h1>
      <div className="buttonContainer">
        {board.map((value, index) => (
          <button
            key={index}
            className="gameButton"
            onClick={() => handleClick(index)}
          >
            {value}
          </button>
        ))}
      </div>
      <div className="gameInfo">{status}</div>
    </div>
  );
}

export default App;
