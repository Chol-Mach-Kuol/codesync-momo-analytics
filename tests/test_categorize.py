from etl.categorize import categorize


def test_receive_money():
    assert categorize("You have received 5,000 RWF from 0788000001") == "Receive Money"


def test_send_money():
    assert categorize("You have transferred 2,000 RWF to 0788000002") == "Send Money"


def test_airtime():
    assert categorize("Your airtime recharge of 500 RWF was successful") == "Airtime"


def test_bill_payment():
    assert categorize("Bill payment of 10,000 RWF completed") == "Bill Payment"


def test_cash_withdrawal():
    assert categorize("You have withdrawn 20,000 RWF from agent") == "Cash Withdrawal"


def test_other():
    assert categorize("Some unrecognized message") == "Other"
