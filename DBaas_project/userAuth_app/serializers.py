from userAuth_app.models import User
from rest_framework import serializers


class userAuthSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'password', 'date_joined', 'last_login', 'is_active']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.role = validated_data.get('role', instance.role)
        password = validated_data.get('password')
        if password:
            instance.set_password(password)
        instance.save()
        return instance

class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['role']
    
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ['id', 'username', 'email', 'role']  # Include fields you want to list
        fields = ['id', 'username', 'email', 'role']  # Include these fields


class ResetPasswordSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    new_password = serializers.CharField(write_only=True, max_length=128)
    
    def validate_username(self, value):
        if not User.objects.filter(username=value).exists():
            raise serializers.ValidationError("User with this username does not exist.")
        return value

    def validate(self, data):
        # You can add additional validation here if needed
        return data


        


