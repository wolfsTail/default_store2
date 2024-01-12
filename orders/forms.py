# class CreateOrderForm(forms.Form):
#     first_name = forms.CharField(
#         widget=forms.TextInput(
#             attrs={
#                 "class": "form-control",
#                 "placeholder": "Введите Ваше имя",
#             }
#         )
#     )
#     last_name = forms.CharField(
#         widget=forms.TextInput(
#             attrs={
#                 "class": "form-control",
#                 "placeholder": "Введите Вашу фамилию",
#             }
#         )
#     )
#     phone_number = forms.CharField(
#         widget=forms.TextInput(
#             attrs={
#                 "class": "form-control",
#                 "placeholder": "Актуальный номер телефона",
#             }
#         )
#     )
#     delivery_address = forms.CharField(        
#         widget=forms.Textarea(
#             attrs={
#                 "class": "form-control",
#                 "id": "delivery_address",
#                 "rows": 2,
#                 "placeholder": "Желаемый адрес доставки",
#             }
#         )
#     )
#     requires_delivery = forms.ChoiceField(
#         widget=forms.RadioSelect(),
#         choices=[
#             ("0", False),
#             ("1", True),
#         ],
#         initial=0,
#     )
#     payment_on = forms.ChoiceField(
#         widget=forms.RadioSelect(),
#         choices=[
#             ("0", False),
#             ("1", True),
#             ],
#         initial=0,
#     )
#  front use in back
import re
from django import forms


class CreateOrderForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()
    delivery_address = forms.CharField(required=False)
    requires_delivery = forms.ChoiceField(choices=[
                     ("0", False),
                     ("1", True),
                    ],)
    payment_on = forms.ChoiceField(choices=[
             ("0", False),
             ("1", True),
             ],)
    
    def clear_phone_number(self):
        phone_number = self.cleaned_data["phone_number"]
        phone_number = phone_number.replace("-", "").replace(" ", "")
        if not phone_number.isdigit():
            raise forms.ValidationError("Номер телефона должен содержать только цифры")        
        pattern = re.compile(r'^\d{10}$')
        if not pattern.match(phone_number):
            raise forms.ValidationError("Неверный формат телефонного номера")
        return phone_number


    