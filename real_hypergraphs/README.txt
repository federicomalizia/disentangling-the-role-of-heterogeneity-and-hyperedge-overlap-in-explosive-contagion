# Higher-Order Network Analysis

This repository contains Python code and Jupyter notebooks for analyzing real-world and contact-based higher-order networks. The project focuses on hypergraphs, inter-order overlaps, and structural characterization of interactions of different orders.

The codes here used were developed for the supplementary material of the work: 'Disentangling the Role of Heterogeneity and Hyperedge Overlap in Explosive Contagion on Higher-Order Networks' by  Federico Malizia,1 Andres Guzman,1 Iacopo Iacopini, and Istvan Z. Kiss.

---


## Real World hypergraphs

For this section we first take the data which can be extracted directly from XGI library or from th edge lists located in the folder *hyperedge_list_real_data*. The jupyter notebook *real_hypergraoh_overlap.ipyn* cotnains the analyss done toobtain the overlap matrix of some real-world examples of hypergraphs.Folder *cleand_edges_lists_datasets* contains clean version of the edge lists onf the hypergraphs, this is, after taking out repeated edges and selfloops. Axuiliary function *overlap_func.py* contains functions used to calculate the overlap matrix. .  The reulst are stored in the floder *overlap_matrices*


## Real contact data

The raw data is stored in the folder *contact_data_raw* and it corresponds to dataset collected by the Copenhagen Network Study https://www.nature.com/articles/s41597-019-0325-x, which records high-resolution Bluetooth proximity data among university students.

The notebook *porcess_contact_data.ipyn* creates the higher-order networks based on a time window and ona minimum number of cotnaxt as explained in the supplementary material of our paper. Tha resulting hypergraphs are stored in the folder *copenhagen_processed_edge_lists*. Notebook *contact_data_overlap.ipynb* contains the analyiss done to obtain the overlap matrices. Folder *edges_lists_clean_contact_data* contains clean version of the edge lists onf the hypergraphs, this is, after taking out repeated edges and selfloops. 