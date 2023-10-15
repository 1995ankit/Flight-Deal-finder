# Flight Deal finder
### This code automatically sends text to our number when there are good deals on our flights

The workflow of the project is as follows:
* Provide the 'Departure' and 'Destination' city, in a Google Excel sheet.
* Mention the threshold price next to every city combination. The threshold price is the price below which we want to book our flight ticket.
* The code then connects the Excel sheet to Python, using the Google sheet API.
* The code then uses kiwi website API to find flight ticket prices between the two cities.
* The code then uses twilio api to send us the flight deal if the price is lower than the threshold.
