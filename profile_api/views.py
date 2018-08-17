from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """
    Dummy api view for framework test
    """
    def get(self, request, format=None):
        """
        Get method implementation for api view
        :return: json
        """
        an_apiview = [
            "Uses http metods as function (get, post, put, delete)",
            "It is similar to tradtional django view",
            "Gives you the most control over your logic",
        ]

        return Response({"data":an_apiview, "message": "Hello"})

