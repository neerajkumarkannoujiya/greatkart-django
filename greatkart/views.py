from django.shortcuts import render
from store.models import Product, ReviewRating

def home(request):
    # Fetch all available products
    products = Product.objects.all().filter(is_available=True).order_by('created_date')

    # Calculate average rating for each product
    for product in products:
        reviews = ReviewRating.objects.filter(product_id=product.id, status=True)
        if reviews.exists():
            # Calculate average rating
            total_rating = sum(review.rating for review in reviews)
            average_rating = total_rating / len(reviews)
            product.averageReview = round(average_rating, 1)  # Round to 1 decimal place
        else:
            product.averageReview = 0  # Default value if no reviews exist

    # Pass products to the template
    context = {
        'products': products,
    }
    return render(request, 'home.html', context)