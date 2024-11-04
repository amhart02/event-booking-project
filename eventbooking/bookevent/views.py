from django.shortcuts import render
from bookevent.models import EventResponse
from django.shortcuts import redirect
from django.urls import reverse
# Create your views here.

def bookEvent(request):
    if request.method == "POST":
        new_name = request.POST["name"]
        new_email = request.POST["email"]

        if not new_name or not new_email:
            error_message = "Name and email are required."
            return render(request, "bookevent.html", {"error": error_message})

        EventResponse.objects.filter(name=new_name, email=new_email).delete()

        event_names = {"bouncy": "Bouncy House", 
                    "willy": "Willy Wonka\'s \"Fantastic\" Experience", 
                    "spooky": "Spooky Movie Night", 
                    "robert": "Robert Louis Stevenson Book Reading",
                    "blood": "Blood Drive"}

        for event_key, full_name in event_names.items():
            response_key = f'event_{event_key}'
            response = request.POST.get(response_key)

            if response:
                new_event = EventResponse(
                    name = new_name,
                    email = new_email,
                    event_name=full_name,
                    response=response
                )

            new_event.save()

        return redirect(f"{reverse('booked')}?name={new_name}&email={new_email}")
        
    return render(request, "bookevent.html")

def bookedEvents(request):
    print("bookedEvents view called")
    
    user_name = request.GET.get("name")
    user_email = request.GET.get("email")
    
    if user_name and user_email:
        booked_events = EventResponse.objects.filter(name=user_name, email=user_email, response="yes")
    else: 
        booked_events = EventResponse.objects.none


    return render(request, "bookedevent.html", {"booked_events": booked_events, "name": user_name})