FROM ubuntu:20.04

RUN echo "What's my hash?" > file.txt

CMD ["md5sum", "file.txt"]
