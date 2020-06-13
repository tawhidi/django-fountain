from django.db import models
from django.forms import ModelForm
from django.forms.widgets import TextInput


class Pen(models.Model):
    brand_name = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)
    color      = models.CharField(max_length=7)
    date_purchase = models.DateField()

    NIB_SIZES = (
        ('B','Broad'),
        ('M','Medium'),
        ('F','Fine'),
        ('EF','Extra Fine')
    )

    nib_size = models.CharField(max_length=2,choices=NIB_SIZES)

    def __str__(self):
        return self.brand_name

class PenForm(ModelForm):
    class Meta:
        model = Pen
        fields = '__all__'

        widgets = {
            'color':TextInput(attrs={'type':'color'})
        }

class Ink(models.Model):
    brand_name = models.CharField(max_length=50)
    color = models.CharField(max_length=7)
    color_name = models.CharField(max_length=50)
    rating = models.IntegerField()

class InkForm(ModelForm):
    class Meta:
        model = Ink
        fields = '__all__'

        widgets = {
            'color':TextInput(attrs={'type':'color'})
        }
    












