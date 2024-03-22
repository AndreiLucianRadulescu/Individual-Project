# User manual 

Theoretically speaking, you do not have to run the code as the files are Python notebooks, and all outputs have been saved. If you however still wish to run the code, here is the guide to do so.


Firstly, you should add the two datasets of UTKFace and appa-real into the data/raw/ folder, with the directories called "UTKFaces" and "appa-real-release". After this step is performed you should run the notebooks located in the data/notebooks directory, in the following order: process_UTK_faces.ipynb -> process_appareal.ipynb -> move_images.ipynb.


Moving forward, you should run the notebook tune_dataset_and_cache.ipynb which removes pictures of babies (age < 5). After this, please run the linear_classifiers_hog.ipynb, as this notebook creates a pandas dataframe and saves it with pickle, to ensure consistency in the data between all approaches. After this dataframe is saved locally, you can run linear_classifiers_lbp.ipynb.


For the CNNs experiment, you should upload all notebooks containing collab in the name to Google Colab, and upload an archive of all images of the dataset, along with all the json files and the dataframe, as these files cache the dataset and the splits.


Finally, to run the binary experiments for LBP and HOG, you must have run the initial experiment of HOG and LBP with 6 classes, and similarly for the CNN for binary classes, you must have the dataframe and the json files created.