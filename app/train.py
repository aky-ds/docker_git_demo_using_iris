from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import pickle
def perform_training():
    # Load the iris dataset
    iris = load_iris()
    X, y = iris.data, iris.target
    lg=LogisticRegression()
    lg.fit(X,y)    # Here you would typically train your model
    # For demonstration, we'll just print the shape of the data
    print(f"Training on dataset with {X.shape[0]} samples and {X.shape[1]} features.")
    with open('artifacts/model.pkl', 'wb') as f:
        pickle.dump(lg, f)

if __name__ == "__main__":
    perform_training()