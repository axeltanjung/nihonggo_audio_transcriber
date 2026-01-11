let timer = null;
let remaining = 0;

function startETA(seconds) {
  remaining = seconds;
  document.getElementById("timer").innerText =
    `⏳ Est. ${remaining} sec remaining`;

  timer = setInterval(() => {
    remaining--;
    if (remaining > 0) {
      document.getElementById("timer").innerText =
        `⏳ ${remaining} sec remaining`;
    }
  }, 1000);
}

function stopTimer(actual) {
  clearInterval(timer);
  document.getElementById("timer").innerText =
    `✅ Finished in ${actual} sec`;
}

async function upload() {
  const f = document.getElementById("file").files[0];
  if (!f) return alert("Choose a file");

  document.getElementById("result").innerText = "";

  const fd = new FormData();
  fd.append("file", f);

  const start = Date.now();

  const res = await fetch("http://localhost:8000/transcribe", {
    method: "POST",
    body: fd
  });

  const data = await res.json();

  // ETA dari backend
  startETA(data.eta_seconds);

  document.getElementById("result").innerText =
    data.segments.map(s =>
      `[${s.start} – ${s.end}] ${s.text}`
    ).join("\n");

  const actual = Math.floor((Date.now() - start) / 1000);
  stopTimer(actual);
}

async function downloadSRT() {
  const f = document.getElementById("file").files[0];
  if (!f) return alert("Choose a file");

  const fd = new FormData();
  fd.append("file", f);

  document.getElementById("timer").innerText = "⏳ Exporting...";

  const res = await fetch("http://localhost:8000/export/srt", {
    method: "POST",
    body: fd
  });

  const text = await res.text();

  const blob = new Blob([text], { type: "application/x-subrip" });
  const url = window.URL.createObjectURL(blob);

  const a = document.createElement("a");
  a.href = url;
  a.download = "subtitle.srt";
  a.click();

  document.getElementById("timer").innerText = "✅ Subtitle downloaded";
}
