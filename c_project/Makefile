CC = gcc

main : main.o main_code.o

main.o : main.c

main_code.o : main_code.c main_code.h

run : main
      ./main

clean : 
      $(RM) *.o./main