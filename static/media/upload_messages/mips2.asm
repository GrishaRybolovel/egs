.data
msg: .asciiz "ahahah ahahah ahahah hahah h"
.text
main:
la $a0, msg 
li $t1, 100
li $t3, 32
counter:
lb $t2, 0($a0) 
beq $t2, $t3, adding
back:
addi $t1, $t1, -1
addi $a0, $a0, 1 
bgtz $t1, counter
addi $s0, $s0, 1
move $a0, $s0
li $v0, 1 # syscall code to print a string
syscall # printing string
li $v0, 10 # syscall code to terminate the program
syscall 


adding:
addi $s0, $s0, 1
j back