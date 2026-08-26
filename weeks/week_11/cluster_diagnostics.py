"""Week 11 clustering diagnostics.

Clustering is diagnostic only; it does not replace the primary GP/acquisition
optimisation workflow.
"""
from dataclasses import dataclass
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

@dataclass(frozen=True)
class ClusterSummary:
    cluster_id:int
    size:int
    mean_objective:float
    best_objective:float
    centroid:np.ndarray

def nearest_neighbour_distance(X):
    X=np.asarray(X,float)
    if len(X)<2: return np.full(len(X), np.nan)
    D=np.linalg.norm(X[:,None,:]-X[None,:,:], axis=2)
    np.fill_diagonal(D, np.inf)
    return D.min(axis=1)

def cluster_observations(X,y,n_clusters=None,random_state=42):
    X=np.asarray(X,float); y=np.asarray(y,float).reshape(-1)
    if len(X)!=len(y): raise ValueError("X and y length mismatch")
    if n_clusters is None:
        n_clusters=int(np.clip(round(np.sqrt(len(X))),2,5))
    n_clusters=min(n_clusters,len(X))
    Z=StandardScaler().fit_transform(X)
    labels=KMeans(n_clusters=n_clusters,n_init=20,
                  random_state=random_state).fit_predict(Z)
    summaries=[]
    for cid in sorted(np.unique(labels)):
        m=labels==cid
        summaries.append(ClusterSummary(
            int(cid), int(m.sum()), float(y[m].mean()), float(y[m].max()),
            X[m].mean(axis=0)))
    summaries.sort(key=lambda s:s.best_objective, reverse=True)
    return labels,summaries
