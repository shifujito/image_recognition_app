import numpy as np
from keras.models import model_from_json
import ml_book.preprecessing as pp
import ml_book.heatmap as ht

def main(test_path):
    """ 入力画像のパスから年齢推定をする関数
    ヒートマップを同じパスに上書きする

    Args:
        test_path: 入力画像のパス

    Returns(str): 予測年齢

    """
    img = pp.load_image(test_path)
    model = model_from_json(open('./model.json').read())
    model.load_weights('./model.hdf5')
    X_test = pp.TestProcess(img).process()
    y_pred_class = model.predict(X_test)
    y_pred = self.age_class(y_pred_class)
    heatmap = ht.Heatmap(model,
                        X_test,
                        img,
                        int(np.argmax(y_pred_class)),
                        'conv2d_1')
    heatmap.grad_cam(img)
    K.clear_session()
    return pred_age  # , out_path , 上書きなので戻り値にしない


if __name__ == '__main__':
    main(test_path)
