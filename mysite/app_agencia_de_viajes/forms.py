from django import forms
from .models import Destino, Paquete_Turistico, Cliente_Viajes, Agente_Viajes, Reserva_Viaje, Vuelo, Alojamiento

class FormularioDestino(forms.ModelForm):
    class Meta:
        model = Destino
        fields = '__all__'
        widgets = {
            'id_destino': forms.NumberInput(attrs={'class': 'form-control'}),
            'nombre_destino': forms.TextInput(attrs={'class': 'form-control'}),
            'pais': forms.TextInput(attrs={'class': 'form-control'}),
            'continente': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'atracciones_principales': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'clima': forms.TextInput(attrs={'class': 'form-control'}),
            'divisa_local': forms.TextInput(attrs={'class': 'form-control'}),
        }

class FormularioPaqueteTuristico(forms.ModelForm):
    class Meta:
        model = Paquete_Turistico
        fields = '__all__'
        widgets = {
            'id_paquete': forms.NumberInput(attrs={'class': 'form-control'}),
            'nombre_paquete': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'fecha_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'id_destino': forms.Select(attrs={'class': 'form-control'}),
            'precio_adulto': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio_nino': forms.NumberInput(attrs={'class': 'form-control'}),
            'cupo_maximo': forms.NumberInput(attrs={'class': 'form-control'}),
            'incluye_vuelo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'incluye_alojamiento': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class FormularioCliente(forms.ModelForm):
    class Meta:
        model = Cliente_Viajes
        fields = '__all__'
        widgets = {
            'id_cliente': forms.NumberInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'preferencias_viaje': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'pasaporte': forms.TextInput(attrs={'class': 'form-control'}),
        }

class FormularioAgenteViajes(forms.ModelForm):
    class Meta:
        model = Agente_Viajes
        fields = '__all__'
        widgets = {
            'id_agente': forms.NumberInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'dni': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_contratacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'salario_base': forms.NumberInput(attrs={'class': 'form-control'}),
            'comision_porcentaje': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class FormularioReserva(forms.ModelForm):
    class Meta:
        model = Reserva_Viaje
        fields = '__all__'
        widgets = {
            'id_reserva': forms.NumberInput(attrs={'class': 'form-control'}),
            'id_paquete': forms.Select(attrs={'class': 'form-control'}),
            'id_cliente': forms.Select(attrs={'class': 'form-control'}),
            'num_adultos': forms.NumberInput(attrs={'class': 'form-control'}),
            'num_ninos': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_pagado': forms.NumberInput(attrs={'class': 'form-control'}),
            'estado_reserva': forms.Select(choices=[('Pendiente', 'Pendiente'), ('Confirmada', 'Confirmada'), ('Cancelada', 'Cancelada')], attrs={'class': 'form-control'}),
            'fecha_vencimiento_pago': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'id_agente_venta': forms.Select(attrs={'class': 'form-control'}),
        }

class FormularioVuelo(forms.ModelForm):
    class Meta:
        model = Vuelo
        fields = '__all__'
        widgets = {
            'id_vuelo': forms.NumberInput(attrs={'class': 'form-control'}),
            'num_vuelo': forms.TextInput(attrs={'class': 'form-control'}),
            'aerolinea': forms.TextInput(attrs={'class': 'form-control'}),
            'origen': forms.TextInput(attrs={'class': 'form-control'}),
            'destino': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_salida': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'hora_salida': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'fecha_llegada': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'hora_llegada': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'precio_clase_economica': forms.NumberInput(attrs={'class': 'form-control'}),
            'asientos_disponibles': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class FormularioAlojamiento(forms.ModelForm):
    class Meta:
        model = Alojamiento
        fields = '__all__'
        widgets = {
            'id_alojamiento': forms.NumberInput(attrs={'class': 'form-control'}),
            'nombre_hotel': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_alojamiento': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
            'pais': forms.TextInput(attrs={'class': 'form-control'}),
            'estrellas': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio_noche_estandar': forms.NumberInput(attrs={'class': 'form-control'}),
            'servicios_incluidos': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
        }
