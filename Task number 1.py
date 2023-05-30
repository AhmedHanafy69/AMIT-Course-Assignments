M_earth= float(input("Enter M_earth : "))
M_moon= float(input("Enter M_moon : "))
r = float(input("Enter r : "))
G = float(input("Enter G : "))


M_earth = M_earth * (10**24)
M_moon = M_moon * (10**22)
r = r * (10**8)
G = G * (10**-11)

fg = (G * M_earth * M_moon) / (r**2)
print(f"The gravitational force is: {fg} N")

# Rounded fg
rounded_fg = "{:.2e}".format(fg)
print("The gravitational force is:", rounded_fg, "N")
