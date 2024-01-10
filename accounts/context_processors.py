from vendor.models import Vendor


def get_vendor(request):
    try:
        vendor = Vendor.objects.get(user=request.user)
    except (TypeError, ValueError, OverflowError, Vendor.DoesNotExist):
        vendor = None
    return dict(vendor=vendor)


def get_google_api_key(request):
    from django.conf import settings
    return dict(google_api_key=settings.GOOGLE_API_KEY)
