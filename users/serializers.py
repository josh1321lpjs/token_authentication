from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import gettext as _
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer): #Depende del modelo 
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 8}
        }
    #created user validation
    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

class AuthTokenSerializer(serializers.Serializer): #Hereda de Serializer para la validadción 
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=255, trim_whitespace=False) #Si es True, se recortan los espacios en blanco iniciales y finales

    def validate(self, attrs): #sobreescribimos el metodo validate de Zerializer
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )

        if not user:
            msg = _('Unable to authenticate with the provided credentials')
            raise serializers.ValidationError(msg, code='authorization')
        
        attrs['user'] = user

        return attrs