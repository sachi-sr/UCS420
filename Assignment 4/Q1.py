import pandas as pd
rollno="1024170398"
fixedentries=[
{
  "question": "what is the annual fee",
  "answer": "The annual fee is Rs 500",
  "keywords": "Fee cost price charge",
  "category": "billing"
},
{
  "question": "how to reset password",
  "answer": "Go to Settings>Reset Password",
  "keywords": "password reset login",
  "category": "account"
},
{
  "question": "what are your working hours",
  "answer": "We are open 9 to 5",
  "keywords": "hours timing open time",
  "category": "general"
},
{
        "question": "how can i pay the fee",
        "answer": "You can pay via UPI, card, or net banking.",
        "keywords": "pay payment upi fee",
        "category": "billing"
    }
]

last_two_digits = rollno[-2:]

categories = ["billing", "account", "general"]


personalized_entries = []

for digit in last_two_digits:
    d = int(digit)
    category = categories[d % 3]

    if category == "billing":
        entry = {
            "question": "how can i check my payment status",
            "answer": "You can check your payment status in the billing section.",
            "keywords": "payment status billing transaction",
            "category": "billing"
        }

    elif category == "account":
        entry = {
            "question": "how do i update my registered mobile number",
            "answer": "Go to Account Settings and update your registered mobile number.",
            "keywords": "mobile number update account",
            "category": "account"
        }

    else:
        entry = {
            "question": "where can i get general help",
            "answer": "You can contact the help desk for general assistance.",
            "keywords": "help support assistance general",
            "category": "general"
        }

    personalized_entries.append(entry)


all_entries = fixedentries + personalized_entries


df = pd.DataFrame(all_entries)

print("Final 6-row FAQ DataFrame:")
print(df)