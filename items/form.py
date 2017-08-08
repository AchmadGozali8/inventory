from django.forms import ModelForm, TextInput, Textarea, Select 
from models import Item

text_input = TextInput(attrs={'class': 'form-control', 'type': 'text'})

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'types', 'quantity', 'description', 'location')
        widgets = {
            'name': text_input,
            'types': Select(attrs={'class': 'form-control show-tick'}),
            'quantity': text_input,
            'location': text_input,
            'description': Textarea(attrs={'cols': "30", 'rows': "5",\
                        'class': "form-control no-resize"})

        }

class ItemUpdateForm(ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'types', 'description', 'location')
        widgets = {
            'name': text_input,
            'types': Select(attrs={'class': 'form-control show-tick'}),
            'description': Textarea(attrs={'cols': "30", 'rows': "5",\
                        'class': "form-control no-resize"}),
            'location': text_input
        }
        print ModelForm
