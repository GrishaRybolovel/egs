.text
main:
li $v0,5
syscall
move $s0,$v0
li $s1, 1
factorial:
mult $s0, $s1
mflo $s1
addi $s0, $s0, -1
bgtz $s0, factorial
li $v0, 1
move $a0, $s1
syscall
li $v0, 10
syscall