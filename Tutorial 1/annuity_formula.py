def present_value_annuity(interest_rate, number_of_periods, payment_amount):
    return payment_amount * (1 - (1 + interest_rate)**-number_of_periods) / interest_rate