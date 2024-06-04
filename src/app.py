from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.exceptions import BadRequest
import pickle
import pandas as pd

app = Flask(__name__)
CORS(app)

# Carregar o modelo treinado
model_path = "best_model_k-NN.pkl"  # Atualize para o nome do melhor modelo salvo


with open(model_path, 'rb') as file:
    best_model = pickle.load(file)

@app.route('/')
def index():
    return "Servidor Flask está rodando!"

@app.route('/evaluate', methods=['POST'])
def evaluate():
    try:
        data = request.json
        board = data.get('board')
        if not board or not isinstance(board, list) or len(board) != 9:
            raise BadRequest("Formato de tabuleiro inválido.")

        result = evaluate_board(board)
        return jsonify(result)
    except BadRequest as e:
        return jsonify({"error": str(e)}), 400

def evaluate_board(board):
    transformed_board = transform_board(board)
    predicao = best_model.predict(transformed_board)[0]
    status = determine_game_status(predicao, board)
    return {'status': status}

def transform_board(board):
    board_df = pd.DataFrame([board], columns=[f"L{i//3+1}C{i%3+1}" for i in range(9)])
    board_df.replace({'x': 1, 'o': -1, ' ': 0}, inplace=True)
    board_df = board_df.apply(pd.to_numeric)  # Garantir que os dados sejam convertidos corretamente para inteiros
    return board_df

def determine_game_status(result, board):
    if check_winner(board, 'o'):
        return 'O ganhou'
    elif check_winner(board, 'x'):
        return 'X ganhou'
    elif is_draw(board):
        return 'Empate'
    else:
        return 'Tem jogo'

def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    return any(all(board[i] == player for i in condition) for condition in win_conditions)

def is_draw(board):
    return all(cell != ' ' for cell in board)

if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1")
