from keras import layers, models, optimizers
from keras.applications import VGG16, Xception, ResNet50

class Vgg16_classifier:
    def __init__(self, epochs, batch_size):
        self.epochs = epochs
        self.batch_size = batch_size

    def fit(self, X_train, y_train):
        top_dense = len(y_train[0])
        print('分類の数は{}'.format(top_dense))
        base_vgg = VGG16(
                    weights = 'imagenet',
                    include_top = False,
                    input_shape = X_train[0].shape)
        model = models.Sequential()
        model.add(base_vgg)
        model.add(layers.Conv2D(512, (3, 3), activation = 'relu', padding = 'same'))
        model.add(layers.MaxPool2D((2,2)))
        model.add(layers.Flatten())
        model.add(layers.Dense(top_dense, activation = 'softmax'))
        for layer in base_vgg.layers[:-4]:
            layer.trainable = False
        model.compile(optimizer = optimizers.RMSprop(lr = 1e-5),
                      loss = 'categorical_crossentropy',
                      metrics = ['acc'])
        model.fit(X_train, y_train, epochs =self.epochs, batch_size = self.batch_size)
        model_json = model.to_json()
        open('model.json', 'w').write(model_json)
        model.save_weights('model.hdf5')
        return self
