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


#1. Start the program.
#2. Display the Railway Enquiry Chatbot menu.
#3. Ask the user to enter a choice.
#4. If the choice is Train Timings, take the train name and display departure time.
#5. If the choice is Ticket Booking Guidance, display booking instructions.
#6. If the choice is Fare Enquiry, take source and destination stations and display fare.
#7. If the choice is Seat Availability, display seat availability information.
#8. If the choice is Exit, display thank you message and stop the program.
#9. If the choice is invalid, display an error message.
#10. Repeat the menu until the user chooses Exit.
#11. End the program.
