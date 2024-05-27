from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.exceptions import BadRequest

app = Flask(__name__)
CORS(app)

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

@app.route('/next-player', methods=['POST'])
def next_player():
    try:
        data = request.json
        board = data.get('board')
        if not board or not isinstance(board, list) or len(board) != 9:
            raise BadRequest("Formato de tabuleiro inválido.")
        
        player = 'X' if sum(1 for cell in board if cell) % 2 == 0 else 'O'
        return jsonify({'player': player})
    except BadRequest as e:
        return jsonify({"error": str(e)}), 400

def evaluate_board(board):
    if check_winner(board, 'O'):
        return {'status': 'O ganhou'}
    elif check_winner(board, 'X'):
        return {'status': 'X ganhou'}
    elif is_draw(board):
        return {'status': 'Empate',}
    else:
        return {'status': 'Tem jogo'}

def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    return any(all(board[i] == player for i in condition) for condition in win_conditions)

def is_draw(board):
    return all(cell is not None for cell in board)

if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1")
