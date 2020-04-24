from qiskit import ClassicalRegister, QuantumRegister
from qiskit import QuantumCircuit
from qiskit import execute
from qiskit import Aer

sumando_1 = input("Primer sumando en binario (4 bits)")
sumando_2 = input("Segundo sumando en binario(4 bits)")

n = 4

a = QuantumRegister(n,"a")
b = QuantumRegister(n+1, "b")
c = QuantumRegister(1, "c")
resultado = ClassicalRegister(n+1, "result")

qc = QuantumCircuit(a,b,c,resultado)

for i in range(n):
    if sumando_1[i] == "1":
        qc.x(a[n - (i+1)])
for i in range(n):
    if sumando_2[i] == "1":
        qc.x(b[n - (i+1)])

for i in range(1, n):
    qc.cx(a[i], b[i])

qc.cx(a[1], c[0])

qc.ccx(a[0], b[0], c[0])
qc.cx(a[2], a[1])

qc.ccx(c[0], b[1], a[1])
qc.cx(a[3], a[2])

for i in range(2, n-2):
    qc.ccx(a[i-1], b[i], a[i])
    qc.cx(a[i+2], a[i+1])

qc.ccx(a[n-3], b[n-2], a[n-2])
qc.cx(a[n-1], b[n])

qc.ccx(a[n-2], b[n-1], b[n])
for i in range(1, n-1):
    qc.x(b[i])

qc.cx(c[0], b[1])
for i in range(2, n):
    qc.cx(a[i-1], b[i])

qc.ccx(a[n-3], b[n-2], a[n-2])

for i in range(n-3,1,-1):
    qc.ccx(a[i-1], b[i], a[i])
    qc.cx(a[i+2], a[i+1])
    qc.x(b[i+1])

qc.ccx(c[0], b[1], a[1])
qc.cx(a[3], a[2])
qc.x(b[2])

qc.ccx(a[0], b[0], c[0])
qc.cx(a[2], a[1])
qc.x(b[1])

qc.cx(a[1], c[0])

for i in range(n):
    qc.cx(a[i], b[i])

qc.measure(b,resultado)    

my_backend = Aer.get_backend("qasm_simulator")  
job = execute(qc, my_backend, shots=20)
job_stats = job.result().get_counts()
print(job_stats) 