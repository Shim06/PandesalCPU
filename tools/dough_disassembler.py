def main():
    def hasOperand(i):
        if i in imm: 
            return 1
        elif i in absolute:
            return 2
        else:
            return 0
        
    imm = []
    absolute = []

    instructions = []
    with open("instructions.txt", "r") as file:
        content = file.read()
        instructions = content.split('\n')


    for i, m in enumerate(instructions):
        for c in m:
            if c == "#":
                imm.append(i)

    for i, m in enumerate(instructions):
        if "abs" in m:
            absolute.append(i)

    inp = input("Binary Code: ")
    inp = inp.split()
    op = 0
    while op < len(inp):
        operand = hasOperand(int(inp[op], base=16))
        if operand:
            current_op = instructions[int(inp[op], base=16)]
            print(f"{current_op[0:3]} ", end="")
            for i in range(operand, 0, -1):
                print(inp[op + i], end="")
            print()
            op += 1 + operand
            continue
        else:
            current_op = instructions[int(inp[op], base=16)]
            print(current_op[0:3])
        op += 1
        #print(instructions[int(i, base=16)])
    
if __name__ == "__main__":
    main()