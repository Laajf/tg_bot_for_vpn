from yoomoney import Quickpay
import time
import random

def payment1(client_id):
    curt = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    l=f"red01+{client_id}+{curt}"
    tok = random.randint(1, 10000000)
    quickpay = Quickpay(receiver="4100118962392510", quickpay_form="shop", targets="Buy VPN for a month", paymentType="SB", sum=5, label=str(tok))
    print(tok)
    return quickpay.base_url, tok
    #print(quickpay.base_url)

