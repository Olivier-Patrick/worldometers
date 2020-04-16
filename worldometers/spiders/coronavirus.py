# -*- coding: utf-8 -*-
import scrapy

class CoronavirusSpider(scrapy.Spider):
    name = 'coronavirus'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/coronavirus/#countries/']

    def parse(self, response):
        #title = response.xpath("//h3/text()").get()
        rows = response.xpath("//table/tbody/tr")
        for row in rows:
            name_country = row.xpath('.//td[1]/a/text()').get()
            total_cases = row.xpath('.//td[2]/text()').get()
            new_cases = row.xpath('.//td[3]/text()').get()
            total_deaths = row.xpath('.//td[4]/text()').get()
            new_deaths = row.xpath('.//td[5]/text()').get()
            total_recovered = row.xpath('.//td[6]/text()').get()
            active_cases = row.xpath('.//td[7]/text()').get()
            serious_critical = row.xpath('.//td[8]/text()').get()
            tot_cases_m_pop = row.xpath('.//td[9]/text()').get()
            death_cases_m_pop = row.xpath('.//td[10]/text()').get()
            total_tests = row.xpath('.//td[11]/text()').get()
            tests_m_pop = row.xpath('.//td[12]/text()').get()
            
            

        
            yield{
                 'name country' : name_country,
                 'Total cases': total_cases,
                 'New cases': new_cases,
                 'Total deaths': total_deaths,
                 'New deaths': new_deaths,
                 'Total recovered': total_recovered,
                 'Active cases': active_cases,
                 'Serious critical': serious_critical,
                 'Tot cases/ 1M pop': tot_cases_m_pop,
                 'Deaths cases/ 1M pop': death_cases_m_pop,
                 'Total tests': total_tests,
                 'Tests/ 1M pop': tests_m_pop,


                 
            }

        

    