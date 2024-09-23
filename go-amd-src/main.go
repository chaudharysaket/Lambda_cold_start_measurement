package main

import (
	"context"
	"fmt"
	"github.com/newrelic/go-agent/v3/integrations/nrlambda"
	"github.com/newrelic/go-agent/v3/newrelic"
)

func handler(ctx context.Context) (string, error) {

	fmt.Println("hello world!")

	return "Success!", nil
}

func main() {
	app, err := newrelic.NewApplication(nrlambda.ConfigOption())
	if nil != err {
		fmt.Println("error creating app (invalid config):", err)
	}
	nrlambda.Start(handler, app)
}