from pyg2fa import *



def generateCaptcha():
    randomSeed = "KKK67SDNLXIOG65U" #random 16 digit base 32 no # store this inside DB hardcode first
    print qrCodeURL("CryptoKnocker", randomSeed) ## url for qr code. Basically user need to key in this random 16 digit base 32 no
    userOTP = raw_input("Enter OTP: ")
    print validate(randomSeed, int(userOTP), 4)
    
    
generateCaptcha()