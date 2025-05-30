#0. Weather Recommendation Program
user_response = str(input("What's the weather like today? (sunny/rainy/cold):"))
if user_response == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif user_response == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif user_response == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
