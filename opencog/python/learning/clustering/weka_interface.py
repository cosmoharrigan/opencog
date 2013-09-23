__author__ = 'Cosmo Harrigan'

from py4j.java_gateway import JavaGateway, GatewayClient


class WekaInterface(object):
    """
    Provides an interface to the Weka machine learning toolkit in Java from Python using Py4J,
    allowing access the classes from the Weka Javadoc in Python.

    Weka Javadoc:
    http://weka.sourceforge.net/doc.stable/

    Weka examples in Java:
    http://weka.wikispaces.com/Use+WEKA+in+your+Java+code

    Example usage:
    from learning.clustering import weka_interface
    weka_interface = WekaInterface()
    weka = weka_interface.weka

    Then you can access the classes like this:
    em = weka.clusterers.EM()

    The related Java code is: opencog/python/learning/clustering/WekaInterface.java

    Prerequisites:
    1. Py4J http://py4j.sourceforge.net/download.html
    2. Weka JAR http://www.cs.waikato.ac.nz/ml/weka/downloading.html
    3. Java
    4. The WekaInterface.java class should be exported into a JAR and must already be running on the system
    java -jar wekainterface.jar
    """
    def __init__(self):
        # Create the Py4J interface between Python and the Java Virtual Machine
        self.gateway = JavaGateway()

        # Define a shortcut to the Weka classes
        self.weka = self.gateway.jvm.weka

        # Define the DataSource utility
        # http://weka.sourceforge.net/doc.stable/weka/core/converters/ConverterUtils.DataSource.html
        self.data_source = self.weka.core.converters.ConverterUtils.DataSource


