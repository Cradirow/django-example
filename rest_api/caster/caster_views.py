from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CasterSerializer
from .models import Caster
import requests, json

class CasterList(APIView):
	def get(self, request, format=None):
		casters = Caster.objects.all()
		serializer = CasterSerializer(casters, many=True)
		return Response(serializer.data)

	"""
	def post(self, request, format=None):
		msg = {
			"responseType": "inChannel",
			"text": "Hello!"
		}
		return Response(msg)
	"""

	def post(self, request, format=None):
		channelId = request.data['channelId']
		tenantDomain = request.data['tenantDomain']
		triggerId = request.data['triggerId']
		cmdToken = request.data['cmdToken']

		dialogUrl = f"https://{tenantDomain}/messenger/api/channels/{channelId}/dialogs"
		print('url: ' + dialogUrl)	

		msg = {
			    "token": cmdToken,
			    "triggerId": triggerId,
			    "callbackId": "guide-a1b2c3",
			    "dialog": {
			        "callbackId": "setup",
			        "title": "Guide Dialog",
			        "submitLabel": "Send",
				"elements": [
			            {
			                "type": "text",
			                "subtype": "number",
			                "label": "Page Number",
			                "name": "page",
			                "value": "0",
			                "minLength": "1",
			                "maxLength": "2",
			                "placeholder": "0 ~ 50",
			                "hint": "Must in 0 ~ 50"
			            },
			            {
			                "type": "textarea",
			                "label": "Note",
			                "name": "note",
			                "optional": "true"
			            },
			            {
			                "type": "select",
			                "label": "Is this important?",
			                "name": "important",
			                "value": "false",
			                "options": [
			                    {
			                        "label": "Yes",
			                        "value": "true"
			                    },
			                    {
			                        "label": "No",
			                        "value": "false"
			                    }
			                ]
			            }
			        ]
			}
		}
		headers = {"token": cmdToken}
		response = requests.post(url=dialogUrl, headers=headers, json=msg)
		# print(response.headers)
		return Response()
	
