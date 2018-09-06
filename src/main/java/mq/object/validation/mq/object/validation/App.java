package mq.object.validation.mq.object.validation;


import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Iterator;
import java.util.Set;

import org.apache.poi.POIXMLDocument;
import org.apache.poi.hssf.usermodel.HSSFSheet;
import org.apache.poi.hssf.usermodel.HSSFWorkbook;
import org.apache.poi.poifs.filesystem.POIFSFileSystem;
import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.xssf.usermodel.XSSFSheet;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

public class App {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		
		
		/*
		  String count[] = {"krish", "krishna","krish","abc","qaz","ddddd"};
	      Set<String> set = new HashSet<String>();
	      try {
	         for(int i = 0; i < count.length; i++) {
	            set.add(count[i]);
	         }
	         System.out.println(set);

	         
	      }
	      catch(Exception e) {e.printStackTrace();}*/
		
		
		
		

		try {
			TestTCPConnection();
		}catch(Exception e) {
			System.out.println(e.getStackTrace());
		}


	}


	public static void MQconfigValidation() {

		//String fdir = "C:\\Users\\KrishnakantSadhu\\Desktop\\Dipen\\UAT_MQCONFIG_V7.4.9\\UAT_MQCONFIG_V7.4.9";

		String fdir = "C:\\Users\\KrishnakantSadhu\\Desktop\\Dipen\\UAT_MQCONFIG_V7.4.10\\UAT_MQCONFIG_V7.4.10";
		ArrayList<File> files = new ArrayList<File>();
		App mqObjectValidation = new App();
		mqObjectValidation.listf(fdir, files);

		mqObjectValidation.readExcel(files);

		// TODO Auto-generated method stub

	}


	public static void TestTCPConnection() throws Exception {

		File file = new File("C:\\curl-7.61.0\\SOMA_input_file.txt");

		BufferedReader br = new BufferedReader(new FileReader(file));


		String stTrim = "";

		String h1 = "<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:man=\"http://www.datapower.com/schemas/management\">\n" +
				"\t<soapenv:Header/>\n" +
				"\t<soapenv:Body>\n" +
				"\t\t<man:request domain=\"SUMERUUAT\">\n" +
				"\t\t\t<man:do-action>" ;


		System.out.println(h1);

		int lenoffset = 6;

		int a = 1;
		 Set<String> set = new HashSet<String>();
		while ((stTrim = br.readLine()) != null) {

			int endIndex = -1;

			int startIndex = stTrim.indexOf("http://");
			if (startIndex == -1) {
				startIndex = stTrim.indexOf("https://");
				lenoffset = 7;
			}

			if(startIndex != -1)
				endIndex = stTrim.indexOf("/",lenoffset);

			if(startIndex != -1) {
				stTrim = stTrim.substring(startIndex+lenoffset, endIndex);
					
				set.add(stTrim);
               // add in set
			}

			startIndex = -1;	
			// System.out.println(a);
			// a++;
		}


		Iterator iter = set.iterator();
		
		while (iter.hasNext()) {
			String ipport= iter.next().toString();
		   
		    int posColon = ipport.indexOf(":");
			if(posColon != -1) {
				System.out.println("\t\t\t\t<TCPConnectionTest>");
				System.out.println("\t\t\t\t\t<RemoteHost>"+ipport.substring(0,posColon)+"</RemoteHost>");
				System.out.println("\t\t\t\t\t<RemotePort>"+ipport.substring(posColon+1,ipport.length())+"</RemotePort>");
				System.out.println("\t\t\t\t</TCPConnectionTest>");	
			}else {
				System.out.println("\t\t\t\t<TCPConnectionTest>");
				System.out.println("\t\t\t\t\t<RemoteHost>"+ipport.substring(0,ipport.length())+"</RemoteHost>");
				System.out.println("\t\t\t\t\t<RemotePort>80</RemotePort>");
				System.out.println("\t\t\t\t</TCPConnectionTest>");
			}
		}
				
		System.out.println("\t\t\t</man:do-action>");
		System.out.println("\t\t</man:request>"); 
		System.out.println("\t</soapenv:Body>"); 
		System.out.println("</soapenv:Envelope>");



	}



	public void listf(String directoryName, ArrayList<File> files) {
		File directory = new File(directoryName);

		// get all the files from a directory
		File[] fList = directory.listFiles();
		for (File file : fList) {
			if (file.isFile()) {
				files.add(file);
				//System.out.println(file);
			} else if (file.isDirectory()) {
				listf(file.getAbsolutePath(), files);
			}
		}
	}

	public void readExcel(ArrayList<File> files) {
		System.out.println("FileName,API,IP,Port,QMGR,Channel,qcf");
		for (File f : files) {
			//File f = new File("C:\\Users\\KrishnakantSadhu\\Desktop\\Dipen\\UAT_MQCONFIG_V7.4.9\\UAT_MQCONFIG_V7.4.9\\CPOS\\CPOS_Write - GU1_NE.xlsx");
			try {
				FileInputStream excelFile = new FileInputStream(f);

				Sheet sheet = null;
				if (f.getName().endsWith(".xlsx") || f.getName().endsWith(".XLSX")) {
					XSSFWorkbook wb = new XSSFWorkbook(excelFile);
					sheet = wb.getSheetAt(0);
				} else {
					HSSFWorkbook wb = new HSSFWorkbook(excelFile);
					sheet = wb.getSheetAt(0);
				}

				Iterator<Row> rowIterator = sheet.iterator();
				int api = -1;
				int ip = -1;
				int port = -1;
				int qmgr = -1;
				int qcf = -1;
				int channel = -1;
				boolean isFirstRow = true;

				while (rowIterator.hasNext()) {
					if (isFirstRow) {
						boolean isFirstRowHeader = false;
						Row headerRow = rowIterator.next();
						Iterator<Cell> cellIterator = headerRow.cellIterator();
						while (cellIterator.hasNext()) {
							Cell cell = cellIterator.next();
							String cellVal = getValue(cell);
							if(cellVal.equalsIgnoreCase("IP") || cellVal.equalsIgnoreCase("IP/Port") ) {
								ip = cell.getColumnIndex();
								isFirstRowHeader = true;
							}else if(cellVal.equalsIgnoreCase("Port")) {
								port = cell.getColumnIndex();
								isFirstRowHeader = true;
							}else if(cellVal.equalsIgnoreCase("Queue Manager") || cellVal.equalsIgnoreCase("QMGR") || cellVal.equalsIgnoreCase("Queue Manager Name")) {
								qmgr = cell.getColumnIndex();
								isFirstRowHeader = true;
							}else if(cellVal.equalsIgnoreCase("Channel name") || cellVal.equalsIgnoreCase("SVRCONN") || cellVal.equalsIgnoreCase("CHANNEL")) {
								channel = cell.getColumnIndex();
								isFirstRowHeader = true;
							}else if(cellVal.equalsIgnoreCase("QCF")) {
								qcf = cell.getColumnIndex();
								isFirstRowHeader = true;
							}else if(cellVal.equalsIgnoreCase("API/Event Details") || cellVal.equalsIgnoreCase("API Name") || cellVal.equalsIgnoreCase("ServiceName") || cellVal.equalsIgnoreCase("Surrounding Appl.") || cellVal.equalsIgnoreCase("EAI Service Name") || cellVal.equalsIgnoreCase("API")) {
								api = cell.getColumnIndex();
							}
						}

						if(isFirstRowHeader) 
							isFirstRow = false;
					}
					else {

						Row row = rowIterator.next();
						StringBuffer str = new StringBuffer();	
						str.append(api!=-1?getValue(row.getCell(api)):"").append(",");
						str.append(ip!=-1?getValue(row.getCell(ip)):"").append(",");
						str.append(port!=-1?getValue(row.getCell(port)):"").append(",");
						str.append(qmgr!=-1?getValue(row.getCell(qmgr)):"").append(",");
						str.append(channel!=-1?getValue(row.getCell(channel)):"").append(",");
						str.append(qcf!=-1?getValue(row.getCell(qcf)):"");

						if(str.toString().trim().length() > 5)
							System.out.println(f.getName()+","+str.toString());

					}

				}// end of while (rowIterator.hasNext()) 

			} catch (FileNotFoundException e) {
				System.out.println(f);
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (IOException e) {
				System.out.println(f);
				// TODO Auto-generated catch block
				e.printStackTrace();
			}

		} // end of for loop

	}

	/*
	 * public void readExcel() { try {
	 * 
	 * ArrayList<String> templateCache = new ArrayList<String>(); ArrayList<String>
	 * onlyAtLastLine = new ArrayList<String>(); ArrayList<String> outPutScript =
	 * new ArrayList<String>();
	 * 
	 * /////////////////// reading template/////////////////////////////////////////
	 * FileInputStream templatefile = new FileInputStream(new
	 * File(".\\templates\\QueueCreate.template")); //FileInputStream templatefile =
	 * new FileInputStream(new File(".\\templates\\auth_script.template"));
	 * 
	 * DataInputStream in = new DataInputStream(templatefile); BufferedReader br =
	 * new BufferedReader(new InputStreamReader(in));
	 * 
	 * String strLine = ""; while ((strLine = br.readLine()) != null) {
	 * if(strLine.indexOf("$atLastLine$") == -1) templateCache.add(strLine); else
	 * onlyAtLastLine.add(strLine); }
	 * 
	 * br.close(); in.close(); templatefile.close();
	 * 
	 * ////////////////////// reading excel ////////////////////////////
	 * 
	 * FileInputStream file = new FileInputStream(new File("C:\\temp\\test1.xls"));
	 * 
	 * HSSFWorkbook workbook = new HSSFWorkbook(file); HSSFSheet sheet =
	 * workbook.getSheetAt(2); Iterator<Row> rowIterator = sheet.iterator();
	 * 
	 * Row headerRow = null;
	 * 
	 * while (rowIterator.hasNext()) {
	 * 
	 * if (headerRow == null) { headerRow = rowIterator.next(); } else {
	 * 
	 * Row dataRow = rowIterator.next();
	 * 
	 * for (String templateLine : templateCache) {
	 * 
	 * //System.out.println("template line : " + templateLine);
	 * 
	 * Iterator<Cell> headerCellIterator = headerRow.cellIterator(); while
	 * (headerCellIterator.hasNext()) { Cell headerCell = headerCellIterator.next();
	 * Cell dataCell = dataRow.getCell(headerCell.getColumnIndex());
	 * 
	 * templateLine = templateLine.replace("$" + getValue(headerCell) + "$",
	 * getValue(dataCell));
	 * 
	 * }
	 * 
	 * outPutScript.add(templateLine); //System.out.println("script line : " +
	 * templateLine);
	 * 
	 * }// end of Enumeration
	 * 
	 * }
	 * 
	 * }
	 * 
	 * for (String lastLine : onlyAtLastLine) { lastLine =
	 * lastLine.replace("$atLastLine$",""); outPutScript.add(lastLine); }
	 * 
	 * 
	 * file.close();
	 * 
	 * 
	 * ///////////////////// printing in output file
	 * ///////////////////////////////////////////
	 * 
	 * 
	 * 
	 * FileOutputStream scriptfile = new FileOutputStream(new
	 * File(".\\Scripts\\Queue_EntCRM_Billing.mqsc")); //FileOutputStream scriptfile
	 * = new FileOutputStream(new File(".\\Scripts\\cpos_auth.txt"));
	 * 
	 * DataOutputStream out = new DataOutputStream(scriptfile); BufferedWriter bw =
	 * new BufferedWriter(new OutputStreamWriter(out));
	 * 
	 * for (String scriptLine : outPutScript) { bw.write(scriptLine+"\n"); }
	 * 
	 * 
	 * bw.close(); out.close(); scriptfile.close();
	 * 
	 * 
	 * } catch (FileNotFoundException e) { e.printStackTrace(); } catch (IOException
	 * e) { e.printStackTrace(); } }
	 */
	public String getValue(Cell c) {
		String strReturn;
		if (c == null)
			return "";
		switch (c.getCellType()) {
		case Cell.CELL_TYPE_BLANK:
			strReturn = "";
			break;
		case Cell.CELL_TYPE_BOOLEAN:
			strReturn = String.valueOf(c.getBooleanCellValue());
			break;
		case Cell.CELL_TYPE_ERROR:
			strReturn = String.valueOf(c.getErrorCellValue());
			break;
		case Cell.CELL_TYPE_NUMERIC:
			// if(c.getNumericCellValue() instanceof Long )
			// System.out.println(c.getRichStringCellValue().getString());
			strReturn = String.valueOf((long) c.getNumericCellValue());
			// else
			// strReturn = String.valueOf(c.getNumericCellValue());
			// System.out.print(Math.));
			break;
		case Cell.CELL_TYPE_STRING:
			strReturn = c.getStringCellValue().trim();
			break;
		default:
			strReturn = "";
			break;
		}

		return strReturn;
	}

}
