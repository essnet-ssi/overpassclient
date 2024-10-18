# overpassclient

A simple python OSM overpass client to perform queries

## usage

```bash
python python/main.py <in.csv> <out.csv> <tags>
```

- in.csv: a csv with header lat,lon,radius
- out.csv: output csv (same format as in.csv but with additional column 'result')
- tags: a file with a single OSM tag per line. The tags will be used for the search query.

Example in.csv file:

```bash
lat,lon,radius
51.18,4.3502777778,50
```

Example tags file:

```bash
aerialway=station
aeroway="aerodrome|heliport|terminal"
amenity
leisure
shop
sport
tourism
```

Example out.csv file:

```bash
lat,lon,radius,result
51.18,4.3502777778,50,"{'version': 0.6, 'generator': 'Overpass API 0.7.62.1 084b4234', 'osm3s': {'timestamp_osm_base': '2024-10-18T12:15:26Z', 'copyright': 'The data included in this document is from www.openstreetmap.org. The data is made available under ODbL.'}, 'elements': [{'type': 'node', 'id': 997895864, 'lat': 51.1802449, 'lon': 4.350333, 'tags': {'addr:city': 'Hoboken', 'addr:housenumber': '12/1', 'addr:postcode': '2660', 'addr:street': 'IJskelderstraat', 'climbing:boulder': '130', 'climbing:grade:french:max': '8', 'climbing:grade:french:min': '3a', 'fee': 'yes', 'indoor': 'yes', 'leisure': 'sports_centre', 'name': 'Klimzaal Blok', 'opening_hours': 'Mo-Fr 10:00-23:00; Su 13:00-21:00; Sa 11:00-21:00', 'outdoor': 'no', 'phone': '+32 3 825 55 33', 'sport': 'climbing', 'website': 'https://klimzaalblok.be/'}}]}"
```

OSM Map features can be found [here](https://wiki.openstreetmap.org/wiki/Map_features).
