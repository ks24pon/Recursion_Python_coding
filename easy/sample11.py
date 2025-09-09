def redirectionUrl(language):
    url = "www.example.org/"

    if language == "Japanese": url += "ja"
    elif language == "English": url += "en"
    elif language == "Spanish": url += "es"
    elif language == "Russian": url += "ru"

    return url