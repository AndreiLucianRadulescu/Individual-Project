# Readme

Our project tackles the problem of age estimation from faces. We have two separate folders in our structure, src and data. In the data folder, we have only included the notebooks folder, which contains both python notebooks as well as python scripts. These deal with preprocessing the images, i.e. detecting the faces in both of our datasets, resizing the images to 128x128. There are python scripts that do this and one of them utilises 8 processes at once, and thus could be computationally expensive.


The json files represent important information about the train, test and validation splits. Furthermore, they are re-created upon running the HOG notebook.


In order to explain what the second folder, src, contains, we must explain how we conducted our experiments. There are 2 parts: traditional approaches and CNNs. For the traditional approaches, we have one notebook for HOG and LBP, and the HOG notebook *must* be run first, as it creates json splits of data and a pickled dataframe that we just load in the LBP notebook. For our second part, where we used neural networks, we conducted the experiment on Google Colab as we could not train the networks on our system. In order to run these, it *is advised* to import them into Colab.

## Build instructions

In order to build our code, you have to run the HOG experiment notebook *first*, as it creates a pickled file that is loaded in the LBP and CNN experiments, and also some json files that contain relevant information about our splits. Furthermore, in some of our notebooks we just re-imported the already trained models and tested them in order to compute graphs, plots, etc (on Google Colab). We would have included the model in the submission, but they are too large.

### Requirements

All Python libraries are located in the requirements.txt files. However, be aware that we combined the requirements from Google Colab with the requirements on our own machine. Therefore, for a better experience, run the notebooks that contain _colab in their name on Google Colab.


Furthermore, it is important to note that you need the datasets. The datasets should be placed in the folder data/raw/ in two separate folders, namely 'appa-real-release' and 'UTKFaces'.


* Python 3.10.11
* Packages: listed in `src/requirements.txt` 
* To use our face detector, you have to install CMake.

* Tested on Windows 11, and Google Colab

### Build steps
First, you have to download and place the datasets into the folder highlighted above.
To build our code just run *pip install requirements.txt*, and then run the notebooks one by one. The order should be: notebooks in the data folder, that preprocess the images, then the HOG notebook, then LBP/CNN.

### Test steps

In order to verify that our code worked correctly you can visualise the notebook outputs, as all outputs have been saved. If you want to run the notebooks yourself, please refer to the above section.

### Contact
If you have any trouble running the code, please contact me at 2577007r@student.gla.ac.uk. Also, you can access the project at https://github.com/AndreiLucianRadulescu/Individual-Project.