# forms.py
from django import forms

class ExcelFileUploadForm(forms.Form):
    excel_file = forms.FileField(label='Select an Excel file')

