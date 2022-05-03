import math

x = math.radians(90)
print(round(math.cos(x), 5))


def cos_sine_proof(angle):
    # Convert angle value to radians
    cos_rad_angle = math.radians(angle)

    # Calculate the Cosine value for the angle and round it to 5 decimal places
    cos_angle = round(math.cos(cos_rad_angle), 5)
