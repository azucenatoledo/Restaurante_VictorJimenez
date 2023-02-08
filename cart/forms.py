from django import forms
from django.contrib.auth import get_user_model
from .models import Bebidavariacion, Direccion, ordenIten ,Producto

User = get_user_model()


class AddToCartForm(forms.ModelForm):
    bebida=forms.ModelChoiceField(queryset=Bebidavariacion.objects.none(),label='ELIGE EL TIPO DE TUS BEBIDAS',help_text='Selecione por favor un tipo de bebida',widget=forms.RadioSelect(attrs={'class':'form-check-input'})  )
    cantidad=forms.IntegerField(min_value=1, max_value=100, initial=1,label='ELIGE LA CANTIDAD DE TU PRODUCTO',help_text='Selecione por favor una cantidad mayor o igual a 1',widget=forms.NumberInput(attrs={'class':'form-control'}))
    class Meta:
        model=ordenIten
        fields=['cantidad','bebida']

    def __init__(self, *args, **kwargs):
        product_id=kwargs.pop('producto_id')   
        producto=Producto.objects.get(id=product_id)
        super().__init__(*args, **kwargs)
        self.fields['bebida'].queryset=producto.avalible_bebida.all()
class AdressForm(forms.Form):

    direccion_de_envio_1=forms.CharField(required=False,help_text=' Av. de la Constitución',label='Dirección de envío calle principal')
    direccion_de_envio_2=forms.CharField(required=False,help_text=' 10 de Agosto',label='Dirección de envío calle secundaria')
    ciudad_de_envio=forms.CharField(required=False,help_text='Guayaquil',label='Ciudad de envío')

    direccion_de_facturacion_1=forms.CharField(required=False,help_text=' Av. de la Constitución',label='Dirección de facturación calle principal')
    direccion_de_facturacion_2=forms.CharField(required=False,help_text=' 10 de Agosto',label='Dirección de facturación calle secundaria')
    ciudad_de_facturacion=forms.CharField(required=False,help_text='Guayaquil',label='Ciudad de facturación')

    selecionar_direccion_de_envio=forms.ModelChoiceField(
        Direccion.objects.none(),required=False,label='Seleccione una dirección para el envío de su compra'
    )
    selecionar_direccion_de_facturacion=forms.ModelChoiceField(
        Direccion.objects.none(),required=False,label='Seleccione una dirección para la facturación de su compra'
    )
    def __init__(self,*args,**kwargs):
        user_id = kwargs.pop('user_id')
        super().__init__(*args, **kwargs)
        user = User.objects.get(id=user_id)

        direccion_de_envio_qs=Direccion.objects.filter(
            user=user,
            tipo_de_direccion='S'
        )
        direccion_de_Fcacturacion_qs=Direccion.objects.filter(
            user=user,
            tipo_de_direccion='B'
        )

        self.fields['selecionar_direccion_de_envio'].queryset= direccion_de_envio_qs
        self.fields['selecionar_direccion_de_facturacion'].queryset= direccion_de_Fcacturacion_qs
    def clean(self):
        data = self.cleaned_data
        selecionar_direccion_de_envio=data.get('selecionar_direccion_de_envio',None)
        if selecionar_direccion_de_envio is None:
            if not data.get('direccion_de_envio_1',None):
                self.add_error("direccion_de_envio_1","Por favor complete este campo")

            if not data.get('direccion_de_envio_2',None):
                self.add_error("direccion_de_envio_2","Por favor complete este campo")

            if not data.get('ciudad_de_envio',None):
                self.add_error("ciudad_de_envio","Por favor complete este campo")

        selecionar_direccion_de_facturacion=data.get('selecionar_direccion_de_facturacion',None)
        if selecionar_direccion_de_facturacion is None:
            if not data.get("direccion_de_facturacion_1",None):
                self.add_error("direccion_de_facturacion_1","Por favor complete este campo")

            if not data.get('direccion_de_facturacion_2',None):
                self.add_error("direccion_de_facturacion_2","Por favor complete este campo")

            if not data.get('ciudad_de_envio',None):
                self.add_error("ciudad_de_facturacion","Por favor complete este campo")
 
