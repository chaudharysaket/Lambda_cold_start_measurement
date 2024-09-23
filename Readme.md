



GOOS=linux GOARCH=arm64 go build -o main ./go-arm-src/main.go

GOOS=linux GOARCH=amd64 go build -o main ./go-amd-src/main.go

sam deploy --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM --guided

