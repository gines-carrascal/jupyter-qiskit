FROM jupyter/minimal-notebook:latest

RUN pip install qiskit && \
    pip install ipywidgets && \
    pip install matplotlib && \
    pip install seaborn && \
    pip install qiskit-terra[visualization]

ADD ./sample /sample