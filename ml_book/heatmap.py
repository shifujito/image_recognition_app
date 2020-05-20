from keras import backend as K
import cv2
import numpy as np

class Heatmap:
    def __init__(self, model, x,image, y_pred, layer_name):
        self.model = model
        self.x = x
        self.image = image
        self.y_pred = y_pred
        self.layer_name = layer_name

    def grad_cam(self):
        pred_vector = self.model.output[:,self.y_pred]
        last_conv_layer = self.model.get_layer(self.layer_name)
        grads = K.gradients(pred_vector, last_conv_layer.output)[0]
        pooled_grads = K.mean(grads, axis= (0, 1, 2))
        iterate = K.function([self.model.input], [pooled_grads, last_conv_layer.output[0]])
        pooled_grads_value, last_conv_layer_value = iterate([self.x])
        for i in range(512):
            last_conv_layer_value[:,:,i] *= pooled_grads_value[i]
        heatmap = np.mean(last_conv_layer_value, axis = -1)
        heatmap = np.maximum(heatmap, 0)
        heatmap /= np.max(heatmap)
        self.heatmap_output(heatmap)

    def heatmap_output(self,heatmap_img):
        img = cv2.imread(self.image)
        heatmap_img = cv2.resize(heatmap_img, (img.shape[1], img.shape[0]))
        heatmap_img = np.uint8(255 * heatmap_img)
        heatmap_img = cv2.applyColorMap(heatmap_img, cv2.COLORMAP_JET)
        superimposed_img = heatmap_img * 0.4 + img
        cv2.imwrite('./heat.jpg', superimposed_img)
