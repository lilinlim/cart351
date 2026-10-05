# lilin
# CART 351 EXERCISE ONE PART TWO B

#import the lib
import requests

#setting up table and console
from rich.console import Console
from rich.table import Table

def fetch_swapi_data():

    #url
    url = f"https://swapi.info/api/planets/"

    #make request
    response = requests.get(url)

    #get response as a json
    data = response.json()

    console = Console()

    #column for each table
    table = Table(show_header=True, header_style="bold")
    table.add_column("NAME", style="magenta")
    table.add_column("DIAMETER", style="blue")
    table.add_column("POPULATION", style="turquoise4")

    #planet for loop
    for planet in data:
        #adding each table row
        table.add_row(planet['name'], planet['diameter'], planet['population'])

    #printing table
    console.print(table)

fetch_swapi_data()
