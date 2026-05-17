def shopping_chatbot():

    print("===== Online Shopping Chatbot =====")

    while True:

        print("\n1. Product Search")
        print("2. Order Tracking")
        print("3. Return Policy")
        print("4. Payment Methods")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            product = input("Enter product name: ")
            print("Bot:", product, "is available.")

        elif choice == "2":
            order_id = input("Enter Order ID: ")
            print("Bot: Order", order_id, "is out for delivery.")

        elif choice == "3":
            print("Bot: Products can be returned within 7 days.")

        elif choice == "4":
            print("Bot: We accept UPI, Debit Card, Credit Card and Net Banking.")

        elif choice == "5":
            print("Bot: Thank you for visiting!")
            break

        else:
            print("Invalid choice.")

shopping_chatbot()


#1. Start the program.
#2. Display the Online Shopping Chatbot menu.
#3. Ask the user to enter a choice.
#4. If the choice is Product Search, take the product name and display availability.
#5. If the choice is Order Tracking, take the order ID and display order status.
#6. If the choice is Return Policy, display return policy information.
#7. If the choice is Payment Methods, display accepted payment methods.
#8. If the choice is Exit, display thank you message and stop the program.
#9. If the choice is invalid, display an error message.
#10. Repeat the menu until the user chooses Exit.
#11. End the program.
