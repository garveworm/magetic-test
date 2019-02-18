
def filter_by_keywords(data, keywords):
    """
    This function(really ugly) filters results by keywords to provide search functionality
    :param data:
    :param keywords:
    :return: filtered data
    """
    keywords = [keyword.lower() for keyword in keywords.split()]
    filtered_data = {}
    for key, value in data.items():
        filtered_games = []
        for index in range(len(value)-1):
            if any(word in value[index].lower() for word in keywords):
                filtered_games.append(value[index])

        filtered_data[key] = filtered_games

    return filtered_data
