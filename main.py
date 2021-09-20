from bs4 import BeautifulSoup
import requests as r
import json


def main():
    result = {}

    for i in range(1, 10):
        URL = "https://data.gov.uz/uz/datasets/4253?dp-1-page={}&dp-1-sort=G2".format(i)
        response = r.get(URL)
        soup = BeautifulSoup(response.text, "html.parser")

        try:
            j = 1
            while True:
                region = soup.select("#w5 > div > table > tbody > tr:nth-child({}) > td:nth-child(2)".format(j))
                district = soup.select("#w5 > div > table > tbody > tr:nth-child({}) > td:nth-child(3)".format(j))

                region_text = clean_region(region[0].get_text())
                district_text = clean_district(district[0].get_text())

                if region_text in result:
                    result[region_text].append(district_text)
                else:
                    result[region_text] = []

                j += 1
            
        except Exception as e:
            print("---------------")
            print(e)
        

    with open("data.json", "w") as file:
        json.dump(result, file)


def clean_region(region):
    if region == "QQR":
        region = "Qoraqalpog'iston Respublikasi"
    
    region = region.replace("shaxri", "shahri")

    if region.split()[-1] == "shahar":
        region = region.replace("shahar", "shahri")
    
    if region.split()[-1] == "viloyat":
        region = region.replace("viloyat", "viloyati")
    
    region = region.replace("`", "'")
    region = region.replace("‘", "'")

    return region


def clean_district(district):
    district = district.replace("shaxri", "shahri")

    if len(district.split()) == 1:
        district = district + " tumani"

    if district.split()[-1] == "shahar":
        district = district.replace("shahar", "shahri")
    
    if district.split()[-1] == "tuman":
        district = district.replace("tuman", "tumani")
    
    if district.split()[-1] == "t.":
        district = district.replace("t.", "tumani")
    
    district = district.replace("`", "'")
    district = district.replace("‘", "'")

    return district


if __name__ == "__main__":
    main()


[
    {
        "region": {
            "latin": "",
            "crill": ""
        },
        "districts": [
            {
                "latin": "",
                "crill": ""
            },
            {
                "latin": "",
                "crill": ""
            },
            {
                "latin": "",
                "crill": ""
            }
        ]
    }
]