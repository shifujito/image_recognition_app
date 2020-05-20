import numpy as np
from keras.models import model_from_json
from keras import backend as K  # Kが定義されてなかったので, Import

import ml_book.preprecessing as pp
import ml_book.heatmap as ht
from predict import Predict


def main(test_path):
    """ 入力画像のパスから年齢推定をする関数
    ヒートマップを同じパスに上書きする

    Args:
        test_path: 入力画像のパス

    Returns(str): 予測年齢

    """
    # img = pp.load_image(test_path)  # [fixed] @1, 3, 4の修正で使わなくなったのでコメントアウトしたよ
    model = model_from_json(open('./model.json').read())
    model.load_weights('./model.hdf5')
    # X_test = pp.TestProcess(img).process()
    X_test = pp.TestProcess(test_path).process()  # [fixed] 中見た感じバイナリじゃなくて, パスっぽかったので修正 @1
    y_pred_class = model.predict(X_test)
    y_pred = Predict().age_class(y_pred_class)  # [fixed] self.age_class => Predict().age_class へ 修正 @2
    heatmap = ht.Heatmap(model,
                         X_test,
                         test_path,  # [fixed] 中見た感じバイナリじゃなくて, パスっぽかったので修正 @3
                         int(np.argmax(y_pred_class)),
                         'conv2d_1')
    heatmap.grad_cam(test_path)  # [fixed] 中見た感じバイナリじゃなくて, パスっぽかったので修正 @
    K.clear_session()
    return y_pred  # , out_path , 上書きなので戻り値にしない


if __name__ == '__main__':
    main(test_path)
