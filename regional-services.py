import requests
import json

def run():
    # fetch json data from url
    url = 'https://api.regional-table.region-services.aws.a2z.com/index.json'
    response = requests.get(url)
    data = response.json()

    region_counters = {}
    for item in data['prices']:
        region = item['attributes']['aws:region']
        if region not in region_counters:
            region_counters[region] = 0

        region_counters[region] += 1

    # sort by value
    sorted_region_counters = sorted(region_counters.items(), key=lambda x: x[1], reverse=True)
    print(json.dumps(sorted_region_counters, indent=4))

if __name__ == '__main__':
    run()
