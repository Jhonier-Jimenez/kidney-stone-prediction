import argparse
import pickle
import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from loguru import logger


# Definir los valores por defecto para los argumentos
DEFAULT_DATA_FILE = 'datasets/train.csv'

parser = argparse.ArgumentParser()
parser.add_argument('--data_file', required=True, type=str, default=DEFAULT_DATA_FILE, help='a csv file with train data')
parser.add_argument('--model_file', required=True, type=str, help='where the trained model will be stored')
parser.add_argument('--overwrite_model', default=False, action='store_true', help='if sets overwrites the model file if it exists')


args = parser.parse_args()

model_file = args.model_file
data_file  = args.data_file
overwrite = args.overwrite_model

# Load data from a CSV file
logger.info("loading train data")
data = pd.read_csv(data_file)

# Data cleaning
train_data = data.drop('id', axis=1)

# split data into X and y
X = train_data.drop(['target'], axis=1)
y = train_data['target']

# split data into train and test sets
X_train, X_test, y_train,y_test = train_test_split(X, y, test_size=0.24, random_state=7)

# fit model no training data
logger.info("fitting model")
model = XGBClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
predictions = [round(value) for value in y_pred]
# evaluate predictions
accuracy = accuracy_score(y_test, predictions)
print("Accuracy: %.2f%%" % (accuracy * 100.0))


logger.info(f"saving model to {model_file}")
with open(model_file, "wb") as f:
    pickle.dump(model, f)