import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.inspection import permutation_importance
from sklearn.model_selection import cross_val_score

# Load the amoxicillin resistance data
resistance_data = pd.read_csv("CS 177 Final Project Data.csv", index_col=0, header=0)
resistance_data.head()
resistance_data = resistance_data.reset_index()

# Drop the Biosample, Resistance phenotype, Resistance number, and Antibiotic columns
indicators = resistance_data.drop(['Biosample', 'Organism Group', 'Resistance Phenotype', 'Resistance Binary', 'Antibiotic'], axis=1)

# Create an interaction term for if the MIC is available, this will be 0 when no MIC is available and the actual MIC when available
indicators['MIC_interaction'] = indicators['Has MIC'] * indicators['MIC (mg/L)']

# Create a series with the resistance binary values
resistance_labels = resistance_data['Resistance Binary']

# Use train_test_split directly with the features and labels
x_train, x_test, y_train, y_test = train_test_split(indicators, resistance_labels, test_size=0.3, random_state=0, stratify=resistance_labels)

# Train a logistic regression classifier
logistic_regression = LogisticRegression(solver="lbfgs")
logistic_regression.fit(x_train, y_train)

# Evaluate the classifier’s performance on the test set by identifying the classifier’s accuracy and generating a confusion matrix
accuracy = logistic_regression.score(x_test, y_test)
y_pred = logistic_regression.predict(x_test)
matrix = confusion_matrix(y_test, y_pred)

# Evaluate false positive rate and false negative rate
false_positive_rate = matrix[0][1] / (matrix[0][1] + matrix[0][0])
false_negative_rate = matrix[1][0] / (matrix[1][0] + matrix[1][1])

# Evaluate cross-validation score
cross_val_score = cross_val_score(logistic_regression, x_train, y_train, cv=10).mean()

# Create a graph of relevant classifier performance metrics
performance_metrics = pd.DataFrame({'Accuracy': [accuracy], 'False Positive': [false_positive_rate], 'False Negative': [false_negative_rate], 'Cross Validation Score': [cross_val_score]})
fig, ax = plt.subplots()
bars_1 = plt.bar(performance_metrics.columns, performance_metrics.iloc[0])
plt.bar_label(bars_1,fmt=lambda x: f'{x:.3f}')
plt.ylabel('Performance')
plt.xlabel('Metric')
plt.title('Classifier Performance Metrics for Logistic Regression')
plt.xticks(rotation=45)
plt.show()

# Calculate the permutation importance of the different indictors
perm_importance = permutation_importance(logistic_regression, x_test, y_test, n_repeats=30, random_state=0)
importance_data = pd.DataFrame({'Indicator': indicators.columns, 'Importance': perm_importance.importances_mean})
importance_data = importance_data.sort_values(by='Importance', ascending=False)

# Create a graph of the permutation importance of different indicators
fig, ax = plt.subplots()
bars_2 = plt.bar(importance_data['Indicator'], importance_data['Importance'], color='steelblue')
plt.bar_label(bars_2, fmt=lambda x: f'{x:.3f}')
plt.xlabel('Biologic Indicator')
plt.ylabel('Permutation Importance')
plt.title('Permutation Importance of Biologic Indicators of AMR')
plt.xticks(rotation=90)
plt.show()

# Repeat process removing all other indicators other than the presence of genese to assess how it performs

# Drop all columns except for the presence of the 5 genes
gene_indicators = resistance_data.drop(['Biosample', 'Organism Group', 'Resistance Phenotype', 'Resistance Binary', 'Antibiotic', 'Gram-Positive', 'Enterbacteriaceae', 'Non-Fermenting Gram-Negative ', 'Has MIC', 'MIC (mg/L)', 'Total AMR Gene Count'], axis=1)

# Create a series with the resistance binary values
gene_resistance_labels = resistance_data['Resistance Binary']

# Use train_test_split directly with the features and labels
x_train_g, x_test_g, y_train_g, y_test_g = train_test_split(gene_indicators, gene_resistance_labels, test_size=0.2, random_state=0, stratify=gene_resistance_labels)

# Train a logistic regression classifier
gene_logistic_regression = LogisticRegression(solver="lbfgs")
gene_logistic_regression.fit(x_train_g, y_train_g)

# Evaluate the classifier’s performance on the test set by identifying the classifier’s accuracy and generating a confusion matrix
gene_accuracy = gene_logistic_regression.score(x_test_g, y_test_g)
y_pred_g = gene_logistic_regression.predict(x_test_g)
gene_matrix = confusion_matrix(y_test_g, y_pred_g)

# Evaluate false positive rate and false negative rate
false_positive_rate_g = gene_matrix[0][1] / (gene_matrix[0][1] + gene_matrix[0][0])
false_negative_rate_g = gene_matrix[1][0] / (gene_matrix[1][0] + gene_matrix[1][1])

# Evaluate cross-validation score
from sklearn.model_selection import cross_val_score as sklearn_cv_score
gene_cross_val_score = sklearn_cv_score(gene_logistic_regression, x_train_g, y_train_g, cv=10).mean()

# Create a graph of relevant classifier performance metrics
gene_performance_metrics = pd.DataFrame({'Accuracy': [gene_accuracy], 'False Positive': [false_positive_rate_g], 'False Negative': [false_negative_rate_g], 'Cross Validation Score': [gene_cross_val_score]})
fig, ax = plt.subplots()
bars_3 = plt.bar(gene_performance_metrics.columns, gene_performance_metrics.iloc[0])
plt.bar_label(bars_3, fmt=lambda x: f'{x:.3f}')
plt.ylabel('Performance')
plt.xlabel('Metric (Genes Only)')
plt.title('Classifier Performance Metrics for Logistic Regression (Genes Only)')
plt.xticks(rotation=45)
plt.show()

# Calculate the permutation importance of the different genes
gene_perm_importance = permutation_importance(gene_logistic_regression, x_test_g, y_test_g, n_repeats=30, random_state=0)
gene_importance_data = pd.DataFrame({'Indicator': gene_indicators.columns, 'Importance': gene_perm_importance.importances_mean})
gene_importance_data = gene_importance_data.sort_values(by='Importance', ascending=False)

# Create a graph of the permutation importance of different genes
fig, ax = plt.subplots()
bars_4 = plt.bar(gene_importance_data['Indicator'], gene_importance_data['Importance'], color='steelblue')
plt.bar_label(bars_4, fmt=lambda x: f'{x:.3f}')
plt.xlabel('Gene')
plt.ylabel('Permutation Importance')
plt.title('Permutation Importance of AMR Genes')
plt.xticks(rotation=90)
plt.show()