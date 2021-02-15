from testing_code.name_function import get_formatted_name

print("enter 'q' at any time to exit ")
while True:
    first = input("\n Enter your first name ")
    if first == 'q':
        break
    last = input("\n Enter your last name")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first,last)
    print(f"\t Formatted Name: {formatted_name}")


