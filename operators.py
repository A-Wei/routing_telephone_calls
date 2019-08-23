import argparse

Operator_A = [(1, 0.9), (268, 5.1), (46, 0.17), (4620, 0.0), (468, 0.15), (4631, 0.15), (4673, 0.9), (46732, 1.1)]
Operator_B = [(1, 0.92), (44, 0.5), (46, 0.2), (467, 1.0), (48, 1.2)]

ops = {
    'Operator_A': Operator_A,
    'Operator_B': Operator_B,
}


class Operators():
    """Handls operator to find the best match"""
    def __init__(self, number):
        self.number = number

    def best_operator_and_price(self):
        best_price = None
        best_operator = None

        for op_name, op_value in ops.items():
            op_value.sort(reverse=True)
            for i in op_value:
                if str(self.number).startswith(str(i[0])):
                    if best_price is None or best_price > i[1]:
                        best_price = i[1]
                        best_operator = op_name
                    break

        return best_operator, best_price

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", help="Number to call!", type=int)
    args = parser.parse_args()

    if args.n is None:
        phone_number = input("Phone Number: ")
    else:
        phone_number = str(args.n)

    # Validate the given phone number, if too short, print a message
    if len(phone_number) < 8:
        print("Given phone number is too short, minimum 8 digits")
        raise Exception("Phone number too short!")

    # Save the returned operator and best_price
    operator, best_price = Operators(phone_number).best_operator_and_price()
    if operator is None:
        print("No operator found")
    else:
        print(f"{operator} has the best price ${best_price}/min for number {phone_number}")


if __name__ == '__main__':
    main()
