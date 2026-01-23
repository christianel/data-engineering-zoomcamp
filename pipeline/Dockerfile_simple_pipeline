#FROM python:3.13.11-slim 
FROM ghcr.io/mamba-org/micromamba:latest 

WORKDIR /code

COPY environment.yml .

RUN micromamba create -f environment.yml

ENV PATH /opt/conda/envs/engineering/bin:$PATH
RUN echo "source activate engineering" < ~/.bashrc

COPY pipeline.py .

ENTRYPOINT ["python", "pipeline.py"]