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
public class Entry {

    public String weekday;
    public String hour;
    public String bidId;
    public String userId;
    public String useragent;
    public String IP;
    public String region;
    public String city;
    public String adexchange;
    public String domain;
    public String url;
    public String urlId;
    public String slotId;
    public String slotWidth;
    public String slotHeight;
    public String slotVisibility;
    public String slotFormat;
    public String slotPrice;
    public String creative;
    public String keypage;
    public String advertiser;
    public String userTag;

    public Entry(String[] nextRecord) {
        weekday = nextRecord[0];
        hour = nextRecord[1];
        bidId = nextRecord[2];
        userId = nextRecord[3];
        useragent = nextRecord[4];
        IP = nextRecord[5];
        region = nextRecord[6];
        city = nextRecord[7];
        adexchange = nextRecord[8];
        domain = nextRecord[9];
        url = nextRecord[10];
        urlId = nextRecord[11];
        slotId = nextRecord[12];
        slotWidth = nextRecord[13];
        slotHeight = nextRecord[14];
        slotVisibility = nextRecord[15];
        slotFormat = nextRecord[16];
        slotPrice = nextRecord[17];
        creative = nextRecord[18];
        keypage = nextRecord[19];
        advertiser = nextRecord[20];
        userTag = nextRecord[21];
    }

    @Override
    public String toString() {
        return "Entry{" + "weekday=" + weekday + ", hour=" + hour + ", bidId=" + bidId + ", userId=" + userId + ", useragent=" + useragent + ", IP=" + IP + ", region=" + region + ", city=" + city + ", adexchange=" + adexchange + ", domain=" + domain + ", url=" + url + ", urlId=" + urlId + ", slotId=" + slotId + ", slotWidth=" + slotWidth + ", slotHeight=" + slotHeight + ", slotVisibility=" + slotVisibility + ", slotFormat=" + slotFormat + ", slotPrice=" + slotPrice + ", creative=" + creative + ", keypage=" + keypage + ", advertiser=" + advertiser + ", userTag=" + userTag + '}';
    }

}
