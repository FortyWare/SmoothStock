from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from tasks.views import *
from contacts.views import *
from .models import Inventory
from .forms import AddInventoryForm, UpdateInventoryForm

# Create your views here.
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def inventory_list(request):
    inventories = Inventory.objects.all()
    context = {
        "inventories": inventories
    }
    return render(request, 'inventory_list.html', context=context)

@login_required
def per_product_view(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    context = {
        'inventory': inventory
    }
    return render(request, "per_product.html", context=context)

@login_required
def add_product(request):
    if request.method == "POST":
        add_form = AddInventoryForm(data=request.POST)
        if add_form.is_valid():
            new_inventory = add_form.save(commit=False)
            new_inventory.sales = float(add_form.data['cost_per_item']) * float(add_form.data['quantity_sold'])
            new_inventory.save()
            return redirect("/inventory/list/")
    else:
        add_form = AddInventoryForm()

    return render(request, "inventory_add.html", {"form": add_form})

@login_required
def delete_inventory(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    inventory.delete()
    return redirect("/inventory/list")

def update_inventory(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    if request.method == 'POST':
        updateForm = UpdateInventoryForm(data=request.POST)
        if updateForm.is_valid():
            inventory.name = updateForm.data['name']
            inventory.cost_per_item = updateForm.data['cost_per_item']
            inventory.quantity_in_stock = updateForm.data['quantity_in_stock']
            inventory.quantity_sold = updateForm.data['quantity_sold']
            inventory.sales = float(inventory.cost_per_item) * float(inventory.quantity_sold)
            inventory.save()
            return redirect(f"/inventory/product/{pk}")
    else:
        updateForm = UpdateInventoryForm(instance=inventory)
    context = {"form": updateForm}
    return render(request, "inventory_detail.html", context=context)