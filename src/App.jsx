/* eslint-disable no-unused-vars */
import React, { useState } from "react";
import axios from 'axios';
import "./App.css";

export function App() {
  const [buttons, setButtons] = useState(Array(9).fill(null));
  const [isXNext, setIsXNext] = useState(true);

  const handleClick = (index) => {
    if (buttons[index] !== null) {
      return;
    }

    const newButtons = buttons.slice();
    newButtons[index] = isXNext ? "X" : "O";
    setButtons(newButtons);
    setIsXNext(!isXNext);
  };

  return (
    <div className="container">
      <h1 className="title">Jogo da velha</h1>

      <div className="buttonContainer">
        {buttons.map((value, index) => (
          <button
            key={index}
            className="gameButton"
            onClick={() => handleClick(index)}
          >
            {value}
          </button>
        ))}
      </div>

      <h2 className="gameInfo">É a vez de {isXNext ? "X" : "O"}</h2>
    </div>
  );
}
