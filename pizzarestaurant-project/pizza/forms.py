from django import forms
from .models import Pizza, Size

# class PizzaForms(forms.Form):
#     # The below line introduces a multi select check box for toppings.
#     # toppings = forms.MultipleChoiceField(choices=[
#     #     ('cheese','Cheese'),('olives','Olives'),
#     #     ('jalapeno','Jalapeno'),
#     #     ('onion','Onion')], widget=forms.CheckboxSelectMultiple)
#     topping1 = forms.CharField(label="Topping1", max_length=100)
#     topping2 = forms.CharField(label="Topping2", max_length=100)
#     size = forms.ChoiceField(label="Size", choices=[('Small','Small'),('Medium','Medium'),('Large','Large')])

class PizzaForm(forms.ModelForm):
    class Meta:
            model = Pizza
            fields = ['topping1', 'topping2', 'size']
            labels = {
            "topping1": "Topping 1",
            "topping2": "Topping 2",
            }
            # we can include widgets in the model forms as well, as shown below
            # widgets = {'topping1':forms.Textarea}

class MultiplePizzaForm(forms.Form):
    number = forms.IntegerField(min_value=2, max_value=6)