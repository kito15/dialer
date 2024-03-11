from flask import Flask, jsonify, render_template, request, Response
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import VoiceGrant
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

@app.route('/voice', methods=['POST'])
def voice():
    # Extract parameters from the Twilio request
    from_number = '18552961873'
    to_number = '8624149576'
    
    # Create a TwiML response to forward the call to the recipient
    twiml_response = VoiceResponse()
    dial = twiml_response.dial(caller_id=from_number)  # Set the caller ID
    dial.number(to_number)  # Dial the recipient's number
    
    # Return the TwiML response
    return Response(str(twiml_response), mimetype='text/xml')
    
@app.route('/token', methods=['GET'])
def get_token():
    # Your Twilio Account SID and Auth Token
    account_sid = 'AC7934dddd0bb09f3f348a59192b509642'
    auth_token = 'feedcb988d685a25b0a159b25ee50239'
    # Twilio API Key SID and Secret (recommended to use for generating tokens)
    api_key = 'SK35a16612b7e4490d3ea1522e0961c946'
    api_secret = 'sBuAlrI8JsbVglMnQr2eR5WQlF9pP0Wy'

    # Create an access token with credentials
    token = AccessToken(account_sid, api_key, api_secret, identity="kito7911@gmail.com")
    # Create a Voice grant and add to token
    voice_grant = VoiceGrant(
        outgoing_application_sid='AP3e5ab6c27b1c8f4ae57079325db5502c',
        incoming_allow=True,  # Optional: set to True to allow incoming calls
    )
    token.add_grant(voice_grant)

    # Return token info as JSON
    return jsonify(token=token.to_jwt())

@app.route('/')
def index():
    return render_template('test.html')
    
if __name__ == '__main__':
    app.run(debug=True)