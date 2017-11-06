Notes on server set-up

environment name on GPU server dogbreed-demo

server is only configured to work with tensorflow_gpu==1.0.0


https://gist.github.com/baraldilorenzo/07d7802847aaad0a35d3

```
conda create --name dogbreed-demo python=3.6
source activate dogbreed-demo
pip install -r requirements.txt 
``` 

Note: if you have issues installing keras tensorflow already comes packaged with it

https://www.kaggle.com/kmader/food41/data