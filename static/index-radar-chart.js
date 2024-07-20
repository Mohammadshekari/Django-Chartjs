// For Bar Chart

fetch('/api/sample-radar-data')
    .then(radarData => radarData.json())
    .then(radarData => {
            console.log("Data Received From '/api/sample-radar-data': ", radarData)
            new Chart(
                document.getElementById('radar-chart'),
                {
                    type: 'radar',
                    data: {
                        labels: radarData.labels,
                        datasets: radarData.datasets
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
