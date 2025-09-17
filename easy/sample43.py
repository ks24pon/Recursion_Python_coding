def redirectionUrl(language):
    url = "www.example.org/"
    if language == "English": return url + "en"
    elif language == "Japanese": return url + "ja"
    elif language == "Spanish": return url + "es"
    elif language == "Russian": return url + "ru"
    else: return url