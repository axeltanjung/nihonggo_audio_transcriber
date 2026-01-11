async function upload() {
  const f = document.getElementById("file").files[0];
  const fd = new FormData();
  fd.append("file", f);

  const res = await fetch("http://localhost:8000/transcribe", { method:"POST", body:fd });
  const data = await res.json();

  document.getElementById("result").innerText =
    data.map(x => `[${x.start} – ${x.end}] ${x.text}`).join("\n");
}
