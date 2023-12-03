const eventSource = new EventSource("http://localhost:5000/connection/tiaz");

eventSource.addEventListener("alarm", (event) => {
  console.log(event.data);
});

eventSource.onerror = function() {
    eventSource.close()
    console.log("error")
    // 필요에 따라 여기에서 재연결 로직을 구현할 수 있습니다.
};