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
    public String keypage;
    public int advertiser;
    public String userTag;

    public Entry(String[] nextRecord) {
        weekday = Integer.valueOf(nextRecord[0]);
        hour = Integer.valueOf(nextRecord[1]);
        bidId = nextRecord[2];
        userId = nextRecord[3];
        useragent = nextRecord[4];
        IP = nextRecord[5];
        regionCode = Integer.valueOf(nextRecord[6]);
        cityCode = Integer.valueOf(nextRecord[7]);
        adexchange = Integer.valueOf(nextRecord[8]);
        domain = nextRecord[9];
        url = nextRecord[10];
        urlId = nextRecord[11];
        slotId = nextRecord[12];
        slotWidth = Integer.valueOf(nextRecord[13]);
        slotHeight = Integer.valueOf(nextRecord[14]);
        slotVisibility = nextRecord[15];
        slotFormat = nextRecord[16];
        slotPrice = Integer.valueOf(nextRecord[17]);
        creative = nextRecord[18];
        keypage = nextRecord[19];
        advertiser = Integer.valueOf(nextRecord[20]);
        userTag = nextRecord[21];
    }

    @Override
    public String toString() {
        return "Entry{" + "weekday=" + weekday + ", hour=" + hour + ", bidId=" + bidId + ", userId=" + userId + ", useragent=" + useragent + ", IP=" + IP + ", region=" + regionCode + ", city=" + cityCode + ", adexchange=" + adexchange + ", domain=" + domain + ", url=" + url + ", urlId=" + urlId + ", slotId=" + slotId + ", slotWidth=" + slotWidth + ", slotHeight=" + slotHeight + ", slotVisibility=" + slotVisibility + ", slotFormat=" + slotFormat + ", slotPrice=" + slotPrice + ", creative=" + creative + ", keypage=" + keypage + ", advertiser=" + advertiser + ", userTag=" + userTag + '}';
    }
}
