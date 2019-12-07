# script to execute notebooks using the Python API interface
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert.preprocessors import CellExecutionError

# Path of notebooks
classification_directory = "classification-models/"
regression_directory = "regression-models/"
classifierInter_directory = "Classifier interpretability/"

Cfile_paths = ["Adult/", "Breast Cancer Wisconsin/", "Default of credit card clients/", "Diabetic Retinopathy/", "Seismic-Bumps/", "Statlog-Australian credit approval/",
                "Statlog-German credit data/", "Steel Plates Faults/", "Thoracic Surgery Data/", "Yeast/"]

Rfile_paths = ["Bike Sharing/", "Communities and Crime/", "Concrete Compressive Strength/", "Facebook metrics/", "Merck Molecular Activity Challenge/", 
                "Parkinson Speech/", "QSAR aquatic toxicity/", "SGEMM GPU kernel performance/", "Student Performance/", "Wine Quality/"]

file_name = "model.ipynb"

def execute_notebook(datasetName):
    print("\nexecuting..."+str(datasetName))
    
    with open(datasetName+file_name) as f:
        nb = nbformat.read(f, as_version=4)

    ep = ExecutePreprocessor(timeout=36000, kernel_name='python3')


    try:
        out = ep.preprocess(nb, {'metadata': {'path': datasetName}})
    except CellExecutionError:
        out = None
        msg = 'Error executing the notebook "%s".\n\n' % datasetName+file_name
        msg += 'See notebook "%s" for the traceback.' % datasetName+file_name
        print(msg)
        raise
    finally:
        with open(datasetName+file_name, mode='w', encoding='utf-8') as f:
            nbformat.write(nb, f)

def start_classification():
          
    for i, file_path in enumerate(Cfile_paths):
        datasetname = classification_directory + file_path
        execute_notebook(datasetname)
        print("complete the execution of..."+str(datasetname))

def start_regression():
          
    for i, file_path in enumerate(Rfile_paths):
        datasetname = regression_directory + file_path
        execute_notebook(datasetname)
        print("complete the execution of..."+str(datasetname))

def start_classifierInterpretability():
    execute_notebook(classifierInter_directory)
    print("complete the execution of..."+str(classifierInter_directory))

start_classification()
start_regression()
start_classifierInterpretability()

          
    
     
   
  