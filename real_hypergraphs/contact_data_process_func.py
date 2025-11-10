import numpy as np
import networkx as nx
import json




def extract_networks(data_dir, dataset, n_minutes, original_nets=True, tmax=1000000):
    """Function that reads the edgelist (t, i, j) and returns
    a network aggregated at n_minutes snapshots as a dictionary of nx.Graph()s,
    having t as a key.
    If original_nets is set to True it also returns the original non-aggregated network."""
    
    #Reading the data and setting t0
    f = open(data_dir + dataset +'.dat')
    (t0,i,j) = map(float,str.split(f.readline()))
    aggtime=t0
    #Special temporal scale for these two Datasets
    f.close()
    
    #Aggregation on scale of x minutes
    delta_t = 60*n_minutes;  
    #print(delta_t)
    if original_nets==True:
        originalnetworks = {}
    aggnetworks = {}
    f = open(data_dir + dataset +'.dat')
    counter=0
    for line in f:
        (t,i,j) = map(float,str.split(line))
        #Special temporal scale for these two Datasets
        if original_nets==True:
            if t not in originalnetworks:
                originalnetworks[t] = nx.Graph()
            originalnetworks[t].add_edge(i,j)
        #this is a trick using the integer division in python
        #aggtime = t0 + ((t-t0)/delta_t)*delta_t 
        if t>=aggtime+delta_t:
            aggtime=aggtime+delta_t
        if aggtime not in aggnetworks:
            aggnetworks[aggtime] = nx.Graph()
        aggnetworks[aggtime].add_edge(i,j)
    f.close();
    print('last time',aggtime)
    #for aggtime in aggnetworks:
        #print('time',aggtime)
        #G_=aggnetworks[aggtime]
        #print('networksize',len(G_.edges()))
    if original_nets==True:
        return originalnetworks, aggnetworks;
    else:
        return aggnetworks;
    
def extract_cliques(gs):
    listsaggcliques = {}
    #looping over the networks in temporal order
    for t in sorted(gs.keys()):
        listsaggcliques[t] = list(nx.find_cliques(gs[t]));
    #returning a dictionary with list of cliques as values
    return listsaggcliques;
    
def clique_weights(cliques):
    from collections import Counter;
    tot_c = [];
    for t in cliques:
        tot_c.extend(map(frozenset,cliques[t]))
    return Counter(tot_c);

def average_clique_size(ws):
    return np.sum(map(lambda x: 1.0 * ws[x] * len(x), ws.keys()))/np.sum(ws.values());

def clean_non_maximal(ws):
    sd = dict(zip(ws.keys(), map(len,ws.keys())));
    import operator
    sizes = set(map(len,ws.keys()));
    sorted_sd = sorted(sd.items(), key=operator.itemgetter(1));
    simplices = dict.fromkeys(list(sizes),[]);
    maximal_simplices = {};
    for x in ws:
        maximal = True;
        for xx in ws:
            if (len(x)<len(xx)):
                if (set(x)<set(xx)):
                    maximal=False;
                    break;
        if maximal:
            maximal_simplices[x] = ws[x];
    return maximal_simplices;

def save_cliques(ws, data_dir, dataset,n_minutes, thr=None):
    if thr==None:
        ls = map(list,ws.keys());
    else:
        ls = [list(x) for x in ws if ws[x]>=thr];
    jd = open(data_dir+'25daysaggr_'+str(n_minutes)+'min_cliques_thr'+str(thr)+'_'+dataset+'.json','w')
    json.dump(ls,jd)
    jd.close()
    return;