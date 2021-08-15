import pickle

# load a model
model = pickle.load(open('diabetic_79.pkl', 'rb'))

result = model.predict([[1, 1, 1, 1, 1, 1, 1, 1]])

if result[0] == 1:
    print('Person is diabetic')
else:
    print('Person is not diabetic')

