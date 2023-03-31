import requests
import pandas as pd
from bs4 import BeautifulSoup

''' This script scrapes data from a Pokemon database website and uses BeautifulSoup to parse and find the relevant data.
The data is then used to create a pandas DataFrame object for a tidy way to display it.'''

page = requests.get("https://pokemondb.net/pokedex/all")

soup = BeautifulSoup(page.content, 'html.parser')

table = soup.find_all('tr')

#print(soup.prettify())

#print(table[1].text)

pokemon_name = []
pokemon_all_types = []

for i in table[1:]:
    pokemon_name.append(i.a.text.strip())
    
    type = i.find_all('a', class_='type-icon')
    pokemon_type = []
    for t in type:
        pokemon_type.append(t.text.strip())
    pokemon_all_types.append(pokemon_type)

pokemon_df = pd.DataFrame({'pokemon_name': pokemon_name, 'pokemon_type': pokemon_all_types})

print(pokemon_df)




