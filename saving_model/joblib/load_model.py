import joblib

# load a model
model = joblib.load('diabetic_79.pkl')

result = model.predict([[1, 1, 1, 1, 1, 1, 1, 1]])

if result[0] == 1:
    print('Person is diabetic')
else:
    print('Person is not diabetic')

