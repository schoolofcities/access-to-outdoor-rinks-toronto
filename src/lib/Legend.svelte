<script>
     $: labels = [
        "<15",
        "15-30",
        "30-45",
        "45-60",
        ">60"
    ]

    $: title1 = "Travel Time to the Nearest Outdoor Skating Rink (Minutes):"

    $: colour = [
        "#f1eef6",
        "#bdc9e1",
        "#74a9cf",
        "#2b8cbe",
        "#045a8d"
    ]
</script>

<p class="legend-title">{title1} </p>

<svg width="250" height="30">
    <rect
        class="box"
        width="50"
        height="19"
        x="0"
        y="0"
        style="fill:{colour[0]};"
    />
    <rect
        class="box"
        width="50"
        height="19"
        x="50"
        y="0"
        style="fill:{colour[1]};"
    />
    <rect
        class="box"
        width="50"
        height="19"
        x="100"
        y="0"
        style="fill:{colour[2]};"
    />
    <rect
        class="box"
        width="50"
        height="19"
        x="150"
        y="0"
        style="fill:{colour[3]};"
    />
    <rect
        class="box"
        width="50"
        height="19"
        x="200"
        y="0"
        style="fill:{colour[4]};"
    />

    <text class="legend-label" x="13" y="15">{labels[0]}</text>
	<text class="legend-label" x="58" y="15">{labels[1]}</text>
	<text class="legend-label legend-label-dark" x="110" y="15">{labels[2]}</text>
	<text class="legend-label legend-label-dark" x="158" y="15">{labels[3]}</text>
	<text class="legend-label legend-label-dark" x="213" y="15">{labels[4]}</text>

</svg>


<style>

    .box {
            stroke-width: 0.5px;
            stroke: rgb(206, 206, 206);
        }
    .legend-label {
            font-size: 13px;
            fill:var(--brandDarkBlue);
            font-weight: 400;
        }

    .legend-label-minutes {
        font-size: 13px;
        fill: var(--brandDarkBlue);
    }


    .legend-label-dark {
        font-size: 13px;
        fill: var(--brandWhite)
    }
        
    .legend-title {
            font-family: RobotoBold;
            /* font-weight: 600; */
            font-size: 16px;
            color: var(--brandDarkBlue);
            margin-bottom: 0px;
            vertical-align: top;
            padding-bottom: 4px;
        }
    </style>
