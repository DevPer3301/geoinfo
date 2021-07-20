# __GeoInfo__
##### __GeoInfo__ is a Python module for getting a lot information/data about countries

##### Supported info:
1. Capital
2. Region
3. Population
4. Area
5. Currency
6. Borders
## Installing
```
git clone https://github.com/DevPer3301/geoinfo.git
```
## Pre-Requiredment
```
pip3 install -r requirements.txt
```

## Using
```python
from geoinfo import geoinfo


print(geoinfo.get_capital("Germany")) #With using get_capital you can get  information about capital of the country

print(geoinfo.get_borders("Usa")) #With using get_borders you can get  information about borders of the country

print(geoinfo.get_population("China")) #With using get_population you can get  information about population of the country

print(geoinfo.get_region("Australia")) #With using get_region you can get  information about region of the country

print(geoinfo.get_area("Russia")) #With using get_area you can get  information about area of the country

print(geoinfo.get_currency("Ukraine")) #With using get_currency you can get  information about currency of the country
```
> Berlin
>
> ['CAN', 'MEX']
>
> 1377422166
>
>Oceania
>
>17124442.0
>
>{'code': 'UAH', 'name': 'Ukrainian hryvnia', 'symbol': '₴'}