import math

def calculate_boxes(guests, slices_per_box):
    
    return math.ceil(guests / slices_per_box)

def calculate_leftovers(guests, slices_per_box, boxes):
    
    return (boxes * slices_per_box) - guests

def calculate_cost(boxes, price_per_box):
    
    return boxes * price_per_box

def main():
    print("WELCOME TO IYA MOSES PIZZA JOINT!")

    
    guests = int(input("Enter number of guests: "))

    print("       Choose the pizza type       ")
    print("1. Sapa size (4 slices, 2500)")																
    print("2. Small money (6 slices, 2900)")
    print("3. Big boys  (8 slices, 4000)")
    print("4. Odogwu  (12 slices, 5200)")

    
    choice = int(input("Enter your choice (1-4): "))

    
    slices_per_box = 0
    price_per_box = 0

    
    if choice == 1:
        slices_per_box = 4
        price_per_box = 2500
    elif choice == 2:
        slices_per_box = 6
        price_per_box = 2900
    elif choice == 3:
        slices_per_box = 8
        price_per_box = 4000
    elif choice == 4:
        slices_per_box = 12
        price_per_box = 5200
    else:
        print("Your choice is invalid. Please restart and select a valid option.")
        return

    
    boxes = calculate_boxes(guests, slices_per_box)
    leftovers = calculate_leftovers(guests, slices_per_box, boxes)
    total_cost = calculate_cost(boxes, price_per_box)

    
    print("\nOrder Summary:")
    print(f"Number of guests: {guests}")

    
    if choice == 1:
        pizza_type = "Sapa size"
    elif choice == 2:
        pizza_type = "Small money"
    elif choice == 3:
        pizza_type = "Big boys"
    elif choice == 4:
        pizza_type = "Odogwu"

    print(f"Pizza type: {pizza_type}")
    print(f"Boxes needed: {boxes}")
    print(f"Slices leftover: {leftovers}")
    print(f"Total cost: {total_cost}")

    print("Thanks for your patronage! We would be delighted to have you come patronize Iya Moses Pizza Joint again.")

if __name__ == "__main__":
    main()
