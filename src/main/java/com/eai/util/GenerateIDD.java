package com.eai.util;

import java.io.File;
import java.io.IOException;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.FactoryConfigurationError;
import javax.xml.parsers.ParserConfigurationException;

import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;

import javax.xml.validation.SchemaFactory;
import javax.xml.validation.Schema;
import javax.xml.XMLConstants;
import java.io.File;



import org.xml.sax.SAXException;

public class GenerateIDD {

	public static void main(String[] s) {
		Document doc = getRoot(".\\templates\\SRVcreateNetworkTicketByHPSM_Req_ESB.xsd");
		NodeList list = doc.getChildNodes();

		getNodes(list);

	}

	private static Document getRoot(String docPath) {

		Document document = null;
		try {
			DocumentBuilder documentbuilder = DocumentBuilderFactory
					.newInstance().newDocumentBuilder();
			document = documentbuilder.parse(new File(docPath));
			System.out.println("getting file path : " + docPath);

			NodeList nodes = document.getChildNodes();

		} catch (SAXException saxexception) {
			saxexception.printStackTrace();
		} catch (IOException ioexception) {
			ioexception.printStackTrace();
		} catch (ParserConfigurationException parserconfigurationexception) {
			parserconfigurationexception.printStackTrace();
		} catch (FactoryConfigurationError factoryconfigurationerror) {
			factoryconfigurationerror.printStackTrace();
		}

		return document;
	}

	private static void getNodes(NodeList nodeList) {
		
		
		for (int i = 0; i < nodeList.getLength(); i++) {
			
			
			Node first =  nodeList.item(i);
			
			
			
			String nam = first.getNodeName();
						
			String nam1 = first.getNodeValue();
			System.out.println("name=" + nam +" type="+nam1); 
			
			
			/*if( first.hasAttributes()) 
			{
			String nam = first.
			
			String nam1 = first.getAttribute("type"); 
			System.out.println("name=" + nam +" type="+nam1); 
			}*/

			//System.out.println(element.getNodeName() + " "
			//		+ element.getTagName() + " " + element.getNodeType());

			NodeList childNodeList = first.getChildNodes();

			getNodes(childNodeList);
		}
	}
	
	
	public static Schema loadSchema(String name) {
	    Schema schema = null;
	    try {

	      // getting the default implementation of XML Schema factory
	      String language = XMLConstants.W3C_XML_SCHEMA_NS_URI;
	      SchemaFactory factory = SchemaFactory.newInstance(language);
	      System.out.println();
	      System.out.println("Schema Language: "+language);
	      System.out.println("Factory Class: "
	        + factory.getClass().getName());

	      // parsing the schema file      
	      schema = factory.newSchema(new File(name));
	      
	     
	      System.out.println();
	      System.out.println("Schema File: "+name);
	      System.out.println("Schema Class: "
	        + schema.getClass().getName());

	    } catch (Exception e) {
	      // catching all exceptions
	      System.out.println();
	      System.out.println(e.toString());
	    }
	    return schema;
	  }

	

}
