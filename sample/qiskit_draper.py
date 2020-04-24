from qiskit import ClassicalRegister, QuantumRegister
from qiskit import QuantumCircuit
from qiskit import execute
from qiskit import Aer
from math import pi

sumando_1 = input("Primer sumando en binario (4 bits)")
sumando_2 = input("Segundo sumando en binario(4 bits)")

n = 4

n+=1

a = QuantumRegister(n,"a")
b = QuantumRegister(n, "b")
resultado = ClassicalRegister(n, "result")

qc = QuantumCircuit(a,b,resultado)

for i in range(1,n):
    if sumando_1[i-1] == "1":
        qc.x(a[n - (i+1)])
for i in range(1,n):
    if sumando_2[i-1] == "1":
        qc.x(b[n - (i+1)])
        
# Take the QFT.
# Iterate through the target.
for i in range(n,0,-1):
    # Apply the Hadamard gate to the target.
    qc.h(b[i-1])

    # Iterate through the control.
    for j in range(i-1,0,-1):
        qc.cu1(2*pi/2**(i-j+1), b[j-1], b[i-1])
        
# Compute controlled-phases.
# Iterate through the targets.
for i in range(n,0,-1):
    # Iterate through the controls.
    for j in range(i,0,-1):
        qc.cu1(2*pi/2**(i-j+1), a[j-1], b[i-1])

# Take the inverse QFT.
# Iterate through the target.
for i in range(1,n+1):
    # Iterate through the control.
    for j in range(1,i):
        # The inverse Fourier transform just uses a negative phase.
        qc.cu1(-2*pi/2**(i-j+1), b[j-1], b[i-1])

    # Apply the Hadamard gate to the target.
    qc.h(b[i-1])

# Measure
qc.measure(b,resultado)    

my_backend = Aer.get_backend("qasm_simulator")  
job = execute(qc, my_backend, shots=20)
job_stats = job.result().get_counts()
print(job_stats) 