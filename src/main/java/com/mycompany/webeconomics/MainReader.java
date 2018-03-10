/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mycompany.webeconomics;

import com.mycompany.webeconomics.models.Advertiser;
import com.mycompany.webeconomics.models.Impression;
import com.opencsv.CSVReader;
import java.io.IOException;
import java.io.Reader;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.text.DecimalFormat;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;

/**
 *
 * @author ziadalhalabi
 */
public class MainReader {
    
    private static List<Impression> impressions = new ArrayList<>();
    private static List<Advertiser> advertisers = new ArrayList<>();
    
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
        HashSet<Integer> uniqueAdvertiserIds = new HashSet<>();
        while ((entry = csvReader.readNext()) != null) {
            if(i == 0){ i = 1; continue; }
            Impression imp = new Impression(entry);
            impressions.add(imp);
            uniqueAdvertiserIds.add(imp.getAdvertiser());
            i++;
        }
        for(Integer uniqueAdvertiserId : uniqueAdvertiserIds){
            advertisers.add(new Advertiser(uniqueAdvertiserId));
        }
        
        for(Impression impression : impressions){
            int advertiserId = impression.getAdvertiser();
            for(Advertiser advertiser : advertisers){
                if(advertiser.getId() == advertiserId) { advertiser.addImpression(impression); break; }
            }
        }
    }

    // analyse impressions here
    private static void doStats() {
        // insufficient data for 'bids, conversions, win ratio and conversion ratio', these are ommitted for the coursework dataset
        String[] header = {"Advertiser | ", "Impressions | ", "Clicks | ", "Total Cost (CNY) | ", "CTR (%) | ", "CPM | ", "eCPC"};
        System.out.format(createHeaderFormatString(header.length), header[0], header[1], header[2], header[3], header[4], header[5], header[6]);
        System.out.println();
        for(Advertiser advertiser : advertisers){
            // for each advertiser, do stats on their impressions
        }
    }  
    
    /**
     * Format given double to number of decimal places specified by 'decimals'.
     * @param d double to format
     * @param decimals the number of decimal places to format d to
     * @return the formatted string
     */
    private static String formatTo(double d, int decimals){
        String decimalPlaces = "#.";
        for(int i = 0; i < decimals; i++) decimalPlaces += "#";
        return new DecimalFormat(decimalPlaces).format(d);
    }
    
    private static String createHeaderFormatString(int headerLength){
        String s = "";
        for(int i = 0; i < headerLength; i++) s += "%5s";
        return s;
    }
    
    private static String createRowFormatString(String[] header){
        String s = "";
        for(int i = 0; i < header.length; i++){
            s += "%" + header[i].length() + "s";
        }
        return s;
    }
    
}
