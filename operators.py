Operator_A = {
    '1': 0.9,
    '268': 5.1,
    '46': 0.17,
    '4620': 0.0,
    '468': 0.15,
    '4631': 0.15,
    '4673': 0.9,
    '46732': 1.1,
}

Operator_B = {
    '1': 0.92,
    '44': 0.5,
    '46': 0.2,
    '467': 1.0,
    '48': 1.2,
}
ops = {
    'Operator_A': Operator_A,
    'Operator_B': Operator_B,
}


class Operators():
    """Handls operator to find the best match"""
    def __init__(self):
        pass

    def find_prefix(self, phone_number, prefixs):
        """Find the longest match between prefixs and phone number"""
        # Get the total number of prefixs
        n = len(prefixs)

        # For each prefix in the list
        for i in range(0,n-1):
            #Get the actual prifix
            prefix = prefixs[i]

            # Calcualte the prefix length
            l = len(prefix)

            # The the same length as prefix from phone number
            short_phone_number = phone_number[0:l]

            # Compare prefix and short phone number
            if prefix == short_phone_number:
                return prefix
            else:
                pass

        return None


    def best_price(self, phone_number):
        """Find the best price to call the given phone number"""
        operator = ''
        best_price = None

        # Get all operators in a list
        for name, dict_ in ops.items():
            # Convert dict keys to a list
            prefixs = list(dict_.keys())

            # Sort the list of keys by length in reversed order, prefixs saved as string
            prefixs.sort(key=len, reverse=True)

            # Find the best prifix of phone number by the given operator
            prefix = self.find_prefix(phone_number, prefixs)

            # Try to find the price of the prefix return, set price to None if can't find the prefix
            try:
                price = dict_[prefix]
            except KeyError:
                price = None

            # Evaluate and compare the price with the best_price
            if best_price is None:
                best_price = price
                operator = name
            elif best_price > price:
                best_price = price
                operator = name
            else:
                pass

        return operator, best_price


def main():
    # Save the given phone number into a variable
    phone_number = input("Phone Number: ")

    # Validate the given phone number, if too short, print a message
    if len(phone_number) < 8:
        print("Given phone number is too short, minimum 8 digits")

    # Save the returned operator and best_price
    operator, best_price = Operators().best_price(phone_number)

    # Validate the operator
    if operator is None:
        # If none of the operator can handle the phone, return a message.
        print(f"Can't find an operator to call this number: {phone_number}")
    else:
        # Return the operator with best price find
        print(f"{operator} has the best price ${best_price}/min for number {phone_number}")


if __name__ == '__main__':
    main()
