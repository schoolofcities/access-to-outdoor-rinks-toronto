<script>
    // https://github.com/schoolofcities/place-and-politics-toronto/blob/467ccdfbb0518cdc3f28669e19cd172c898c9c6b/src/routes/lib/Bar.svelte

    // The percentage of each demographics group for each time range (distance from the cloest rink)
    const percentageData = {
        populationTimePercent: {
            "Under 15 Mins": 21.2,
            "15-30 Mins": 32.3,
            "30-45 Mins": 19.5,
            "45-60 Mins": 13.7,
            "More than 60 Mins": 13.3
        }, 
        immigrantTimePrecent: {
            "Under 15 Mins": 17.5,
            "15-30 Mins": 29.0,
            "30-45 Mins": 21.2,
            "45-60 Mins": 16.4,
            "More than 60 Mins": 16.0
        },
        lowIncomeTimePercent: {
            "Under 15 Mins": 21.9,
            "15-30 Mins": 30.6,
            "30-45 Mins": 20.3,
            "45-60 Mins": 14.5,
            "More than 60 Mins": 12.8
        },
        vmTimePercent:{
            "Under 15 Mins": 16.6,
            "15-30 Mins": 26.5,
            "30-45 Mins": 20.9,
            "45-60 Mins": 17.2,
            "More than 60 Mins": 18.8
        }
    }
    // the box dimension
    const margin = {top:1, bottom:1, left:1, right:1};
    let divWidth;
    const height = 40; 
    let boxes = [];
    const demographicsId = {"populationTimePercent": "General Population",
                            "immigrantTimePrecent": "Immigrant Population", 
                            "lowIncomeTimePercent": "Low Income Population", 
                            "vmTimePercent": "Visible Minority Population"
                        };

    $: innerWidth = divWidth-margin.left - margin.right

    //
    $: {
        let bars = {} //empty dictionary to be filled with data after looping
        for (let demographics in percentageData) { //e.g. immigrantTimePrecent...vmTimePercent
            const timeData = percentageData[demographics]; // the dict for each demographics containing percentages
            let boxSizes = {} // to be populated as is: {"Under 15 Mins": [start, width], "15-30 Mins": ...}
            let cumulative = 0;
            for (let timeRange in timeData){ //for key in dict e.g. "Under 15 Mins" in dict "immigrantTimePrecent"
                boxSizes[timeRange] = [cumulative, timeData[timeRange] / 100 * innerWidth]; //for each percentage, the start and width
                cumulative = cumulative + timeData[timeRange] / 100 * innerWidth; //update the cumulative number after each iteration
            }
            bars[demographics]=boxSizes
        }
        boxes = Object.entries(bars)
    }

    $: labels = [
        "<15",
        "15-30",
        "30-45",
        "45-60",
        "<60"
    ]

    $: title1 = "Walking Time (minutes)"

    $: colour = [
        "#f1eef6",
        "#bdc9e1",
        "#74a9cf",
        "#2b8cbe",
        "#045a8d"
    ]

</script>



<p class="graphTitle"> Percentage of People by Walking Time to the Closest Rink and Demographic Group</p>

<div id="container" class="svg-container" bind:offsetWidth={divWidth}>
    {#each boxes as [demographics, boxSizes]}
    <p>
        {demographicsId[demographics]}
    </p>
        <svg width={divWidth} {height} class="svg-content">
            <g transform={`translate(${margin.left},${margin.top})`}>
                <rect x={boxSizes["Under 15 Mins"][0]} y="10" width={boxSizes["Under 15 Mins"][1]} height="25"
                style="fill:#f1eef6;stroke:white;stroke-width:1;" />
                <rect x={boxSizes["15-30 Mins"][0]} y="10" width={boxSizes["15-30 Mins"][1]} height="25"
                style="fill:#bdc9e1;stroke:white;stroke-width:1;" />
                <rect x={boxSizes["30-45 Mins"][0]} y="10" width={boxSizes["30-45 Mins"][1]} height="25"
                style="fill:#74a9cf;stroke:white;stroke-width:1;" />
                <rect x={boxSizes["45-60 Mins"][0]} y="10" width={boxSizes["45-60 Mins"][1]} height="25"
                style="fill:#2b8cbe;stroke:white;stroke-width:1;" />
                <rect x={boxSizes["More than 60 Mins"][0]} y="10" width={boxSizes["More than 60 Mins"][1]} height="25"
                style="fill:#045a8d;stroke:white;stroke-width:1;" />
            </g>
                <text class="legend-label" x={boxSizes["Under 15 Mins"][0]+boxSizes["Under 15 Mins"][1]/2} y="30">{percentageData[demographics]["Under 15 Mins"]}%</text>
                <text class="legend-label" x={boxSizes["15-30 Mins"][0]+boxSizes["15-30 Mins"][1]/2} y="30">{percentageData[demographics]["15-30 Mins"]}%</text>
                <text class="legend-label" x={boxSizes["30-45 Mins"][0]+boxSizes["30-45 Mins"][1]/2} y="30">{percentageData[demographics]["30-45 Mins"]}%</text>
                <text class="legend-label legend-label-dark" x={boxSizes["45-60 Mins"][0]+boxSizes["45-60 Mins"][1]/2} y="30">{percentageData[demographics]["45-60 Mins"]}%</text>
                <text class="legend-label legend-label-dark" x={boxSizes["More than 60 Mins"][0]+boxSizes["More than 60 Mins"][1]/2} y="30">{percentageData[demographics]["More than 60 Mins"]}%</text>
        </svg>
    {/each}
</div>

<style>
p {
    color: var(--brandDarkBlue);
    font-size: 16px;
    font-weight: 400;
    line-height: 24px;
    margin-left: 0px;
    margin-top: 10px;
    margin-right: 0px;
    margin-bottom: 0px;
}
.graphTitle {
    color: var(--brandDarkBlue);
    font-size: 16px;
    font-weight: 700;
    line-height: 30px;
    text-decoration: underline;
    margin-left: 0px;
    margin-top: 10px;
    margin-right: 0px;
    margin-bottom: 0px;
}
.box {
		stroke-width: 0.5px;
		stroke: rgb(206, 206, 206);
	}
.legend-label {
		font-size: 13px;
		fill: rgb(0, 0, 0);
        text-anchor: middle;
	}
.legend-label-dark {
    fill: rgb(255, 255, 255);
}
.legend-title {
		font-size: 13px;
		fill: rgb(17, 17, 17);
        margin-bottom: 0px;
        vertical-align: top;
	}
</style>