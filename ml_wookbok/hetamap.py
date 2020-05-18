import cv2
import numpy as np
from keras import backend as K


def make_hetamap(model, X_test):
    img_output = model.output[:,1]
    last_conv_layer = model.get_layer('conv2d_31')
    grads = K.gradients(img_output, last_conv_layer.output)[0]
    pooled_grads = K.mean(grads, axis=(0,1,2))
    iterate = K.function([model.input],[pooled_grads, last_conv_layer.output[0]])
    pooled_grads_value, conv_layer_output_value = iterate([X_test])
    for i in range(512):
        conv_layer_output_value[: , : , i] *= pooled_grads_value[i]
    hetamap = np.mean(conv_layer_output_value, axis=-1)
    img3 = cv2.imread(test_data)
    heatmap = cv2.resize(heatmap, (img3.shape[1], img3.shape[0]))
    heatmap = np.uint8(255 * heatmap)
    heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)
    saveimg = heatmap * 0.4 + img3
    X_test = './heat.jpg'
    cv2.imwrite(X_test, saveimg)
    return X_test
