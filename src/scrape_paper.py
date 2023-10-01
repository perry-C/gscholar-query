import json

import pandas as pd
import requests
from serpapi import GoogleSearch

import config
from chat import get_chat_summary
from utils import md_to_html


def extract_bibtex_link(result):
    serpapi_cite_link = "{}&api_key={}".format(
        result["inline_links"]["serpapi_cite_link"], config.serpi_api_key
    )
    r_json = requests.get(serpapi_cite_link).json()
    bibtex_link = r_json["links"][0]["link"]
    return bibtex_link


def scrape_paper(input_string):
    params = {
        "engine": "google_scholar",
        "hl": "en",
        "q": input_string,
        "api_key": config.serpi_api_key,
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    organic_results = results["organic_results"]

    processed_results = []
    for result in organic_results:
        bibtex_link = extract_bibtex_link(result)

        # * Uncomment if want to turn on the chatGPT feature
        # chat_summary = get_chat_summary(result['title'])

        processed_result = {
            "title": result["title"],
            "cited_by": result["inline_links"]["cited_by"]["total"],
            " link": result["link"],
            "snippet": result["snippet"],
            "bibtex_link": bibtex_link,
            # * Uncomment if want to turn on the chatGPT feature
            # "chat_summary": chat_summary,
        }
        processed_results.extend([processed_result])

    df = pd.DataFrame(processed_results)
    with open("data/data.md", "w") as f:
        df_to_md = df.to_markdown()
        f.write(df_to_md)

    md_to_html("data")
