# Deutsch-Jozsa Part II and Qubit Visualization

The content in these notebooks are meant to sum up some of the topics of the last workshop ( [Deutsch-Jozsa](https://youtu.be/NPf_kPRmK5k)) as well as provide more detail on some core topics that did not get sufficient coverage (Phase Kickback and the alternative formulations for the Hadamard Operation/Phase Oracle). 

The relevant notebooks for the above are (in order of the material presented):
* `Fundamentals.ipynb`
* `Deutsch's-Algorithm.ipynb`
* `Deutsch-Jozsa.ipynb`

There is also additional content on visualizing Qubits with the Bloch Sphere in the `Qubit-Visualization.ipynb` notebook, based off of [QCaD-Circuits-I.ipynb](https://github.com/QC-at-Davis/npquantum/blob/master/QCaD-Circuits-I.ipynb) (which you are encouraged to experiment with as well, considering it covers many of the gates this workshop didn't), along with `QCaD-Circuits-II.ipynb` in the same repository.


## Getting Set Up
* intsall [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
  * After installation open your terminal and run `git --version` just to make sure it installed properly
* install [conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html)
  * After installation open your terminal and run `conda --version` just to make sure it installed properly
* Clone this repository to a place on your system
  * Run the following in the cloned folder
  * `conda env create --file=environments.yml`
* run `jupyter-lab` in your command line, you should see the Jupyter Lab pop up in your browser. On the left hand side you should be able to navigate through the different notebooks.
