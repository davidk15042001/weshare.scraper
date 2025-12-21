import requests
from serpapi import GoogleSearch
from decouple import config
import json



def search_github(user_data):
    print("QUIRYING GITHUB APIS")
    github_list = []
    vals = []
    for i in user_data.keys():
        if user_data[i]:
            vals.append(user_data[i])
    query = " OR ".join(vals)
    url = f"https://api.github.com/search/users?q={query}"
    res = requests.get(url)
    res = res.json()
    if res["total_count"]>0:
        for i in res["items"]:
            github_dict = {
                "platform": "Github",
                "title": i["login"],
                "link": i["html_url"],
                "avatar_url": i["avatar_url"]
            }
            github_list.append(github_dict)
        return github_list
    else:
        return []

def search_vimeo(user_data):
    print("QUIRYING VIMEO APIS")
    vimeo_list = []
    vals = []
    if user_data["first_name"]:
        vals.append(user_data["first_name"])
    if user_data["last_name"]:
        vals.append(user_data["last_name"])
    query = " ".join(vals)
    url = f"https://api.vimeo.com/users?direction=asc&page=2&per_page=20&query={query}&sort=relevant"
    headers = {
        "Authorization":f"bearer {config('VIMEO_PAK')}",
        "Accept": "application/vnd.vimeo.*+json;version=3.4"
    }
    res = requests.get(url, headers=headers)
    res = res.json()
    if res["total"]>0:
        for i in res["data"]:
            vimeo_dict = {
                "platform": "Vimeo",
                "title": i["name"],
                "link": i["link"],
                "avatar_url": i["pictures"]["base_link"]
            }
            vimeo_list.append(vimeo_dict)
        return vimeo_list
    else:
        return []


def search_gitlab(user_data):
    print("QUIRYING GITLAB APIS")
    gitlab_list = []
    vals = []
    if user_data["first_name"]:
        vals.append(user_data["first_name"])
    if user_data["last_name"]:
        vals.append(user_data["last_name"])
    query = " ".join(vals)
    url = f"https://gitlab.com/api/v4/users?search={query}&page=1&per_page=20"
    headers = {
        "Authorization":f"bearer {config('GITLAB_PAK')}",
    }
    res = requests.get(url, headers=headers)
    res = res.json()
    if len(res)>0:
        for i in res:
            gitlab_dict = {
                "platform": "Gitlab",
                "title": i["name"],
                "link": i["web_url"],
                "avatar_url": i["avatar_url"]
            }
            gitlab_list.append(gitlab_dict)
        return gitlab_list
    else:
        return []


def search_stack_exchange(user_data):
    print("QUIRYING STACK EXCHANGE APIS")
    sk_ex_list = []
    vals = []
    if user_data["first_name"]:
        vals.append(user_data["first_name"])
    if user_data["last_name"]:
        vals.append(user_data["last_name"])
    query = " ".join(vals)
    url = f"https://api.stackexchange.com/2.3/users?order=desc&sort=reputation&inname={query}&site=stackoverflow"
    res = requests.get(url)
    res = res.json()
    if len(res["items"])>0:
        for i in res["items"]:
            sk_ex_dict = {
                "platform": "Stack Overflow",
                "title": i["display_name"],
                "link": i["link"],
                "avatar_url": i["profile_image"]
            }
            sk_ex_list.append(sk_ex_dict)
        return sk_ex_list
    else:
        return []


INDEXED_SITES = {
    "LinkedIn": "linkedin.com/in/",
    "Facebook": "facebook.com",
    "Instagram": "instagram.com",
    "X (Twitter)": "x.com",

    # "TikTok": "tiktok.com",
    # "Pinterest": "pinterest.com",
    # "Bitbucket": "bitbucket.org",
    # "YouTube": "youtube.com/channel",
    # "Behance": "behance.net",
    # "Dribbble": "dribbble.com",
    # "Medium": "medium.com",
    # "Reddit": "reddit.com/user",
    # "Quora": "quora.com/profile",
    # "ProductHunt": "producthunt.com"
}


def search_indexed_google(user_data):
    print("QUIRYING GOOGLE APIS")
    serf_api_key = config('SERP_API_KEY')

    if user_data["country"]:
        with open("google-countries.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        gl_countries = next(
            (gl for gl in data if gl["country_name"] == user_data["country"].title()),
            None
        )
        country_code = gl_countries["country_code"]
    else:
        country_code = ""
    
    vals = []
    if user_data["first_name"]:
        vals.append(user_data["first_name"])
    if user_data["last_name"]:
        vals.append(user_data["last_name"])
    if user_data["country"]:
        vals.append(user_data["country"])
    query_user = " ".join(vals)

    found_profiles = []
    for platform_name, domain in INDEXED_SITES.items():
        query = f'site:{domain} "{query_user}"'
        params = {
            "q": query,
            "api_key": serf_api_key,
            "engine": "google",
            "num": 5,
            "hl": "en"
        }
        if country_code:
            params["gl"]=country_code
        try:
            search = GoogleSearch(params)
            results = search.get_dict()
            organic_results = results.get("organic_results", [])
            
            for item in organic_results:
                if domain in item.get("link", ""):
                    found_profiles.append({
                        "platform": platform_name,
                        "title": item.get("title"),
                        "link": item.get("link"),
                        "snippet": item.get("snippet")
                    })
        except Exception as e:
            return f"Error -> {e}"
    return found_profiles