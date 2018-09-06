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
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Iterator;

import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.xssf.usermodel.XSSFSheet;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;





public class MqObjectValidation {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		String fdir = "C:\\Users\\KrishnakantSadhu\\Desktop\\Dipen\\UAT_MQCONFIG_V7.4.9\\UAT_MQCONFIG_V7.4.9";
		ArrayList<File> files = new ArrayList<File>();
		MqObjectValidation mqObjectValidation = new MqObjectValidation();
		mqObjectValidation.listf(fdir,files);
		
		mqObjectValidation.readAllExcel(files);
		
		// TODO Auto-generated method stub

	}
	
	
	public void listf(String directoryName, ArrayList<File> files) {
	    File directory = new File(directoryName);

	    // get all the files from a directory
	    File[] fList = directory.listFiles();
	    for (File file : fList) {
	        if (file.isFile()) {
	            files.add(file);
	            System.out.println(file);
	        } else if (file.isDirectory()) {
	            listf(file.getAbsolutePath(), files);
	        }
	    }
	}
	
	public void readAllExcel(ArrayList<File> files){
		for (File f : files){
			try {
				FileInputStream excelFile = new FileInputStream(f);
				
				// Workbook wb = WorkbookFactory.create(f);
				
				


				XSSFWorkbook wb = new XSSFWorkbook(excelFile); 
				XSSFSheet sheet = wb.getSheetAt(0);
				
				//Iterator<Row> rowIterator = sheet.iterator();

				Row headerRow = sheet.getRow(0);
				
				System.out.print(f.getName()+",");
				
				Iterator<Cell> cellIterator = headerRow.cellIterator();
				while (cellIterator.hasNext()){
					System.out.print(getValue(cellIterator.next())+",");
				}
				
				System.out.print(System.lineSeparator());
				

				
				
			} catch (FileNotFoundException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			
		}
		
	}
	
	/*
	public void readExcel() {
		try {

			ArrayList<String> templateCache = new ArrayList<String>();
			ArrayList<String> onlyAtLastLine = new ArrayList<String>();
			ArrayList<String> outPutScript = new ArrayList<String>();
			
			/////////////////// reading template/////////////////////////////////////////
			FileInputStream templatefile = new FileInputStream(new File(".\\templates\\QueueCreate.template"));
			//FileInputStream templatefile = new FileInputStream(new File(".\\templates\\auth_script.template"));

			DataInputStream in = new DataInputStream(templatefile);
			BufferedReader br = new BufferedReader(new InputStreamReader(in));

			String strLine = "";
			while ((strLine = br.readLine()) != null) {
				if(strLine.indexOf("$atLastLine$") == -1)
					templateCache.add(strLine);
				else
					onlyAtLastLine.add(strLine);
			}
			
			br.close();
			in.close();
			templatefile.close();

			////////////////////// reading excel ////////////////////////////	
			
			FileInputStream file = new FileInputStream(new File("C:\\temp\\test1.xls"));
		
			HSSFWorkbook workbook = new HSSFWorkbook(file); 
			HSSFSheet sheet = workbook.getSheetAt(2); 
			Iterator<Row> rowIterator = sheet.iterator();

			Row headerRow = null;

			while (rowIterator.hasNext()) {

				if (headerRow == null) {
					headerRow = rowIterator.next();
				} else {

					Row dataRow = rowIterator.next(); 

					for (String templateLine : templateCache) {

						//System.out.println("template line : " + templateLine);

						Iterator<Cell> headerCellIterator = headerRow.cellIterator();
						while (headerCellIterator.hasNext()) {
							Cell headerCell = headerCellIterator.next();
							Cell dataCell = dataRow.getCell(headerCell.getColumnIndex());
							
							templateLine = templateLine.replace("$"
									+ getValue(headerCell) + "$",
									getValue(dataCell));

						}
						
						outPutScript.add(templateLine);
						//System.out.println("script line : " + templateLine);

					}// end of Enumeration

				}

			}
			
			for (String lastLine : onlyAtLastLine) {
				lastLine = lastLine.replace("$atLastLine$",""); 
				outPutScript.add(lastLine);
			}
			
			
			file.close();
			
			
			///////////////////// printing in output file ///////////////////////////////////////////
			
			
			
			FileOutputStream scriptfile = new FileOutputStream(new File(".\\Scripts\\Queue_EntCRM_Billing.mqsc"));
			//FileOutputStream scriptfile = new FileOutputStream(new File(".\\Scripts\\cpos_auth.txt"));

			DataOutputStream out = new DataOutputStream(scriptfile);
			BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(out));

			for (String scriptLine : outPutScript) {
				bw.write(scriptLine+"\n");
			}
			
			
			bw.close();
			out.close();
			scriptfile.close();
			
			
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
*/
	public String getValue(Cell c) {
		String strReturn;
		if(c == null) return "";
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
