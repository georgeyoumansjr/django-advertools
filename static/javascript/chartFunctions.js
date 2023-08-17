export function dualLineChart(title, data1, data2, label1, label2) {
  var ctx = document.getElementById("lineChart").getContext("2d");

  var data1 = data1;
  var data2 = data2;

  var chartData = {
    datasets: [
      {
        
        label: label1,
        backgroundColor: "rgba(255, 99, 132, 0.2)",
        borderColor: "rgba(255, 99, 132, 1)",
        borderWidth: 1,
        data: data1,
      },
      {
        
        label: label2,
        backgroundColor: "rgba(54, 162, 235, 0.2)",
        borderColor: "rgba(54, 162, 235, 1)",
        borderWidth: 1,
        data: data2,
      },
    ],
  };

  var chartOptions = {
    responsive: true,
    // scales: {
    //   x: {
    //     display: false, // Hide x-axis labels
    //   },
    //   y: {
    //     display: false, // Hide y-axis labels
    //   },
    // },
    plugins: {
      title: {
        display: true,
        text: title,
        font: {
          size: 18,
        },
      },
      datalabels: {
        backgroundColor: function(context) {
          return context.dataset.backgroundColor;
        },
        borderColor: 'white',
        borderRadius: 4,
        borderWidth: 2,
        color: 'white',
        font: {
          weight: 'bold'
        },
        formatter: function(value, context) {
          // Display the data index as label
          return context.dataIndex;
        }
      }
    },
  };

  var myChart = new Chart(ctx, {
    type: "line",
    data: chartData,
    options: chartOptions,
  });
}

// donut chart func
export function createDonutChart(
    jsonData,
    title = "Donut Chart",
    label = "label",
    elementId = ""
  ) {
    var ctx = document.getElementById(elementId).getContext("2d");
    if (typeof jsonData === 'string'){
      jsonData = JSON.parse(jsonData);
    }
    var labels = Object.keys(jsonData);
    // console.log(labels)
    var length = labels.length;
  
    var data = Object.values(jsonData);
  
    var colors = generateRandomColors(length);
    // Define the chart data
    var data = {
      labels: labels,
      datasets: [
        {
          label: label,
          backgroundColor: colors,
          data: data,
        },
      ],
    };
  
    // Create the chart
    var donutChart = new Chart(document.getElementById(elementId), {
      type: "doughnut",
      data: data,
      options: {
        cutoutPercentage: 70, // Adjust the size of the hole in the middle (optional)
        responsive: true,
        plugins: {
          afterDraw: function (chart) {
            var width = chart.chart.width;
            var height = chart.chart.height;
            var ctx = chart.chart.ctx;
  
            ctx.restore();
            var fontSize = (height / 114).toFixed(2);
            ctx.font = fontSize + "em sans-serif";
            ctx.textBaseline = "middle";
  
            var text = "Status Frequencies";
            var textX = Math.round((width - ctx.measureText(text).width) / 2);
            var textY = height / 2;
  
            ctx.fillText(text, textX, textY);
            ctx.save();
          },
          title: {
            display: true,
            text: title,
            font: {
              size: 18,
            },
          },
        },
      },
    });
    // Apply ellipsis and hover display for labels
    
  }

//create a pie chart functionality
export function createPieChart(
    jsonData,
    title = "Pie Chart",
    label = "label",
    elementId = ""
  ) {
    var ctx = document.getElementById(elementId).getContext("2d");
    if (typeof jsonData === 'string'){
      jsonData = JSON.parse(jsonData);
    }
    var labels = Object.keys(jsonData);
    // console.log(labels)
    var length = labels.length;
  
    var data = Object.values(jsonData);
  
    var colors = generateRandomColors(length);
    // Define the chart data
    var data = {
      labels: labels,
      datasets: [
        {
          label: label,
          backgroundColor: colors,
          data: data,
        },
      ],
    };
  
    // Create the chart
    var pieChart = new Chart(document.getElementById(elementId), {
      type: "pie",
      data: data,
      options: {
        cutoutPercentage: 70, // Adjust the size of the hole in the middle (optional)
        responsive: true,
        plugins: {
          afterDraw: function (chart) {
            var width = chart.chart.width;
            var height = chart.chart.height;
            var ctx = chart.chart.ctx;
  
            ctx.restore();
            var fontSize = (height / 114).toFixed(2);
            ctx.font = fontSize + "em sans-serif";
            ctx.textBaseline = "middle";
  
            var text = "Status Frequencies";
            var textX = Math.round((width - ctx.measureText(text).width) / 2);
            var textY = height / 2;
  
            ctx.fillText(text, textX, textY);
            ctx.save();
          },
          title: {
            display: true,
            text: title,
            font: {
              size: 18,
            },
          },
        },
      },
    });
    
  }
