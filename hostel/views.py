# views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import RoomDetails, Hosteller, RentHistory
from .forms import RoomDetailsForm, HostellerForm, RentHistoryForm

# RoomDetails Views
def room_details_list(request):
    rooms = RoomDetails.objects.all()
    return render(request, 'room_details_list.html', {'rooms': rooms})

def room_details_create(request):
    if request.method == 'POST':
        form = RoomDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('room_details_list')
    else:
        form = RoomDetailsForm()
    return render(request, 'room_details_form.html', {'form': form})

def room_details_update(request, pk):
    room = get_object_or_404(RoomDetails, pk=pk)
    if request.method == 'POST':
        form = RoomDetailsForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('room_details_list')
    else:
        form = RoomDetailsForm(instance=room)
    return render(request, 'room_details_form.html', {'form': form})

def room_details_delete(request, pk):
    room = get_object_or_404(RoomDetails, pk=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('room_details_list')
    return render(request, 'room_details_confirm_delete.html', {'room': room})

# Hosteller Views
def hosteller_list(request):
    hostellers = Hosteller.objects.all()
    return render(request, 'hosteller_list.html', {'hostellers': hostellers})

def hosteller_create(request):
    if request.method == 'POST':
        form = HostellerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hosteller_list')
    else:
        form = HostellerForm()
    return render(request, 'hosteller_form.html', {'form': form})

def hosteller_update(request, pk):
    hosteller = get_object_or_404(Hosteller, pk=pk)
    if request.method == 'POST':
        form = HostellerForm(request.POST, instance=hosteller)
        if form.is_valid():
            form.save()
            return redirect('hosteller_list')
    else:
        form = HostellerForm(instance=hosteller)
    return render(request, 'hosteller_form.html', {'form': form})

def hosteller_delete(request, pk):
    hosteller = get_object_or_404(Hosteller, pk=pk)
    if request.method == 'POST':
        hosteller.delete()
        return redirect('hosteller_list')
    return render(request, 'hosteller_confirm_delete.html', {'hosteller': hosteller})

# RentHistory Views
def rent_history_list(request):
    histories = RentHistory.objects.all()
    return render(request, 'rent_history_list.html', {'histories': histories})

def rent_history_create(request):
    if request.method == 'POST':
        form = RentHistoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rent_history_list')
    else:
        form = RentHistoryForm()
    return render(request, 'rent_history_form.html', {'form': form})

def rent_history_update(request, pk):
    history = get_object_or_404(RentHistory, pk=pk)
    if request.method == 'POST':
        form = RentHistoryForm(request.POST, instance=history)
        if form.is_valid():
            form.save()
            return redirect('rent_history_list')
    else:
        form = RentHistoryForm(instance=history)
    return render(request, 'rent_history_form.html', {'form': form})

def rent_history_delete(request, pk):
    history = get_object_or_404(RentHistory, pk=pk)
    if request.method == 'POST':
        history.delete()
        return redirect('rent_history_list')
    return render(request, 'rent_history_confirm_delete.html', {'history': history})
