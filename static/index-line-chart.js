// For Bar Chart

fetch('/api/sample-line-data')
    .then(data => data.json())
    .then(jsonData => {
            console.log("Data Received From '/api/sample-line-data': ", jsonData)
            new Chart(
                document.getElementById('line-chart'),
                {
                    type: 'line',
                    data: {
                        labels: jsonData.labels,
                        datasets: jsonData.datasets
                    }
                }
            )
        }
    );
