"""
Functions for customer segmentation using K-means clustering.
"""

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def run_kmeans(data, n_clusters=3):
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(data)

    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(X_scaled)

    return kmeans.labels_, kmeans
