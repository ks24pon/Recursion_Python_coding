def redirectionUrl(language):
    URL = "www.example.org/"

    langMap = {
        "Japanese": "ja",
        "English": "en",
        "Spanish": "es",
        "Russian": "ru"
    }

    code = langMap.get(language, "")
    return URL + code