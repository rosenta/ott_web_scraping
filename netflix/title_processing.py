import json
import requests
import pandas as pd
from bs4 import BeautifulSoup

def get_titles_info(title_id: str):
    title_info_dict = {
        "title": "",
        "overview": "",
        "genres": [],
        "cast": [],
        "content_is": [],
        "subtitles": [],
        "audio": [],
    }

    request_url = f"https://www.netflix.com/title/{title_id}"
    response = requests.get(request_url)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    if soup:

        title_h1 = soup.find("h1", class_="title-title")
        if title_h1:
            title_info_dict.update({
                "title": title_h1.text
            })

        overview_div = soup.find("div", class_="title-info-synopsis")
        if overview_div:
            title_info_dict.update({            
                "overview": overview_div.text
            })

        genre_div = soup.find("div", "more-details-cell cell-genres")
        if genre_div:
            title_info_dict.update({
                "genres": [spn.text.replace(',', '').strip() for spn in genre_div.findAll('span')]
            })
            

        cast_div = soup.find("div", "more-details-cell cell-cast")
        if cast_div:
            title_info_dict.update({
                "cast": [spn.text.replace(',', '').strip() for spn in cast_div.findAll('span')]
            })


        content_mood_div = soup.find("div", "more-details-cell cell-mood-tag")
        if content_mood_div:
            title_info_dict.update({
                "content_is": [spn.text.replace(',', '').strip() for spn in content_mood_div.findAll('span')]
            })

        subtitles_div = soup.find("div", "more-details-cell cell-subtitle")
        if subtitles_div:
            title_info_dict.update({
                "subtitles": [spn.text.replace(',', '').strip() for spn in subtitles_div.findAll('span')]
            })

        audio_div = soup.find("div", "more-details-cell cell-audio")
        if subtitles_div:
            title_info_dict.update({
                "audio": [spn.text.replace(',', '').strip() for spn in audio_div.findAll('span')]
            })

    return title_info_dict


def process_title(item_summ, result_list):
    title_info_dict = {}

    if not item_summ["itemSummary"].get("value"):
        return

    item_summ_val = item_summ["itemSummary"]["value"]

    print(f"processing for title_id -> {item_summ_val['id']}")

    misc_title_info_dict = get_titles_info(str(item_summ_val["id"]))

    title_info_dict.update({
        "id": str(item_summ_val["id"]),
        "title": item_summ_val["title"],
        "type": item_summ_val["type"],
        "release_year": item_summ_val["releaseYear"],
        "runtime": item_summ_val.get("infoDensityRuntime"),
        "backdrop_path": item_summ_val["boxArt"]["url"],
        "made_by_netflix": item_summ_val["isOriginal"],
        "maturity_rating": item_summ_val["maturity"]["rating"]["value"],
        "maturity_warning": item_summ_val["maturity"]["rating"]["maturityDescription"],
        "maturity_rating_reason": [ix for ix in item_summ_val["maturity"]["rating"]["specificRatingReason"].split(', ')],
        "maturity_rating_board": item_summ_val["maturity"]["rating"]["board"],
    })

    title_info_dict = {**title_info_dict, **misc_title_info_dict}
    result_list.append(title_info_dict)

    # return title_info_dict

def process_titles_data_batch_worker(batch, result_list):
    for item_summ_val in batch:
        process_title(item_summ_val, result_list)