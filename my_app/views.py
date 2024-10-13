from django.shortcuts import render, redirect
from .forms import FeedbackForm
from django.contrib import messages

# Create your views here.

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your feedback has been recorded.')
            return redirect('feedback')
    else:
        form = FeedbackForm()

    return render(request, 'feedback.html', {'form': form})
