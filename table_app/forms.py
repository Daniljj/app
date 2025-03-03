from django import forms
from .models import TableData, Filter
from django.core.exceptions import ValidationError
import pandas as pd
from django.core.validators import FileExtensionValidator

class TableUploadForm(forms.ModelForm):
    class Meta:
        model = TableData
        fields = ['sheet_name', 'file']
        widgets = {
            'sheet_name': forms.TextInput(attrs={'class': 'form-control'}),
            'file': forms.FileInput(attrs={'class': 'form-control'})
        }

class FilterForm(forms.ModelForm):
    class Meta:
        model = Filter
        fields = ['contractor', 'payment_purpose', 'internal_purpose']
        widgets = {
            'contractor': forms.TextInput(attrs={'class': 'form-control'}),
            'payment_purpose': forms.TextInput(attrs={'class': 'form-control'}),
            'internal_purpose': forms.Select(attrs={'class': 'form-control'})
        }

    def clean(self):
        cleaned_data = super().clean()
        contractor = cleaned_data.get('contractor')
        payment_purpose = cleaned_data.get('payment_purpose')
        internal_purpose = cleaned_data.get('internal_purpose')

        # Проверяем, что заполнено хотя бы два поля, включая internal_purpose
        if internal_purpose:
            if not (contractor or payment_purpose):
                raise forms.ValidationError(
                    'Необходимо заполнить либо поле "Контрагент", либо "Банковское назначение платежа" '
                    'вместе с "Внутренним назначением"'
                )
        elif contractor or payment_purpose:
            raise forms.ValidationError(
                'Поле "Внутреннее назначение" обязательно при заполнении других полей'
            )

        return cleaned_data

class ReportFilterForm(forms.Form):
    start_date = forms.DateField(
        label='Начальная дата',
        required=False,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    end_date = forms.DateField(
        label='Конечная дата',
        required=False,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    currency = forms.ChoiceField(
        label='Валюта',
        required=False,
        choices=[('', 'Все')] + [
            ('RUB', 'RUB'),
            ('USD', 'USD'),
            ('EUR', 'EUR'),
            ('GBP', 'GBP'),
            ('JPY', 'JPY'),
            ('CNH', 'CNH')
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )

class TableDataAppendForm(forms.Form):
    file = forms.FileField(
        label='Файл с данными',
        validators=[
            FileExtensionValidator(allowed_extensions=['xlsx', 'xls', 'csv', 'ods'])
        ]
    )
    
    def clean_file(self):
        file = self.cleaned_data['file']
        try:
            file_extension = file.name.split('.')[-1].lower()
            
            if file_extension == 'csv':
                df = pd.read_csv(file)
            elif file_extension == 'ods':
                df = pd.read_excel(file, engine='odf')
            else:
                df = pd.read_excel(file)
            
            # Проверка обязательных колонок
            required_columns = ["Дата", "Дебит", "Кредит", "Банковское назначение платежа"]
            missing_columns = [col for col in required_columns if col not in df.columns]
            if missing_columns:
                raise ValidationError(f"В файле отсутствуют обязательные колонки: {', '.join(missing_columns)}")
            
            if df.empty:
                raise ValidationError("Файл не содержит данных")
                
            return file
        except Exception as e:
            raise ValidationError(f"Ошибка при чтении файла: {str(e)}") 