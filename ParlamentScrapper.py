import requests
from bs4 import BeautifulSoup
import json

# person_url_list = []
#
# for i in range(0, 721, 20):
#     url = f"https://www.bundestag.de/ajax/filterlist/en/members/863330-863330?limit=20&noFilterSet=true&offset={i}"
#     print(url)
#
#     req = requests.get(url)
#     result = req.content
#
#     soup = BeautifulSoup(result, "lxml")
#
#     persons = soup.select("div.bt-slide-content > a")
#     asd = persons[0]["href"]
#     index = 0
#     for person in persons:
#         person_url = person.get("href")
#         person_url_list.append(person_url)
#
# with open ("list.txt", "a") as f:
#     for line in person_url_list:
#         f.write(f"{line}\n")


with open("list.txt") as f:
    lines = [line.strip() for line in f.readlines()]
    data_dict = []
    count = 0
    for line in lines:
        req = requests.get(line)
        result = req.content
        soup = BeautifulSoup(result, "lxml")
        person = soup.find(class_="bt-biografie-name").find("h3").text
        person_name_company = person.strip().split(",")
        person_name = person_name_company[0]
        person_company = person_name_company[1].strip()
        social_networks = soup.find_all(class_="bt-link-extern")

        sn_urls = []
        for items in social_networks:
            sn_urls.append(items.get("href"))

        data = {
            "person_name": person_name,
            "person_compamy": person_company,
            "social_networks": sn_urls
        }

        count += 1
        print(f"Iteration count {count}: done")
        data_dict.append(data)

        with open("data.json", "w") as f:
            json.dump(data_dict, f, indent=4, ensure_ascii=False)