from django.http import HttpResponse


class StripeWH_handler:
    """
    Handle Stripe webhooks
    """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic or unknown event
        """
        return HttpResponse(
            content  f'Webhook received: {event[type]}',
            status = 200)