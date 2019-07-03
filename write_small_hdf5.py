#!/usr/bin/env python3

import pandas as pd
import numpy as np
from h5py import File

filename="atlas-higgs-challenge-2014-v2.csv.gz"

data = pd.read_csv(filename)

# map the large pandas datatypes to something smaller
dtmap = {'i':'i8', 'f': 'f2', 'O': '|S1'}
newtypes = []
for k, tp in data.dtypes.items():
    newtypes.append((k,dtmap[tp.kind]))

# convert to a numpy recarray
rec = data.to_records(index=False)

# now convert to a numpy array with smaller types
arr = np.array(rec,dtype=newtypes)

# write out the file
with File('output.h5','w') as h5file:
    h5file.create_dataset('ds',data=arr,compression='gzip')
