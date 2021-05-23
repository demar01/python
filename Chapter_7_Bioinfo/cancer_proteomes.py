import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#%matplotlib inline
sns.set_style("whitegrid")

#load data
proteomes_orig = pd.read_csv('Chapter_7_Bioinfo/77_cancer_proteomes_CPTAC_itraq.csv')
clinical = pd.read_csv('Chapter_7_Bioinfo/clinical_data_breast_cancer.csv', index_col=0)
PAM50 = pd.read_csv('Chapter_7_Bioinfo/PAM50_proteins.csv')


#drop unused columns in proteomes
proteomes_orig.shape #(12553, 86)
proteomes_orig.columns
proteomes = proteomes_orig.drop(['gene_symbol','gene_name'], axis=1)


#Match patient IDs between datasets
clinical.index = clinical.index.to_series().apply(lambda title : title.split('CGA-')[1])
proteomes.rename(columns = proteomes.columns.to_series().apply(lambda title: title.split('.')[0]), inplace=True)


#Transpose and organize proteomes data
proteomes = proteomes.transpose()
proteomes.columns =  proteomes.iloc[0]
proteomes.drop('RefSeq_accession_number', axis=0, inplace=True)


#Convert gender to numbers
def num_gender(gender):
    if gender == 'MALE':
        return 0
    elif gender == 'FEMALE':
        return 1
    else:
        return float('NaN')

    
clinical['Gender'] = clinical['Gender'].apply(lambda gender: num_gender(gender))


#Convert status to numbers
def num_status(status):
    if status == 'Negative':
        return 0
    elif status == 'Positive':
        return 1
    else:
        return 


clinical['ER Status'] = clinical['ER Status'].apply(lambda status: num_status(status))
clinical['PR Status'] = clinical['PR Status'].apply(lambda status: num_status(status))
clinical['HER2 Final Status'] = clinical['HER2 Final Status'].apply(lambda status: num_status(status))


#Convert tumor, node, metastasis to numbers
clinical['Tumor'] = clinical['Tumor'].apply(lambda tumor: tumor.split('T')[1])
clinical['Node'] = clinical['Node'].apply(lambda tumor: tumor.split('N')[1])
clinical['Metastasis'] = clinical['Metastasis'].apply(lambda tumor: tumor.split('M')[1])


#Remove unused columns
clinical.drop('Tumor--T1 Coded', axis=1, inplace=True)
clinical.drop('Metastasis-Coded', axis=1, inplace=True)
clinical.drop('Node-Coded', axis=1, inplace=True)


#Merge clinical data with proteomes data
dataset = clinical.merge(proteomes, left_index=True,right_index=True)


#Patient age. This is a barplot histogram
sns.distplot(dataset['Age at Initial Pathologic Diagnosis'], kde=False, bins=[30,40,50,60,70,80,90], hist_kws=dict(alpha=1))


#Cancer spread to lymph nodes. Nodes will be in x axis, will be 0,1,2,3 and each bar in the barplot will be a different color. 
sns.countplot(dataset['Node'])

#Tumor size. Sizes will be in x axis, will go 2,1,3,4 (shorted biggest count first) and each bar in the barplot will be a different color. 
sns.countplot(dataset['Tumor'])


#Tumor stage
fig, ax = plt.subplots(figsize=(12,4))
sns.countplot(sorted(clinical['AJCC Stage']), ax=ax)


#Before I go further, I will fill NaNs with the column average. This step takes a while 
means = dataset.mean()
dataset = dataset.fillna(means)


#Drop all other columns besides node. Dataset has  12579 columns and nodedata has 12554 columns
nodedata = dataset.drop([x for x in list(clinical.columns.values) if x != 'Node'], axis=1)

#0=Clean lymph nodes, 1=spread to 1+ lymph nodes
nodedata['Node'] = nodedata['Node'].apply(lambda x: 1 if x != '0' else 0)


#Splitting data

from sklearn.model_selection import train_test_split
X = nodedata.drop('Node', axis=1)
y = nodedata['Node']
#note that there are 4 outputs
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


#Let's try a kNN model first

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train,y_train)
pred = knn.predict(X_test)
from sklearn.metrics import classification_report,confusion_matrix
print(confusion_matrix(y_test,pred))
print('\n')
print(classification_report(y_test,pred))

#This will print accuracy, macro avg, weighted avg

error_rate = []

# Will take some time
for i in range(1,20):
    
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train,y_train)
    pred_i = knn.predict(X_test)
    error_rate.append(np.mean(pred_i != y_test))


error_rate

plt.figure(figsize=(10,6))
plt.plot(range(1,20),error_rate,color='blue', linestyle='dashed', marker='o', markerfacecolor='red', markersize=10)
plt.title('Error Rate vs. K Value')
plt.xlabel('K')
plt.ylabel('Error Rate')

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=2)
knn.fit(X_train,y_train)
pred = knn.predict(X_test)
from sklearn.metrics import classification_report,confusion_matrix
print(confusion_matrix(y_test,pred))
print('\n')
print(classification_report(y_test,pred))


#How about logistic regression