import requests
from bs4 import BeautifulSoup
import smtplib
import time

# Function to check ticket availability
def check_tickets():
    try:

        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if the request fails
        soup = BeautifulSoup(response.text, 'html.parser')

        # Check for specific elements indicating ticket availability
        tickets_available = soup.select(css_selector)

        print(f'tickets_available: {tickets_available}')  # Print the value of tickets_available

        if tickets_available:
            send_notification()  # Call the function to send notification
            print('Tickets are available!')
        else:
            print('Tickets are not available.')
    
    except requests.exceptions.RequestException as e:
        print(f'Request error: {e}')
    except Exception as e:
        print(f'An error has occured: {e}')

# Function to send email notification
def send_notification():
            
    try:
        subject = 'Tickets are available!'
        body = 'Tickets for the event are now available. Book your tickets as soon as possible!'
        message = f'Subject: {subject}\n\n{body}'

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
    
    except smtplib.SMTPException as e:
        print(f'Failed to send email: {e}')
    except Exception as e:
        print(f'An error has occured: {e}')

if __name__ == '__main__':
    url = input('Enter the ticket site URL: \n>')
    css_selector = input('Enter the tickets CSS selector: \n>')
    sender_email = input('Enter your email address: \n>')
    receiver_email = input('Enter the recipient email address: \n>')
    password = input('Enter your email password: \n>')

    while True:
        print('Starting a new iteration of the while loop...')
        check_tickets()
        print('After calling check_tickets()')
        print('Waiting for the next check...')
        time.sleep(5)
        print('After waiting for 5 seconds')
