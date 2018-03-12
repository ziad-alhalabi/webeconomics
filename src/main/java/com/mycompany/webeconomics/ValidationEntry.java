/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mycompany.webeconomics;

/**
 *
 * @author ziadalhalabi
 */
public class ValidationEntry {

    public int click;
    public int weekday;
    public int hour;
    public String bidId;
    public String userId;
    public String useragent;
    public String IP;
    public int regionCode;
    public int cityCode;
    public int adexchange;
    public String domain;
    public String url;
    public String urlId;
    public String slotId;
    public int slotWidth;
    public int slotHeight;
    public String slotVisibility;
    public String slotFormat;
    public int slotPrice;
    public String creative;

    //The bid price from iPinYou for this bid request.
    public double bidPrice;

    //The paying price is the highest bid from competitors
    public double payPrice;

    public String keypage;
    public int advertiser;
    public String userTag;
    public int[] userTagIntArray;

    public ValidationEntry(String[] nextRecord) {
        try {
            click = Integer.valueOf(nextRecord[0]);
        } catch (Exception e) {
            click = 0;

        }

        try {
            weekday = Integer.valueOf(nextRecord[1]);
        } catch (Exception e) {

        }

        try {
            hour = Integer.valueOf(nextRecord[2]);
        } catch (Exception e) {

        }
        bidId = nextRecord[3];
        userId = nextRecord[4];
        useragent = nextRecord[5];
        IP = nextRecord[6];
        try {
            regionCode = Integer.valueOf(nextRecord[7]);
        } catch (Exception e) {

        }

        try {
            cityCode = Integer.valueOf(nextRecord[8]);
        } catch (Exception e) {

        }

        try {
            adexchange = Integer.valueOf(nextRecord[9]);
        } catch (Exception e) {

        }
        domain = nextRecord[10];
        url = nextRecord[11];
        urlId = nextRecord[12];
        slotId = nextRecord[13];
        try {
            slotWidth = Integer.valueOf(nextRecord[14]);
        } catch (Exception e) {

        }

        try {
            slotHeight = Integer.valueOf(nextRecord[15]);
        } catch (Exception e) {

        }
        slotVisibility = nextRecord[16];
        slotFormat = nextRecord[17];

        try {
            slotPrice = Integer.valueOf(nextRecord[18]);
        } catch (Exception e) {

        }
        creative = nextRecord[19];

        try {
            bidPrice = Integer.parseInt(nextRecord[20]);
        } catch (Exception e) {

        }
        try {
            payPrice = Integer.parseInt(nextRecord[21]);
        } catch (Exception e) {

        }

        keypage = nextRecord[22];
        try {
            advertiser = Integer.valueOf(nextRecord[23]);
        } catch (Exception e) {

        }
        userTag = nextRecord[24];
        try {
            userTagIntArray = userTagIntArray(userTag);
        } catch (Exception e) {

        }
    }

    public final int[] userTagIntArray(String userTag) {

        String[] userTagStrArray = userTag.split(",");

        int[] intArray = new int[userTagStrArray.length];
        int i = 0;
        for (String item : userTagStrArray) {
            intArray[i] = Integer.parseInt(item);
            i++;
        }

        return intArray;
    }

    @Override
    public String toString() {
        return "ValidationEntry{" + "click=" + click + ", weekday=" + weekday + ", hour=" + hour + ", bidId=" + bidId + ", userId=" + userId + ", useragent=" + useragent + ", IP=" + IP + ", regionCode=" + regionCode + ", cityCode=" + cityCode + ", adexchange=" + adexchange + ", domain=" + domain + ", url=" + url + ", urlId=" + urlId + ", slotId=" + slotId + ", slotWidth=" + slotWidth + ", slotHeight=" + slotHeight + ", slotVisibility=" + slotVisibility + ", slotFormat=" + slotFormat + ", slotPrice=" + slotPrice + ", creative=" + creative + ", bidPrice=" + bidPrice + ", payPrice=" + payPrice + ", keypage=" + keypage + ", advertiser=" + advertiser + ", userTag=" + userTag + ", userTagIntArray=" + userTagIntArray + '}';
    }

}
