#FROM python:3.13.11-slim 
FROM ghcr.io/mamba-org/micromamba:latest 

WORKDIR /code

COPY ../environment.yml .

RUN micromamba create -f environment.yml

ENV PATH /opt/conda/envs/engineer/bin:$PATH
RUN echo "source activate engineer" < ~/.bashrc

COPY ingest_data.py .

ENTRYPOINT ["python", "ingest_data.py"]