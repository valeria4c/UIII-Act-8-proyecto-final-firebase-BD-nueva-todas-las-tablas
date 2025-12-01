from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from .models import (
    Destino, Paquete_Turistico, Cliente_Viajes, Agente_Viajes, Reserva_Viaje, Vuelo, Alojamiento
)
from .forms import (
    FormularioDestino, FormularioPaqueteTuristico, FormularioCliente, 
    FormularioAgenteViajes, FormularioReserva, FormularioVuelo, FormularioAlojamiento
)

# ==========================================
# VISTA DE INICIO
# ==========================================
class HomeView(TemplateView):
    template_name = 'app_agencia_de_viajes/home.html'

# ==========================================
# VISTAS PARA DESTINO
# ==========================================
class DestinoListView(ListView):
    model = Destino
    template_name = 'app_agencia_de_viajes/destino/ver.html'
    context_object_name = 'destinos'

class DestinoCreateView(CreateView):
    model = Destino
    form_class = FormularioDestino
    template_name = 'app_agencia_de_viajes/destino/agregar.html'
    success_url = reverse_lazy('ver_destinos')

class DestinoUpdateView(UpdateView):
    model = Destino
    form_class = FormularioDestino
    template_name = 'app_agencia_de_viajes/destino/actualizar.html'
    success_url = reverse_lazy('ver_destinos')

class DestinoDeleteView(DeleteView):
    model = Destino
    template_name = 'app_agencia_de_viajes/destino/eliminar.html'
    success_url = reverse_lazy('ver_destinos')

# ==========================================
# VISTAS PARA PAQUETE TURÍSTICO
# ==========================================
class PaqueteTuristicoListView(ListView):
    model = Paquete_Turistico
    template_name = 'app_agencia_de_viajes/paquete_turistico/ver.html'
    context_object_name = 'paquetes'

class PaqueteTuristicoCreateView(CreateView):
    model = Paquete_Turistico
    form_class = FormularioPaqueteTuristico
    template_name = 'app_agencia_de_viajes/paquete_turistico/agregar.html'
    success_url = reverse_lazy('ver_paquetes_turisticos')

class PaqueteTuristicoUpdateView(UpdateView):
    model = Paquete_Turistico
    form_class = FormularioPaqueteTuristico
    template_name = 'app_agencia_de_viajes/paquete_turistico/actualizar.html'
    success_url = reverse_lazy('ver_paquetes_turisticos')

class PaqueteTuristicoDeleteView(DeleteView):
    model = Paquete_Turistico
    template_name = 'app_agencia_de_viajes/paquete_turistico/eliminar.html'
    success_url = reverse_lazy('ver_paquetes_turisticos')

# ==========================================
# VISTAS PARA CLIENTE
# ==========================================
class ClienteListView(ListView):
    model = Cliente_Viajes
    template_name = 'app_agencia_de_viajes/cliente_viajes/ver.html'
    context_object_name = 'clientes'

class ClienteCreateView(CreateView):
    model = Cliente_Viajes
    form_class = FormularioCliente
    template_name = 'app_agencia_de_viajes/cliente_viajes/agregar.html'
    success_url = reverse_lazy('ver_clientes')

class ClienteUpdateView(UpdateView):
    model = Cliente_Viajes
    form_class = FormularioCliente
    template_name = 'app_agencia_de_viajes/cliente_viajes/actualizar.html'
    success_url = reverse_lazy('ver_clientes')

class ClienteDeleteView(DeleteView):
    model = Cliente_Viajes
    template_name = 'app_agencia_de_viajes/cliente_viajes/eliminar.html'
    success_url = reverse_lazy('ver_clientes')

# ==========================================
# VISTAS PARA AGENTE DE VIAJES
# ==========================================
class AgenteViajesListView(ListView):
    model = Agente_Viajes
    template_name = 'app_agencia_de_viajes/agente_viajes/ver.html'
    context_object_name = 'agentes'

class AgenteViajesCreateView(CreateView):
    model = Agente_Viajes
    form_class = FormularioAgenteViajes
    template_name = 'app_agencia_de_viajes/agente_viajes/agregar.html'
    success_url = reverse_lazy('ver_agentes')

class AgenteViajesUpdateView(UpdateView):
    model = Agente_Viajes
    form_class = FormularioAgenteViajes
    template_name = 'app_agencia_de_viajes/agente_viajes/actualizar.html'
    success_url = reverse_lazy('ver_agentes')

class AgenteViajesDeleteView(DeleteView):
    model = Agente_Viajes
    template_name = 'app_agencia_de_viajes/agente_viajes/eliminar.html'
    success_url = reverse_lazy('ver_agentes')

# ==========================================
# VISTAS PARA RESERVA
# ==========================================
class ReservaListView(ListView):
    model = Reserva_Viaje
    template_name = 'app_agencia_de_viajes/reserva_viaje/ver.html'
    context_object_name = 'reservas'

class ReservaCreateView(CreateView):
    model = Reserva_Viaje
    form_class = FormularioReserva
    template_name = 'app_agencia_de_viajes/reserva_viaje/agregar.html'
    success_url = reverse_lazy('ver_reservas')

class ReservaUpdateView(UpdateView):
    model = Reserva_Viaje
    form_class = FormularioReserva
    template_name = 'app_agencia_de_viajes/reserva_viaje/actualizar.html'
    success_url = reverse_lazy('ver_reservas')

class ReservaDeleteView(DeleteView):
    model = Reserva_Viaje
    template_name = 'app_agencia_de_viajes/reserva_viaje/eliminar.html'
    success_url = reverse_lazy('ver_reservas')

# ==========================================
# VISTAS PARA VUELO
# ==========================================
class VueloListView(ListView):
    model = Vuelo
    template_name = 'app_agencia_de_viajes/vuelo/ver.html'
    context_object_name = 'vuelos'

class VueloCreateView(CreateView):
    model = Vuelo
    form_class = FormularioVuelo
    template_name = 'app_agencia_de_viajes/vuelo/agregar.html'
    success_url = reverse_lazy('ver_vuelos')

class VueloUpdateView(UpdateView):
    model = Vuelo
    form_class = FormularioVuelo
    template_name = 'app_agencia_de_viajes/vuelo/actualizar.html'
    success_url = reverse_lazy('ver_vuelos')

class VueloDeleteView(DeleteView):
    model = Vuelo
    template_name = 'app_agencia_de_viajes/vuelo/eliminar.html'
    success_url = reverse_lazy('ver_vuelos')

# ==========================================
# VISTAS PARA ALOJAMIENTO
# ==========================================
class AlojamientoListView(ListView):
    model = Alojamiento
    template_name = 'app_agencia_de_viajes/alojamiento/ver.html'
    context_object_name = 'alojamientos'

class AlojamientoCreateView(CreateView):
    model = Alojamiento
    form_class = FormularioAlojamiento
    template_name = 'app_agencia_de_viajes/alojamiento/agregar.html'
    success_url = reverse_lazy('ver_alojamientos')

class AlojamientoUpdateView(UpdateView):
    model = Alojamiento
    form_class = FormularioAlojamiento
    template_name = 'app_agencia_de_viajes/alojamiento/actualizar.html'
    success_url = reverse_lazy('ver_alojamientos')

class AlojamientoDeleteView(DeleteView):
    model = Alojamiento
    template_name = 'app_agencia_de_viajes/alojamiento/eliminar.html'
    success_url = reverse_lazy('ver_alojamientos')
