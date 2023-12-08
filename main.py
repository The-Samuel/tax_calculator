def tax_calculate(taxable_income):
    j = 44275 * 0.12
    k = (95375-44275) * 0.22
    lc = (182.100-95.375) * 0.24
    m = (231.250-182.100) * 0.32
    n = (578.125-231.250) * 0.35
    tax = 0
    marginal = 0
    if 0 < taxable_income <= 11000:
        tax = 0
        marginal = 0
    elif 11000 < taxable_income <= 44275:
        tax = 0.12*taxable_income
        marginal = 12
    elif 44275 < taxable_income <= 95375:
        tax = 0.22*(taxable_income-44275)+j
        marginal = 22
    elif 95375 < taxable_income <= 182100:
        tax = 0.24*(taxable_income-95375)+k+j
        marginal = 24
    elif 182100 < taxable_income <= 231250:
        tax = 0.32*(taxable_income-182100)+lc+k+j
        marginal = 32
    elif 231250 < taxable_income <= 578125:
        tax = 0.35*(taxable_income-231250)+m+lc+k+j
        marginal = 35
    elif taxable_income > 578125:
        tax = 0.37*(taxable_income-578125)+n+m+lc+k+j
        marginal = 37
    effective = round((tax * 100)/taxable_income, 1)
    return round(tax, 2), marginal, effective


def taxes():
    yes_list = ["yes", "yep", "yeah", "correct", "yea", "i do"]
    no_list = ["no", "nope", "nah", "incorrect", "i do not"]
    income = int(input("What is your annual income? "))
    deduct = 0
    if income < 0:
        print("Please provide a valid number.")
        taxes()
    deduction = input("Would you like to take the standard deduction? ")
    if deduction.lower() in yes_list:
        deduct = 13850
    elif deduction.lower() in no_list:
        deduct = int(input("What is the total amount of business and personal expenses and charitable donations you "
                           "have? "))
        if deduct < 13850 and input("That amount is less than the standard deduction; I recommend"
                                    " you take the standard deduction of $13,850. \nIs this something you want to do? "
                                    "") in yes_list:
            deduct = 13850
    total_tax, mar_tax, eff_tax = tax_calculate(income-deduct)
    print(f"You owe the IRS {total_tax} dollars in total. Your marginal tax rate is {mar_tax}% and your effective "
          f"tax rate is {eff_tax}%.")


taxes()
