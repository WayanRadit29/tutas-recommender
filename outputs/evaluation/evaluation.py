import tensorflow as tf
import pandas as pd
import numpy as np

SAVEDMODEL_DIR = r"../models/tutas-v1"
loaded = tf.saved_model.load(SAVEDMODEL_DIR)