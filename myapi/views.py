# Common Imports
from pydoc import describe
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from myapi.common.serializers.serializers import MasterListFilterBackend
from myapi.common.responses.error_response import FormatResponses
from lyrics_extractor import SongLyrics
# Module Imports


class FetchLyricsView(GenericAPIView):
    serializer_class = ""
    filter_backends = (MasterListFilterBackend,)

    @classmethod
    def get(cls, request):
        data = request.GET
        search = data.get("search")
        extract_lyrics = SongLyrics(
            "AIzaSyBTaviVA06f95Os-v2jOR9o6YGO9Y2h_EY", "80a378f3beacb7309")

        response = extract_lyrics.get_lyrics(search)
        status_code = status.HTTP_200_OK
        return Response(response, status=status_code)
