import requests
import argparse
import csv

class OverpassClient:
    def __init__(self):
        pass

    def request_using_query(self, server, lat, lon, radius, query):
        query = query.replace("AROUND", "around:%f,%.10f,%.10f" % (radius,lat,lon))
        query = "data=[out:json][timeout:25]; %s ; out;" % (query)
        url = "%s?%s" % (server,query)
        print(url)
        result = requests.get(url)
        if result.status_code != 200:
            warning = "Warning: status code %s" % (result.status_code)
            print(warning)
        return result.json()

    def request_using_tags(self, server, lat, lon, radius, tags):
        query = "data=[out:json][timeout:100];"

        query += "("
        for t in tags:
            query += "nwr[%s](around:%f,%.10f,%.10f);" % (t,radius,lat,lon)
        query += ")->.r;"

        query += "(.r;);"
        query += "out;"

        url = "%s?%s" % (server,query)
        #print("query: " + url)
        result = requests.get(url)
        if result.status_code != 200:
            warning = "Warning: status code %s" % (result.status_code)
            print(warning)
        return result.json()

def main(csv_in, csv_out, tags):
    client = OverpassClient()

    with open(csv_out, 'w') as file_out:
        writer = csv.writer(file_out)
        with open(csv_in, 'r') as file_in:
            reader = csv.reader(file_in)
            header = next(reader, None)
            header.append('result')
            writer.writerow(header)
            for row in reader:
                print("processing %s" % (row))
                lat = float(row[0])
                lon = float(row[1])
                radius = float(row[2])
                r = client.request_using_tags("https://overpass-api.de/api/interpreter",lat,lon,radius,tags)
                row.append(r)
                writer.writerow(row)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('csv_in', type=str, help='csv input file with following format: lat,lon,radius')
    parser.add_argument('csv_out', type=str, help='csv output file')
    parser.add_argument('tags', type=str, help='file with an osm tag per line')
    args = parser.parse_args()

    with open(args.tags) as file:
        tags = [line.rstrip() for line in file]

    print("Using tags: " + str(tags))

    main(args.csv_in,args.csv_out,tags)
