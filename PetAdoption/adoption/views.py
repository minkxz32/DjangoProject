from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from .forms import LoginForm
from .models import Pet
from .forms import PetForm
from .forms import UserRegistrationForm
from django.contrib import messages

def pet_list(request):
    pets = Pet.objects.all()
    return render(request, 'adoption/pet_list.html', {'pets': pets})

def pet_detail(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    return render(request, 'adoption/pet_detail.html', {'pet': pet})

@login_required
def pet_create(request):
    if request.method == "POST":
        form = PetForm(request.POST, request.FILES)  # Include request.FILES to handle file uploads
        if form.is_valid():
            pet = form.save(commit=False)
            pet.owner = request.user  # Set the pet's owner to the logged-in user
            pet.save()
            return redirect('pet_list')  # Redirect to the pet list page after saving
        else:
            print(form.errors)  # Debug: print form errors to console
    else:
        form = PetForm()  # Initialize a blank form for GET requests

    return render(request, 'adoption/pet_form.html', {'form': form})  # Render the pet form template


@login_required
def pet_update(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    if request.method == "POST":
        form = PetForm(request.POST,request.FILES, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet_list')
    else:
        form = PetForm(instance=pet)
    return render(request, 'adoption/pet_form.html', {'pet': pet,'form': form})

@login_required
def pet_delete(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    if request.method == "POST":
        pet.delete()
        return redirect('pet_list')
    return render(request, 'adoption/pet_confirm_delete.html', {'pet': pet})

@login_required
def request_adopt(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    
    # Ensure the user requesting adoption is not the pet's owner
    if request.user != pet.owner:
        # Add logic here, e.g., notify the owner or save the request to the database
        messages.success(request, f'Adoption request for {pet.name} has been sent.')
    else:
        messages.error(request, "You cannot adopt your own pet.")

    return redirect('pet_detail', pet_id=pet_id)

def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user to the database
            login(request, user)  # Log the user in after successful signup
            return redirect('pet_list')  # Redirect to the pet list or any other page
    else:
        form = UserRegistrationForm()
    return render(request, 'adoption/signup.html', {'form': form})

def home(request):
    return render(request, 'adoption/base.html')

def user_login(request):
    if request.user.is_authenticated:  # Check if the user is already logged in
        return redirect('home')  # Redirect to homepage if authenticated
    
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('pet_list')  # Or redirect to another page after login
            else:
                form.add_error(None, "Invalid username or password.")
    else:
        form = LoginForm()

    return render(request, 'adoption/login.html', {'form': form})
