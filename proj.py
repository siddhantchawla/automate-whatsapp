from twilio.rest import Client 
 

def sendMessage():
    account_sid = 'AC65009f8de0bd9644ccb6bb468bcc942d' 
    auth_token = '6b0a00767abe805783ae16c0f4a1d2ec' 
    client = Client(account_sid, auth_token) 
    
    # message = client.messages.create( 
    #                               from_='whatsapp:+918789386710',  
    #                               body='Your appointment is coming up on July 21 at 3PM',      
    #                               to='whatsapp:+917782852299'
    #                           ) 

    message = client.messages.create( 
                                from_='whatsapp:+14155238886',  
                                body='Hey babe, are you free tonight?',      
                                to='whatsapp:+918789386710'
                            )
    
    print(message.sid)
