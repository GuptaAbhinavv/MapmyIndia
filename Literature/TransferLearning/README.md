## Transfer Learning
Transfer Learning involves storing the knowledge gained while solving one problem and applying it to different but related problem. 

### Pre-Training
When we train the network on a large dataset(for example: ImageNet) , we train all the parameters of the neural network and therefore the model is learned. It may take hours on a GPU.

### Fine Tuning
We can give the new dataset to fine tune the pre-trained CNN. Consider that the new dataset is almost similar to the orginal dataset used for pre-training. Since the new dataset is similar, the same weights can be used for extracting the features from the new dataset.
If the new dataset is very small, it’s better to train only the final layers of the network to avoid overfitting, keeping all other layers fixed. So remove the final layers of the pre-trained network. Add new layers . Retrain only the new layers.
If the new dataset is very much large, retrain the whole network with initial weights from the pretrained model.


A very simple tutorial for applying Transfer Learning on pre-trained ResNet can be found on [Kaggle](https://www.kaggle.com/dansbecker/transfer-learning).

