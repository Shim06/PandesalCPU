# Pandesal CPU

**Pandesal CPU** is an 8-bit multi-cycle general-purpose CPU architecture inspired by the classic **MOS 6502**. Built at the logic-gate level and implemented in Logisim Evo.

---

## Architecture Specs

- **Data Bus:** 8-bit  
- **Address Bus:** 16-bit (64 KB addressable memory)  
- **Endianness:** Little Endian  
- **Arithmetic:** Integer only  
- **Design Inspired by:** MOS 6502  

---

## CPU Registers

| Register                  | Size  | Description                          |
|---------------------------|-------|--------------------------------------|
| Program Counter (PC)      | 16-bit| Points to the current instruction    |
| Accumulator (A)           | 8-bit | Main register for arithmetic         |
| ALU B Register (B)        | 8-bit | Second operand register for ALU      |
| Status Register (SR)      | 4-bit | Holds CPU flags                      |
| X Index Register (X)      | 8-bit | Used for indexing and addressing     |
| Y Index Register (Y)      | 8-bit | Same as above                        |
| Stack Pointer (SP)        | 8-bit | Stack offset within page $0100       |
| General-Purpose Registers | 8-bit | 5 additional general registers       |

---

## Status Flags

| Flag     | Bit | Description                        |
|----------|-----|------------------------------------|
| Negative | N   | Set if result is negative          |
| Overflow | O   | Set if signed overflow occurred    |
| Zero     | Z   | Set if result is zero              |
| Carry    | C   | Set if carry/borrow occurred       |

---

## ALU Instructions

- `ADC` – Add with Carry  
- `SBC` – Subtract with Carry  
- `NOT` – Bitwise NOT  
- `AND` – Bitwise AND  
- `XOR` – Bitwise XOR  
- `OR`  – Bitwise OR  
- `LSH` – Logical Shift Left  
- `RSH` – Logical Shift Right  

---

## Branch Instructions

| Mnemonic | Description                   |
|----------|-------------------------------|
| `BCC`    | Branch if Carry Clear         |
| `BCS`    | Branch if Carry Set           |
| `BEQ`    | Branch if Equal (Zero set)    |
| `BMI`    | Branch if Minus (Negative set)|
| `BNE`    | Branch if Not Equal           |
| `BPL`    | Branch if Positive            |
| `BVC`    | Branch if Overflow Clear      |
| `BVS`    | Branch if Overflow Set        |
