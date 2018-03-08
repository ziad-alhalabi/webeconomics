/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mycompany.webeconomics;

/**
 *
 * @author dani_
 */
public class BasicStats {
    private int impressionCount;
    private int clickCount;
    private int cost;
    private double ctr; //click-through rate
    private double avgCPM;
    private int eCPC;
    private int advertiserCount;

    public int getImpressionCount() {
        return impressionCount;
    }

    public void setImpressionCount(int impressionCount) {
        this.impressionCount = impressionCount;
    }

    public void bumpImpressionCount(){
        this.impressionCount++;
    }
    
    public int getClickCount() {
        return clickCount;
    }

    public void setClickCount(int clickCount) {
        this.clickCount = clickCount;
    }
    
    public void bumpClickCount(){
        this.clickCount++;
    }    

    public int getCost() {
        return cost;
    }

    public void setCost(int cost) {
        this.cost = cost;
    }
    
    public void addCost(int cost){
        this.cost += cost;
    }

    public double getCtr() {
        return ctr;
    }

    public void setCtr(double ctr) {
        this.ctr = ctr;
    }

    public double getAvgCPM() {
        return avgCPM;
    }

    public void setAvgCPM(double avgCPM) {
        this.avgCPM = avgCPM;
    }

    public int geteCPC() {
        return eCPC;
    }

    public void seteCPC(int eCPC) {
        this.eCPC = eCPC;
    }
    
    public int getAdvertiserCount(){
        return this.advertiserCount;
    }
    
    public void setAdvertiserCount(int count){
        this.advertiserCount = count;
    }
    
    public void bumpAdvertisercount(){
        this.advertiserCount++;
    }
    
    
}
