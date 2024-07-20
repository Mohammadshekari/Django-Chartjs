// For Bar Chart

fetch('/api/sample-pie-data')
    .then(pieData => pieData.json())
    .then(pieData => {
            console.log("Data Received From '/api/sample-pie-data': ", pieData)
            new Chart(
                document.getElementById('pie-chart'),
                {
                    type: 'pie',
                    data: {
                        labels: pieData.labels,
                        datasets: pieData.datasets
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
