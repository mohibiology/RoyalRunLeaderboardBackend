from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import LeaderboardEntry
from .serializers import LeaderboardEntrySerializer

# POST: Submit Score
class SubmitScoreView(APIView):
    def post(self, request):
        serializer = LeaderboardEntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# GET: Fetch Leaderboard
class LeaderboardView(APIView):
    def get(self, request):
        entries = LeaderboardEntry.objects.all().order_by('-score')[:10]  # Top 10 scores
        serializer = LeaderboardEntrySerializer(entries, many=True)
        return Response(serializer.data)

# POST: Check Username Availability
class UsernameCheckView(APIView):
    def post(self, request):
        username = request.data.get('name', None)
        if not username:
            return Response({'available': False, 'message': 'No username provided.'}, status=400)

        if LeaderboardEntry.objects.filter(name=username).exists():
            return Response({'available': False, 'message': 'Username already taken.'})
        else:
            return Response({'available': True, 'message': 'Username is available.'})
