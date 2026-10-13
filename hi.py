import json
import os

FILENAME = "contacts.json"


def load_contacts():
  """Loads contacts from a JSON file."""
  if os.path.exists(FILENAME):
    try:
      with open(FILENAME, "r") as file:
        return json.load(file)
    except json.JSONDecodeError:
      return {}
  return {}


def save_contacts(contacts):
  """Saves contacts to a JSON file."""
  with open(FILENAME, "w") as file:
    json.dump(contacts, file, indent=4)


def add_contact(contacts):
  """Adds a new contact."""
  print("\n--- Add New Contact ---")
  name = input("Enter name: ").strip()
  if not name:
    print("Name cannot be empty.")
    return

  if name in contacts:
    print(f"Contact '{name}' already exists.")
    return

  phone = input("Enter phone number: ").strip()
  email = input("Enter email address: ").strip()
  address = input("Enter physical address: ").strip()

  contacts[name] = {"phone": phone, "email": email, "address": address}
  save_contacts(contacts)
  print(f"Contact '{name}' added successfully!")


def view_contacts(contacts):
  """Views all stored contacts."""
  print("\n--- Contact List ---")
  if not contacts:
    print("No contacts found.")
    return

  for name, info in contacts.items():
    print(f"\nName: {name}")
    print(f"  Phone:   {info.get('phone', 'N/A')}")
    print(f"  Email:   {info.get('email', 'N/A')}")
    print(f"  Address: {info.get('address', 'N/A')}")


def search_contact(contacts):
  """Searches for a contact by name."""
  print("\n--- Search Contact ---")
  query = input("Enter name to search: ").strip().lower()
  found = False

  for name, info in contacts.items():
    if query in name.lower():
      print(f"\nFound Contact - Name: {name}")
      print(f"  Phone:   {info.get('phone', 'N/A')}")
      print(f"  Email:   {info.get('email', 'N/A')}")
      print(f"  Address: {info.get('address', 'N/A')}")
      found = True

  if not found:
    print("No matching contacts found.")


def edit_contact(contacts):
  """Edits an existing contact."""
  print("\n--- Edit Contact ---")
  name = input("Enter the name of the contact to edit: ").strip()

  if name not in contacts:
    print(f"Contact '{name}' not found.")
    return

  print(
      f"Leave field blank if you do not want to change it."
  )
  phone = input(f"New phone ({contacts[name]['phone']}): ").strip()
  email = input(f"New email ({contacts[name]['email']}): ").strip()
  address = input(f"New address ({contacts[name]['address']}): ").strip()

  if phone:
    contacts[name]["phone"] = phone
  if email:
    contacts[name]["email"] = email
  if address:
    contacts[name]["address"] = address

  save_contacts(contacts)
  print(f"Contact '{name}' updated successfully!")


def delete_contact(contacts):
  """Deletes a contact."""
  print("\n--- Delete Contact ---")
  name = input("Enter the name of the contact to delete: ").strip()

  if name in contacts:
    del contacts[name]
    save_contacts(contacts)
    print(f"Contact '{name}' deleted successfully!")
  else:
    print(f"Contact '{name}' not found.")


def main():
  """Main loop for the contact manager CLI."""
  contacts = load_contacts()

  while True:
    print("\n====================")
    print("   CONTACT MANAGER  ")
    print("====================")
    print("1. View Contacts")
    print("2. Add Contact")
    print("3. Search Contact")
    print("4. Edit Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Choose an option (1-6): ").strip()

    if choice == "1":
      view_contacts(contacts)
    elif choice == "2":
      add_contact(contacts)
    elif choice == "3":
      search_contact(contacts)
    elif choice == "4":
      edit_contact(contacts)
    elif choice == "5":
      delete_contact(contacts)
    elif choice == "6":
      print("Exiting Contact Manager. Goodbye!")
      break
    else:
      print("Invalid choice. Please enter a number from 1 to 6.")
print("process is done bro!")

if __name__ == "__main__":
  main()

