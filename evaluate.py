from sklearn.metrics import mean_absolute_error

def evaluate_model(model, x, y):
    predictions = model.predict(x)
    error = mean_absolute_error(predictions, y)
    return error
