/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mycompany.webeconomics;

import com.opencsv.CSVReader;
import java.io.Reader;
import java.nio.file.Files;
import java.nio.file.Paths;

/**
 *
 * @author ziadalhalabi
 */
public class MainReader {
    
    private static final String SAMPLE_CSV_FILE_PATH = "./test.csv";
    
    public static void main(String[] args){
        try{
            Reader reader = Files.newBufferedReader(Paths.get(SAMPLE_CSV_FILE_PATH));
            CSVReader csvReader = new CSVReader(reader);
            
            // test for coursework
            // Reading Records One by One in a String array
            String[] nextRecord;
            int i = 0;
            while ((nextRecord = csvReader.readNext()) != null) {
                Entry entry = new Entry(nextRecord);
                 
                System.out.println("Entry at "+i+": " + entry);
                System.out.println("===========================");
                i++;
            }
        }catch(Exception e){
            
        }
      
    }
    
}
