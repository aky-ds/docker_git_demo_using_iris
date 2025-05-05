import unittest
import pickle
import numpy as np

class TestModel(unittest.TestCase):
    def test_prediction_shape(self):
        model = pickle.load(open('artifacts/model.pkl', 'rb'))
        sample = np.array([[5.1, 3.5, 1.4, 0.2]])
        prediction = model.predict(sample)
        self.assertEqual(prediction.shape, (1,))

if __name__ == '__main__':
    unittest.main()
