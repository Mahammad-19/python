import random
def generate_otp():
    otp = random.randint(100000, 999999)
    return otp
if __name__ == "__main__":
    print("Your 6-digit OTP is:", generate_otp())
