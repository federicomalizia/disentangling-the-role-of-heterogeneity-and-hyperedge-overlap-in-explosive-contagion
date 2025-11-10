import numpy as np
from itertools import combinations
from collections import Counter
# import numba  # Uncomment if you wish to JIT compile later
# from numba import njit


def list_edges_by_size(edges, edge_sizes, max_order, min_order):
    """
    Group edges by their size (order).

    Parameters
    ----------
    edges : list of tuples
        Each element is a (key, members) pair, where members is an iterable of nodes.
    edge_sizes : list of int
        The order (size) of each edge.
    max_order : int
        The largest edge size in the hypergraph.
    min_order : int
        The smallest edge size in the hypergraph.

    Returns
    -------
    dict
        A dictionary mapping edge order -> list of edge member sets.
    """
    grouped_edges = {}
    for i in range(min_order, max_order + 1):
        grouped_edges[i] = [edges[j][1] for j, size in enumerate(edge_sizes) if size == i]
    return grouped_edges


def interorder_overlap_mn(L, m, n, N):
    """
    Compute the inter-order overlap between hyperedges of orders m and n.

    Parameters
    ----------
    L : dict
        Dictionary mapping order -> list of edges of that order.
    m : int
        Lower-order edge size.
    n : int
        Higher-order edge size.
    N : int
        Total number of nodes in the hypergraph (unused but kept for consistency).

    Returns
    -------
    float
        Normalized interorder overlap between m-edges and n-edges, or np.nan if undefined.
    """
    if not L[m] or not L[n]:
        return np.nan

    # Convert each hyperedge to a sorted tuple for consistency and fast set comparison
    Lm = [tuple(sorted(e)) for e in L[m]]
    Ln = [tuple(sorted(e)) for e in L[n]]

    overlap_count = 0
    for e_m in Lm:
        for e_n in Ln:
            # Check if m-edge is a subset of n-edge
            if set(e_m).issubset(e_n):
                overlap_count += 1
                break  # Only count each m-edge once

    # Compute possible (m+1)-size subsets of n-edges
    possible_subsets = set()
    for e_n in Ln:
        for subset in combinations(e_n, m + 1):
            possible_subsets.add(tuple(sorted(subset)))

    return overlap_count / len(possible_subsets) if possible_subsets else np.nan


def inter_order_overlap_alpha_matrix(H, max_order=None):
    """
    Compute the inter-order overlap matrix (alpha matrix) for a hypernetwork.

    Parameters
    ----------
    H : object
        Hypergraph-like object with:
        - H.edges.size.aslist() -> list of edge sizes
        - H.num_nodes -> number of nodes
        - H.edges.members(dtype=dict) -> dictionary of edge_id -> member list
    max_order : int, optional
        Maximum order to consider. Defaults to the maximum edge size in H.

    Returns
    -------
    np.ndarray
        Matrix of inter-order overlap coefficients between different orders.
    """
    edge_sizes = H.edges.size.aslist()
    num_nodes = H.num_nodes
    edge_dict = H.edges.members(dtype=dict)
    edges = list(edge_dict.items())

    # Adjust edge sizes to reflect order (subtract 1)
    edge_sizes = [size - 1 for size in edge_sizes]

    if max_order is None:
        max_order = max(edge_sizes)
    min_order = min(edge_sizes)

    print(f'Max order: {max_order}, Min order: {min_order}')

    # Group edges by order
    grouped_edges = list_edges_by_size(edges, edge_sizes, max_order, min_order)

    # Initialize overlap matrix
    alpha_matrix = np.full((max_order - min_order, max_order - min_order), np.nan)

    # Compute overlaps only for m < n (upper triangle)
    
    for m in range(1, max_order):
        print(f'Computing overlaps for order {m}/{max_order}')
        for n in range(m + 1, max_order):
            alpha_matrix[m - 1, n - 1] = interorder_overlap_mn(grouped_edges, m, n, num_nodes)

    return alpha_matrix