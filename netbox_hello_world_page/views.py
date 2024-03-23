import random

from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import PermissionRequiredMixin

class HelloWorldView(PermissionRequiredMixin, View):
    """
    Display the "Hello, World!" page
    """
    # This allows only users having View access to prefixes.
    # If you don't need this kind of control, just remove this and
    # the PermissionRequiredMixin from the class.
    permission_required = "ipam.view_prefix"

    def get(self, request):
        # This is our code that gets run every time the page is visited
        number = random.randint(0, 999999)
        # Let's also see the query parameters
        query_params = str(dict(request.GET))
        # Now let's render the page output, using our variables
        return render(
            request,
            "netbox_hello_world_page/helloworld.html",
            {
                "number": number,
                "query_params": query_params,
            },
        )
