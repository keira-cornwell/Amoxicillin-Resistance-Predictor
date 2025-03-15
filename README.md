### Predicting Amoxicillin Resistance via Logistic Regression
Keira Cornwell and  Jesse Grayson\
Stanford University\
CHEMENG 177 Final Project\
March 13, 2025

### Project Overview
This project created a binary logistic regression model for predicting if a given bacteria sample will be susceptible or resistant to amoxicillin. Antibiotic resistance is a critical public health concern, contributing to over one million deaths annually. With amoxicillin being the most commonly prescribed antibiotic, it's important to not only understand if a given bacteria sample will be resistant to amoxicillin, but also what drives antibiotic resistance for amoxicillin.

The provided model in "CS 177 Final.py" takes in a .csv file that contains data on different 331 bacteria samples. The data provided in the "CS 177 Final Data.csv" file comes from the NIH's National Database of Antibiotic Resistant Organisms (NDARO). Specifically, it takes in the following data categories:
* Biosample Number
* Organism Group
* Gram Classification
* Resistance Pehnotype
* If the sample has a minimum inhibitory concentration (MIC) value
* MIC (mg/L) if applicable
* If it has a mutation in the blaTEM gene
* If it has a mutation in the bla_CTX_M gene
* If it has a mutation in the bla_SHV gene
* If it has a mutation in the pbp2b gene
* Total number of mutations lined to anti-microbial resistance (AMR) genes

The model was trained and tested on this data to predict the resistance phenotype, created a graph displaying the accuracy, false positive and negative rates, and cross-validation score, and produced a graph representing the importance of each indicator in predicting amoxicillin resistance. The model then repeated the same presence, but only considered the presence/lack of presence of a mutation in one of those 5 genes. The same process was then repeated where the model was trained and tested on the data set to predict amoxicillin resistance, created a graph displaying the accuracy, false positive and negative rates, and cross-validation score, and produced a graph representing the importance of a mutation in each of the five genes in predicting amoxicillin resistance.

### Data Preparation
The data from each bacteria sample can be found in the "CS 177 Final Data.csv" file. Download the file, in addition to the python program in "CS 177 Final.py" from the Amoxicillin Resistance Predictor Github repository, and run the Python program to generate graphs of the accuracy of the model, permutation importance of each indicator, accuracy of the model with only considering individual genetic mutations, and permutation importance of individual genetic mutations alone. 
