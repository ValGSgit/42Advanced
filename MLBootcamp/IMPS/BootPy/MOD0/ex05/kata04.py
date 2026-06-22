# Put this at the top of your kata04.py file
kata = (0, 4, 132.42222, 10000, 12345.67)

def main():
    return print(f"module_{kata[0]:02}, ex_{kata[1]:02} : {kata[2]:.2f}, {kata[3]:.2e}, {kata[4]:.2e}")

if __name__ == "__main__":
    main()