import pandas as pd
from twilio.rest import Client

# Load the data from CSV
data = pd.read_csv('output_data.csv')

#extract temperature from 'message column
def extract_temperature(s):
    try:
        return float(s.split(';')[0])
    except (AttributeError, TypeError, IndexError, ValueError):
        return None

data['temperature'] = data['message'].apply(extract_temperature)

# Remove rows with None in 'temperature' if any exist
data = data.dropna(subset=['temperature'])

# Define the temperature threshold
threshold = 37

# Twilio credentials
account_sid = 'AC558000ff1b5196a2722a17c821fb2562'
auth_token = 'f2d603ea2f6761ea15ababb21f6699a7'
client = Client(account_sid, auth_token)

# Twilio Phone numbers
from_number = '+17753698542'  # Twilio phone number
to_number = '+6581838924'    # Your phone number to receive SMS

# Check if any temperature exceeds the threshold
if data['temperature'].max() > threshold:
    message_body = f"The highest temperature recorded is {data['temperature'].max()}°C, which exceeds the threshold of {threshold}°C."
else:
    message_body = "No temperature exceeds the threshold of 37°C."

# Send SMS
message = client.messages.create(
    body=message_body,
    from_=from_number,
    to=to_number
)

print(f"SMS sent: {message.sid}")
