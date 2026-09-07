const DATA_URL = "data/processed/dashboard.json";

async function loadDashboard() {
  const res = await fetch(DATA_URL);
  const data = await res.json();
  renderKPIs(data.kpis);
  renderCategoryChart(data.categories);
}

function renderKPIs(kpis) {
  const section = document.getElementById("kpis");
  section.innerHTML = Object.entries(kpis)
    .map(
      ([label, value]) => `
      <div class="kpi-card">
        <h3>${label}</h3>
        <p>${value}</p>
      </div>`,
    )
    .join("");
}

function renderCategoryChart(categories) {
  const canvas = document.createElement("canvas");
  document.getElementById("charts").appendChild(canvas);
  new Chart(canvas, {
    type: "doughnut",
    data: {
      labels: categories.map((c) => c.name),
      datasets: [
        {
          data: categories.map((c) => c.count),
          backgroundColor: [
            "#2563eb",
            "#0d9488",
            "#7c3aed",
            "#16a34a",
            "#ea580c",
            "#0f172a",
          ],
        },
      ],
    },
    options: {
      plugins: {
        legend: { position: "bottom" },
      },
    },
  });
}

loadDashboard();