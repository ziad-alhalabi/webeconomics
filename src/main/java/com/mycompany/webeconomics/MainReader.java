/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mycompany.webeconomics;

import com.mycompany.webeconomics.models.Impression;
import com.opencsv.CSVReader;
import java.io.File;
import java.io.IOException;
import java.io.Reader;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author ziadalhalabi
 */
public class MainReader {
    
    private static List<Impression> impressions = new ArrayList<>();
    
    public static void main(String[] args) throws IOException{
        process("we_data/train.csv");
        doStats();
    }
    
    
    private static void process(String filePath) throws IOException{
        Reader reader = Files.newBufferedReader(Paths.get(filePath));
        CSVReader csvReader = new CSVReader(reader);

        // test for coursework
        // Reading Records One by One in a String array
        String[] entry;
        int i = 0;
        while ((entry = csvReader.readNext()) != null) {
            if(i == 0){ i = 1; continue; }
            impressions.add(new Impression(entry));
            i++;
        }        
    }

    // analyse impressions here
    private static void doStats() {
        BasicStats bs = new BasicStats();
        int impressionsCount = impressions.size();
        HashSet<Integer> advertisers = new HashSet<>(); // want to have collection of unique advertisers
        for(Impression impression : impressions){
            advertisers.add(impression.getAdvertiser());
            //... etc
        }
    }
    
}
