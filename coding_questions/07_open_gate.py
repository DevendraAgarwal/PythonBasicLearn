total_gates = 100
gates = [False for i in range(1,total_gates+1)]

# For 1 To 100 
for i in range(1,total_gates+1):
    print(f"--Person {i} Comes--")
    # First Gate Set to Person Number 1
    gate = i
    while(gate<=total_gates):
        if gates[gate-1] is False:
            gates[gate-1] = True
            print(f"Gate {gate} Open")
        else:
            gates[gate-1] = False
            print(f"Gate {gate} Close")
            
        # Gate Number Incremented By Person Number 
        gate = gate+i
        print("--------------------")

print(f"Total Opened Gate {int(total_gates**0.5)}")       
print(f"Total Opened Gates Is {gates.count(True)}")