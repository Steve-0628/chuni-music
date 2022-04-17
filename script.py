import json
from bs4 import BeautifulSoup
import requests


def run():
    songs_url_1 = "https://chunithm.gamerch.com/CHUNITHM%20NEW%20PLUS%20%E6%A5%BD%E6%9B%B2%E4%B8%80%E8%A6%A7"
    songs_url_2 = "https://chunithm.gamerch.com/CHUNITHM%20NEW%20PLUS%20%E6%A5%BD%E6%9B%B2%E4%B8%80%E8%A6%A72"

    html_1 = requests.get(songs_url_1).text
    soup_1 = BeautifulSoup(html_1, "html.parser")

    unparsed_songs = {}
    parsed_songs = {}
    categories = {
        "pops_anime": "POPS&ANIME",
        "niconico": "niconico",
        "toho": "東方Project",
        "variety": "VARIETY",
        "irodori": "イロドリミドリ",
        "gekimai": "ゲキマイ",
        "original": "ORIGINAL"
    }
    unparsed_songs["pops_anime"] = soup_1.select_one("div.t-line-img:nth-child(3) > table:nth-child(15)")
    unparsed_songs["niconico"] = soup_1.select_one("div.t-line-img:nth-child(3) > table:nth-child(18)")
    unparsed_songs["toho"] = soup_1.select_one("div.t-line-img:nth-child(3) > table:nth-child(21)")
    unparsed_songs["variety"] = soup_1.select_one("div.t-line-img:nth-child(3) > table:nth-child(24)")

    html_2 = requests.get(songs_url_2).text
    soup_2 = BeautifulSoup(html_2, "html.parser")

    unparsed_songs["irodori"] = soup_2.select_one("div.t-line-img:nth-child(3) > table:nth-child(15)")
    unparsed_songs["gekimai"] = soup_2.select_one("div.t-line-img:nth-child(3) > table:nth-child(19)")
    unparsed_songs["original"] = soup_2.select_one("div.t-line-img:nth-child(3) > table:nth-child(23)")

    # print(unparsed_songs.keys())

    for key in unparsed_songs.keys():
        # print(key)
        song = unparsed_songs[key]
        parsed_songs[key] = {"name": categories[key], "songs": []}
        tbody = song.select_one("tbody")
        trs = tbody.select("tr")
        for tr in trs:
            th = tr.select_one("th")
            tds = tr.select("td")
            note = ""
            if th["style"].replace(" ", "").find("background:lightgreen") == -1:
                note = "配信待ち"
            elif th["style"].replace(" ", "").find("background:skyblue") == -1:
                note = "マップ解放/後日通常配信"
            elif th["style"].replace(" ", "").find("background:gold") == -1:
                note = "ゲキマイ連携"
            elif th["style"].replace(" ", "").find("background:lightpink") == -1:
                note = "特殊条件"
            parsed_song = {
                "title": th.text,
                "artist": tds[0].text,
                "bpm": tds[1].text,
                "note": note,
                "diff": {
                    "basic": tds[2].text,
                    "advanced": tds[3].text,
                    "expert": tds[4].text,
                    "master": tds[5].text
                }
            }
            parsed_songs[key]["songs"].append(parsed_song)
        print(parsed_songs[key]["songs"].__len__())

    # print(parsed_songs["niconico"][0])
    json.dump(parsed_songs, open("chunithm.json", "w", encoding="utf-8"), indent=4, ensure_ascii=False)



if __name__ == "__main__":
    run()