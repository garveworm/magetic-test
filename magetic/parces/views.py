from django.http import HttpResponse
from django.template import Context, loader

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .parser import Parser
from .utils import filter_by_keywords


class ResultAPIView(APIView):
    """
        renders list of games and categories in html
        :return:
        """
    google_play_parser = Parser('https://play.google.com/store/apps/category/GAME')
    data = google_play_parser.parse()

    def get(self, request):
        return Response(self.data, status.HTTP_200_OK)


def ResultHTMLView(request):
    """
    renders list of games and categories in html
    :param request:
    :return:
    """
    # init parser and get data
    google_play_parser = Parser('https://play.google.com/store/apps/category/GAME')
    data = google_play_parser.parse()
    html = ""

    query_params = request.GET.get('search')
    if query_params:
        data = filter_by_keywords(data, query_params)

    # construct html
    for key, values in data.items():
        html += f'<ol><h2>{key}</h2>'
        for value in values:
            html += f'<li>{value}</li>'
        html += '</ol>'

    return HttpResponse(html)


