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
import org.apache.poi.ss.usermodel.CellType;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;


public class QueueConnectionFactoryScript {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		System.out.println(">>>>>>>>> Program Start >>>>>>>>>>");

		QueueConnectionFactoryScript s = new QueueConnectionFactoryScript();
		s.readExcel();
		System.out.println(">>>>>>>>> Program End >>>>>>>>>>");
	}

	public void readExcel() {
		try {

			ArrayList<String> templateCache = new ArrayList<String>();
			ArrayList<String> onlyAtLastLine = new ArrayList<String>();
			ArrayList<String> outPutScript = new ArrayList<String>();
			
			/////////////////// reading template/////////////////////////////////////////
			System.out.println("Reading template >>> MQCF.template");
			FileInputStream templatefile = new FileInputStream(new File(".\\templates\\MQCF.template"));

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
			System.out.println("Reading data >>> ActivationSpec.xlsx");
			FileInputStream file = new FileInputStream(new File(".\\Data\\ActivationSpec.xlsx"));
		
			XSSFWorkbook workbook = new XSSFWorkbook(file); 
			Sheet sheet = workbook.getSheet("QCF"); 
			Iterator<Row> rowIterator = sheet.iterator();

			Row headerRow = null;
			
			int index = 0;

			while (rowIterator.hasNext()) {

				if (headerRow == null) {
					headerRow = rowIterator.next();
				} else {
						
					Row dataRow = rowIterator.next(); 
					index++;
					for (String templateLine : templateCache) {

						//System.out.println("template line : " + templateLine);

						Iterator<Cell> headerCellIterator = headerRow.cellIterator();
						while (headerCellIterator.hasNext()) {
							Cell headerCell = headerCellIterator.next();
							Cell dataCell = dataRow.getCell(headerCell.getColumnIndex());
							
							templateLine = templateLine.replace("$"
									+ headerCell.getStringCellValue().trim() + "$",
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
			
			workbook.close();
			file.close();
			
			
			///////////////////// printing in output file ///////////////////////////////////////////
			
			System.out.println("Generating script >>> QCF.jacl...");
			
			FileOutputStream scriptfile = new FileOutputStream(new File(".\\Scripts\\QCF.jacl"));

			DataOutputStream out = new DataOutputStream(scriptfile);
			BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(out));
			
			if(outPutScript.size() > 0) {
				bw.write("###################################### Run script ##################################################\n");
				bw.write("## wsadmin.sh -lang jacl -user <<user_name>> -password <<password>> -f <<path of script file>>  ##\n");
				bw.write("####################################################################################################\n\n");
			}

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
	
	public static String getValue(Cell dataCell) {
		String valueStr="";
		
		if(Cell.CELL_TYPE_NUMERIC == dataCell.getCellType()) {
			Double d = new Double(dataCell.getNumericCellValue());
			valueStr = Integer.toString(d.intValue());
		}else {
			valueStr = dataCell.getStringCellValue().replaceAll(" ", "");
		}
		
		return valueStr;
	}

	

}
