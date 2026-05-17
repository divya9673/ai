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