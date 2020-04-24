from qiskit import ClassicalRegister, QuantumRegister
from qiskit import QuantumCircuit
from qiskit import execute
from qiskit import Aer

sumando_1 = input("Primer sumando en binario (4 bits)")
sumando_2 = input("Segundo sumando en binario(4 bits)")

n = 4

a = QuantumRegister(n,"a")
b = QuantumRegister(n+1, "b")
c = QuantumRegister(n, "c")
resultado = ClassicalRegister(n+1, "result")

qc = QuantumCircuit(a,b,c,resultado)

for i in range(n):
    if sumando_1[i] == "1":
        qc.x(a[n - (i+1)])
for i in range(n):
    if sumando_2[i] == "1":
        qc.x(b[n - (i+1)])

for i in range(n-1):
    qc.ccx(a[i], b[i], c[i+1])
    qc.cx(a[i], b[i])
    qc.ccx(c[i], b[i], c[i+1])

qc.ccx(a[n-1], b[n-1], b[n])
qc.cx(a[n-1], b[n-1])
qc.ccx(c[n-1], b[n-1], b[n])  

qc.cx(c[n-1], b[n-1])

for i in range(n-1):
    qc.ccx(c[(n-2)-i], b[(n-2)-i], c[(n-1)-i])
    qc.cx(a[(n-2)-i], b[(n-2)-i])
    qc.ccx(a[(n-2)-i], b[(n-2)-i], c[(n-1)-i])
    
    qc.cx(c[(n-2)-i], b[(n-2)-i])
    qc.cx(a[(n-2)-i], b[(n-2)-i])

qc.measure(b,resultado)    

my_backend = Aer.get_backend("qasm_simulator")  
job = execute(qc, my_backend, shots=20)
job_stats = job.result().get_counts()
print(job_stats) 
