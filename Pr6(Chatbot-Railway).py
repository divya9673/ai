def railway_chatbot():

    print("===== Railway Enquiry Chatbot =====")

    while True:

        print("\n1. Train Timings")
        print("2. Ticket Booking Guidance")
        print("3. Fare Enquiry")
        print("4. Seat Availability")
        print("5. Exit")

        choice = input("Enter your choice: ")

        # Train Timings
        if choice == "1":
            train = input("Enter Train Name: ")
            print("Bot:", train, "departs at 6:30 PM.")

        # Ticket Booking Guidance
        elif choice == "2":
            print("Bot: Visit IRCTC website for ticket booking.")

        # Fare Enquiry
        elif choice == "3":
            source = input("Enter Source Station: ")
            destination = input("Enter Destination Station: ")

            print("Bot: Fare from",
                  source, "to", destination,
                  "is Rs. 450.")

        # Seat Availability
        elif choice == "4":
            print("Bot: Seats are available in Sleeper and AC coaches.")

        # Exit
        elif choice == "5":
            print("Bot: Thank you!")
            break

        else:
            print("Invalid choice.")

railway_chatbot()