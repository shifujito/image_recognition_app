import sys
import cv2
import glob
import numpy as np
import ml_wookbok.preprocessing as pp
import ml_wookbok.answer_label as al
from ml_wookbok.build_model import Modelselection
import matplotlib.pyplot as plt
from keras import backend as K
from keras.models import model_from_json
from IPython.display import Image as IM
from keras import layers, models, optimizers
from keras.utils.np_utils import to_categorical
from IPython.display import display_jpeg,display_png
from keras.preprocessing.image import ImageDataGenerator

def main():
    # 前処理
    study = 0 #0が学習する、1が学習済みモデルの使用
    train_data_lists = glob.glob("./data/*")
    X_train, X_test,y_train = [], [], []
    for train_data in train_data_lists:
        train_img =pp.load_image(train_data)
        X_train.append(train_img)
        train_label = pp.Label(train_data)
        y_train_class = train_label.data_to_classifier()
        # y_regress = label.data_to_regression()
        y_train.append(y_train_class)
    X_train,y_train = pp.list_to_array(X_train,y_train)
    y_train_regres = y_train
    y_train_class = to_categorical(y_train)

    if study == 0:
        # 学習
        vgg16_class = Modelselection(X_train, y_train_class).vgg16_class()
        # vgg16_regress = Modelselection(X_train, y_train_regres).vgg16_regress()
        vgg16_class_json= vgg16_class.to_json()
        open('vgg16_model.json', 'w').write(vgg16_class_json)
        vgg16_class.save_weights('vgg16_class.hdf5')
    elif study == 1:
    # 画集済みモデルの使用
        trained_model = model_from_json(open('./ml_wookbok/vgg16_model.json').read())
        trained_model.load_weights('./ml_wookbok/vgg16_model.hdf5')

    # 予測
    test_data = './data/24_0044.jpg'
    test_img = pp.load_image(test_data)
    X_test = np.array(test_img)
    if study == 0:
        y_pred_class = np.argmax(vgg16_class.predict(np.array([X_test])), axis=1)
        # y_pred_regress = vgg16_regress.predict(np.array([X_test]))
        pred_age = al.add_name(y_pred_class)
        # print(pred_age, y_pred_regress)
        print(pred_age)

    elif study == 1:
        y_pred = np.argmax(trained_model.predict(np.array([X_test])), axis=1)
        pred_age = al.add_name(y_pred)
        print(pred_age)
    # ヒートマップ
    img_output = trained_model.output[:,1]
    last_conv_layer = trained_model.get_layer('conv2d_31')
    grads = K.gradients(img_output, last_conv_layer.output)[0]
    pooled_grads = K.mean(grads, axis=(0,1,2))
    iterate = K.function([trained_model.input],[pooled_grads, last_conv_layer.output[0]])
    pooled_grads_value, conv_layer_output_value = iterate([X_test])
    for i in range(512):
        conv_layer_output_value[: , : , i] *= pooled_grads_value[i]
    hetamap = np.mean(conv_layer_output_value, axis=-1)
    heatmap = np.maximum(heatmap, 0)
    heatmap /= np.max(heatmap)
    img3 = cv2.imread(test_data)
    heatmap = cv2.resize(heatmap, (img3.shape[1], img3.shape[0]))
    heatmap = np.uint8(255 * heatmap)
    heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)
    saveimg = heatmap * 0.4 + img3
    savename = './heat.jpg'
    cv2.imwrite(savename, saveimg)



if __name__ == '__main__':
    main()
