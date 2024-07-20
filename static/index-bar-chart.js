// For Bar Chart

fetch('/api/sample-bar-data')
    .then(data => data.json())
    .then(jsonData => {
            console.log("Data Received From '/api/sample-bar-data': ", jsonData)
            new Chart(
                document.getElementById('bar-chart'),
                {
                    type: 'bar',
                    data: {
                        labels: jsonData.labels,
                        datasets: jsonData.datasets
                    }
                }
            )
        }
    );
