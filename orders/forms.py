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
    