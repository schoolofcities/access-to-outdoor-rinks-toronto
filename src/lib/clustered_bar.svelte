<script>
    import * as d3 from "d3";
    import { onMount } from "svelte";
    import { walk } from "svelte/compiler";

    onMount(() => {
        // set the dimensions and margins of the graph
        const margin = { top: 10, right: 30, bottom: 20, left: 50 },
            width = 750 - margin.left - margin.right,
            height = 300 - margin.top - margin.bottom;


        // append the svg object to the body of the page
        const svg = d3
            .select("#my_dataviz")
            .append("svg")
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom + 20)
            .append("g")
            .attr("transform", `translate(${margin.left},${margin.top})`);

        // Parse the Data

        const data = [
            {
                mode: "Walk",
                populationTime: 34.3,
                LIncomeTime: 33.5,
                ImmigratTime: 37.,
                VMTime: 39.7,
            },
            {
                mode: "Tansit (Weekday)",
                populationTime: 23.1,
                LIncomeTime: 22.5,
                ImmigratTime: 24.3,
                VMTime: 25.2,
            },
            {
                mode: "Transit (Weekend)",
                populationTime: 23.4,
                LIncomeTime: 22.8,
                ImmigratTime: 24.6,
                VMTime: 25.5,
            },
        ];

        console.log(data);
        // List of subgroups = header of the csv files = soil condition here
        // const subgroups = data.columns.slice(1);
        const subgroups = [
            "populationTime",
            "LIncomeTime",
            "ImmigratTime",
            "VMTime",
        ];

        // List of groups = species here = value of the first column called group -> I show them on the X axis
        const groups = data.map((d) => d.mode);

        console.log(groups);

        // Add X axis
        const x = d3
            .scaleBand()
            .domain(groups)
            .range([0, width])
            .padding([0.2]);
        svg.append("g")
            .style("font", "14px Roboto")
            .attr("transform", `translate(0, ${height})`)
            .call(d3.axisBottom(x).tickSize(0));

        svg.append("text")      // text label for the x axis
        .attr("x", (width / 2) )
        .attr("y", 300 )
        .style("text-anchor", "middle")
        .style("font", "12px Roboto")
        .style("fill", "#1E3765")
        .text("Mode");

        // Add Y axis
        const y = d3.scaleLinear().domain([0, 45]).range([height, 0]);
        svg.append("g").style("font", "14px Roboto").call(d3.axisLeft(y));

        // y-axis label
        svg.append("text")
        .attr("transform", "rotate(-90)")
        .attr("y", 0 - margin.left)
        .attr("x",0 - (height / 2))
        .attr("dy", "1em")
        .style("text-anchor", "middle")
        .style("font", "12px Roboto")
        .style("fill", "#1E3765")
        .text("Travel Time (Minute)");

        // Another scale for subgroup position?
        const xSubgroup = d3
            .scaleBand()
            .domain(subgroups)
            .range([0, x.bandwidth()])
            .padding([0.05]);

        // color palette = one color per subgroup
        const color = d3
            .scaleOrdinal()
            .domain(subgroups)
            .range(["#D0D1C9", "#1E3765", "#6D247A", "#007FA3"]);

        //title
        svg.append("text")
            .attr("x", (width / 2))             
            .attr("y", 10 - (margin.top / 2))
            .attr("text-anchor", "middle")  
            .style("font-size", "14px") 
            .style("text-decoration", "underline")  
            .style("fill", "#1E3765")
            .text("Population-Weighted Average Travel Time by Demographic Group and Mode of Transportation");

        svg.append("g")
            .selectAll("g")
            // Enter in data = loop group per group
            .data(data)
            .join("g")
            .attr("transform", (d) => `translate(${x(d.mode)}, 0)`)
            .selectAll(".bar-group")
            .data(function (d) {
                console.log(d);
                return subgroups.map(function (key) {
                    return { key: key, value: d[key] };
                });
            })
            .join((enter) => {
                let g = enter;
                g.append("rect")
                    .attr("x", (d) => xSubgroup(d.key))
                    .attr("y", (d) => y(d.value))
                    .attr("width", xSubgroup.bandwidth())
                    .attr("height", (d) => height - y(d.value))
                    .attr("fill", (d) => color(d.key));

                g.append("text")
                    .attr("x", (d) => xSubgroup(d.key) + xSubgroup.bandwidth() / 2)
                    .attr("y", (d) => y(d.value) - 2)
                    .attr("font-family" , "Roboto")
                    .attr("font-size" , "12px")
                    .attr("text-anchor", "middle")
                    .text((d) => d.value);
                return g;
            });

    });
</script>

<!-- Create a div where the graph will take place -->
<div id="my_dataviz"></div>
