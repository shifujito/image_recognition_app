import glob
import argparse
import ml_book.preprecessing as pp
import ml_book.build_model as bm
import ml_book.heatmap as ht

class Train:
    def run():
        train_data = glob.glob('./data/*')
        X_train, y_train =pp.TrainProcess(train_data).process()
        X_vali, y_vali = None, None
        model = bm.Vgg16_classifier(epochs = config.epochs, batch_size = config.batch_size)
        model.fit(X_train, y_train)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'モデルの学習')
    parser.add_argument('-e','--epochs',type = int, default = 15, help = 'epochs数')
    parser.add_argument('-b', '--batch_size', type = int, default = 64, help = 'batch_sizeの数')

    config = parser.parse_args()
    print(config)
    train = Train.run()
