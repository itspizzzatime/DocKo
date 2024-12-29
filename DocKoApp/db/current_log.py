import json

def get_logged_in_user_name(file_path):
    # Load the JSON file
    with open(file_path, 'r') as f:
        data = json.load(f)

    # Find the logged-in user
    for user in data.get('users', []):
        if user.get('logged_in'):
            return user.get('name')

    # If no user is logged in, return None or a default message
    return "No user is currently logged in."


# Example usage
if __name__ == "__main__":
    file_path = 'client.json'  # Path to your JSON file
    logged_in_user = get_logged_in_user_name(file_path)
    print(f"Current logged-in user: {logged_in_user}")
