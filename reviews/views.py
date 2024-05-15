from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .forms import ReviewForm
from .models import Review
from products.models import Product

@login_required
def create_review(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    
    # Check if the user has already written a review for this product
    existing_review = Review.objects.filter(product=product, user=request.user).exists()
    if existing_review:
        messages.warning(request, 'You have already submitted a review for this product.')
        return redirect('product_detail', product_id=product_id)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            
            # Send email notification to admins about the new review
            send_new_review_notification(product, review)
            send_review_submission_notification(product, review)
            messages.success(request, 'Review has been submitted successfully!')
            return redirect('product_detail', product_id=product_id)
    else:
        form = ReviewForm()
    return render(request, 'reviews/create_review.html', {'form': form, 'product': product})

@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Review has been updated successfully!')
            send_edit_review_notification(review.product, review)
            send_review_edited_user_notification(review.product, review)
            return redirect('product_detail', product_id=review.product.pk)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'reviews/edit_review.html', {'form': form, 'review': review})

@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    product_id = review.product.pk
    review.delete()
    messages.success(request, 'Review has been deleted successfully!')
    # Send email notification to admins about the deleted review
    send_review_deleted_notification(review.product, review)
    send_review_deleted_user_notification(review.product, review)
    return redirect('product_detail', product_id=product_id)

def product_reviews(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    review_list = Review.objects.filter(product_id=product_id)
    paginator = Paginator(review_list, 5)  # Show 5 reviews per page

    page_number = request.GET.get('page')
    try:
        product_reviews = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        product_reviews = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        product_reviews = paginator.page(paginator.num_pages)

    context = {
        'product_reviews': product_reviews,
        'product': product,
    }
    return render(request, 'reviews/product_reviews.html', context)

def send_new_review_notification(product, review):
    """
    Send email notification to admins about the new review.
    """
    subject = 'New Review Notification'
    message = render_to_string('admin_emails/new_review_notification.txt', {
        'product_name': product.name,
        'review_title': review.review_title,
        'reviewer_name': review.user.username,
        'review_rating': review.user_rating,
        'review_comment': review.review,
    })
    send_mail(subject, message, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])

def send_review_deleted_notification(product, review):
    """
    Send email notification to admins about the deleted review.
    """
    subject = 'Review Deleted Notification'
    message = render_to_string('admin_emails/review_deleted_admin_notification.txt', {
        'product_name': review.product.name,
        'reviewer_name': review.user.username,
    })
    send_mail(subject, message, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])

def send_edit_review_notification(product, review):
    """
    Send email notification to admins about the edited review.
    """
    subject = 'Review Edited Notification'
    message = render_to_string('admin_emails/review_edited_admin_notification.txt', {
        'product_name': product.name,
        'review_title': review.review_title,
        'reviewer_name': review.user.username,
        'review_rating': review.user_rating,
        'review_comment': review.review,
    })
    send_mail(subject, message, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])

def send_review_submission_notification(product, review):
    """
    Send email notification to the reviewer when a reply is submitted.
    """
    subject = 'Reply Submitted Notification'
    message = render_to_string('user_emails/review_submission_confirmation.txt', {
        'product_name': product.name,
        'reviewer_name': review.user.username,
    })
    send_mail(subject, message, settings.EMAIL_HOST_USER, [review.user.email])

def send_review_deleted_user_notification(product, review):
    '''
    Send email notification to the reviewer when a reply is deleted.
    '''
    subject = 'Review Deleted Notification'
    message = render_to_string('user_emails/review_deleted_confirmation.txt', {
        'product_name': product.name,
        'reviewer_name': review.user.username,
    })
    send_mail(subject, message, settings.EMAIL_HOST_USER, [review.user.email])

def send_review_edited_user_notification(product, review):
    '''
    Send email notification to the reviewer when a reply is edited.
    '''
    subject = 'Review Edited Notification'
    message = render_to_string('user_emails/review_edited_confirmation.txt', {
        'product_name': product.name,
        'reviewer_name': review.user.username,
    })
    send_mail(subject, message, settings.EMAIL_HOST_USER, [review.user.email])
