from rest_framework import serializers

from applications.bills.models import Bill


class BillSerializer(serializers.ModelSerializer):
    date = serializers.DateField(format="%d.%m.%Y", input_formats=['%d.%m.%Y', 'iso-8601'])

    class Meta:
        model = Bill
        fields = '__all__'

    def validate(self, validated_data):
        service = validated_data.get('service')
        if (service == '-'):
            raise serializers.ValidationError('Service field cannot be empty!')
        return validated_data

    def create(self, validated_data):
        bill = Bill.objects.create(**validated_data)
        return bill


class BillDocSerializer(serializers.Serializer):
    excel_file = serializers.FileField()

    def create(self, attrs):
        import pandas as pd
        file_xlsx = attrs.get('excel_file')
        excel_data = pd.read_excel(file_xlsx)
        data_xlsx = pd.DataFrame(excel_data, columns=['client_name', 'client_org', '№', 'sum', 'date', 'service'])
        for i in data_xlsx.iterrows():
            data = {
                'client_name': i[1].client_name,
                'client_org': i[1].client_org,
                'bill_num': i[1]['№'],
                'bill_sum': i[1]['sum'],
                'date': i[1].date.strftime('%d.%m.%Y'),
                'service': i[1].service
            }
            serializer = BillSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
            else:
                continue
        return attrs
