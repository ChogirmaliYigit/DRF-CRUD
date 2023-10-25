from rest_framework import serializers
from .models import Category, Task
from django.utils.text import slugify


class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.ReadOnlyField()

    def create(self, validated_data):
        validated_data['slug'] = slugify(validated_data['title'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data['slug'] = slugify(validated_data['title'])
        return super().update(instance, validated_data)

    class Meta:
        model = Category
        fields = (
            "id",
            "title",
            "slug",
        )


class TaskSerializer(serializers.ModelSerializer):
    slug = serializers.ReadOnlyField()

    def create(self, validated_data):
        validated_data['slug'] = slugify(validated_data['title'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data['slug'] = slugify(validated_data['title'])
        return super().update(instance, validated_data)

    class Meta:
        model = Task
        fields = (
            "id",
            "title",
            "slug",
            "description",
            "status",
            "priority",
            "assignment",
            "category",
        )
