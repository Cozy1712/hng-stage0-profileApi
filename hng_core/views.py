import requests
from django.http import JsonResponse
from datetime import datetime, timezone


# Create your views here.
def me(request):
    
    try:
        # Fetch a random cat fact from the external API
        url = "https://catfact.ninja/fact"
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise an error for bad responses 
        fact_data = response.json()
        cat_fact = fact_data.get("fact", "Cats are mysterious creatures!")
     
    except requests.RequestException:
        cat_fact = "Unable to fetch cat fact right now. Please try again later."

    data = {
        "status": "success",
        "user": {
            "email": "kolakabiru14@gmail.com",
            "name": "Kabiru Kolawole",
            "stack": "Python/Django",
        },
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "fact": cat_fact

    }   
    return JsonResponse(data, content_type="application/json")

