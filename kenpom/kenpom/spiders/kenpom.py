# -*- coding: utf-8 -*-
import scrapy
import pandas as pd
from bs4 import BeautifulSoup


class KenpomSpider(scrapy.Spider):
    name = "kenpom"

    def start_requests(self):
        for season in range(2002, 2018):
            url = 'http://Kenpom.com/index.php?y=' + str(season)
            request = scrapy.Request(url=url, callback=self.parse)
            request.meta['season'] = season
            yield request

    def parse(self, response):
        season = response.meta['season']
        res = BeautifulSoup(response.body)
        teams = pd.read_csv('../../dataset/Teams.csv')
        all_data = pd.DataFrame(columns = ('Rank','Team','Conf','W-L','AdjEM','AdjO','AdjD','AdjT','Luck','SOS AdjEM','SOS OppO','SOS OppD','NCSOS AdjEM'))
        idx = 0
        for row in res.select('#data-area > table > tbody > tr'):
            col = row.select('td')
            t = col[1].select('a')[0].text.replace(r'.', '')
            if t not in teams.Team_Name.values:
                if t is u'Saint Mary\'s':
                    s = 'St Mary\'s CA'
                elif t is u'Middle Tennessee':
                    s = 'MTSU'
                elif t is u'VCU':
                    s = 'Virginia'
                elif t is u'East Tennessee St':
                    s = 'ETSU'
                elif t is u'Monmouth':
                    s = 'Monmouth NJ'
                else:
                    s = 'TBD'
            else:
                s = t
            data = [col[0].text, s, col[2].text, col[3].text, float(col[4].text), float(col[5].text), float(col[7].text), float(col[9].text),
                    float(col[11].text), float(col[13].text), float(col[15].text), float(col[17].text), float(col[19].text)]
            all_data.loc[idx] = data
            idx = idx + 1
        all_data.to_csv(str(season) + '_test.csv', index = False)
