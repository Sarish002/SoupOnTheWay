# Import Statements
import bs4
import requests
from bs4 import BeautifulSoup
import sys

# Class returning distance
class Distance:

    # Class of cities
    class City:

        # Function for finding code
        @staticmethod # Decorator
        def Find_Code(city="") -> str:
            orig1 = (f"https://www.iata.org/en/publications/directories/code-search/?airport.search={city}") # URL
            request1 = requests.get(orig1) # Getting HTML
            soup1 = bs4.BeautifulSoup(request1.text,
                                      "html.parser") # Parser
            try:
                soup1 = soup1.find_all("td")[5].text
            except IndexError:
                print("Not found....")
                return "Not found .. "

            # Code
            return soup1

        # City __init__ function
        def __init__(self,
                     name = ""):
            self.name = name
            self.code = self.Find_Code(name)

    # Finding distance
    @staticmethod
    def Get_Distance(code1: City,
                     code2: City) -> str:
        next = (f"https://www.airmilescalculator.com/distance/{code1.code.lower()}-to-{code2.code.lower()}/") # URL
        find = BeautifulSoup(
            requests.get(next).text, # HTML
            "html.parser"
        ) # Parser

        # Info
        try:
            if find.find_all("p")[1].text == "Search by airport name, city, or IATA/ICAO airport code.":
                find = find.find_all("p")[0].text
                find: str = find.replace("\n", " ")
                find = find.split(")")
                find = "Aeroplane: " + find[2][4 : ]
            else:
                find = find.find_all("p")[0].text + "\n" + find.find_all("p")[1].text
                print(find)
                find: str = find.replace("\n", " ")
                find = find.split(")")
                find = ("Aeroplane: " + find[2][4 : find[2].index(".")] + "\n" + "Car: " +
                        find[4][4 : find[4].index(",")] +
                        " (" + find[4][(find[4].index(",") + 35) : find[4].index(".")]) + ")"
        except:
            return "Not found ... "

        # Info
        return find

    # Distance  __init__ function
    def __init__(self,
                 city1: City | None = None,
                 city2: City | None = None) -> None:

        self.city1 = city1
        self.city2 = city2

        if city1 is not None and city2 is not None: # Check for error
            self.distance = self.Get_Distance(city1,
                                              city2) # Distance
        else:
            self.distance = None

if __name__ == '__main__':

     city1 = Distance().City(input("Take off: "))
     city2 = Distance().City(input("Landing: "))

     distance = Distance(city1, city2)
     print(distance.distance)