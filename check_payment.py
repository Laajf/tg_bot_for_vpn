from yoomoney import Client
import time

def check_payment(l):

    token ="4100118962392510.66D97494CA360D4B57DD307E050AF4D86DB0BA6E0226672BF7DFA1CF12525E94CF556D8B6EE8B9C395C41DBE0ED34BDF81482D628DD8B08EE84691441BBFB83901AB55E9B20ADC059E2246288B3EBE6FEAB3AC39FFCB5FD264684819C0893A87B2FBDEB677E91FBA94B6C1317F86033B404FAB78134FF3CAB3FBBB9DC30AED35"
    time.sleep(90)
    client = Client(token)
    history = client.operation_history(label=l)
    if history.operations:
        return history.operations[0].status 
    else:
        print("No payment found")
#print(check_payment(input()))