from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import User, Note
from .serializers import UserSerializer, NoteSerializer

from .models import Post, Comment, Chat
from .serializers import PostSerializer, CommentSerializer, ChatSerializer

# Create your views here.

class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.all()
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)


class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.all()


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserList(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny] #TODO Change to IsAuthenticated and make it cool buddy cmon

    def get_queryset(self):
        return User.objects.all()
    
    
class PostListCreate(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Post.objects.all()
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)

class PostDelete(generics.DestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Post.objects.all()
    
    
    
class CommentListCreate(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Comment.objects.all()
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user, post= Post.objects.all()[0])
        else:
            print(serializer.errors)

    
class CommentDelete(generics.DestroyAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Comment.objects.all()
    
    
class ChatListCreate(generics.ListCreateAPIView):
    serializer_class = ChatSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        user = self.request.user
        return Chat.objects.all()
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(participant_1=self.request.user, participant_2=self.request.user)
        else:
            print(serializer.errors)