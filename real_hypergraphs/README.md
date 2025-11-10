# Higher-Order Network Analysis

This repository contains Python code and Jupyter notebooks for analyzing **real-world** and **contact-based** higher-order networks. The project focuses on **hypergraphs**, **inter-order overlaps**, and the **structural characterization** of interactions across different orders.

The scripts and notebooks included here were developed as part of the supplementary material for the paper:

> **"Disentangling the Role of Heterogeneity and Hyperedge Overlap in Explosive Contagion on Higher-Order Networks"**  
> Federico Malizia, Andres Guzman, Iacopo Iacopini, and Istvan Z. Kiss.

---

## Real-World Hypergraphs

This section focuses on datasets where higher-order group interactions are **explicitly defined**, such as collaboration networks, tagging systems, or biochemical complexes.  

Data can be extracted either directly from the **[XGI library](https://xgi.readthedocs.io/en/stable/)** or from the edge lists provided in the folder `hyperedge_list_real_data/`.

### Key components

- **Notebook:** `real_hypergraph_overlap.ipynb`  
  Performs the analysis to compute the **inter-order overlap matrices** for several real-world hypergraphs.

- **Cleaned Edge Lists:** `clean_edges_lists_datasets/`  
  Contains **clean versions of the edge lists**, obtained after removing repeated hyperedges and self-loops.

- **Auxiliary Functions:** `overlap_func.py`  
  Contains helper functions used to calculate the overlap matrices and perform hypergraph-level computations.

- **Results:** `overlap_matrices/`  
  Stores the computed **inter-order overlap matrices** for each dataset.

---

## Contact Data

This section deals with higher-order networks **derived from temporal contact data**, specifically the dataset collected by the **[Copenhagen Network Study](https://www.nature.com/articles/s41597-019-0325-x)**.  
This dataset contains high-resolution Bluetooth proximity records among university students.

### Key components

- **Raw Data:** `contact_data_raw/`  
  Contains the original Bluetooth proximity data.

- **Notebook:** `process_contact_data.ipynb`  
  Constructs higher-order networks by aggregating pairwise interactions over fixed time windows and applying a minimum contact threshold, as described in the paper’s supplementary material.  
  The resulting hypergraphs are stored in `copenhagen_processed_edge_lists/`.

- **Notebook:** `contact_data_overlap.ipynb`  
  Computes the **inter-order overlap matrices** for the processed contact-based hypergraphs.

- **Cleaned Edge Lists:** `edges_lists_clean_contact_data/`  
  Contains **cleaned edge lists** for the contact-based hypergraphs (duplicates and self-loops removed).

---

### Summary of Outputs

| Folder | Description |
|--------|--------------|
| `hyperedge_list_real_data/` | Raw real-world hypergraph edge lists |
| `clean_edges_lists_datasets/` | Cleaned real-world edge lists |
| `overlap_matrices/` | Computed inter-order overlap matrices |
| `contact_data_raw/` | Original Bluetooth contact data |
| `copenhagen_processed_edge_lists/` | Processed higher-order contact hypergraphs |
| `edges_lists_clean_contact_data/` | Cleaned contact hypergraphs (no duplicates/self-loops) |

---

### Dependencies

All scripts are implemented in **Python 3** and rely on the following main libraries:

- [`xgi`](https://xgi.readthedocs.io/en/stable/) (for hypergraph representation and analysis)  
- `numpy`, `matplotlib`, `seaborn`  
- `json`, `os`, and `pandas` (for data management and I/O operations)

---

### Citation

If you use this code in your research, please cite the corresponding paper:

> Malizia, F., Guzman, A., Iacopini, I., & Kiss, I. Z. (Year). Disentangling the Role of Heterogeneity and Hyperedge Overlap in Explosive Contagion on Higher-Order Networks. *Journal/Repository*.  
> [Link to publication]
