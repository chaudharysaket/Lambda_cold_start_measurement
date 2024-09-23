build-ColdStartComputationGolangLambdaAMD:
	GOOS=linux GOARCH=amd64 go build -o bootstrap main.go
	chmod +x bootstrap

# The default build target that SAM CLI will use
# build:
# 	make build-ColdStartComputationGolangLambdaAMD

build-ColdStartComputationGolangLambdaARM:
	GOOS=linux GOARCH=arm64 go build -o bootstrap main.go
	chmod +x bootstrap

# The default build target that SAM CLI will use
# build:
# 	make build-ColdStartComputationGolangLambdaARM
