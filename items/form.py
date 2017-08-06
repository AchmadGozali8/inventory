from django.forms import ModelForm, TextInput, Textare 
from models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'type', 'quantity', 'description', 'location')
        text_input = TextInput(attrs={'class': 'form-input', 'type': 'text})'
        widgets = {
            'name': text_input,
            'type': Select(attrs={'class': 'form-control show-tick'}),
            'quantity': text_input,
            'location': text_input,
            'description': TextArea(attrs={'cols'="30", 'rows'="5", \
                                           'class'="form-control no-resize"}
        }
