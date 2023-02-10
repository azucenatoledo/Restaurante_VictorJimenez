from django import forms
from django.contrib.auth import get_user_model
from .models import Bebidavariacion, Direccion, ordenIten, Producto

User = get_user_model()


class AddToCartForm(forms.ModelForm):
    class Meta:
        model = ordenIten
        fields = ['cantidad', 'bebida']
        queryset = {
            'bebida': Bebidavariacion.objects.none(),
        }
        labels = {
            'cantidad': 'ELIGA LA CANTIDAD DE SU PRODUCTO',
            'bebida': 'ELIGA EL TIPO DE SU BEBIDA',
        }
        help_texts = {
            'cantidad': 'Selecione por favor una cantidad mayor o igual a 1',
            'bebida': 'Selecione por favor un tipo de bebida',
        }

        widgets = {
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'bebida': forms.RadioSelect(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        product_id = kwargs.pop('producto_id')
        producto = Producto.objects.get(id=product_id)
        super().__init__(*args, **kwargs)
        self.fields['bebida'].queryset = producto.avalible_bebida.all()


class AdressForm(forms.Form):
    direccion_de_envio_1 = forms.CharField(required=False,
                                           label='Dirección de envío calle principal',
                                           widget=forms.TextInput(
                                               attrs={'placeholder': ' Ejemplo: Av. de la Constitución'}))

    direccion_de_envio_2 = forms.CharField(required=False,
                                           label='Dirección de envío calle secundaria',
                                           widget=forms.TextInput(attrs={'placeholder': ' Ejemplo: 10 de Agosto'}))
    ciudad_de_envio = forms.CharField(required=False, label='Ciudad de envío',
                                      widget=forms.TextInput(attrs={'placeholder': ' Ejemplo: Guayaquil'}))

    direccion_de_facturacion_1 = forms.CharField(required=False,
                                                 label='Dirección de facturación calle principal',
                                                 widget=forms.TextInput(
                                                     attrs={'placeholder': ' Ejemplo: Av. 8 de Diciembre'}))
    direccion_de_facturacion_2 = forms.CharField(required=False,
                                                 label='Dirección de facturación calle secundaria',
                                                 widget=forms.TextInput(attrs={'placeholder': ' Ejemplo: Colon'}))
    ciudad_de_facturacion = forms.CharField(required=False, label='Ciudad de facturación',
                                            widget=forms.TextInput(attrs={'placeholder': ' Ejemplo: Guayaquil'}))

    selecionar_direccion_de_envio = forms.ModelChoiceField(
        Direccion.objects.none(), required=False, label='Seleccione una dirección para el envío de su compra'
    )
    selecionar_direccion_de_facturacion = forms.ModelChoiceField(
        Direccion.objects.none(), required=False, label='Seleccione una dirección para la facturación de su compra'
    )

    def __init__(self, *args, **kwargs):
        user_id = kwargs.pop('user_id')
        super().__init__(*args, **kwargs)
        user = User.objects.get(id=user_id)

        direccion_de_envio_qs = Direccion.objects.filter(
            user=user,
            tipo_de_direccion='S'
        )
        direccion_de_Fcacturacion_qs = Direccion.objects.filter(
            user=user,
            tipo_de_direccion='B'
        )

        self.fields['selecionar_direccion_de_envio'].queryset = direccion_de_envio_qs
        self.fields['selecionar_direccion_de_facturacion'].queryset = direccion_de_Fcacturacion_qs

    def clean(self):
        data = self.cleaned_data
        selecionar_direccion_de_envio = data.get('selecionar_direccion_de_envio', None)
        if selecionar_direccion_de_envio is None:
            if not data.get('direccion_de_envio_1', None):
                self.add_error("direccion_de_envio_1", "Por favor complete este campo")

            if not data.get('direccion_de_envio_2', None):
                self.add_error("direccion_de_envio_2", "Por favor complete este campo")

            if not data.get('ciudad_de_envio', None):
                self.add_error("ciudad_de_envio", "Por favor complete este campo")

        selecionar_direccion_de_facturacion = data.get('selecionar_direccion_de_facturacion', None)
        if selecionar_direccion_de_facturacion is None:
            if not data.get("direccion_de_facturacion_1", None):
                self.add_error("direccion_de_facturacion_1", "Por favor complete este campo")

            if not data.get('direccion_de_facturacion_2', None):
                self.add_error("direccion_de_facturacion_2", "Por favor complete este campo")

            if not data.get('ciudad_de_envio', None):
                self.add_error("ciudad_de_facturacion", "Por favor complete este campo")
