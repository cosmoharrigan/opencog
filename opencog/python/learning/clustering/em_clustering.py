"""
Example usage of WekaInterface to run the Weka implementation of EM clustering on a dataset
"""

__author__ = 'Cosmo Harrigan'

from learning.clustering import weka_interface
weka_interface = weka_interface.WekaInterface()
weka = weka_interface.weka

# Sample dataset from this tutorial: http://www.ibm.com/developerworks/library/os-weka2/
# Also available to download here: https://docs.google.com/file/d/0B_8uf-8GCUsUSnN5bWlWNEN6WDQ/edit?usp=sharing
filename = 'http://fedora.cis.cau.edu/~pmolnar/CIS675P13/os-weka2-Examples/bmw-browsers.arff'
source = weka_interface.data_source(filename)
data = source.getDataSet()

# Create Instances from the dataset: http://weka.sourceforge.net/doc.stable/weka/core/Instances.html
instances = weka.core.Instances(data)

# Create an EM clusterer: http://weka.sourceforge.net/doc.stable/weka/clusterers/EM.html
em = weka.clusterers.EM()
em.buildClusterer(data)

# Class for evaluating clusterer models: http://weka.sourceforge.net/doc.stable/weka/clusterers/ClusterEvaluation.html
cluster_evaluation = weka.clusterers.ClusterEvaluation()
cluster_evaluation.setClusterer(em)

# Run the clusterer
cluster_evaluation.evaluateClusterer(instances)

print "Number of clusters: "
print cluster_evaluation.getNumClusters()
print "\nCluster results:"
print cluster_evaluation.clusterResultsToString()