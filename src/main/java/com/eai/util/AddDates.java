package com.eai.util;

import java.util.Calendar;
import java.util.Date;

public class AddDates {
	public static void main(String[] s){
		
		Calendar c1 = Calendar.getInstance();
		c1.set(2013, 0, 01, 10, 0);
		
		
		Calendar c2 = Calendar.getInstance();
		c2.set(2013, 05, 20, 70, 0);
		
		for (int i=0 ; i < 100; i++){
			c1.add(Calendar.DAY_OF_MONTH, 1);
			System.out.println(c1.get(Calendar.DAY_OF_MONTH) + " : "+c1.getTime());
		}
		
	}
}
