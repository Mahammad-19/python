try:
    file = open("demoarif.txt", "r")
except IOError:
    print("Error: Unable to read the file!")
finally:
    file.close()
