# ITCS
Intelligent Traffic Crossing System calculates the pedestrian crossing time based on 3 parameters ie .,Behavioural movement of pedestrain,Classification of human and non-human&amp;Age-wise classification.

Both the behavoiural movement classification and Human and Non human classification is performed using yolo v3 model.
The Age classification is done based on model developed in Caffe framework as explained in https://talhassner.github.io/home/publication/2015_CVPR

The final age brackets are grouped into four: CHILD , YOUNG ,MIDDLE and OLD

The final crossing time allotted are:
Child   = 15 seconds 

Young   = 10 seconds

Middle  = 12 seconds 

Old     = 20 seconds 

Animal  = 10 seconds 

