; By: Shim Manaloto

; Video is compressed using an RLE compression algorithm.
; Bit 7/MSB is the value
; Bits 6-0 is the run length
; Each frame ends in an 0x00 to signify the end of an frame

start:
	LDX #0
	LDY #0
	LDA memoryBank
	STA $3FFF
	JMP drawLoop

advanceBitmap:
	; increment bitmapLocation
	INC bitmapLo
	BNE skipBitmapHi
	INC bitmapHi

skipBitmapHi:
drawLoop:
	; fetch data byte, check if frame end
	LDA (bitmapLocation)
	CMP #00
	BEQ endOfImage

	; Check MSB for color: 0 -> Black, 1 -> White
	ASL A			
	BCC drawBlack

drawWhite:
	LSR A		
	TAX			; Mov length > X as loop counter
drawWhiteLoop:
	; Draw
	LDA #$FF
	STA (drawLocation)

	; Increment draw location
	INC drawLo
	BNE skipDrawHiWhite
	INC drawHi
skipDrawHiWhite:
	DEX
	BEQ advanceBitmap
	JMP drawWhiteLoop	; JMP to loop start

drawBlack:
	LSR A		
	TAX			; Mov length > X as loop counter
drawBlackLoop:
	; Draw
	LDA #$00
	STA (drawLocation)

	; Increment draw location
	INC drawLo
	BNE skipDrawHiBlack
	INC drawHi
skipDrawHiBlack:
	DEX
	BEQ advanceBitmap
	JMP drawBlackLoop	; JMP to loop start


endOfImage:
	; Check if next byte is 0x00, signifying the end of the memory bank
	INC bitmapLo
	BNE bankCheck
	INC bitmapHi
bankCheck:
	LDA (bitmapLocation)
	CMP #0
	BNE sameBank ;	Move to next byte and continue to next image

	; End of memory bank. switch to next ROM bank
	LDA memoryBank
	; Check if it is the last memory bank (30)
	CMP #30
	BEQ end ; End if last memory bank
	ADD #1
	STA $3FFF
	STA memoryBank

	; Reset bitmap pointer to start of bank
	LDA #$00
	STA bitmapLo
	LDA #$80
	STA bitmapHi

sameBank:
	; Reset draw pointer to start of screen
	LDA #$00
	STA drawLo
	LDA #$40
	STA drawHi
	JMP drawLoop


end:
	HLT

bitmapLocation:
bitmapLo: .byte $00
bitmapHi: .byte $80

drawLocation:
drawLo: .byte $00
drawHi: .byte $40

memoryBank: .byte 00