from django.shortcuts import render
from tasks.views import *
from .forms import ContactForm
from .models import Contact
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def Index(request):
    return render(request, 'contacts.html')

@login_required
def contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts.html', {'contacts': contacts})

@login_required
def create_contact(request):
    
    if request.method == 'GET':
        return render(request, 'create_contact.html', {
            "form": ContactForm
        })
    else:
        try:
            form = ContactForm(request.POST)
            new_contact = form.save(commit=False)
            new_contact.user = request.user
            new_contact.save()
            return redirect('contacts')
        except ValueError:
            return render(request, 'create_contact.html', {
                "form": ContactForm,
                "error": 'Please, provide valid data'
            })

@login_required      
def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, user=request.user)
    if request.method == 'POST':
        contact.delete()
        return redirect('contacts')
        
#def contact_detail(request, contact_id):
    #if request.method == 'GET':
        contact = get_object_or_404(Task, pk=contact_id, user=request.user)
        form = ContactForm(instance=contact)
        return render(request, 'task_detail.html', {'contact': contact, "form": form})
    #else:
        try:
            contact = get_object_or_404(Contact, pk=contact_id, user=request.user)
            form = ContactForm(request.POST, instance=contact)
            form.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'contact_detail.html', {
                'contact': contact, 
                "form": form, 
                "error": "Error while updating the contact"})
        
