from vendor.models import Vendor


def get_vendor(request):
    try:
        vendor = Vendor.objects.get(user=request.user)
    except (TypeError, ValueError, OverflowError, Vendor.DoesNotExist):
        vendor = None
    return dict(vendor=vendor)
