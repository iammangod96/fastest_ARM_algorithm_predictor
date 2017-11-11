Fastest Association Rule mining algorithm Predicter

The project contains three python files. The code was written in python 3.6.1, on Windows 10 x64 bit machine, Core i7-4510U quad core processor(2.00GHz 2.60GHz), 8GB RAM.

1. rand_data.py 
This file creates 250 random transactional data files.
This file needs random library and os library to run, both included in python 3.6.1 stock installation

2. dataset_gen.py
This file extracts the mentioned features from the transactional datasets and runs the 3 ARM algorithms (Apriori, FPGrowth, eclat) with varying support values to get the final dataset (final_dataset.txt), which is used for the classification.
This file needs os library and time library to run, both included in python 3.6.1 stock installation. It also needs numpy library, which can be installed using pip. The ARM algoritms implementations provided by Borgelt (http://www.borgelt.net/pyfim.html) were used. The information regarding installation of the same can be found on the link given.   

3. classification.py
This file uses various classification algorithms to classify the dataset created.
This file needs pandas, numpy, scipy and scikit-learn library to run, all of which can be installed using pip.