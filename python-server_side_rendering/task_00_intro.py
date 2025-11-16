def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: Template must be a string")
        return
    
    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print("Error: Attendees must be a list of dictionaries")
        return
 
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    
    if not attendees:
        print("No data provided, no output files generated.")
        return

    for i, attendee in enumerate(attendees, start=1):
        name = attendee.get("name") or "N/A"
        event_title = attendee.get("event_title") or "N/A" 
        event_date = attendee.get("event_date") or "N/A"
        event_location = attendee.get("event_location") or "N/A"

        personalized_message = template
        personalized_message = personalized_message.replace("{name}", name)
        personalized_message = personalized_message.replace("{event_title}", event_title)
        personalized_message = personalized_message.replace("{event_date}", event_date)
        personalized_message = personalized_message.replace("{event_location}", event_location)

        filename = f"output_{i}.txt"
        with open(filename, 'w') as file:
            file.write(personalized_message)

if __name__ == "__main__":
    with open('template.txt', 'r') as file:
        template_content = file.read()

    attendees = [
        {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
    ]

    generate_invitations(template_content, attendees)
    print("Fichiers générés !")
