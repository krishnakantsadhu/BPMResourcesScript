package com.eai.util;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.ObjectInputStream;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Enumeration;
import java.util.Hashtable;
import java.util.Iterator;

import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

public class BPMResourceScriptGenerator {

	private static String ActivationSpecSheetName = "ActivationSpec";
	private static String QCFSheetName = "QCF";
	private static String QueueJNDISheetName = "QueueJNDI";

	private static String activationSpecTemplatePath = ".\\templates\\ActivationSpec_PY.template";
	private static String queueJndiTemplatePath = ".\\templates\\QueueJNDI_PY.template";
	private static String qcfTemplatePath = ".\\templates\\MQCF_PY.template";
	private static String saveConfigTemplatepath = ".\\templates\\SaveConfig_PY.template";
	private static String outPutScriptPath = ".\\Scripts\\BPMResources.py";
	private static String dataFile = ".\\Data\\BPMResourcesData.xlsx";

	ArrayList<String> activationSpecTemplate = new ArrayList<String>();
	ArrayList<String> queueJndiTemplate = new ArrayList<String>();
	ArrayList<String> qcfTemplate = new ArrayList<String>();
	ArrayList<String> saveConfigTemplate = new ArrayList<String>();
	ArrayList<String> outPutScript = new ArrayList<String>();

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		System.out.println(">>>>>>>>> Program Start >>>>>>>>>>");

		BPMResourceScriptGenerator s = new BPMResourceScriptGenerator();
		s.readTemplate(s.activationSpecTemplate, activationSpecTemplatePath);
		s.readTemplate(s.queueJndiTemplate, queueJndiTemplatePath);
		s.readTemplate(s.qcfTemplate, qcfTemplatePath);
		s.readTemplate(s.saveConfigTemplate, saveConfigTemplatepath);

		s.generateScript(dataFile, s.activationSpecTemplate, ActivationSpecSheetName);
		s.generateScript(dataFile, s.qcfTemplate, QCFSheetName);
		s.generateScript(dataFile, s.queueJndiTemplate, QueueJNDISheetName);
		s.generateScript(null, s.saveConfigTemplate, null);
		
		s.printScript(outPutScriptPath);

		// s.readExcel();
		System.out.println(">>>>>>>>> Program End >>>>>>>>>>");
	}

	public void readTemplate(ArrayList<String> template, String templatePath) {
		System.out.println("Reading template ---> " + templatePath);
		DataInputStream in = null;
		BufferedReader br = null;
		FileInputStream templatefile = null;

		try {
			templatefile = new FileInputStream(new File(templatePath));

			in = new DataInputStream(templatefile);
			br = new BufferedReader(new InputStreamReader(in));

			String strLine = "";
			while ((strLine = br.readLine()) != null) {
				template.add(strLine);
			}

		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			try {
				if (br != null)
					br.close();
				if (in != null)
					in.close();
				if (templatefile != null)
					templatefile.close();
			} catch (Exception ignore) {
			}
		}
	}

	public void generateScript(String datafilePath, ArrayList<String> template, String sheetName) {
		XSSFWorkbook workbook = null;
		FileInputStream file = null;
		if(datafilePath == null) {
			for (String templateLine : template) 
				outPutScript.add(templateLine);
		}
		else {
			try {
				System.out.println("Reading Resources data ---> " + datafilePath +" WorkSheet --->"+sheetName);
				file = new FileInputStream(new File(datafilePath));
				workbook = new XSSFWorkbook(file);
				Sheet sheet = workbook.getSheet(sheetName);
				Iterator<Row> rowIterator = sheet.iterator();

				Row headerRow = null;

				while (rowIterator.hasNext()) {
					if (headerRow == null) {
						headerRow = rowIterator.next();
					} else {
						Row dataRow = rowIterator.next();
						if(dataRow.getCell(0) != null && ! dataRow.getCell(0).getStringCellValue().trim().equals("")) {
						for (String templateLine : template) {
							Iterator<Cell> headerCellIterator = headerRow.cellIterator();
							while (headerCellIterator.hasNext()) {
								Cell headerCell = headerCellIterator.next();
								Cell dataCell = dataRow.getCell(headerCell.getColumnIndex());

								templateLine = templateLine
										.replace("$" + headerCell.getStringCellValue().trim() + "$",
												getValue(dataCell));
							}// end of while
							outPutScript.add(templateLine);
							// System.out.println("script line : " + templateLine);
						} // end of for
						}
					}
				}
			} catch (FileNotFoundException e) {
				e.printStackTrace();
			} catch (IOException e) {
				e.printStackTrace();
			} finally {
				try {
					if (workbook != null)
						workbook.close();
					if (file != null)
						file.close();
				} catch (Exception ignore) {
				}
			}

		}
	}

	public void printScript(String scriptPath) {
		System.out.println("Generating script file --->" + scriptPath);
		FileOutputStream scriptfile = null;
		DataOutputStream out = null;
		BufferedWriter bw = null;
		try {

			scriptfile = new FileOutputStream(new File(scriptPath));

			out = new DataOutputStream(scriptfile);
			bw = new BufferedWriter(new OutputStreamWriter(out));

			if (outPutScript.size() > 0) {
				//Tue Jul 12 18:35:37 IST 2016
				bw.write("############################# BPM Resource generation script #################################################\n");
				bw.write("## Author  : Krishnakant                                                                                    ##\n");
				bw.write("## Version : 1.0                                                                                            ##\n");
				bw.write("## Date    : "+new java.util.Date()+"                                                                   ##\n");	
				bw.write("## Usage   : wsadmin.sh -lang jython -user <<user_name>> -password <<password>> -f <<path of script file>>  ##\n");
				bw.write("##############################################################################################################\n\n");
				bw.write("\n\n#-----------------------------------------------------------------------------");
				bw.write("\n# init");
				bw.write("\n#-----------------------------------------------------------------------------");
				bw.write("\nisSkipIfExist = 1");
				bw.write("\ncellName = AdminControl.getCell()");
				bw.write("\ncellID = '/Cell:%s'%cellName");
				bw.write("\nscopeID = AdminConfig.getid(cellID)");
					
				bw.write("\nqueues = AdminConfig.list('MQQueue',scopeID).splitlines()");
				bw.write("\nconnectionFactories = AdminConfig.list( 'MQQueueConnectionFactory', scopeID ).splitlines()");
				bw.write("\nactivationSpecs =  AdminConfig.list( 'J2CActivationSpec', scopeID ).splitlines()");
				bw.write("\nGREEN = '\033[92m'");
				bw.write("\nYELLOW = '\033[93m'");
				bw.write("\nRED = '\033[91m'");
				bw.write("\nEND = '\033[0m'");
				bw.write("\n#-----------------------------------------------------------------------------\n");
				
			}
			
			for (String scriptLine : outPutScript) {
				bw.write(scriptLine + "\n");
			}

		} catch (Exception e) {

		} finally {
			try {
				if (bw != null)
					bw.close();
				if (out != null)
					out.close();
				if (scriptfile != null)
					scriptfile.close();
			} catch (Exception ignore) {
			}
		}

	}

	public static String getValue(Cell dataCell) {
		String valueStr = "";
		try {
		if (dataCell != null && Cell.CELL_TYPE_NUMERIC == dataCell.getCellType()) {
			Double d = new Double(dataCell.getNumericCellValue());
			valueStr = Integer.toString(d.intValue());
		} else {
			valueStr = dataCell.getStringCellValue().replaceAll(" ", "");
		}
		}catch(Exception e) {}

		return valueStr;
	}

}
