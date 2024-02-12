FROM python:3.11.8-alpine3.19

# Gravar arquivos de bytecode (.pyc) no disco. 1 = Não, 0 = Sim
ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

# Copia a pasta "back" e "scripts" para dentro do container.
COPY back /back
COPY scripts /scripts

# Entra na pasta back no container
WORKDIR /back

# Porta 8000 estará disponível para conexões para o Django ao container.
EXPOSE 8000

# RUN executa comandos em um shell dentro do container para construir a imagem. 
RUN python -m venv /venv && \
  /venv/bin/pip install --upgrade pip && \
  /venv/bin/pip install djangorestframework && \
  /venv/bin/pip install django-cors-headers && \
  /venv/bin/pip install -r /back/requirements.txt && \
  adduser --disabled-password --no-create-home duser && \
  mkdir -p /data/web/static && \
  mkdir -p /data/web/media && \
  chown -R duser:duser /venv && \
  chown -R duser:duser /data/web/static && \
  chown -R duser:duser /data/web/media && \
  chmod -R 755 /data/web/static && \
  chmod -R 755 /data/web/media && \
  chmod -R +x /scripts

# Adiciona a pasta scripts e venv/bin 
# no $PATH do container.
ENV PATH="/scripts:/venv/bin:$PATH"

# Muda o usuário para duser
USER duser

# Executa o arquivo scripts/commands.sh
CMD ["commands.sh"]
