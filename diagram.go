
func main() {
    // Register handlers
    http.HandleFunc("/", homeHandler)
    http.HandleFunc("/submit", submitHandler)
    http.HandleFunc("/test", testHandler)
    
    fmt.Println("Server starting on http://localhost:80")
    fmt.Println("Press Ctrl+C to stop the server")
    
    // Start server
    log.Fatal(http.ListenAndServe(":80", nil))
}