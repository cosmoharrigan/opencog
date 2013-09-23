/*
 * opencog/python/learning/clustering/WekaInterface.java
 *
 * Copyright (C) 2013 OpenCog Foundation
 * All Rights Reserved
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU Affero General Public License v3 as
 * published by the Free Software Foundation and including the exceptions
 * at http://opencog.org/wiki/Licenses
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU Affero General Public License
 * along with this program; if not, write to:
 * Free Software Foundation, Inc.,
 * 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
 */

import weka.clusterers.*;
import weka.core.*;
import weka.core.converters.ConverterUtils;
import py4j.GatewayServer;
import java.io.IOException;

/*
 *  Provides an interface to the Weka machine learning toolkit from Python using Py4J
 *  To use, export and run the JAR in the background to allow access to Weka from Python:
 *      java -jar WekaInterface.jar
 *  For example usage, refer to: opencog/python/learning/clustering/weka_interface.py
 *  To add to the available Weka classes, just import from the appropriate subpackage
 *  
 *  Requires the following external JARs to be added to the build path:
 *      py4j0.8.jar		http://py4j.sourceforge.net/download.html
 *      weka.jar		http://www.cs.waikato.ac.nz/ml/weka/downloading.html
 *      
 *  @author Cosmo Harrigan
 */

public class WekaInterface {
	public WekaInterface() {
		System.out.println("Starting Weka interface.");
	}
	
	public static void main(String[] args) throws IOException {
		System.out.println("Starting py4j interface to JVM.");
		GatewayServer gatewayServer = new GatewayServer(new WekaInterface());//, 30001);
		gatewayServer.start();
		
		// Alternatively, this program could be configured as a daemon using Apache Daemon
		System.out.println("Interface is running. Press any key to terminate and exit.");
		System.in.read();
		
		gatewayServer.shutdown();
		System.out.println("Server stopped.");
	}
}

