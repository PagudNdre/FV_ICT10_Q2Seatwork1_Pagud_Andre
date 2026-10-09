from pyscript import document, display

included_members = ['Andre Pagud', 'Sean Chua', 'Edrian Correa', 'Denver Martin']

def generate_result(e):
    First = document.getElementById("First_name").value
    Last = document.getElementById("Last_name").value

    combined = f"{First} {Last}"

    member = combined in included_members

    messages = {
        True: f"Congratulations {combined}! You are verified.",
        False: f"Sorry {combined}, your not in..."
    }

    result = messages[member]

    display(result, target="output")
