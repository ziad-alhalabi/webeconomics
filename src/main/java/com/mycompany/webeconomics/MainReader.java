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
import java.util.Random;

/**
 *
 * @author ziadalhalabi
 */
public class MainReader {

    private static final String SAMPLE_CSV_FILE_PATH = "./validation.csv";
    private static final int BUDGET = 6250000;

    public static void main(String[] args) {
        boolean randomBiding = true;

        if (randomBiding) {
            randomBid();
        } else {
            double constantBid = getMeanBidPrice();
            System.out.println("constantBid=" + constantBid);
            constantBid(constantBid);
        }

    }

    private static void constantBid(double constantBid) {
        int numBidImpressions = 0;
        int numClicked = 0;
        double cost = 0;

        try {
            Reader reader = Files.newBufferedReader(Paths.get(SAMPLE_CSV_FILE_PATH));
            CSVReader csvReader = new CSVReader(reader);

            String[] nextRecord;
            int i = 0;
            csvReader.readNext();//skip header
            while ((nextRecord = csvReader.readNext()) != null) {
                ValidationEntry entry = new ValidationEntry(nextRecord);
                if (constantBid > entry.payPrice && (cost + entry.payPrice <= BUDGET)) {
                    cost += entry.payPrice;

                    //since we won the bid, we get the impression and might get a click 
                    numBidImpressions++;
                    numClicked += entry.click;
                    System.out.println("Entry at " + i + ": " + entry);
                    System.out.println("===========================");
                }else if(cost >= BUDGET){
                    break;
                }

                i++;
            }

            System.out.println("Num Bids= " + numBidImpressions);
            System.out.println("Num Clicked= " + numClicked);
            System.out.println("Cost=" + cost);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static double getMeanBidPrice() {
        double meanBidPrice = -1;
        try {
            Reader reader = Files.newBufferedReader(Paths.get(SAMPLE_CSV_FILE_PATH));
            CSVReader csvReader = new CSVReader(reader);

            String[] nextRecord;
            double i = 0;
            double totalBidPrice = 0;
            csvReader.readNext();//skip header
            while ((nextRecord = csvReader.readNext()) != null) {
                ValidationEntry entry = new ValidationEntry(nextRecord);
                if (entry.bidPrice > -1) {//just to be safe
                    totalBidPrice += entry.bidPrice;
                    i++;
                }
            }

            meanBidPrice = totalBidPrice / i;

        } catch (Exception e) {
            e.printStackTrace();
        }

        return meanBidPrice;
    }

    private static void randomBid() {
        int numBidImpressions = 0;
        int numClicked = 0;
        double cost = 0;

        double[] minMaxBid = getMinMaxBidPrice();
        int min = (int) minMaxBid[0];
        int max = (int) minMaxBid[1];
        Random rn = new Random();

        System.out.println("min=" + min + " max=" + max);
        try {
            Reader reader = Files.newBufferedReader(Paths.get(SAMPLE_CSV_FILE_PATH));
            CSVReader csvReader = new CSVReader(reader);

            String[] nextRecord;
            int i = 0;
            csvReader.readNext();//skip header
            while ((nextRecord = csvReader.readNext()) != null) {
                ValidationEntry entry = new ValidationEntry(nextRecord);
                int randomBid = min + rn.nextInt(max - min + 1);
                if (randomBid > entry.payPrice && (cost + entry.payPrice <= BUDGET)) {
                    cost += entry.payPrice;

                    //since we won the bid, we get the impression and might get a click 
                    numBidImpressions++;
                    numClicked += entry.click;
                    System.out.println("Entry at " + i + ": " + entry);
                    System.out.println("===========================");
                }else if(cost >= BUDGET){
                    break;
                }

                i++;
            }

            System.out.println("Num Bids= " + numBidImpressions);
            System.out.println("Num Clicked= " + numClicked);
            System.out.println("Cost=" + cost);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static double[] getMinMaxBidPrice() {
        double[] minMax = new double[2];
        double min = -1;
        double max = 0;
        try {
            Reader reader = Files.newBufferedReader(Paths.get(SAMPLE_CSV_FILE_PATH));
            CSVReader csvReader = new CSVReader(reader);

            String[] nextRecord;
            csvReader.readNext();//skip header
            while ((nextRecord = csvReader.readNext()) != null) {
                ValidationEntry entry = new ValidationEntry(nextRecord);
                if (entry.bidPrice < min || min == -1) {
                    min = entry.bidPrice;
                }

                if (entry.bidPrice > max) {
                    max = entry.bidPrice;
                }
            }

            minMax[0] = min;
            minMax[1] = max;

        } catch (Exception e) {
            e.printStackTrace();
        }

        return minMax;
    }

}
