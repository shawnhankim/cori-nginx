package main

import (
	"io"
	"net/http"
)

func main() {
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		io.WriteString(w, "Hello, Go on Unit!")
	})
	unit.ListenAndServe(":8080", nil)
}
