# Machine learning models on various 21 datasets (from UCI and Kaggle)
The project is based on datasets from various sectors namely finance, health, industrial, crime, education, social media, biology, product and multimedia from the UCI repository and Kaggle.
Preprocessed the data, split dataset into training and test set, if required and finally transformed it.

- Trained and evaluated 8 classification methods across 10 classification datasets, 7 regression methods across 10 regression datasets and 2 classification methods (Convolutional Neural Network and Decision Tree Classifier) on an image classification dataset (CIFAR10).

- Used selected hyperparameters to search over and find the best combination of them using Grid Search and Randomized Search as required to improve model’s accuracy.
#### IDE used: jupyter notebook.
```
/classification-models/
	 10 jupyter notebooks per classification dataset each named as model.ipynb

/regression-models/
	10 jupyter notebooks per regression dataset each named as model.ipynb

/Classifier interpretability/
	model.ipynb - CNN and Decision Tree Implemented on CIFAR10 dataset
	dataset/ - please put the CIFAR10 dataset inside this folder
	
```
#### 1. To run the entire project run following python script:
	type this command in terminal: python main.py
	
	-It will start executing each jupyter notebook sequentially, a 
	 message regarding which current dataset model is being executed

#### 2. To see the results, please check each jupyter notebook after it completes its execution.

 #### Tech Stack
* [Python 3](https://www.python.org/)
* [Jupyter Notebook](https://jupyter.org/)
* [scikit-learn](https://scikit-learn.org/stable/)
* [NumPy](https://numpy.org/)
* [pandas](https://pandas.pydata.org/)
* [Matplotlib](https://matplotlib.org/)
* [Seaborn](https://seaborn.pydata.org/)
* [pytorch](https://pytorch.org/)

