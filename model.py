from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor

def train_linear_regression(x_train, y_train):
    model = LinearRegression()
    model.fit(x_train, y_train)
    return model

def train_decision_tree(x_train, y_train, depth=3, features=10):
    dt = DecisionTreeRegressor(max_depth=depth, max_features=features, random_state=567)
    dt.fit(x_train, y_train)
    return dt
