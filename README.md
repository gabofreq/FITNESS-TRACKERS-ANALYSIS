#### 1) The script MODULO_RECOLECCION_DATOS.ipynb for the GitHub repository, presents the methodology for data collection, where comments from the Amazon platform are downloaded.

#### 2) The script MODULO_PREPROCESAMIENTO.ipynb for the GitHub repository, presents the data preprocessing methodology, requires the excel file FINAL.xlsx that comes from the previous step, and NOUNS.xlsx. Apply the following processing steps a) Normalization and Tokenization, b) Clause Segmentation, c) Stemming and POS Tagging, d) Deleting Stop Words, and e) Features Extraction. The tagging of sentiments and aspects is done manually for model training.

#### 3) The script MODULO_AUMENTO.ipynb for the GitHub repository, presents the methodology to stabilize the classes for the technical aspects, with the data augmentation algorithms and data processing logic in step 2. It uses excel AMAZON_FINAL.xlsx which comes from the previous step.

#### 4) The script MODULO_MODELAJE.ipynb for the GitHub repository, presents the modeling methodology and classification of technical features, uses the excel AMAZON_AUGMENTED.xlsx that comes from the previous step, and MANUFACTURER.xlsx that contains the clauses, aspects and sentiments that are developed manually.
