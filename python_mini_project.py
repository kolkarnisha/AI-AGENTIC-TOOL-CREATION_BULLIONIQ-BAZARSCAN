print("nishazareentaj")
allvoterss=[]
for i in range(5):
    age = int(input("enter your age: "))
    name = str(input("enter your name: "))
    aadhar = input("Enter your Aadhar number: ")
    location = input("Enter your location: ")
    if age >= 18:
        print(f"{name} eligible to vote")
        parties = ["YSR CONGRESS PARTY", "INDIAN NATIONAL CONGRESS PARTY", "TELUGHUDHESHAM PARTY", "JANASENA PARTY", "BJP", "Other", "NOTA"]
        print("\nSelect your favourite party:")
        for idx, party in enumerate(parties, 1):
            print(f"{idx}. {party}")
        
        choice = int(input("Enter choice number: "))
        if 1 <= choice <= len(parties):
            selected_party = parties[choice - 1]
            print(f"{name} selected: {selected_party}")
        else:
            print("Invalid choice, no party selected")
        print()  # Empty line for spacing
        leader_name=input('\n enter your favourite leader name:')
        leader_qualities=input("enter qualities using comma:")
        qualitieslist=[q.strip() for q in leader_qualities.split(",")]
        print("\nOpinion Section:")
        evm_opinion = input("Do you think EVM manipulation happened in 2024 elections? (yes/no): ").lower()
        if evm_opinion == "yes":
            resign_opinion = input("Do you think the present chandhrababunaidu and narendramodi should resign? (yes/no): ").lower()
            if resign_opinion == "yes":
                print("\nPeople is govt and govt is people, fight for your valid vote\n")
            else:
                print(input(list("\nso,you like present govt qualities,enter your govt benefits:")))
        else:
            print("\nSo, you trust the election process and the current government.\n")
        user_data={
            "age":str(age),
            "name":name,
            "party":selected_party,
            "leader":leader_name,
            "qualities":qualitieslist
        }
        print(f"\nStored details:{user_data}")
    else:
        print(f"{name} not eligible to vote\n")
       