// For Bar Chart

fetch('/api/sample-doughnut-data')
    .then(doughnutData => doughnutData.json())
    .then(doughnutData => {
            console.log("Data Received From '/api/sample-doughnut-data': ", doughnutData)
            new Chart(
                document.getElementById('doughnut-chart'),
                {
                    type: 'doughnut',
                    data: {
                        labels: doughnutData.labels,
                        datasets: doughnutData.datasets
                    },
                    options: {
                        responsive: true,
                        plugins: {
                            legend: {
                                position: 'top',
                            },
                        }
                    },
                }
            )
        }
    );
