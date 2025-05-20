input_file = "input.txt"
output_file = "microcode.txt"

def main():
    print("1: CLI Input")
    print("2: Input.txt")
    mode = input("Mode: ")
    if mode == "1":
        microcode = input("Enter microcode:")
    elif mode == "2":
        pass
        with open(input_file, "r") as file:
            microcode = file.read()
    else: return
    
    code = []
    counter = 0
    counter2 = 0
    hex_list = []
    for c in microcode:
        if c == "0" or c == "1":
            code.append(c)
    code = "".join(code)

    print()
    print()
    # Convert Microcode to Mnemonics
    instruction = 0
    instructions = []
    with open("instructions.txt", "r") as file:
        content = file.read()
        instructions = content.split('\n')

    Reg_Src = {}
    Reg_Dst = {}
    ALU_Op = {}
    ALU_Out = {}
    HiB_Sel = {}
    Mod = {}
    Inc = {}

    Reg_Src["0000"] = "PC"
    Reg_Src["0001"] = "1"
    Reg_Src["0010"] = "IR"
    Reg_Src["0011"] = "GP0"
    Reg_Src["0100"] = "Status"
    Reg_Src["0101"] = "ALU_Out"
    Reg_Src["0110"] = "Accumulator"
    Reg_Src["0111"] = "ALU_B"
    Reg_Src["1000"] = "SP"
    Reg_Src["1001"] = "X"
    Reg_Src["1010"] = "Y"
    Reg_Src["1011"] = "GP1"
    Reg_Src["1100"] = "GP2"
    Reg_Src["1101"] = "GP3"
    Reg_Src["1110"] = "GP4"
    Reg_Src["1111"] = "Memory"

    Reg_Dst["0000"] = "PC"
    Reg_Dst["0001"] = "Address Bus"
    Reg_Dst["0010"] = "IR"
    Reg_Dst["0011"] = "GP0"
    Reg_Dst["0100"] = "Status"
    Reg_Dst["0101"] = "ALU_Out"
    Reg_Dst["0110"] = "Accumulator"
    Reg_Dst["0111"] = "ALU_B"
    Reg_Dst["1000"] = "SP"
    Reg_Dst["1001"] = "X"
    Reg_Dst["1010"] = "Y"
    Reg_Dst["1011"] = "GP1"
    Reg_Dst["1100"] = "GP2"
    Reg_Dst["1101"] = "GP3"
    Reg_Dst["1110"] = "GP4"
    Reg_Dst["1111"] = "Memory"

    ALU_Op["000"] = "ADC"
    ALU_Op["001"] = "SBC"
    ALU_Op["010"] = "NOT"
    ALU_Op["011"] = "AND"
    ALU_Op["100"] = "XOR"
    ALU_Op["101"] = "OR"
    ALU_Op["110"] = "LSH"
    ALU_Op["111"] = "RSH"

    ALU_Out["1"] = "ALU_Out"
    ALU_Out["0"] = ""
    HiB_Sel["1"] = "HiB_Sel"
    HiB_Sel["0"] = ""
    Mod["00"] = ""
    Mod["01"] = "IC"
    Mod["10"] = "Br_En"
    Mod["11"] = "Bus Inc"
    Inc["1"] = "Inc"
    Inc["0"] = ""

    for c in code:
        if counter2 == 16:
            counter2 = 0
            instruction += 1
            print()
        
        hex_list.append(c)
        counter += 1
        if counter == 16:
            if counter2 == 0:
                print(instructions[instruction])

            counter = 0
            counter2 += 1
            microcode = "".join(hex_list)
            hex_list = []
            if microcode != "0000000000000000" and counter2 > 3:
                text = ""
                if Reg_Src[microcode[:4]] != "":
                    text += f"{Reg_Src[microcode[:4]]}"
                if Reg_Dst[microcode[4:8]] != "":
                    text += f" > {Reg_Dst[microcode[4:8]]}"
                if ALU_Op[microcode[8:11]] != "":
                    text += f" | {ALU_Op[microcode[8:11]]}"
                if ALU_Out[microcode[11]] != "":
                    text += f" | {ALU_Out[microcode[11]]}"
                if HiB_Sel[microcode[12]] != "":
                    text += f" | {HiB_Sel[microcode[12]]}"
                if Mod[microcode[13:15]] != "":
                    text += f" | {Mod[microcode[13:15]]}"
                if Inc[microcode[15]] != "":
                    text += f" | {Inc[microcode[15]]}"
                print(text)


    if mode == "1":
        print("Microcode: ")
        for c in code:
            hex_list.append(c)
            counter += 1
            if counter == 16:
                counter = 0
                number = hex(int("".join(hex_list), 2))[2:]
                if number == "0": number = "0000"
                print(number, end=" ")
                hex_list = []
    elif mode == "2":
        with open(output_file, "w") as file:
            file.write("v3.0 hex words plain\n")
            for c in code:
                hex_list.append(c)
                counter += 1
                if counter == 16:
                    counter = 0
                    number = hex(int("".join(hex_list), 2))[2:]
                    if number == "0": number = "0000"
                    file.write(number)
                    file.write(" ")
                    hex_list = []

if __name__ == "__main__":
    main()