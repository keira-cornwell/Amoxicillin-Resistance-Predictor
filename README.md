### Predicting Amoxicillin Resistance via Logistic Regression
Keira Cornwell and  Jesse Grayson\
Stanford University\
CHEMENG 177 Final Project\
March 13, 2025

### Project Overview
This project created a binary logistic regression model for predicting if a given bacteria sample will be susceptible or resistant to amoxicillin. Antibiotic resistance is a critical public health concern, contributing to over one million deaths annually. With amoxicillin being the most commonly prescribed antibiotic, it's important to not only understand if a given bacteria sample will be resistant to amoxicillin, but also what drives antibiotic resistance for amoxicillin.

The provided model in "CHEMENG 177 Final.py" takes in a .csv file that contains data on different 331 bacteria samples. The data provided in the "CHEMENG 177 Final Data.csv" file comes from the NIH's National Database of Antibiotic Resistant Organisms (NDARO). Specifically, it takes in the following data categories:
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
For a given bacteria sample from NDARO, input in the .csv file holding the data as follows:
1. In the first column, write the biosample number
2. In the second column, write the organism group the sample is from
3. In the third column, write a "1" if the sample is gram-positive, write a "0" if it is not
4. In the fourth column, write a "1" if the sample is gram-negative and part of the enterbacteriaceae class, write a "0" if it is not
5. In the fifth column, write a "1" if the sample is gram-negative and part of the non-fermenting gram-negative class, write a "0" if it is not
6. In the sixth column, write the antibiotic for which resistance is being tested. In the provided model, that is amoxicillin for all samples.
7. In the seventh column, write "resistant" if the sample was found to be resistant to amoxicillin, write "susceptible" if not
8. In the eigth column, write a "1" if the sample was found to be resistant to amoxicillin, write a "0" if not
9. In the ninth column, write a "1" if the sample has a MIC value, write a "0' if not
10. In the tenth column, write the MIC value (mg/L) if the sample has one, write a "0" if not
11. In the eleventh column, write a "1" if the sample has a mutation in the bla_TEM gene, write a "0" if not
12. In the twelfth column, write a "1" if the sample has a mutation in the bla_CTX-M gene, write a "0" if not
13. In the thirteenth column, write a "1" if the sample has a mutation in the bla_OXA gene, write a "0" if not
14. In the fourteenth column, write a "1" if the sample has a mutation in the bla_SHV gene, write a "0" if not
15. In the fifteenth column, write the total number of mutations the sample has related to AMR

After formatting the data in a .csv file, change the tenth line of code in the provided file to read: resistance_data = pd.read_csv("[YOUR .CSV FILE NAME", index_col=0, header=0). The data is then successfully prepared, and the program can be run. 
