# Custom L1 Distance layer module 

import tensorflow as tf
from tensorflow.keras.layers import Layer

# Custom L1 Distance Layer from Jupyter 
class L1Dist(Layer):
    
    # Init method - inheritancess
    def __init__(self, **kwargs):
        super().__init__()
       
    # Magic happens here - similarity calculation
    def call(self, input_embedding, validation_embedding):
        return tf.math.abs(input_embedding - validation_embedding)
