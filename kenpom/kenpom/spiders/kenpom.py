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
        teams = pd.read_csv('../../dataset/kaggle/Teams.csv')
        all_data = pd.DataFrame(columns = ('Rank','Team','Conf','W-L','AdjEM','AdjO','AdjD','AdjT','Luck','SOS AdjEM','SOS OppO','SOS OppD','NCSOS AdjEM'))
        cmp_data = pd.DataFrame(columns = ('OriTeamName','AdjTeamName'))
        idx = 0
        for row in res.select('#data-area > table > tbody > tr'):
            col = row.select('td')
            t = col[1].select('a')[0].text.replace(r'.', '')
            if t not in teams.Team_Name.values:
                if t == u'Kent St':
                    s = 'Kent'
                elif t == u'North Carolina St':
                    s = 'NC State'
                elif t == u'Western Kentucky':
                    s = 'WKU'
                elif t == u'Southern Illinois':
                    s = 'S Illinois'
                elif t == u'Saint Joseph\'s':
                    s = 'St Joseph\'s PA'
                elif t == u'UC Santa Barbara':
                    s = 'Santa Barbara'
                elif t == u'College of Charleston':
                    s = 'Col Charleston'
                elif t == u'Saint Louis':
                    s = 'St Louis'
                elif t == u'East Tennessee St':
                    s = 'ETSU'
                elif t == u'Milwaukee':
                    s = 'WI Milwaukee'
                elif t == u'Arkansas Little Rock':
                    s = 'Ark Little Rock'
                elif t == u'Louisiana Lafayette':
                    s = 'ULL'
                elif t == u'Southwest Missouri St':
                    s = 'Missouri St'
                elif t == u'Illinois Chicago':
                    s = 'IL Chicago'
                elif t == u'VCU':
                    s = 'VA Commonwealth'
                elif t == u'Loyola Chicago':
                    s = 'Loyola-Chicago'
                elif t == u'Western Michigan':
                    s = 'W Michigan'
                elif t == u'Georgia Southern':
                    s = 'Ga Southern'
                elif t == u'Central Connecticut':
                    s = 'Central Conn'
                elif t == u'The Citadel':
                    s = 'Citadel'
                elif t == u'Troy St':
                    s = 'Troy'
                elif t == u'Cal Poly':
                    s = 'Cal Poly SLO'
                elif t == u'Eastern Washington':
                    s = 'E Washington'
                elif t == u'UTSA':
                    s = 'UT San Antonio'
                elif t == u'UMKC':
                    s = 'Missouri KC'
                elif t == u'Texas Pan American':
                    s = 'UTRGV'
                elif t == u'Cal St Northridge':
                    s = 'CS Northridge'
                elif t == u'Northern Illinois':
                    s = 'N Illinois'
                elif t == u'Louisiana Monroe':
                    s = 'ULM'
                elif t == u'Florida Atlantic':
                    s = 'FL Atlantic'
                elif t == u'Boston University':
                    s = 'Boston Univ'
                elif t == u'George Washington':
                    s = 'G Washington'
                elif t == u'Middle Tennessee':
                    s = 'MTSU'
                elif t == u'Central Michigan':
                    s = 'C Michigan'
                elif t == u'American':
                    s = 'American Univ'
                elif t == u'Green Bay':
                    s = 'WI Green Bay'
                elif t == u'Saint Mary\'s':
                    s = 'St Mary\'s CA'
                elif t == u'Southwest Texas St':
                    s = 'Texas St'
                elif t == u'Western Carolina':
                    s = 'W Carolina'
                elif t == u'Eastern Illinois':
                    s = 'E Illinois'
                elif t == u'Monmouth':
                    s = 'Monmouth NJ'
                elif t == u'FIU':
                    s = 'Florida Intl'
                elif t == u'Northwestern St':
                    s = 'Northwestern'
                elif t == u'Tennessee Martin':
                    s = 'TN Martin'
                elif t == u'Texas A&M Corpus Chris':
                    s = 'Texas A&M'
                elif t == u'Western Illinois':
                    s = 'W Illinois'
                elif t == u'Stephen F Austin':
                    s = 'SF Austin'
                elif t == u'Loyola Marymount':
                    s = 'Loy Marymount'
                elif t == u'South Carolina St':
                    s = 'S Carolina St'
                elif t == u'North Carolina A&T':
                    s = 'NC A&T'
                elif t == u'Southeast Missouri St':
                    s = 'SE Missouri St'
                elif t == u'Sacramento St':
                    s = 'CS Sacramento'
                elif t == u'Charleston Southern':
                    s = 'Charleston So'
                elif t == u'Mississippi Valley St':
                    s = 'Mississippi St'
                elif t == u'Cal St Fullerton':
                    s = 'CS Fullerton'
                elif t == u'Bethune Cookman':
                    s = 'Bethune-Cookman'
                elif t == u'Eastern Kentucky':
                    s = 'E Kentucky'
                elif t == u'Maryland Eastern Shore':
                    s = 'MD E Shore'
                elif t == u'Birmingham Southern':
                    s = 'Birmingham So'
                elif t == u'Southeastern Louisiana':
                    s = 'SE Louisiana'
                elif t == u'Coastal Carolina':
                    s = 'Coastal Car'
                elif t == u'Eastern Michigan':
                    s = 'E Michigan'
                elif t == u'Saint Peter\'s':
                    s = 'St Peter\'s'
                elif t == u'Grambling St':
                    s = 'Grambling'
                elif t == u'Texas Southern':
                    s = 'TX Southern'
                elif t == u'Albany':
                    s = 'Albany NY'
                elif t == u'Southern':
                    s = 'Southern Univ'
                elif t == u'Fairleigh Dickinson':
                    s = 'F Dickinson'
                elif t == u'Prairie View A&M':
                    s = 'Prairie View'
                elif t == u'LIU Brooklyn':
                    s = 'Long Island'
                elif t == u'Arkansas Pine Bluff':
                    s = 'Ark Pine Bluff'
                elif t == u'Mount St Mary\'s':
                    s = 'Mt St Mary\'s'
                elif t == u'UT Rio Grande Valley':
                    s = 'UTRGV'
                elif t == u'Cal St Bakersfield':
                    s = 'CS Bakersfield'
                elif t == u'Florida Gulf Coast':
                    s = 'FL Gulf Coast'
                elif t == u'Northern Kentucky':
                    s = 'N Kentucky'
                elif t == u'Fort Wayne':
                    s = 'IPFW'
                elif t == u'North Carolina Central':
                    s = 'NC Central'
                elif t == u'North Dakota St':
                    s = 'N Dakota St'
                elif t == u'Nebraska Omaha':
                    s = 'NE Omaha'
                elif t == u'South Dakota St':
                    s = 'S Dakota St'
                elif t == u'Houston Baptist':
                    s = 'Houston Bap'
                elif t == u'USC Upstate':
                    s = 'SC Upstate'
                elif t == u'Little Rock':
                    s = 'Ark Little Rock'
                elif t == u'Kennesaw St':
                    s = 'Kennesaw'
                elif t == u'Northern Colorado':
                    s = 'N Colorado'
                elif t == u'UMass Lowell':
                    s = 'MA Lowell'
                elif t == u'Abilene Christian':
                    s = 'Abilene Chr'
                elif t == u'Central Arkansas':
                    s = 'Cent Arkansas'
                elif t == u'SIU Edwardsville':
                    s = 'Edwardsville'
                elif t == u'Winston Salem St':
                    s = 'W Salem St'
                elif t == u'Utah Valley St':
                    s = 'Utah Valley'
                elif t == u'Middle Tennessee St':
                    s = 'MTSU'
                else:
                    s = 'TBD'
                    print(str(season) + ": " + t)
            else:
                s = t
            data1 = [col[0].text, s, col[2].text, col[3].text, float(col[4].text), float(col[5].text), float(col[7].text), float(col[9].text),
                    float(col[11].text), float(col[13].text), float(col[15].text), float(col[17].text), float(col[19].text)]
            data2 = [t,s]
            all_data.loc[idx] = data1
            cmp_data.loc[idx] = data2
            idx = idx + 1
        all_data.to_csv(str(season)[2:] + 'PCBR.csv', index = False)
        cmp_data.to_csv(str(season)[2:] + 'TeamNameCmp.csv', index = False)
