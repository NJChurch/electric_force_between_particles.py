#defining constants
k_e = 8.9875517923e9  # Coulomb's constant in N·m²/C²

def main():
    while True:
        try:
            #taking user inputs for charges and distance
            q_1 = float(input("Enter the charge of the first particle (in Coulombs): "))
            q_2 = float(input("Enter the charge of the second particle (in Coulombs): "))
            r = float(input("Enter the distance between the two particles (in meters): "))
            if r <= 0:
                print("Distance must be greater than zero.")
                continue

            q_tot = q_1 * q_2
            F = k_e * abs(q_tot) / r**2

            #displaying the result
            if q_tot > 0:
                print(f"The electric force between the two particles is {F} Newtons (repulsive force).")
            else:
                print(f"The electric force between the two particles is {F} Newtons (attractive force).")

        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        ans = input("Do you want to calculate again? (yes/no): ").strip().lower()
        if ans not in ("yes", "y"):
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()