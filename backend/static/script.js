document.getElementById("searchForm")?.addEventListener("submit", e => {
  e.preventDefault();
  const q = document.getElementById("query").value.trim();
  const loc = document.getElementById("location").value.trim();
  const cat = document.getElementById("category").value;
  const jobs = ["Online Job","Nearby Job","Work From Home","Part Time Job","Full Time Job"];
  const page = jobs.includes(cat) ? "jobs.html" : (cat === "Spa Centre" || cat === "Massage" ? "spa.html" : (q.toLowerCase().includes("job") ? "jobs.html" : "jobs.html"));
  const p = new URLSearchParams();
  if(q) p.set("search", q); if(loc) p.set("location", loc); if(cat) p.set("type", cat);
  location.href = page + "?" + p.toString();
});
