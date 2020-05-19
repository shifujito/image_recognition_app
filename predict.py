import numpy as np
import argparse
from keras.models import model_from_json
import ml_book.preprecessing as pp
import ml_book.heatmap as ht

class Predict:
    def predict(self):
        model = model_from_json(open('./model.json').read())
        model.load_weights('./model.hdf5')
        X_test = pp.TestProcess(config.data).process()
        y_pred_class = model.predict(X_test)
        y_pred = self.age_class(y_pred_class)

    def age_class(self, y_pred_class):
        y_pred = np.argmax(y_pred_class)
        y_pred = pp.age_name(y_pred)
        return y_pred

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = '年齢推定')
    parser.add_argument('-d','--data',type = str, default = './data/25_2169.jpg', help = 'input_data_path')
    parser.add_argument('-o', '--out', type = str, default = 'out/heat.jpg', help = 'out_put')

    config = parser.parse_args()
    print(config)

    Predict().predict()
