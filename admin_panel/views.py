# admin_panel/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from apps.models import App

@login_required
def app_approval_page(request):
    if not request.user.is_staff:
        return redirect('home')  # Redirect non-admins
    apps = App.objects.filter(status='Pending')  # Fetch pending apps
    return render(request, 'admin_panel/app_approval.html', {'apps': apps})

@login_required
def approve_app(request, app_id):
    app = get_object_or_404(App, id=app_id)
    if not request.user.is_staff:
        return redirect('home')
    app.status = 'Approved'
    app.save()
    return redirect('admin:app_approval_page')

@login_required
def reject_app(request, app_id):
    app = get_object_or_404(App, id=app_id)
    if not request.user.is_staff:
        return redirect('home')
    if request.method == 'POST':
        feedback = request.POST.get('feedback', '')
        app.feedback = feedback
        app.status = 'Rejected'
        app.save()
        return redirect('admin:app_approval_page')
    return render(request, 'admin_panel/reject_app.html', {'app': app})

@login_required
def request_revision(request, app_id):
    app = get_object_or_404(App, id=app_id)
    if not request.user.is_staff:
        return redirect('home')
    if request.method == 'POST':
        feedback = request.POST.get('feedback', '')
        app.feedback = feedback
        app.status = 'Needs Revision'
        app.save()
        return redirect('admin:app_approval_page')
    return render(request, 'admin_panel/request_revision.html', {'app': app})
