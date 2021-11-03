FROM golang:latest

COPY ./main.go .

CMD ["go","run","main.go"]