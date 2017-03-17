from twilio.rest import TwilioRestClient

account_sid = "AC8e94d448e9d1b0eb746bb868ad9a6182" # Your Account SID from www.twilio.com/console
auth_token  = ""  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    body = "Anuja using Twilio <3",
    to="+1415606****",    # Replace with your phone number
    from_="+1415498**** ") # Replace with your Twilio number

print(message.sid)