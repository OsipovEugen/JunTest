from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.utils import timezone
from like.models import Like
import datetime as DT
from django.db.models import Count
from authentication.models import User



from like.models import Like

class EugenView(APIView):
	permission_classes = [IsAuthenticated]
	def get(self, request):
		return Response({'key':'JWT token was successfully accepted '})


class StatView(APIView):
	permission_classes = [AllowAny]

	def get(self, request):
		date_from = DT.datetime.strptime(request.GET.get('date_from'), '%Y-%m-%d').date()
		date_to = DT.datetime.strptime(request.GET.get('date_to'), '%Y-%m-%d').date()
		amount_likes = Like.objects.filter(date__range=[date_from, date_to])
		likes = Like.objects.filter(date__range=[date_from, date_to]).values('date').annotate(cnt=Count('id'))
		return Response({'Amount of Likes':amount_likes.count(),
						'likes':likes,
			})


class LastLogin(APIView):
	permission_classes = [AllowAny]
	def get(self, request):
		user = User.objects.get(email=request.user.email)
		last_login = user.last_login
		return Response({
			'Last_login':last_login
			})