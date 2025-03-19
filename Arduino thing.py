lights = 300
now  = 0
with open("File.py", 'w') as file:
    while now<lights:
        file.write("    pixels.setPixelColor("+str(now)+", pixels.Color(200, 255, 0));\n") 
        now = now + 1
        file.write("    pixels.setPixelColor("+str(now)+", pixels.Color(0, 255, 0));\n") 
        now = now + 1
        file.write("    pixels.setPixelColor("+str(now)+", pixels.Color(0, 255, 0));\n") 
        now = now + 1
        file.write("    pixels.setPixelColor("+str(now)+", pixels.Color(100, 0, 255));\n") 
        now = now + 1
    file.write("    pixels.show();\n") 
    file.write("    delay(1000);\n")
    now=0
    while now<lights:
        file.write("    pixels.setPixelColor("+str(now)+", pixels.Color(100, 0, 255));\n") 
        now = now + 1
        file.write("    pixels.setPixelColor("+str(now)+", pixels.Color(200, 255, 0));\n") 
        now = now + 1
        file.write("    pixels.setPixelColor("+str(now)+", pixels.Color(0, 255, 0));\n") 
        now = now + 1
        file.write("    pixels.setPixelColor("+str(now)+", pixels.Color(0, 255, 0));\n") 
        now = now + 1
    file.write("    pixels.show();\n") 
    file.write("    delay(1000);\n")
    now=0
    while now<lights:
        file.write("    pixels.setPixelColor("+str(now)+", pixels.Color(0, 255, 0));\n") 
        now = now + 1
        file.write("    pixels.setPixelColor("+str(now)+", pixels.Color(100, 0, 255));\n") 
        now = now + 1
        file.write("    pixels.setPixelColor("+str(now)+", pixels.Color(200, 255, 0));\n") 
        now = now + 1
        file.write("    pixels.setPixelColor("+str(now)+", pixels.Color(0, 255, 0));\n") 
        now = now + 1
    file.write("    pixels.show();\n") 
    file.write("    delay(1000);\n")
    now=0
    while now<lights:
        file.write("    pixels.setPixelColor("+str(now)+", pixels.Color(0, 255, 0));\n") 
        now = now + 1
        file.write("    pixels.setPixelColor("+str(now)+", pixels.Color(0, 255, 0));\n") 
        now = now + 1
        file.write("    pixels.setPixelColor("+str(now)+", pixels.Color(100, 0, 255));\n") 
        now = now + 1
        file.write("    pixels.setPixelColor("+str(now)+", pixels.Color(200, 255, 0));\n") 
        now = now + 1
    file.write("    pixels.show();\n") 
    file.write("    delay(1000);\n")
    now=0