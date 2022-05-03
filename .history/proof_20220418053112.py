import math

x = math.radians(90)
x_result = round(math.cos(x), 5)
print(x_result)
print(type(x_result))

y = math.radians(90 + 90)
y_result = round(math.sin(y), 5)
print(y_result)
print(type(y_result))


def cos_sine_proof(angle):
    # Convert angle value to radians for cosine calculation
    cos_rad_angle = math.radians(angle)

    # Calculate the Cosine value for the angle and round it to 5 decimal places
    cos_angle = round(math.cos(cos_rad_angle), 5)

    # Convert angle value to radians for sine calculation
    sine_rad_angle = math.radians(angle + 90)

    # Calculate the Sine value for the angle and round it to 5 decimal places
    sine_angle = round(math.cos(sine_rad_angle), 5)

    # Compare the results
    if cos_angle == sine_angle:
        print(f"Cos {angle} = Sin({angle} + 90")
    else:
        print("The program mulfunctioned...")


cos_sine_proof(90)
