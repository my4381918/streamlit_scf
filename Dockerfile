FROM python:3.9
RUN echo 'Asia/Shanghai' >/etc/timezone && \
    apt-get update && \
    apt-get install iputils-ping rsync -y && \
    apt-get install net-tools -y && \
    apt-get install openssh-server -y && \
    groupadd -g 2000 op_biz && \
    useradd -u 2000 -g op_biz op_biz
WORKDIR /app
COPY ./requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 8501
COPY ./images ./images
COPY ./.streamlit ./.streamlit
COPY . /app
ENTRYPOINT [ "streamlit", "run" ]
CMD ["main.py"]
