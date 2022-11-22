#import mod
import utils
import readcsv
import charts
import pandas as pd

'''data = [
   {
      'Country' : 'Colombia',
      'Population' : 500
   },
   {
      'Country' : 'Bolivia',
      'Population' : 300
   }
]'''

'''def run():
   keys, values = mod.get_population()
   print(keys,values)
   country = input('Type Country = ')
   result = mod.population_by_country(data,country)
   print(result)'''

def run():
   
   data = readcsv.read_csv('world_population.csv')
   print(data)
   df = pd.read_csv('world_population.csv')
   df = df[df['Continent']=='South America']
   counties = df['Country/Territory'].values
   percentages = df['World Population Percentage'].values
   charts.generate_pie_chart(counties, percentages)


   country = input('Type Country => ')
   
   result = utils.population_by_country(data, country)
   if len(result) > 0:
      country = result[0]
      labels, values = utils.get_population(country)
      charts.generate_bar_chart(labels, values)


if __name__ == '__main__':
  run()
