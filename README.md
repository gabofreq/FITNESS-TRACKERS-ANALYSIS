# Comparison of Sentiment of User vs Manufacturers on fitness trackers, using reviews of Amazon

## Abstract

### Fitness trackers encourage teens and adults to count their steps and be more active, people with obesity to lose weight and track their diet, and older adults to understand their health by knowing their heart rate. Companies display advertisements for these types of products and describe them as beneficial. In this studio we evaluate the opinion of users, testing the veracity of the technical characteristics that device offer. Using natural language processing techniques, we construct an analysis based on technical aspects and user sentiment. The RoBERTa model was pretrained, extracting 19 technical aspects (96% precision), and classifying aspects (70% precision). A comparison was made between the average sentiment of the users versus that of the manufacturer, grouped by aspects. Estimating the difference between the user's sentiment and the manufacturer's, concluding that there is a difference of 0.88 (3.11 Users ~ 3.99 Manufacturer), with the user's sentiment having a lower expectation than the manufacturers



![Fitness Tracker pipeline - english](https://user-images.githubusercontent.com/36687480/213279659-e95f02e7-ff07-4e48-be94-26a94c409464.jpeg)
#### Modules of the Technical Characteristics Evaluation System


![imagen](https://user-images.githubusercontent.com/36687480/213280478-d082ef9e-06ab-4b3f-9e0b-860e950a401a.png)
#### Comparison of average sentiments (Users vs Manufacturers)


### 1) The script MODULO_RECOLECCION_DATOS.ipynb for the GitHub repository, presents the methodology for data collection, where comments from the Amazon platform are downloaded.

### 2) The script MODULO_PREPROCESAMIENTO.ipynb for the GitHub repository, presents the data preprocessing methodology, requires the excel file FINAL.xlsx that comes from the previous step, and NOUNS.xlsx. Apply the following processing steps a) Normalization and Tokenization, b) Clause Segmentation, c) Stemming and POS Tagging, d) Deleting of Stop Words, and e) Features Extraction. The tagging of sentiments and aspects is done manually for model training.

### 3) The script MODULO_AUMENTO.ipynb for the GitHub repository, presents the methodology to stabilize the classes for the technical aspects, with the data augmentation algorithms and data processing logic in step 2. It uses excel AMAZON_FINAL.xlsx which comes from the previous step.

### 4) The script MODULO_MODELAJE.ipynb for the GitHub repository, presents the modeling methodology and classification of technical features, uses the excel AMAZON_AUGMENTED.xlsx that comes from the previous step, and MANUFACTURER.xlsx that contains the clauses, aspects and sentiments that are developed manually.
