import numpy as np
import ml_wookbok.preprocessing as pp
import ml_wookbok.answer_label as al
from keras.models import model_from_json
from keras import backend as K


def main(test_path):
    img = pp.load_image(test_path)
    model = model_from_json(open('./ml_wookbok/vgg16_model.json').read())
    model.load_weights('./ml_wookbok/vgg16_model.hdf5')
    pred = np.argmax(model.predict(np.array([img])), axis=1)
    pred_age = al.add_name(pred)
    K.clear_session()
    return pred_age  # ,out_path 予想の年代と出力のpath


if __name__ == '__main__':
    test_data = '../data/12_0052.png'
    main(test_data)
