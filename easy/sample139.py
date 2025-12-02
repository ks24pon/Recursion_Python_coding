def redirectionUrl(language):
    URL = "www.example.org/"
    if language == "English":
        return URL + "en"
    elif language == "Japanese":
        return URL + "ja"
    elif language == "Spanish":
        return URL + "es"
    elif language == "Russian":
        return URL + "ru"
    return URL
