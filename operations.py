import argparse

def add(args):
    result = args.num1 + args.num2
    print(f"Result of addition: {result}")

def subtract(args):
    result = args.num1 - args.num2
    print(f"Result of subtraction: {result}")

def multiply(args):
    result = args.num1 * args.num2
    print(f"Result of multiplication: {result}")

def divide(args):
    if args.num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = args.num1 / args.num2
        print(f"Result of division: {result}")

def main():
    parser = argparse.ArgumentParser(description="CLI Calculator for basic operations")

   
    subparsers = parser.add_subparsers(title="Operations", description="Available operations", help="Choose an operation")

    parser_add = subparsers.add_parser("add", help="Perform addition")
    parser_add.add_argument("num1", type=float, help="First number")
    parser_add.add_argument("num2", type=float, help="Second number")
    parser_add.set_defaults(func=add)

   
    parser_subtract = subparsers.add_parser("subtract", help="Perform subtraction")
    parser_subtract.add_argument("num1", type=float, help="First number")
    parser_subtract.add_argument("num2", type=float, help="Second number")
    parser_subtract.set_defaults(func=subtract)

 
    parser_multiply = subparsers.add_parser("multiply", help="Perform multiplication")
    parser_multiply.add_argument("num1", type=float, help="First number")
    parser_multiply.add_argument("num2", type=float, help="Second number")
    parser_multiply.set_defaults(func=multiply)

    parser_divide = subparsers.add_parser("divide", help="Perform division")
    parser_divide.add_argument("num1", type=float, help="First number")
    parser_divide.add_argument("num2", type=float, help="Second number")
    parser_divide.set_defaults(func=divide)

   
    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
