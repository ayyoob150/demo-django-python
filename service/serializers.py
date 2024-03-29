from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.Serializer):
    id= serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, allow_blank=True, max_length=50)
    price = serializers.CharField(required=False, allow_blank=True,max_length=50)
    description = serializers.CharField(required=False, allow_blank=True)
    
    def create(self, validated_data):
        return Product.objects.create(**validated_data)
    
    def update(self,instance , validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.price = validated_data.get('price',instance.price)
        instance.description = validated_data.get('description',instance.description)
        instance.save()
        return instance
        
        

# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Snippet.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance
