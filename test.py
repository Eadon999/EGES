import pandas as pd
import numpy as np
from itertools import chain
import pickle
import time
import networkx as nx
from walker import RandomWalker
from sklearn.preprocessing import LabelEncoder
import argparse

sku_lbe = LabelEncoder()
s = sku_lbe.fit_transform([12, 33, 565])
print(s)

