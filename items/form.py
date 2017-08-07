from django.forms import ModelForm, TextInput, Textarea, Select 
from models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'types', 'quantity', 'description', 'location')
        text_input = TextInput(attrs={'class': 'form-control', 'type': 'text'})
        widgets = {
            'name': text_input,
            'types': Select(attrs={'class': 'form-control show-tick'}),
            'quantity': text_input,
            'location': text_input,
            'description': Textarea(attrs={'cols': "30", 'rows': "5",\
                        'class': "form-control no-resize"})

        }
