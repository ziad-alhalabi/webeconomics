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
    
    private static final String SAMPLE_CSV_FILE_PATH = "./tweets.csv";
    
    public static void main(String[] args){
        try{
            Reader reader = Files.newBufferedReader(Paths.get(SAMPLE_CSV_FILE_PATH));
            CSVReader csvReader = new CSVReader(reader);
            
            // Reading Records One by One in a String array
            String[] nextRecord;
            while ((nextRecord = csvReader.readNext()) != null) {
                System.out.println("userid : " + nextRecord[0]);
                System.out.println("username : " + nextRecord[1]);
                System.out.println("tweet : " + nextRecord[2]);
                System.out.println("createdat : " + nextRecord[3]);
                System.out.println("==========================");
            }
        }catch(Exception e){
            
        }
      
    }
    
}
