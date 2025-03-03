print("*****Welcome to Red bus Booking*****")

print("Go to the home page and select your Language")
Destinations = {
    "Chennai": 800, 
    "Madurai": 1100, 
    "Coimbatore": 950, 
    "Trichy": 600, 
    "Bangalore": 1800
}
drop={"Mayiladuthurai","Kumbakonam","Thanjavur", "Karaikkal"}
Language={"1.Tamil","2.English"}
Select_language=input("Select your Language:")
select_services={"1.Book ticket", "2.Cancel ticket","3.view ticket"}
service_you_want=input("Which service you want:")
your_destination=input("Enter your pickup point:")

if your_destination in Destinations:
    print(f"Yes..! {your_destination}  is available in our Red bus.")
    booking=input("Do you want to book your tickets here..! Enter 1:")

    if booking=="1":
        Enter_destination=input("Enter your Drop point:")
        Full_name=input("Enter your Full name:")
        Age=int(input("Enter your Age:"))
        Id_Proof=input("which id card Are you going to use:")
        No_of_tickets=int(input("How many tickets you want:"))
        total_amount=Destinations[your_destination]*No_of_tickets

        gst_rate=5
        gst_amount=(total_amount*gst_rate)/100
        Final_price=total_amount+gst_amount

        print(f" Hi {Full_name} Your ticket is booked to {Enter_destination}. \n Total amount is{total_amount}\n  Added GST amount{gst_amount}\n The final price is {Final_price}")

    else:
        print("Sorry..!! Your Destination place currently Unavailable in this portal...!")
