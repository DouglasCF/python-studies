from twilio.rest import Client

client = Client()

from_whatsapp_number='whatsapp:+5519999736313'
to_whatsapp_number='whatsapp:+yournumber'
client.messages.create(body='Ahoy, world!',
                       from_=from_whatsapp_number,
                       to=to_whatsapp_number)

