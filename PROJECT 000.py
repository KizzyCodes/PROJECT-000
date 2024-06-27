def calculate_triangle_area(base, height):
    return 0.5 * base * height

def main():
    try:
        Base= float(input("Enter the base of the triangle: "))
        Height = float(input("Enter the height of the triangle: "))
        Area = calculate_triangle_area(Base, Height)
        print(f"The area of the triangle is: {Area}")
    except ValueError:
        print("Invalid input. Please enter numeric values for base and height.")

if __name__ == "__main__":
    main()
