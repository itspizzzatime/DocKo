import json

def append_user_to_client(db_file, client_file):
    # Load the data from db.json
    with open(db_file, 'r') as db_f:
        db_data = json.load(db_f)

    # Load the data from client.json
    try:
        with open(client_file, 'r') as client_f:
            client_data = json.load(client_f)
    except FileNotFoundError:
        # If client.json doesn't exist, start with an empty list
        client_data = []

    # Append each user from db.json to client.json
    for user in db_data:
        client_data.append(user)

    # Save the updated data back to client.json
    with open(client_file, 'w') as client_f:
        json.dump(client_data, client_f, indent=4)

    print(f"Appended {len(db_data)} user(s) to {client_file}.")

