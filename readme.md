# WeRecogngnizer_DL
Simple python utility for running SpikeCV wheat segmentation and classification models. See demo page at https://spikecv-demo.sysbio.ru for additional examples.

# Requirements
* python >= 3.6.6

# Usage
## 1. As python function
```python
get_masks(filename, save_files=True)
```
### Description
Sends file to server, load models output as text and image of masks
### Args:
* `filename` - file path to wheat image to download into the model
* `save_files` - `True` (as default), if you agree to save your file and model call results on server. If the image is saved on the server, then your image can be used to test and improve the quality of the model. Files wont saved if `save_files=False`
###  Example:
```python
from werecognizer_dl import get_masks

models_output = get_masks('example_image.png')
print(models_output)'
```
## 2. As command line program
``` 
python werecognizer_dl.py example_image.png
```