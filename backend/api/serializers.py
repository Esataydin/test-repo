from rest_framework import serializers

from .models import Note
from .models import User
from .models import Post, Comment, File, Chat


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id",
                  "email",
                  "name",
                  "student_id",
                  "birthday_date",
                  "phone_number",
                  "profile_picture",
                  "faculty",
                  "department",
                  "field",
                  "graduation_year",
                  "job_title",
                  "working_company",
                  "work_experience",
                  "is_staff_member",
                  "password"
                  ]
        extra_kwargs = {"password": {"write_only": True}}
        
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "author"]
        extra_kwargs = {"author": {"read_only": True}}


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "author", "content", "created_at"]
        extra_kwargs = {"author": {"read_only": True}}

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "author", "post", "content", "created_at"]
        extra_kwargs = {"author": {"read_only": True},
                        "post":{"read_only": True}
                        }
        
class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ["id", "messages", "participant_1", "participant_2", "created_at"]
        extra_kwargs = {"participant_1": {"read_only": True},
                        }