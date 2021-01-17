# WeRecogngnizer_DL
Simple python utility for running SpikeCV wheat segmentation and classification models. See demo page at https://spikecv-demo.sysbio.ru for additional examples.

# Requirements
* python >= 3.6.6

## Usage
* ### As python function
```python
from werecognizer_dl import get_masks

models_output = get_masks('example_image.png')
print(models_output)'
```
* ### As command line program
``` 
python werecognizer_dl.py example_image.png
```