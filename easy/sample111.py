def redirectionUrl(language):
    URL = "www.example.org/"

    if language == "Japanese":
        return URL + "ja"
    elif language == "English":
        return URL + "en"
    elif language == "Spanish":
        return URL + "es"
    elif language == "Russian":
        return URL + "ru"
    else:
        return URL
