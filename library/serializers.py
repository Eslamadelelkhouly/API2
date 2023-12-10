class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class bookSerializers(serializers.ModelSerializer):
    class Meta:
        model = book
        fields = '__all__'