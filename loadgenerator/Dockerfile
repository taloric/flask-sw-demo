FROM python:3.10-slim AS base

WORKDIR /usr/src/app/

COPY ./ ./

RUN pip install --prefix="/usr/local/" -r ./requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

ENTRYPOINT locust --host="http://${FRONTEND_ADDR}" --headless -u "${USERS}"%