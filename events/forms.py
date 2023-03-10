from django import forms
from users.models import Person
from .models import Event
CHOIX =(
        ('Musique','Musique'),
        ('Cinema','Cinema'),
        ('Sport','Sport')
    )
class EventForm(forms.Form):
    title = forms.CharField(label="Title")
    description = forms.CharField(label="description" ,
                                  widget=forms.Textarea(attrs={
        'class' :'form-control'
    }))
    image= forms.ImageField(label="Event Image")
    category =forms.ChoiceField(label="category" , choices=CHOIX,
                                widget=forms.RadioSelect())
    nbe_participant = forms.IntegerField(min_value=0)
    evt_date =forms.DateField(
        label="Event Date",
        widget=forms.DateInput(attrs={
            'type' : 'date',
            'class' :'form-control date-input'
        })
    )
    organizer =forms.ModelChoiceField(label="Organizer",queryset=Person.objects.all())
    

class EventModelForm(forms.ModelForm):
    class Meta:
        model =Event
        # fields='__all__'
        fields=['title','description','image','category',
                'nbe_participant','evt_date']
        # exclude=('state')
    evt_date =forms.DateField(
        label="Event Date",
        widget=forms.DateInput(attrs={
            'type' : 'date',
            'class' :'form-control date-input'
        })
    )
    # organizer =forms.ModelChoiceField(label="Organizer",queryset=Person.objects.all())