# Assessing User and Manufacturer Perceptions of Fitness Trackers through Amazon Review Analysis

## Abstract

### Fitness trackers encourage people to be more active, people with obesity track their diet, and older adults to understand their health by knowing their heart rate. Companies display advertisements for these types of products and describe them as beneficial. However, users are looking for the products that best suit their personal needs, for which they often review the opinions of other users on e-commerce platforms such as Amazon. In this research, we study the opinion of users who have used physical activity trackers, to assess whether their satisfaction meets the quality offered by the manufacturer. Through: the use of natural language processing techniques, and the analysis of information provided in Amazon reviews. A sentiment analysis was carried out based on the technical characteristics of the device. We employ transfer learning of a Transformer-based language model (RoBERTa: Robustly Optimized BERT Pretraining Approach). Which was retrained for two classification problems in independent modules, the first module classified 20 technical aspects of the device (96% precision), and the second module classified user sentiments (70% precision). A comparison was made between the average feeling of the user vs. the manufacturer, getting a 3.11 for users and 3.99 for manufacturers with a difference of 0.88, concluding that the user's sentiment having a lower expectation than the manufacturers.



![Fitness Tracker pipeline - english](https://user-images.githubusercontent.com/36687480/213279659-e95f02e7-ff07-4e48-be94-26a94c409464.jpeg)
#### Modules of the Technical Characteristics Evaluation System


![imagen](https://user-images.githubusercontent.com/36687480/213280478-d082ef9e-06ab-4b3f-9e0b-860e950a401a.png)
#### Comparison of average sentiments (Users vs Manufacturers)


### 1) The script MODULO_RECOLECCION_DATOS.ipynb for the GitHub repository, presents the methodology for data collection, where comments from the Amazon platform are downloaded.

### 2) The script MODULO_PREPROCESAMIENTO.ipynb for the GitHub repository, presents the data preprocessing methodology, requires the excel file FINAL.xlsx that comes from the previous step, and NOUNS.xlsx. Apply the following processing steps a) Normalization and Tokenization, b) Clause Segmentation, c) Stemming and POS Tagging, d) Deleting of Stop Words, and e) Features Extraction. The tagging of sentiments and aspects is done manually for model training.

### 3) The script MODULO_AUMENTO.ipynb for the GitHub repository, presents the methodology to stabilize the classes for the technical aspects, with the data augmentation algorithms and data processing logic in step 2. It uses excel AMAZON_FINAL.xlsx which comes from the previous step.

### 4) The script MODULO_MODELAJE.ipynb for the GitHub repository, presents the modeling methodology and classification of technical features, uses the excel AMAZON_AUGMENTED.xlsx that comes from the previous step, and MANUFACTURER.xlsx that contains the clauses, aspects and sentiments that are developed manually.
