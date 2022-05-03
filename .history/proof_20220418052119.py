import math


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


cos_sine_proof(100)
