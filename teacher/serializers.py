# coding=utf-8

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from . import models
from common import serializers as common_serializer


# get teacher serializer

class TeacherSubjectSerializer(serializers.ModelSerializer):
    """教师学科"""

    subject = common_serializer.SubjectSerializer()

    class Meta:
        model = models.TeacherSubjectsShip
        fields = ("id", "subject")


class TeacherTypeSerializer(serializers.ModelSerializer):
    """教师特点"""

    teacher_type = common_serializer.TeacherTypeSerializer()

    class Meta:
        model = models.TeacherTypesShip
        fields = ("id", "teacher_type")


class TeacherSerializer(serializers.ModelSerializer):

    city = common_serializer.CitySerializer()
    school = common_serializer.SchoolSerializer()
    subjects = TeacherSubjectSerializer(many=True)
    teacher_types = TeacherTypeSerializer(many=True)
    follower_count = serializers.IntegerField()

    class Meta:
        model = models.Teacher
        fields = "__all__"


# create teacher

class CreateTeacherSubjectSerializer(serializers.ModelSerializer):
    """创建教师学科"""

    class Meta:
        model = models.TeacherSubjectsShip
        fields = ("id", "subject")


class CreateTeacherTypeSerializer(serializers.ModelSerializer):
    """创建教师特点"""

    class Meta:
        model = models.TeacherTypesShip
        fields = ("id", "teacher_type")


class CreateTeacherSerializer(serializers.ModelSerializer):
    """
        创建老师
    """

    subjects = serializers.ListField(required=True)
    teacher_types = serializers.ListField(required=True)

    class Meta:
        model = models.Teacher
        fields = "__all__"


# 修改教师

class UpdateTeacherSerializer(serializers.ModelSerializer):
    """
        修改教师
    """

    phone = serializers.CharField(required=False)
    city = serializers.CharField(required=False)
    school = serializers.CharField(required=False)
    subjects = CreateTeacherSubjectSerializer(required=False, many=True)
    teacher_types = CreateTeacherTypeSerializer(required=False, many=True)

    class Meta:
        model = models.Teacher
        fields = "__all__"

# 教师被收藏序列化

class CreateTeacherFollowerSerializer(serializers.ModelSerializer):
    """
        收藏 教师
    """

    class Meta:
        model = models.TeacherFollowers
        fields = '__all__'