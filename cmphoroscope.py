from lxml import html
import requests
import urllib.request
#import urllib
#from urllib2 import urlopen
from bs4 import BeautifulSoup
import re

####################################################################
# API
####################################################################

class CMPHoroscope:


    @staticmethod
    def get_todays_horoscope_hindi(sunsign_en, sunsign_hn, language):
        global horoscope
        #url_hindi = "https://hindi.astroyogi.com/rashiphal/"+sunsign_hn+"-dainik-rashiphal"
        # https://hindi.mpanchang.com/rashifal/aaj-ka-rashifal/vrishabha-rashi/
        url_hindi = "https://hindi.astroyogi.com/rashifal/aaj-ka/" + sunsign_hn + "fal"
        #https://hindi.astroyogi.com/rashifal/aaj-ka/vrishabha-rashifal

        url_english = "http://www.ganeshaspeaks.com/horoscopes/daily-horoscope/" + sunsign_en
        ######## for Date ################
        #print("-1-->" + url_hindi)
        response = requests.get(url_english)
        #print("-2-->" + str(response.content,'utf-8'))
        tree = html.fromstring(response.content)
        date = str(tree.xpath(
            "//*[@id=\"daily\"]/div/div[1]/div[1]/div[2]/div/p/text()"))
        #print("-3-->" + date)
        date = date.replace("']", "").replace("['", "")
        #print("-4-->" + date)

        ######### fro Horoscope ################
        hdr = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive'}
        req = urllib.request.Request(url_hindi, headers=hdr)
        #try:
        web_page = urllib.request.urlopen(req)
        #except urllib2.HTTPError, e:
        #    print "--------------" +e.fp.read()
		#web_page = urlopen(url_hindi)
        soup = BeautifulSoup(web_page, 'html.parser')
        #print("---TODAY---")
        for extract_div in soup.findAll("div", {"id": "today1"}):
            horoscope = extract_div.text
        #print(horoscope)
        horoscope = horoscope.replace("\n", "").replace("  ", "").replace("[\"", "").replace("\"]", "")
        dict = {
            'date': date,
            'horoscope': horoscope,
            'sunsign english': sunsign_en,
            'sunsign hindi': sunsign_hn
        }

        return dict


    @staticmethod
    def get_tomorrow_horoscope_hindi(sunsign_en, sunsign_hn, language):
        #url_hindi = "https://hindi.astroyogi.com/rashiphal/"+sunsign_hn+"-dainik-rashiphal"
        # https://hindi.mpanchang.com/rashifal/aaj-ka-rashifal/vrishabha-rashi/
        url_hindi = "https://hindi.astroyogi.com/rashifal/aaj-ka/" + sunsign_hn + "fal#tomorrow"
        #https://hindi.astroyogi.com/rashifal/aaj-ka/vrishabha-rashifal#tomorrow
        url_english = "http://www.ganeshaspeaks.com/horoscopes/tomorrow-horoscope/" + sunsign_en
        ######## for Date ################
        response = requests.get(url_english)
        # print("-2-->" + response.content)
        tree = html.fromstring(response.content)
        date = str(tree.xpath(
            "//*[@id=\"daily\"]/div/div[1]/div[1]/div[2]/div/p/text()"))
        # print("-3-->" + date)
        date = date.replace("']", "").replace("['", "")
        #print("-4-->" + date)

        ######### fro Horoscope ################
        hdr = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive'}
        req = urllib.request.Request(url_hindi, headers=hdr)
        #try:
        web_page = urllib.request.urlopen(req)
        #except urllib2.HTTPError, e:
        #    print "--------------" +e.fp.read()
		#web_page = urlopen(url_hindi)
        soup = BeautifulSoup(web_page, 'html.parser')
        #print "---TOMORROW---"
        for extract_div in soup.findAll("div", {"id": "tomorrow"}):
            horoscope = extract_div.text
        #print horoscope
        horoscope = horoscope.replace("\n", "").replace("  ", "").replace("[\"", "").replace("\"]", "")
        dict = {
            'date': date,
            'horoscope': horoscope,
            'sunsign english': sunsign_en,
            'sunsign hindi': sunsign_hn
        }

        return dict


    @staticmethod
    def get_yesterday_horoscope_hindi(sunsign_en, sunsign_hn, language):
        #url_hindi = "https://hindi.astroyogi.com/rashiphal/"+sunsign_hn+"-dainik-rashiphal"
        # https://hindi.mpanchang.com/rashifal/aaj-ka-rashifal/vrishabha-rashi/
        url_hindi = "https://hindi.astroyogi.com/rashifal/aaj-ka/" + sunsign_hn + "fal"
        # https://hindi.astroyogi.com/rashifal/aaj-ka/vrishabha-rashifal
        url_english = "http://www.ganeshaspeaks.com/horoscopes/yesterday-horoscope/" + sunsign_en
        ######## for Date ################
        response = requests.get(url_english)
        # print("-2-->" + response.content)
        tree = html.fromstring(response.content)
        date = str(tree.xpath(
            "//*[@id=\"daily\"]/div/div[1]/div[1]/div[2]/div/p/text()"))
        # print("-3-->" + date)
        date = date.replace("']", "").replace("['", "")
        #print("-4-->" + date)

        ######### fro Horoscope ################
        hdr = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive'}
        req = urllib.request.Request(url_hindi, headers=hdr)
        #try:
        web_page = urllib.request.urlopen(req)
        #except urllib2.HTTPError, e:
        #    print "--------------" +e.fp.read()
		#web_page = urlopen(url_hindi)
        soup = BeautifulSoup(web_page, 'html.parser')
        #print "---TODAY---"
        for extract_div in soup.findAll("div", {"id": "yesterday"}):
            horoscope = extract_div.text
        #print horoscope
        horoscope = horoscope.replace("\n", "").replace("  ", "").replace("[\"", "").replace("\"]", "")
        dict = {
            'date': date,
            'horoscope': horoscope,
            'sunsign english': sunsign_en,
            'sunsign hindi': sunsign_hn
        }

        return dict

    @staticmethod
    def get_weekly_horoscope_hindi(sunsign_en, sunsign_hn, language):
        #url_hindi = "https://hindi.astroyogi.com/rashiphal/"+sunsign_hn+"-saptahik-rashiphal"
        # https://hindi.mpanchang.com/rashifal/aaj-ka-rashifal/vrishabha-rashi/
        url_hindi = "https://hindi.astroyogi.com/rashifal/saptahik/" + sunsign_hn + "fal"
        # https://hindi.astroyogi.com/rashifal/saptahik/vrishabha-rashifal
        url_english = "http://www.ganeshaspeaks.com/horoscopes/weekly-horoscope/" + sunsign_en
        ######## for Date ################
        response = requests.get(url_english)
        # print("-2-->" + response.content)
        tree = html.fromstring(response.content)
        date = str(tree.xpath(
            "//*[@id=\"daily\"]/div/div[1]/div[1]/div[2]/div/p/text()"))
        # print("-3-->" + date)
        date = date.replace("']", "").replace("['", "")
        # print("-4-->" + date)

        ######### fro Horoscope ################
        hdr = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive'}
        req = urllib.request.Request(url_hindi, headers=hdr)
        #try:
        web_page = urllib.request.urlopen(req)
        #except urllib2.HTTPError, e:
        #    print "--------------" +e.fp.read()
		#web_page = urlopen(url_hindi)
        soup = BeautifulSoup(web_page, 'html.parser')
        #print "---TODAY---"
        for extract_div in soup.findAll("div", {"id": "today1"}):
            horoscope = extract_div.text
        # print horoscope
        horoscope = horoscope.replace("\n", "").replace("  ", "").replace("[\"", "").replace("\"]", "")
        dict = {
            'week': date,
            'horoscope': horoscope,
            'sunsign english': sunsign_en,
            'sunsign hindi': sunsign_hn
        }

        return dict

    @staticmethod
    def get_monthly_horoscope_hindi(sunsign_en, sunsign_hn, language):
        # url_hindi = "https://hindi.astroyogi.com/rashiphal/"+sunsign_hn+"-masik-rashifal"
        # https://hindi.mpanchang.com/rashifal/aaj-ka-rashifal/vrishabha-rashi/
        url_hindi = "https://hindi.astroyogi.com/rashifal/masik/" + sunsign_hn + "fal"
        # https://hindi.astroyogi.com/rashifal/masik/vrishabha-rashifal
        url_english = "http://www.ganeshaspeaks.com/horoscopes/monthly-horoscope/" + sunsign_en
        ######## for Date ################
        response = requests.get(url_english)
        # print("-2-->" + response.content)
        tree = html.fromstring(response.content)
        date = str(tree.xpath(
            "//*[@id=\"daily\"]/div/div[1]/div[1]/div[2]/div/p/text()"))
        # print("-3-->" + date)
        date = date.replace("']", "").replace("['", "")
        # print("-4-->" + date)

        ######### fro Horoscope ################
        hdr = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive'}
        req = urllib.request.Request(url_hindi, headers=hdr)
        #try:
        web_page = urllib.request.urlopen(req)
        #except urllib2.HTTPError, e:
        #    print "--------------" +e.fp.read()
		#web_page = urlopen(url_hindi)
        soup = BeautifulSoup(web_page, 'html.parser')
        #print "---TODAY---"
        for extract_div in soup.findAll("div", {"id": "today1"}):
            horoscope = extract_div.text
        # print horoscope
        horoscope = horoscope.replace("\n", "").replace("  ", "").replace("[\"", "").replace("\"]", "")
        dict = {
            'month': date,
            'horoscope': horoscope,
            'sunsign english': sunsign_en,
            'sunsign hindi': sunsign_hn
        }

        return dict

    @staticmethod
    def get_yearly_horoscope_hindi(sunsign_en, sunsign_hn, language):
        # url_hindi = "https://hindi.astroyogi.com/rashiphal/"+sunsign_hn+"-masik-rashifal"
        # https://hindi.mpanchang.com/rashifal/aaj-ka-rashifal/vrishabha-rashi/

        # https://hindi.astroyogi.com/rashifal2020/vrishabha-rashifal-2020
        url_english = "http://www.ganeshaspeaks.com/horoscopes/yearly-horoscope/" + sunsign_en
        ######## for Date ################
        response = requests.get(url_english)
        # print("-2-->" + response.content)
        tree = html.fromstring(response.content)
        date = str(tree.xpath(
            "//*[@id=\"daily\"]/div/div[1]/div[1]/div[2]/div/p/text()"))
        #print("-3-->" + date)
        date = date.replace("']", "").replace("['", "")
        #print("-4-->" + date)
        url_hindi = "https://hindi.astroyogi.com/rashifal"+date+"/"+sunsign_hn+"-rashifal-"+date
        # https://hindi.astroyogi.com/rashifal2020/vrishabha-rashifal-2020
        #print url_hindi
        ######### fro Horoscope ################
        hdr = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive'}
        req = urllib.request.Request(url_hindi, headers=hdr)
        #try:
        web_page = urllib.request.urlopen(req)
        #except urllib2.HTTPError, e:
        #    print "--------------" +e.fp.read()
		#web_page = urlopen(url_hindi)
        soup = BeautifulSoup(web_page, 'html.parser')
        #print "---TODAY---"
        horoscope=""
        for extract_div in soup.findAll("p", {"class": "text-justify"}):
            horoscope+=extract_div.text
        #print horoscope
        horoscope = horoscope.replace("\n", "").replace("  ", "").replace("[\"", "").replace("\"]", "")
        dict = {
            'year': date,
            'horoscope': horoscope,
            'sunsign english': sunsign_en,
            'sunsign hindi': sunsign_hn
        }

        return dict

