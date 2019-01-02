from lxml import html
import requests
from urllib2 import urlopen
from bs4 import BeautifulSoup
import re

####################################################################
# API
####################################################################

class CMPHoroscope:


    @staticmethod
    def get_todays_horoscope_hindi(sunsign_en, sunsign_hn, language):
        url_hindi = "https://hindi.astroyogi.com/rashiphal/"+sunsign_hn+"-dainik-rashiphal"
        #url_hindi = "https://hindi.mpanchang.com/rashifal/aaj-ka-rashifal/vrishabha-rashi/"
        url_english = "http://www.ganeshaspeaks.com/horoscopes/daily-horoscope/" + sunsign_en
        ######## for Date ################
        response = requests.get(url_english)
        #print("-2-->" + response.content)
        tree = html.fromstring(response.content)
        date = str(tree.xpath(
            "//*[@id=\"daily\"]/div/div[1]/div[1]/div[2]/div/p/text()"))
        #print("-3-->" + date)
        date = date.replace("']", "").replace("['", "")
        #print("-4-->" + date)

        ######### fro Horoscope ################
        web_page = urlopen(url_hindi)
        soup = BeautifulSoup(web_page, 'html.parser')
        print "---TODAY---"
        for extract_div in soup.findAll("div", {"id": "today1"}):
            horoscope = extract_div.text
        print horoscope
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
        url_hindi = "https://hindi.astroyogi.com/rashiphal/"+sunsign_hn+"-dainik-rashiphal"
        # url_hindi = "https://hindi.mpanchang.com/rashifal/aaj-ka-rashifal/vrishabha-rashi/"
        url_english = "http://www.ganeshaspeaks.com/horoscopes/tomorrow-horoscope/" + sunsign_en
        ######## for Date ################
        response = requests.get(url_english)
        # print("-2-->" + response.content)
        tree = html.fromstring(response.content)
        date = str(tree.xpath(
            "//*[@id=\"daily\"]/div/div[1]/div[1]/div[2]/div/p/text()"))
        # print("-3-->" + date)
        date = date.replace("']", "").replace("['", "")
        print("-4-->" + date)

        ######### fro Horoscope ################
        web_page = urlopen(url_hindi)
        soup = BeautifulSoup(web_page, 'html.parser')
        print "---TOMORROW---"
        for extract_div in soup.findAll("div", {"id": "tomorrow"}):
            horoscope = extract_div.text
        print horoscope
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
        url_hindi = "https://hindi.astroyogi.com/rashiphal/"+sunsign_hn+"-dainik-rashiphal"
        # url_hindi = "https://hindi.mpanchang.com/rashifal/aaj-ka-rashifal/vrishabha-rashi/"
        url_english = "http://www.ganeshaspeaks.com/horoscopes/yesterday-horoscope/" + sunsign_en
        ######## for Date ################
        response = requests.get(url_english)
        # print("-2-->" + response.content)
        tree = html.fromstring(response.content)
        date = str(tree.xpath(
            "//*[@id=\"daily\"]/div/div[1]/div[1]/div[2]/div/p/text()"))
        # print("-3-->" + date)
        date = date.replace("']", "").replace("['", "")
        print("-4-->" + date)

        ######### fro Horoscope ################
        web_page = urlopen(url_hindi)
        soup = BeautifulSoup(web_page, 'html.parser')
        print "---TODAY---"
        for extract_div in soup.findAll("div", {"id": "yesterday"}):
            horoscope = extract_div.text
        print horoscope
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
        url_hindi = "https://hindi.astroyogi.com/rashiphal/"+sunsign_hn+"-saptahik-rashiphal"
        # url_hindi = "https://hindi.mpanchang.com/rashifal/aaj-ka-rashifal/vrishabha-rashi/"
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
        web_page = urlopen(url_hindi)
        soup = BeautifulSoup(web_page, 'html.parser')
        print "---TODAY---"
        for extract_div in soup.findAll("div", {"id": "today1"}):
            horoscope = extract_div.text
        # print horoscope
        horoscope = horoscope.replace("\n", "").replace("  ", "").replace("[\"", "").replace("\"]", "")
        dict = {
            'date': date,
            'horoscope': horoscope,
            'sunsign english': sunsign_en,
            'sunsign hindi': sunsign_hn
        }

        return dict

    @staticmethod
    def get_monthly_horoscope_hindi(sunsign_en, sunsign_hn, language):
        url_hindi = "https://hindi.astroyogi.com/rashiphal/"+sunsign_hn+"-masik-rashifal"
        # url_hindi = "https://hindi.mpanchang.com/rashifal/aaj-ka-rashifal/vrishabha-rashi/"
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
        web_page = urlopen(url_hindi)
        soup = BeautifulSoup(web_page, 'html.parser')
        print "---TODAY---"
        for extract_div in soup.findAll("div", {"id": "today1"}):
            horoscope = extract_div.text
        # print horoscope
        horoscope = horoscope.replace("\n", "").replace("  ", "").replace("[\"", "").replace("\"]", "")
        dict = {
            'date': date,
            'horoscope': horoscope,
            'sunsign english': sunsign_en,
            'sunsign hindi': sunsign_hn
        }

        return dict

    @staticmethod
    def get_yearly_horoscope_hindi(sunsign_en, sunsign_hn, language):
        # url_hindi = "https://hindi.mpanchang.com/rashifal/aaj-ka-rashifal/vrishabha-rashi/"
        url_english = "http://www.ganeshaspeaks.com/horoscopes/yearly-horoscope/" + sunsign_en
        ######## for Date ################
        response = requests.get(url_english)
        # print("-2-->" + response.content)
        tree = html.fromstring(response.content)
        date = str(tree.xpath(
            "//*[@id=\"daily\"]/div/div[1]/div[1]/div[2]/div/p/text()"))
        print("-3-->" + date)
        date = date.replace("']", "").replace("['", "")
        print("-4-->" + date)
        url_hindi = "https://hindi.astroyogi.com/rashifal"+date+"/"+sunsign_hn+"-rashifal-"+date
        print url_hindi
        ######### fro Horoscope ################
        web_page = urlopen(url_hindi)
        soup = BeautifulSoup(web_page, 'html.parser')
        print "---TODAY---"
        horoscope=""
        for extract_div in soup.findAll("p", {"class": "text-justify"}):
            horoscope+=extract_div.text
        print horoscope
        horoscope = horoscope.replace("\n", "").replace("  ", "").replace("[\"", "").replace("\"]", "")
        dict = {
            'date': date,
            'horoscope': horoscope,
            'sunsign english': sunsign_en,
            'sunsign hindi': sunsign_hn
        }

        return dict

