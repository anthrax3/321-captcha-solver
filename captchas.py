import dataset
import os

print(os.listdir('.'))
data_dir = 'captchas'
mnist = dataset.read_data_sets(data_dir, one_hot=True)
