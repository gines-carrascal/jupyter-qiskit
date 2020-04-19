FROM jupyter/minimal-notebook:latest

RUN python -m pip install qiskit && \
    python -m pip install ipywidgets && \
    python -m pip install matplotlib && \
    python -m pip install seaborn && \
    python -m pip install qiskit-terra[visualization]

ADD ./sample /home/jovyan/sample

