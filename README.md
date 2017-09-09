

Keras-FCN
---------

Fully convolutional networks and semantic segmentation with Keras.

![Biker Image](doc/2007_000129.jpg)

![Biker Ground Truth](doc/2007_000129.png)

![Biker as classified by AtrousFCN_Resnet50_16s](doc/AtrousFCN_Resnet50_16s_2007_000129.png)


### Pre-requirement

해당 코드를 실행시키기 위해서는 아래와 같은 모듈이 설치되어야합니다.

```
Keras -> 2.0.8
Tensorflow -> 1.3.0
Pillow -> 4.2.1
sacred -> 0.7.0
scikit-image(skimage) - > 0.13.0
```

### Dataset Download

[Pascal VOC 2012](http://host.robots.ox.ac.uk/pascal/VOC/voc2012/) augmented with [Berkeley Semantic Contours](https://www2.eecs.berkeley.edu/Research/Projects/CS/vision/grouping/) is the primary dataset used for training Keras-FCN. Note that the default configuration maximizes the size of the dataset, and will not in a form that can be submitted to the pascal [VOC2012 segmentation results leader board](http://host.robots.ox.ac.uk:8080/leaderboard/displaylb.php?challengeid=11&compid=6), details are below.

다운로드 받은 코드경로에서 아래와 같은 경로로 진입한 후에 스크립트 파일을 실행합니다.

```
cd path/to/tf-image-segmentation/tf_image_segmentation/recipes/pascal_voc/
python data_pascal_voc.py pascal_voc_setup
```


### Training and Testing

기본 설정은 pascal voc 2012 with berkeley data augmentation 데이터를 기반으로한 `AtrousFCN_Resnet50_16s` 모델을 사용합니다.
아래와 같은 명령어로 학습하고 테스트 할 수 있습니다.

```
cd ~/src/Keras-FCN
cd utils

# Generate pretrained weights
python transfer_FCN.py

cd ~/src/Keras-FCN

# Run training
python train.py

# Evaluate the performance of the network
python evaluate.py

```

Model weights will be in `~/src/Keras-FCN/Models`, along with saved image segmentation results from the validation dataset.

### Detail

조금 더 자세한 내용을 확인하고 싶으시면, 다음 링크에서 확인하실 수 있습니다.

https://github.com/aurora95/Keras-FCN