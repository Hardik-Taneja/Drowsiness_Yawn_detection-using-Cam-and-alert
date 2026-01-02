const video = document.getElementById("video");
const canvas = document.getElementById("canvas");
const statusText = document.getElementById("status");

navigator.mediaDevices.getUserMedia({ video: true })
  .then(stream => video.srcObject = stream);

setInterval(() => {
  canvas.width = video.videoWidth;
  canvas.height = video.videoHeight;
  canvas.getContext("2d").drawImage(video, 0, 0);

  const image = canvas.toDataURL("image/jpeg");

  fetch("/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ image })
  })
  .then(res => res.json())
  .then(data => {
    statusText.innerText = "Status: " + data.status;
    if (data.status !== "SAFE") {
      new Audio("/static/alert.mp3").play();
    }
  });
}, 1000);
