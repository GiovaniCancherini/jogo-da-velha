import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pickle

class TicTacToeAI:
    def __init__(self, data_path):
        self.data_path = data_path
        self.models = {
            'k-NN': KNeighborsClassifier(),
            'MLP': MLPClassifier(max_iter=1000, random_state=42),
            'Decision Tree': DecisionTreeClassifier(random_state=42)
        }
        self.param_grids = {
            'k-NN': {'n_neighbors': [1, 2, 3, 4, 5, 6, 7]},
            'MLP': {'hidden_layer_sizes': [(50,), (100,), (50, 50)], 'alpha': [0.0001, 0.001, 0.01]},
            'Decision Tree': {'max_depth': [None, 10, 20, 30], 'min_samples_split': [2, 5, 10]}
        }
        self.accuracies = {}
        self.best_model_name = None
        self.best_model = None

    def load_and_prepare_data(self):
        df = pd.read_csv(self.data_path, sep=",", header=None)
        df.columns = ['L1C1', 'L1C2', 'L1C3', 'L2C1', 'L2C2', 'L2C3', 'L3C1', 'L3C2', 'L3C3', 'RESULTADO']
        
        # Exibir colunas do dataset
        print("Colunas do dataset:", df.columns)

        resultados = df['RESULTADO'].value_counts()
        print("\nDistribuição dos resultados:")
        print(resultados)

        # Transformar dados categóricos em numéricos
        df.replace({'x': 1, 'o': -1, 'b': 0, 'empate': 0, 'positive': 1, 'negative': -1}, inplace=True, method=None)

        X = df.drop(columns=['RESULTADO'])
        y = df['RESULTADO']

        # Dividir dados em treino e teste
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        return X_train, X_test, y_train, y_test

    def train_and_evaluate_models(self, X_train, X_test, y_train, y_test):
        for model_name, model in self.models.items():
            param_grid = self.param_grids[model_name]
            grid_search = GridSearchCV(model, param_grid, cv=5, scoring='accuracy')
            grid_search.fit(X_train, y_train)
            best_model = grid_search.best_estimator_
            y_test_pred = best_model.predict(X_test)
            accuracy = accuracy_score(y_test, y_test_pred)
            self.accuracies[model_name] = accuracy
            self.models[model_name] = best_model  # Atualizar o modelo com o melhor encontrado
            print(f"Acurácia do {model_name} (melhor combinação de hiperparâmetros): {accuracy:.2f}")

    def select_best_model(self):
        self.best_model_name = max(self.accuracies, key=self.accuracies.get)
        self.best_model = self.models[self.best_model_name]
        print(f"Melhor modelo: {self.best_model_name} com acurácia de {self.accuracies[self.best_model_name]:.2f}")

    def save_best_model(self, path):
        with open(path, 'wb') as file:
            pickle.dump(self.best_model, file)


tic_tac_toe_ai = TicTacToeAI("Data/tic-tac-toe-updated.csv")


X_train, X_test, y_train, y_test = tic_tac_toe_ai.load_and_prepare_data()


tic_tac_toe_ai.train_and_evaluate_models(X_train, X_test, y_train, y_test)

# Selecionar o melhor modelo
tic_tac_toe_ai.select_best_model()

# Salvar o melhor modelo
model_path = f"best_model_{tic_tac_toe_ai.best_model_name}.pkl"
tic_tac_toe_ai.save_best_model(model_path)

print(f"Melhor modelo salvo em: {model_path}")
