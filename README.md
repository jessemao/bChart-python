bChart
-----
bChart is a D3-based charting library. bChart provides a simple, clean and easy way to create SVG-style charts and to integrate to daily use web application.

The official documentation is [bChart.org](http://bchart.org)

bChart - Python
----
bChart python is a light weight library for python developers to create SVG-style charts on modern browsers. 
* D3-based
    * bChart is sitting on the top of D3 library. 
    * It gives all the powers and flexibilities D3 provides and make it much simpler to create a visualization chart.  
* Customizable
    * All charts' style can be easily customized without touch of CSS and Javascript.
    * All charts' transition/animation can be customized (coming soon).
* Easy of use 
    * Straight forward. 
    * Chainable methods.
    * Easy API (coming soon).
* Fast generating of charts.

Install
----
1. Install with pip. (virtualenv is recommemded)
        cd [to the path of your app folder]
        virtualenv venv
        source venv/bin/activate
        $pip install bchart 

2. Download "bChart" from [PyPI](https://pypi.python.org/pypi/bChart/0.1.1) or [bChart Github](https://github.com/jessemao/bChart-python)
        put bChart folder into your app folder
        cd [into bchart folder]
        python setup.py install


Tutorial
----
1. Download the example folder from the source code. (Easier to understand if we start with the example).

2. Open "example.html" in your editor. Notice that we add the d3js and bChart.js reference in the <body> and one block of javascript code (will be removed in next version) to render your chart.

        <!-- Load bChart.css -->
        <link href="/path/to/c3.css" rel="stylesheet" type="text/css">
        <!-- Your chart placeholder -->
        <div id='vis'></div>
    
        <!-- Load d3 and bChart -->
        <script src="./js/lib/d3.min.js" charset="utf-8"></script>
        <script src='./js/lib/bChart.js'></script>
        <!-- Render your chart -->
        <script>
            d3.json('bchart.json', function (data) {
              bChart(data.selector, data.chartType, data);
            });
        </script>
 
3. In your python app, you need to **import** bChart
        
        from bchart import *
        # after you import bchart, you could start to create your chart now.

        # firstly, I could set up some properties of my chart, like width and height.
        options = {"width": 500, "height": 500}

        # then I initial an AreaChart, which will be drawn on the DOM whose id = "vis" with the options I initialized.
        chart = AreaChart("#vis", options) 
        # Alts: you can also do
        # chart = bChart("#vis", "area", options)
        
        # then you can start load data, configure chart background, colors, and all other properties that are provided by bChart. Please refer to [bChart.org](http://bchart.org/apis.html) for more information. 
        chart.load([['group1', '34','54','33'], ['group2', '53', '44', '65']]).legend('display', 'none').background('color', "#ffffff").colors(["#dd00dd", '#ffdd00']).option({"isStack": "true"})

        # REQUIRED: remember, you have to make this call to generate the chart for you. Without calling this method, you can not render your chart.
        chart.to_json()
        
        #Notice: as you see above, you can chain the method to update your chart's property.
    
Example
----
1. Download or clone this git to your machine. 
2. **"cd"** to example folder. 
3. Type in "python generate_areachart.py" in your terminal. 
4. Then type in 
        python -m SimpleHTTPServer 8000 
        # use other port if 8000 is taken.
5. Goto your browser and type in "localhost:8000/example.html".

Group
---
Coming soon.

Dependency
---
[D3.js](http://d3js.org/)

